#!/usr/bin/env python3
"""
Upload reference images into the ComfyUI input folder.

The ComfyUI MCP server can only reference images by filename (LoadImage reads
from ComfyUI's own input dir) and has no upload tool, so any new base-ai genga
or pose reference has to be pushed over first with this script.

Usage:
    python3 scripts/upload_ref.py content/assets/base-ai/kaede_face_front_base.jpg
    python3 scripts/upload_ref.py content/assets/base-ai/*.jpg
"""

import json
import mimetypes
import os
import sys
import urllib.request

COMFYUI_URL = os.environ.get("COMFYUI_URL", "http://192.168.40.23:8188")
BOUNDARY = "----WebKitFormBoundary7MA4YWxkTrZu0gW"


def upload(filepath):
    filename = os.path.basename(filepath)
    content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    with open(filepath, "rb") as f:
        img_bytes = f.read()

    body = (
        f"--{BOUNDARY}\r\n"
        f'Content-Disposition: form-data; name="image"; filename="{filename}"\r\n'
        f"Content-Type: {content_type}\r\n\r\n"
    ).encode("utf-8") + img_bytes + f"\r\n--{BOUNDARY}--\r\n".encode("utf-8")

    req = urllib.request.Request(
        f"{COMFYUI_URL}/upload/image",
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={BOUNDARY}"},
    )
    result = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
    print(f"{filename} -> {result}")
    return result


def main():
    paths = sys.argv[1:]
    if not paths:
        print(__doc__)
        sys.exit(1)
    for path in paths:
        if not os.path.isfile(path):
            print(f"skip (not a file): {path}", file=sys.stderr)
            continue
        upload(path)


if __name__ == "__main__":
    main()
