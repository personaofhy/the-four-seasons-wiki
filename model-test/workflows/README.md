# workflows/

各モデルの txt2img を API 形式（ComfyUI の「Export (API)」）で置き、次の値を `PARAM_` に書き換える:

| 入力 | 置き換え |
|---|---|
| プロンプト | `"PARAM_PROMPT"` |
| シード | `"PARAM_INT_SEED"` |
| 幅 / 高さ | `"PARAM_INT_WIDTH"` / `"PARAM_INT_HEIGHT"` |
| ネガティブ（SDXL / Anima のみ） | `"PARAM_NEGATIVE"` |
| SaveImage の filename_prefix | `"PARAM_FILENAME_PREFIX"` |
| その他（steps, cfg, モデル名など） | `"PARAM_INT_STEPS"` `"PARAM_FLOAT_CFG"` `"PARAM_UNET"` など。値は `<名前>.defaults.json` か `--set` |

予定ファイル（推奨値は指示書より）:

- `m9_t2i.json` — Miraclein 9B。UNETLoader + CLIPLoader(qwen3_8b) + FLUX.2 small decoder。12 steps / euler / CFG 1.1。`PARAM_UNET` で FP8 / BF16 / GGUF を差し替え
- `m9_t2i_gguf.json` — 上記の UnetLoaderGGUF 版。CLIPLoaderGGUF にすれば ponpoke Q4_K_M / Q6_K の比較にも使える
- `k3_t2i.json` / `k3_t2i_expand.json` — FLUX 3 Klein INT8（qwen3vl_4b + flux2-vae）。プロンプト拡張なし／あり
- `anima_t2i.json` — Anima（Qwen3 0.6B + Qwen-Image VAE）
- `sdxl_t2i.json` — 既存の SDXL 最良モデル + キャラ LoRA

**まだ作っていない理由**: ノードのクラス名・入力名は ComfyUI のバージョンと導入ノードで変わる（特に FLUX 3 Klein は 0.41 以降の新ノード）。
推測で書くと投入時に弾かれるので、env_survey.py の結果（`/object_info`）を見てから実機で組む。
