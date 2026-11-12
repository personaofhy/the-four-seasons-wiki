# model-test — ComfyUI モデル比較

引き継ぎ指示書（2026-11-12）の検証用フォルダ。スクリプトは Python 標準ライブラリのみ（diff_compare.py だけ Pillow + numpy）。
接続先は `COMFYUI_URL`（既定 `http://192.168.40.23:8188`、リポジトリの `scripts/comfy_run.py` と同じ）。

## 手順

```
python3 scripts/env_survey.py --comfy-dir <ComfyUIのフォルダ>     # → results/00_environment.md（読むだけ・何も変更しない）
python3 scripts/batch_run.py --model M9-FP8 --workflow workflows/m9_t2i.json --free
python3 scripts/batch_run.py --model M9-FP8 --workflow workflows/m9_t2i.json --cel
python3 scripts/diff_compare.py --name M9_expr <基準.png> <目閉じ.png> <口開け.png>
python3 scripts/vram.py                                           # 単体で VRAM を見るとき
```

- `--free` … 開始前にモデルをアンロードして、最初の 1 枚を確実に「初回（読込込み）」にする
- 秒数は ComfyUI の履歴にある実行開始〜終了（サーバー側の時間）。待ち時間（wall）も runs.csv に残る
- ピーク VRAM は GPU 機で実行すれば nvidia-smi、LAN 越しなら `/system_stats`（他プロセス分も含む）を 500ms 間隔で取得
- 同じグラフをそのまま再投入すると ComfyUI のキャッシュで一瞬で終わるので、計測し直すときは `--free` を付ける

## 中身

| パス | 内容 |
|---|---|
| `prompts/` | テストプロンプト（`nsfw.txt` は空。ユーザーが記入） |
| `workflows/` | API 形式ワークフロー（まだ無い。workflows/README.md 参照） |
| `scripts/` | comfy.py（API クライアント）/ env_survey.py / batch_run.py / vram.py / diff_compare.py |
| `outputs/<モデル>/<プロンプト>_<シード>.png` | 生成結果 |
| `results/` | 00_environment.md / eval_table.md / speed_summary.md / runs.csv / diff/ / summary.md |
