"""Minimal ComfyUI HTTP client shared by the model-test scripts (stdlib only).

Server address: env COMFYUI_URL, else the same LAN default as scripts/comfy_run.py.
Template rules are the same as scripts/comfy_run.py: PARAM_x (str), PARAM_INT_x,
PARAM_FLOAT_x placeholders inside node inputs are replaced at run time.
"""
import json, mimetypes, os, time, urllib.request, uuid
from urllib.error import HTTPError, URLError

SERVER = os.environ.get("COMFYUI_URL", "http://192.168.40.23:8188").rstrip("/")
CASTS = {"INT": int, "FLOAT": float}


def api(path, data=None, headers=None, raw=False, timeout=600):
    req = urllib.request.Request(SERVER + path, data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read() if raw else json.load(r)


def reachable():
    try:
        return api("/system_stats", timeout=5)
    except (URLError, HTTPError, OSError):
        return None


def upload(path):
    name = os.path.basename(path)
    boundary = uuid.uuid4().hex
    ctype = mimetypes.guess_type(path)[0] or "application/octet-stream"
    body = b"".join([
        f'--{boundary}\r\nContent-Disposition: form-data; name="image"; filename="{name}"\r\n'
        f"Content-Type: {ctype}\r\n\r\n".encode(),
        open(path, "rb").read(),
        f'\r\n--{boundary}\r\nContent-Disposition: form-data; name="overwrite"\r\n\r\ntrue\r\n'.encode(),
        f"--{boundary}--\r\n".encode(),
    ])
    api("/upload/image", body, {"Content-Type": f"multipart/form-data; boundary={boundary}"})
    return name


def substitute(graph, values):
    """Replace PARAM_ placeholders in place. Returns the names that had no value."""
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
    return sorted(set(missing))


def queue(graph):
    payload = json.dumps({"prompt": graph, "client_id": uuid.uuid4().hex}).encode()
    try:
        return api("/prompt", payload, {"Content-Type": "application/json"})["prompt_id"]
    except HTTPError as e:
        raise RuntimeError("ComfyUI rejected the graph:\n" + e.read().decode()[:3000])


def wait(pid, poll=0.5, limit=3600):
    t0 = time.time()
    while time.time() - t0 < limit:
        hist = api(f"/history/{pid}")
        if pid in hist:
            return hist[pid]
        time.sleep(poll)
    raise TimeoutError(f"prompt {pid} did not finish in {limit}s")


def exec_seconds(entry):
    """Server-side execution time from the history status messages (ms timestamps)."""
    ts = {m[0]: m[1].get("timestamp") for m in entry.get("status", {}).get("messages", [])
          if isinstance(m, list) and len(m) == 2 and isinstance(m[1], dict)}
    start, end = ts.get("execution_start"), ts.get("execution_success")
    return (end - start) / 1000 if start and end else None


def images(entry):
    return [i for o in entry.get("outputs", {}).values() for i in o.get("images", [])]


def fetch_image(img):
    q = f"?filename={img['filename']}&subfolder={img['subfolder']}&type={img['type']}"
    return api("/view" + q.replace(" ", "%20"), raw=True)
