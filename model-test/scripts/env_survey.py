#!/usr/bin/env python3
"""Section 1: environment survey -> results/00_environment.md  (read-only; changes nothing)

  python3 scripts/env_survey.py                         # API only (works over LAN)
  python3 scripts/env_survey.py --comfy-dir D:/ComfyUI  # + file sizes, custom_nodes dir listing

Run it on the GPU machine to also get nvidia-smi / RAM figures.
"""
import argparse, os, platform, shutil, subprocess, sys

sys.path.insert(0, os.path.dirname(__file__))
import comfy  # noqa: E402

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDERS = ["diffusion_models", "unet", "text_encoders", "clip", "vae", "checkpoints", "loras", "controlnet"]
# Node classes the plan depends on. Missing ones are reported, never installed.
NODES = {
    "UNETLoader": "diffusion_models 読み込み（Klein / Anima）",
    "CLIPLoader": "単体テキストエンコーダー読み込み",
    "VAELoader": "VAE 読み込み",
    "CheckpointLoaderSimple": "SDXL チェックポイント",
    "LoraLoader": "キャラ LoRA",
    "UnetLoaderGGUF": "GGUF 版 diffusion model（ComfyUI-GGUF）",
    "CLIPLoaderGGUF": "GGUF 版テキストエンコーダー（ponpoke Q4_K_M/Q6_K 用, ComfyUI-GGUF）",
    "ControlNetLoader": "ControlNet",
    "Canny": "Canny 前処理（標準ノード）",
    "ReferenceLatent": "FLUX.2 系の参照画像編集（差分作成）",
}


def human(n):
    for u in ["B", "KB", "MB", "GB"]:
        if n < 1024:
            return f"{n:.1f} {u}"
        n /= 1024
    return f"{n:.1f} TB"


def sh(cmd):
    if not shutil.which(cmd[0]):
        return None
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception as e:
        return f"(error: {e})"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--comfy-dir", help="ComfyUI のインストール先（ローカル実行時のみ）")
    args = ap.parse_args()
    md = ["# 00 環境調査", "", f"- 調査元ホスト: `{platform.node()}` ({platform.system()} {platform.release()})",
          f"- ComfyUI URL: `{comfy.SERVER}`", ""]

    md += ["## GPU / メモリ", ""]
    smi = sh(["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"])
    md.append(f"- nvidia-smi: {smi or '（このホストに無し。GPU 機で実行すると取得）'}")
    try:
        import psutil  # optional
        md.append(f"- メインメモリ: {human(psutil.virtual_memory().total)}")
    except ImportError:
        if os.path.exists("/proc/meminfo"):
            kb = int(open("/proc/meminfo").readline().split()[1])
            md.append(f"- メインメモリ: {human(kb * 1024)}")
        else:
            md.append("- メインメモリ: （psutil 未導入のため未取得）")

    stats = comfy.reachable()
    md += ["", "## ComfyUI API", ""]
    if not stats:
        md.append(f"- **接続できない**: `{comfy.SERVER}/system_stats`")
        write(md)
        sys.exit(f"ComfyUI に接続できません: {comfy.SERVER}")
    sysi = stats.get("system", {})
    ver = sysi.get("comfyui_version", "?")
    md += [f"- 接続: OK", f"- ComfyUI バージョン: **{ver}**（FLUX 3 Klein は 0.41 以降が必要とされる）",
           f"- Python: {sysi.get('python_version', '?').split()[0]} / PyTorch: {sysi.get('pytorch_version', '?')}",
           f"- 起動引数: `{' '.join(sysi.get('argv', []))}`"]
    for d in stats.get("devices", []):
        md.append(f"- デバイス: {d.get('name')} — VRAM {human(d.get('vram_total', 0))}"
                  f"（空き {human(d.get('vram_free', 0))}）")
    if sysi.get("ram_total"):
        md.append(f"- ComfyUI 側メインメモリ: {human(sysi['ram_total'])}")

    md += ["", "## models/ の中身", ""]
    for f in FOLDERS:
        try:
            files = comfy.api(f"/models/{f}", timeout=15)
        except Exception:
            files = None
        if files is None:
            md.append(f"### {f}\n\n（API で取得できず）\n")
            continue
        md.append(f"### {f}（{len(files)} 件）\n")
        for name in files:
            size = ""
            if args.comfy_dir:
                p = os.path.join(args.comfy_dir, "models", f, name)
                if os.path.exists(p):
                    size = f" — {human(os.path.getsize(p))}"
            md.append(f"- `{name}`{size}")
        md.append("")

    info = comfy.api("/object_info", timeout=60)
    md += ["## 必要ノードの有無", "", "| ノード | 用途 | 有無 |", "|---|---|---|"]
    for cls, why in NODES.items():
        md.append(f"| `{cls}` | {why} | {'○' if cls in info else '**×**'} |")
    clip = info.get("CLIPLoader", {}).get("input", {}).get("required", {}).get("type")
    if clip:
        md += ["", f"- `CLIPLoader` の type 選択肢: {', '.join(map(str, clip[0]))}",
               "  （flux2 / qwen 系 / anima 相当があるかでモデル対応状況が分かる）"]
    packs = sorted({v.get("python_module", "").split(".")[1] for v in info.values()
                    if v.get("python_module", "").startswith("custom_nodes.")})
    md += ["", "## 導入済み custom_nodes（ノード登録元）", ""] + [f"- {p}" for p in packs]
    if args.comfy_dir and os.path.isdir(os.path.join(args.comfy_dir, "custom_nodes")):
        md += ["", "custom_nodes/ ディレクトリ:", ""] + [
            f"- {d}" for d in sorted(os.listdir(os.path.join(args.comfy_dir, "custom_nodes")))]

    md += ["", "## 不足リスト（手動で記入・確認してから DL）", "",
           "| 略称 | ファイル | 配布元 URL | サイズ | 置き場所 | 許可 |", "|---|---|---|---|---|---|",
           "| M9 |  |  |  | diffusion_models |  |",
           "| ENC-ponpoke |  |  |  | text_encoders |  |",
           "| K3 |  |  |  | diffusion_models |  |", "| ANI |  |  |  | diffusion_models |  |", "",
           "合計ダウンロード容量: "]
    write(md)


def write(md):
    out = os.path.join(HERE, "results", "00_environment.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write("\n".join(md) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
