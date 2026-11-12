#!/usr/bin/env python3
"""Batch runner: one model x (prompts x seeds), timing + peak VRAM per image.

  python3 scripts/batch_run.py --model M9-FP8 --workflow workflows/m9_t2i.json \
      --seeds 1111,2222,3333 --size 1024x1024 [--cel] [--prompts standing,hands] \
      [--set STEPS=12 --set CFG=1.1] [--free]

Template placeholders (same rules as scripts/comfy_run.py):
  required  PARAM_PROMPT  PARAM_INT_SEED  PARAM_INT_WIDTH  PARAM_INT_HEIGHT
  optional  PARAM_NEGATIVE (filled from prompts/_negative_sdxl.txt)  PARAM_FILENAME_PREFIX
  anything else via --set NAME=VALUE (or a sibling <workflow>.defaults.json {"NAME": value})

Writes
  outputs/<model>/<prompt>[_cel]_<seed>.png
  results/runs.csv         every run, appended (raw log)
  results/eval_table.md    regenerated from runs.csv; ○△× and メモ you typed are kept
  results/speed_summary.md per model/variant: cold (first, includes load) vs warm median
"""
import argparse, csv, datetime, json, os, statistics, sys, time

sys.path.insert(0, os.path.dirname(__file__))
import comfy  # noqa: E402
from vram import VramMonitor  # noqa: E402

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(HERE, *a)  # noqa: E731
RUNS = P("results", "runs.csv")
FIELDS = ["time", "model", "prompt", "seed", "width", "height", "exec_s", "wall_s", "cold",
          "peak_vram_mib", "vram_source", "workflow", "params", "output"]
EVAL_COLS = ["モデル", "プロンプト", "シード", "線の均一さ", "影の段数", "手足の破綻", "指示への追従",
             "NSFW描写", "秒数", "ピークVRAM", "メモ"]
USER_COLS = ["線の均一さ", "影の段数", "手足の破綻", "指示への追従", "NSFW描写", "メモ"]


def read(path):
    return open(path, encoding="utf-8").read().strip()


def load_prompts(names, cel):
    names = names or sorted({f[:-4] for f in os.listdir(P("prompts"))
                             if f.endswith(".txt") and not f.startswith("_")} | {"nsfw"})
    suffix = read(P("prompts", "_cel_suffix.txt")) if cel else ""
    out = []
    for n in names:
        path = P("prompts", n + ".txt")
        text = read(path) if os.path.exists(path) else ""
        if not text:
            print(f"  skip {n}: prompts/{n}.txt is missing or empty (user fills it in)")
            continue
        out.append((n + ("_cel" if cel else ""), text + suffix))
    return out


def run_one(template, values):
    graph = json.loads(json.dumps(template))
    missing = comfy.substitute(graph, values)
    if missing:
        sys.exit(f"missing params for template: {missing}  (pass with --set NAME=VALUE)")
    t0 = time.time()
    with VramMonitor() as mon:
        pid = comfy.queue(graph)
        entry = comfy.wait(pid)
    wall = time.time() - t0
    if entry.get("status", {}).get("status_str") == "error":
        raise RuntimeError(json.dumps(entry["status"].get("messages", []), ensure_ascii=False)[:3000])
    imgs = comfy.images(entry)
    if not imgs:
        raise RuntimeError("run produced no images")
    return comfy.fetch_image(imgs[0]), comfy.exec_seconds(entry), wall, mon


def append_run(row):
    new = not os.path.exists(RUNS)
    with open(RUNS, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)


def all_runs():
    if not os.path.exists(RUNS):
        return []
    return list(csv.DictReader(open(RUNS, encoding="utf-8")))


def latest_by_key(runs):
    """Latest run per (model, prompt, seed): re-runs replace older numbers in the table."""
    d = {}
    for r in runs:
        d[(r["model"], r["prompt"], r["seed"])] = r
    return d


def parse_existing_eval(path):
    kept = {}
    if not os.path.exists(path):
        return kept
    for line in open(path, encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != len(EVAL_COLS) or cells[0] in ("モデル", "---") or set(cells[0]) <= {"-"}:
            continue
        row = dict(zip(EVAL_COLS, cells))
        kept[(row["モデル"], row["プロンプト"], row["シード"])] = row
    return kept


def write_eval_table():
    path = P("results", "eval_table.md")
    kept = parse_existing_eval(path)
    rows = latest_by_key(all_runs())
    md = ["# 評価表", "",
          "- 秒数・ピークVRAM は batch_run.py が自動記入（秒数はサーバー側の実行時間。`(初回)` はモデル読み込み込み）。",
          "- 線の均一さ / 影の段数 / 手足の破綻 / 指示への追従 / NSFW描写 / メモ は**ユーザー記入欄**（○△×）。"
          "書いた内容は再生成しても保持される。", "",
          "| " + " | ".join(EVAL_COLS) + " |", "|" + "---|" * len(EVAL_COLS)]
    for key in sorted(rows):
        r = rows[key]
        sec = f"{float(r['exec_s'] or r['wall_s']):.1f}" + (" (初回)" if r["cold"] == "1" else "")
        vram = f"{float(r['peak_vram_mib']):.0f} MiB" if r["peak_vram_mib"] else "-"
        old = kept.get(key, {})
        cells = {"モデル": key[0], "プロンプト": key[1], "シード": key[2], "秒数": sec, "ピークVRAM": vram,
                 **{c: old.get(c, "") for c in USER_COLS}}
        md.append("| " + " | ".join(cells[c] for c in EVAL_COLS) + " |")
    open(path, "w", encoding="utf-8").write("\n".join(md) + "\n")


def write_speed_summary():
    groups = {}
    for r in all_runs():
        variant = "cel" if r["prompt"].endswith("_cel") else "base"
        groups.setdefault((r["model"], variant, f"{r['width']}x{r['height']}"), []).append(r)
    md = ["# 速度・メモリ（自動集計）", "",
          "| モデル | 版 | 解像度 | 初回秒数（読込込み） | 2回目以降 中央値 | 最小 | 最大 | ピークVRAM 最大 | 件数 |",
          "|---|---|---|---|---|---|---|---|---|"]
    for (m, v, res), rs in sorted(groups.items()):
        sec = lambda r: float(r["exec_s"] or r["wall_s"])  # noqa: E731
        cold = [sec(r) for r in rs if r["cold"] == "1"]
        warm = [sec(r) for r in rs if r["cold"] != "1"]
        vr = [float(r["peak_vram_mib"]) for r in rs if r["peak_vram_mib"]]
        f = lambda x: f"{x:.1f}"  # noqa: E731
        md.append(f"| {m} | {v} | {res} | {f(cold[-1]) if cold else '-'} | "
                  f"{f(statistics.median(warm)) if warm else '-'} | {f(min(warm)) if warm else '-'} | "
                  f"{f(max(warm)) if warm else '-'} | {f'{max(vr):.0f} MiB' if vr else '-'} | {len(rs)} |")
    open(P("results", "speed_summary.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="略称。出力フォルダ名と評価表のモデル列になる（例 M9-FP8）")
    ap.add_argument("--workflow", required=True, help="API 形式のワークフロー JSON（PARAM_ 入り）")
    ap.add_argument("--prompts", help="カンマ区切り。省略時は prompts/*.txt 全部")
    ap.add_argument("--seeds", default="1111,2222,3333")
    ap.add_argument("--size", default="1024x1024")
    ap.add_argument("--cel", action="store_true", help="prompts/_cel_suffix.txt を末尾に足す")
    ap.add_argument("--set", action="append", default=[], metavar="NAME=VALUE")
    ap.add_argument("--free", action="store_true",
                    help="開始前に ComfyUI の /free でモデルをアンロード（初回を確実にコールドにする）")
    ap.add_argument("--report-only", action="store_true", help="実行せず eval_table / speed_summary だけ再生成")
    args = ap.parse_args()

    if args.report_only:
        write_eval_table(); write_speed_summary(); return  # noqa: E702

    if not comfy.reachable():
        sys.exit(f"ComfyUI に接続できません: {comfy.SERVER}（COMFYUI_URL で変更可）")
    wf = os.path.join(HERE, args.workflow) if not os.path.isabs(args.workflow) else args.workflow
    template = json.load(open(wf, encoding="utf-8"))
    defaults_path = wf[:-5] + ".defaults.json"
    values = json.load(open(defaults_path)) if os.path.exists(defaults_path) else {}
    values = {k: str(v) for k, v in values.items()}
    values.update(dict(kv.split("=", 1) for kv in args.set))
    w, h = args.size.lower().split("x")
    neg = P("prompts", "_negative_sdxl.txt")
    values.setdefault("NEGATIVE", read(neg) if os.path.exists(neg) else "")

    if args.free:
        comfy.api("/free", json.dumps({"unload_models": True, "free_memory": True}).encode(),
                  {"Content-Type": "application/json"})
        time.sleep(2)

    prompts = load_prompts(args.prompts.split(",") if args.prompts else None, args.cel)
    seeds = [s.strip() for s in args.seeds.split(",")]
    os.makedirs(P("outputs", args.model), exist_ok=True)
    first = True
    for name, text in prompts:
        for seed in seeds:
            v = dict(values, PROMPT=text, SEED=seed, WIDTH=w, HEIGHT=h,
                     FILENAME_PREFIX=f"modeltest/{args.model}/{name}_{seed}")
            print(f"[{args.model}] {name} seed={seed} {w}x{h} ...", end=" ", flush=True)
            try:
                png, exec_s, wall, mon = run_one(template, v)
            except Exception as e:
                print(f"FAILED\n{e}")
                print("→ VRAM 不足・読み込みエラーなら、量子化版やオフロード設定を検討（勝手に切り替えはしない）")
                write_eval_table(); write_speed_summary()  # noqa: E702
                sys.exit(1)
            rel = os.path.join("outputs", args.model, f"{name}_{seed}.png")
            open(P(rel), "wb").write(png)
            extra = {k: values[k] for k in sorted(values) if k not in ("NEGATIVE",)}
            append_run({"time": datetime.datetime.now().isoformat(timespec="seconds"), "model": args.model,
                        "prompt": name, "seed": seed, "width": w, "height": h,
                        "exec_s": f"{exec_s:.2f}" if exec_s else "", "wall_s": f"{wall:.2f}",
                        "cold": "1" if first else "0",
                        "peak_vram_mib": f"{mon.peak_mib:.0f}" if mon.peak_mib else "",
                        "vram_source": mon.source, "workflow": args.workflow,
                        "params": json.dumps(extra, ensure_ascii=False), "output": rel})
            print(f"{exec_s or wall:.1f}s  peak {mon.peak_mib or 0:.0f} MiB{'  (初回)' if first else ''}")
            first = False
    write_eval_table()
    write_speed_summary()
    print("updated results/eval_table.md, results/speed_summary.md")


if __name__ == "__main__":
    main()
