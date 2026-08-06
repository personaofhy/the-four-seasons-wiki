#!/usr/bin/env python3
"""
Pull a generated file out of ComfyUI's output folder into this vault.

ComfyUI runs on another machine, so its output directory is not reachable as a
local path - files have to come back over HTTP. Give it the filename the
workflow reported (and the subfolder, if filename_prefix contained one) and it
writes the file into the destination directory.

Usage:
    python3 scripts/fetch_output.py kaede_tpose_00001_.png \\
        --subfolder depth-maps --dest content/assets/depth-maps

    # rename on the way in
    python3 scripts/fetch_output.py kaede_tpose_00001_.png \\
        --subfolder depth-maps --dest content/assets/depth-maps \\
        --as kaede_tpose_depth.png
"""

import argparse
import os
import sys
import urllib.parse
import urllib.request

COMFYUI_URL = os.environ.get("COMFYUI_URL", "http://192.168.40.23:8188")


def fetch(filename, subfolder, folder_type, dest_dir, rename=None):
    query = urllib.parse.urlencode(
        {"filename": filename, "subfolder": subfolder, "type": folder_type}
    )
    url = f"{COMFYUI_URL}/view?{query}"

    with urllib.request.urlopen(url, timeout=120) as resp:
        data = resp.read()

    os.makedirs(dest_dir, exist_ok=True)
    out_path = os.path.join(dest_dir, rename or filename)
    with open(out_path, "wb") as f:
        f.write(data)

    print(f"{filename} -> {out_path} ({len(data):,} bytes)")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Fetch a ComfyUI output file into the vault")
    parser.add_argument("filename", help="Filename reported by the workflow result")
    parser.add_argument("--subfolder", default="", help="Subfolder inside the output dir (from filename_prefix)")
    parser.add_argument("--type", dest="folder_type", default="output",
                        choices=["output", "input", "temp"], help="ComfyUI folder type (default: output)")
    parser.add_argument("--dest", default="content/assets/intermediates", help="Local destination directory")
    parser.add_argument("--as", dest="rename", default=None, help="Save under a different filename")
    args = parser.parse_args()

    try:
        fetch(args.filename, args.subfolder, args.folder_type, args.dest, args.rename)
    except Exception as exc:
        print(f"failed: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
