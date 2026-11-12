#!/usr/bin/env python3
"""Section 4: consistency of edited variants (eyes closed / mouth open / expression) vs a base image.

  python3 scripts/diff_compare.py --name M9_expr outputs/M9-FP8/base.png \
      outputs/M9-FP8/eyes_closed.png outputs/M9-FP8/mouth_open.png

For each variant writes to results/diff/<name>/:
  <v>_absdiff.png   per-pixel difference (brighter = changed)
  <v>_edges.png     outline overlay: base edges red, variant edges cyan, shared edges white
  <v>_onion.png     onion skin: base 50% + variant 50%
and appends a row per variant to results/diff/<name>/metrics.md:
  mean abs diff, % of pixels changed, edge agreement (IoU of 2px-dilated edges; 1.0 = outlines identical).
For limited animation you want: low changed% outside the face, edge IoU near 1 on hair/contour.
Optional --mask face.png (white = region expected to change) to score only the rest.
"""
import argparse, os
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(path, size=None):
    im = Image.open(path).convert("RGB")
    return im.resize(size, Image.LANCZOS) if size and im.size != size else im


def edges(im, thr=40):
    e = np.asarray(im.convert("L").filter(ImageFilter.FIND_EDGES), dtype=np.uint8) > thr
    return e


def dilate(mask, r=2):
    return np.asarray(Image.fromarray(mask.astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(2 * r + 1))) > 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--mask", help="白=変化してよい領域（顔など）。それ以外だけで採点する")
    ap.add_argument("--threshold", type=int, default=24, help="変化とみなす画素差（0-255）")
    ap.add_argument("base")
    ap.add_argument("variants", nargs="+")
    a = ap.parse_args()

    out = os.path.join(HERE, "results", "diff", a.name)
    os.makedirs(out, exist_ok=True)
    base = load(a.base)
    B = np.asarray(base, dtype=np.int16)
    keep = np.ones(B.shape[:2], bool)
    if a.mask:
        keep = ~(np.asarray(load(a.mask, base.size).convert("L")) > 127)
    eb = edges(base)

    rows = []
    for vp in a.variants:
        v = load(vp, base.size)
        V = np.asarray(v, dtype=np.int16)
        tag = os.path.splitext(os.path.basename(vp))[0]
        d = np.abs(B - V).max(axis=2)
        Image.fromarray(np.clip(d * 3, 0, 255).astype(np.uint8)).save(os.path.join(out, f"{tag}_absdiff.png"))

        ev = edges(v)
        ov = np.zeros(B.shape, np.uint8)
        ov[eb] = (255, 60, 60)
        ov[ev] = (60, 220, 255)
        ov[eb & ev] = (255, 255, 255)
        Image.fromarray(ov).save(os.path.join(out, f"{tag}_edges.png"))
        Image.blend(base, v, 0.5).save(os.path.join(out, f"{tag}_onion.png"))

        db, dv = dilate(eb) & keep, dilate(ev) & keep
        iou = (db & dv).sum() / max((db | dv).sum(), 1)
        rows.append((tag, float(d[keep].mean()), float((d[keep] > a.threshold).mean() * 100), float(iou)))
        print(f"{tag}: mean|Δ| {rows[-1][1]:.2f}  changed {rows[-1][2]:.1f}%  edge IoU {iou:.3f}")

    md_path = os.path.join(out, "metrics.md")
    new = not os.path.exists(md_path)
    with open(md_path, "a", encoding="utf-8") as f:
        if new:
            f.write(f"# 差分の一貫性: {a.name}\n\n基準: `{os.path.relpath(a.base, HERE)}`"
                    f"{'  マスク: `' + a.mask + '`（マスク外のみ採点）' if a.mask else ''}\n\n"
                    "| 差分 | 平均画素差 | 変化画素 % | 輪郭一致 IoU | 目視メモ |\n|---|---|---|---|---|\n")
        for t, m, c, i in rows:
            f.write(f"| {t} | {m:.2f} | {c:.1f} | {i:.3f} |  |\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
