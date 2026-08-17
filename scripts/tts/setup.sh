#!/usr/bin/env bash
# Irodori-TTS 実行用 Dockerイメージを構築する（初回のみ、または依存関係を更新したい時）
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
IMAGE_TAG="four-seasons-tts:latest"

if ! command -v docker >/dev/null 2>&1; then
  echo "docker コマンドが見つかりません。Docker Desktop をインストールしてください。" >&2
  exit 1
fi

if ! docker info >/dev/null 2>&1; then
  echo "Docker が起動していません。起動してから再実行してください。" >&2
  echo "  macOS: open -a Docker" >&2
  exit 1
fi

echo "▶ Dockerイメージ ${IMAGE_TAG} をビルドします（初回は依存関係のダウンロードで数分かかります）"
docker build --platform linux/amd64 -t "$IMAGE_TAG" -f "$ROOT_DIR/scripts/tts/Dockerfile" "$ROOT_DIR/scripts/tts"

echo ""
echo "✅ 完了。次のコマンドで音声を生成できます："
echo "   scripts/tts/generate.sh <character_id> <出力名> \"<セリフ>\""
