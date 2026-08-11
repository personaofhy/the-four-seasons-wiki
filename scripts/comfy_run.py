#!/usr/bin/env python3
"""Run a repo workflow template against ComfyUI over its HTTP API.

The MCP bridge on 127.0.0.1:9000 is the normal route; this is the direct
fallback for when it is not running. Same templates, same PARAM_ substitution
rules, so a run here and a run through MCP produce the same graph.

  python3 scripts/comfy_run.py char_ipadapter \
      --set PROMPT="..." --set CHARACTER_REF=momoka_ref_face.png \
      --set FILENAME_PREFIX=momoka_expr_1 \
      --upload wiki/assets/characters/momoka/ref/momoka_ref_face.png \
      --out wiki/assets/characters/momoka/expr/momoka_expr_1_stage1.png
"""
import argparse, json, mimetypes, os, sys, time, urllib.request, uuid
from urllib.error import HTTPError

SERVER = os.environ.get("COMFYUI_URL", "http://192.168.40.23:8188")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# PARAM_INT_x / PARAM_FLOAT_x carry a type; PARAM_x is a plain string.
CASTS = {"INT": int, "FLOAT": float}


def api(path, data=None, headers=None, raw=False):
    req = urllib.request.Request(SERVER + path, data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=600) as r:
        return r.read() if raw else json.load(r)


def upload(path):
    """Push a local file into ComfyUI's input dir; LoadImage only sees that dir."""
    name = os.path.basename(path)
    boundary = uuid.uuid4().hex
    ctype = mimetypes.guess_type(path)[0] or "application/octet-stream"
    body = b"".join([
        f'--{boundary}\r\nContent-Disposition: form-data; name="image"; filename="{name}"\r\n'
        f"Content-Type: {ctype}\r\n\r\n".encode(),
        open(path, "rb").read(),
        f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\ntrue\r\n".encode(),
        f"--{boundary}--\r\n".encode(),
    ])
    api("/upload/image", body, {"Content-Type": f"multipart/form-data; boundary={boundary}"})
    return name


def substitute(graph, values):
    """Replace PARAM_ placeholders in place, casting by the INT_/FLOAT_ infix."""
    missing = []
    for node in graph.values():
        for key, val in node.get("inputs", {}).items():
            if not (isinstance(val, str) and val.startswith("PARAM_")):
                continue
            rest = val[len("PARAM_"):]
            head, _, tail = rest.partition("_")
            cast, name = (CASTS[head], tail) if head in CASTS else (str, rest)
            if name not in values:
                missing.append(name)
                continue
            node["inputs"][key] = cast(values[name])
    return missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workflow")
    ap.add_argument("--set", action="append", default=[], metavar="NAME=VALUE")
    ap.add_argument("--upload", action="append", default=[])
    ap.add_argument("--out", help="save the first output image here")
    args = ap.parse_args()

    for path in args.upload:
        print(f"  uploaded {upload(os.path.join(ROOT, path))}")

    values = dict(kv.split("=", 1) for kv in args.set)
    values.setdefault("SEED", str(uuid.uuid4().int % (2**31)))
    graph = json.load(open(os.path.join(ROOT, "workflows", args.workflow + ".json")))

    missing = substitute(graph, values)
    if missing:
        sys.exit(f"missing required params: {sorted(set(missing))}")

    payload = json.dumps({"prompt": graph, "client_id": uuid.uuid4().hex}).encode()
    try:
        pid = api("/prompt", payload, {"Content-Type": "application/json"})["prompt_id"]
    except HTTPError as e:
        sys.exit(f"ComfyUI rejected the graph:\n{e.read().decode()[:2000]}")
    print(f"  queued {pid} (seed {values['SEED']})")

    for _ in range(600):
        hist = api(f"/history/{pid}")
        if pid in hist:
            break
        time.sleep(2)
    else:
        sys.exit("timed out waiting for the run to finish")

    entry = hist[pid]
    if (status := entry.get("status", {})).get("status_str") == "error":
        sys.exit("run failed:\n" + json.dumps(status.get("messages", []), indent=2)[:3000])

    images = [i for o in entry["outputs"].values() for i in o.get("images", [])]
    if not images:
        sys.exit("run produced no images")
    for img in images:
        print(f"  output {img['subfolder']}/{img['filename']}")
    if args.out:
        i = images[0]
        q = f"?filename={i['filename']}&subfolder={i['subfolder']}&type={i['type']}"
        dest = os.path.join(ROOT, args.out)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "wb").write(api("/view" + q, raw=True))
        print(f"  saved {args.out}")


if __name__ == "__main__":
    main()
