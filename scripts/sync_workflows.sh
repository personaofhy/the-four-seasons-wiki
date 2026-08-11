#!/usr/bin/env bash
# Copy this repo's canonical ComfyUI workflow templates into the MCP server's
# workflow directory so they become callable via mcp__comfyui__run_workflow.
#
# Symlinks do NOT work here: WorkflowManager._safe_workflow_path() resolves the
# path and rejects anything that lands outside its own workflows dir, so the
# files must be real copies. Re-run this after editing anything in workflows/.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_DIR/workflows"
DEST="${COMFY_MCP_WORKFLOW_DIR:-$HOME/.gemini/antigravity-cli/mcp/comfyui-mcp-server/workflows}"

if [ ! -d "$DEST" ]; then
  echo "Workflow dir not found: $DEST" >&2
  echo "Set COMFY_MCP_WORKFLOW_DIR to the MCP server's workflows directory." >&2
  exit 1
fi

for f in "$SRC"/*.json; do
  cp -f "$f" "$DEST/"
  echo "synced $(basename "$f") -> $DEST"
done

echo "Done. run_workflow picks changes up immediately (mtime-based cache invalidation)."
