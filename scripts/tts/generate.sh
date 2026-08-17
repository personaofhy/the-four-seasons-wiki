#!/usr/bin/env bash
# キャラクターボイス生成ワンライナー（Irodori-TTS / VoiceDesign）。
#
# セリフのテキストは AI が書いたものでも、自分で書いた原稿でも構わない
# ——このスクリプトはテキストの出所を問わない。声質（caption）は
# scripts/tts/voices.yaml のキャラクター別プリセットから引く。
#
# Usage:
#   scripts/tts/generate.sh <character_id> <出力名(拡張子なし)> "<セリフ>" [--caption "声質指定を上書き"]
#
# 例:
#   scripts/tts/generate.sh kaede greeting-01 "遠山楓です。よろしくお願いします。"
#   scripts/tts/generate.sh hiiragi my-script-03 "$(cat draft.txt)" --caption "もっと震えた声で"
#
# 出力:
#   wiki/assets/characters/<character_id>/voice/<出力名>.mp3
#   （そのままキャラクターページに ![[<出力名>.mp3]] で貼り付け可能）
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
IMAGE_TAG="four-seasons-tts:latest"

CHARACTER_ID="${1:?character_id を指定してください（例: kaede）。scripts/tts/voices.yaml 参照}"
SLUG="${2:?出力ファイル名を指定してください（拡張子なし、例: greeting-01）}"
TEXT="${3:?セリフのテキストを指定してください}"
shift 3 || true

CAPTION_OVERRIDE=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --caption)
      CAPTION_OVERRIDE="${2:?}"
      shift 2
      ;;
    *)
      echo "unknown option: $1" >&2
      exit 1
      ;;
  esac
done

if ! docker image inspect "$IMAGE_TAG" >/dev/null 2>&1; then
  echo "Dockerイメージ (${IMAGE_TAG}) が見つかりません。先に実行してください:" >&2
  echo "  scripts/tts/setup.sh" >&2
  exit 1
fi

if [[ -n "$CAPTION_OVERRIDE" ]]; then
  CAPTION="$CAPTION_OVERRIDE"
else
  CAPTION="$(cd "$ROOT_DIR" && python3 - "$CHARACTER_ID" <<'PY'
import sys, pathlib
import yaml

character_id = sys.argv[1]
voices = yaml.safe_load(pathlib.Path("scripts/tts/voices.yaml").read_text())
entry = voices.get(character_id)
if entry is None:
    known = ", ".join(sorted(voices.keys()))
    sys.exit(f"'{character_id}' が scripts/tts/voices.yaml に見つかりません（登録済み: {known}）")
print(entry["caption"].strip())
PY
)"
fi

OUT_DIR="$ROOT_DIR/wiki/assets/characters/$CHARACTER_ID/voice"
mkdir -p "$OUT_DIR"

echo "▶ 生成中: [$CHARACTER_ID] \"$TEXT\""
echo "  caption: $CAPTION"

docker run --rm --platform linux/amd64 \
  -v "four-seasons-tts-hf-cache:/root/.cache/huggingface" \
  -v "$OUT_DIR:/out" \
  "$IMAGE_TAG" \
  python infer.py \
    --hf-checkpoint Aratako/Irodori-TTS-v4.1-Small \
    --text "$TEXT" \
    --caption "$CAPTION" \
    --no-ref \
    --model-device cpu --codec-device cpu \
    --output-wav "/out/${SLUG}.wav"

ffmpeg -y -loglevel error -i "$OUT_DIR/${SLUG}.wav" -codec:a libmp3lame -qscale:a 3 "$OUT_DIR/${SLUG}.mp3"
rm -f "$OUT_DIR/${SLUG}.wav"

REL_PATH="wiki/assets/characters/$CHARACTER_ID/voice/${SLUG}.mp3"
echo ""
echo "✅ 完成: $REL_PATH"
echo ""
echo "キャラクターページへの貼り付け（Obsidian/Quartz どちらでも再生ボタン付きで表示される）:"
echo "  ![[${SLUG}.mp3]]"
