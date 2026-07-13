#!/usr/bin/env python3
"""
optimize_images.py — Core Web Vitals fix, part 1: generate WebP siblings for
every PNG/JPG under images/.

Keeps the original file (so any hardcoded <img src="x.png"> reference and any
external hotlink keeps working) and adds an x.webp next to it. Part 2
(rewrite_img_tags.py) wraps each <img> in a <picture> that serves the WebP
first with the original as fallback.

Quality: 82 for JPEG source, lossless-ish 85 for PNG (visually indistinguishable
at web sizes, meaningfully smaller). Skips images/favicon* (tiny, not worth it)
and anything that already has a same-name .webp.

Usage: python3 scripts/optimize_images.py [--apply]
"""
import os, sys, glob
from PIL import Image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLY = "--apply" in sys.argv
SKIP_SUBSTR = ("favicon",)


def main():
    paths = [p for p in glob.glob(os.path.join(BASE, "images", "**", "*"), recursive=True)
             if p.lower().endswith((".png", ".jpg", ".jpeg"))
             and not any(s in os.path.basename(p).lower() for s in SKIP_SUBSTR)]

    total_before = total_after = 0
    converted = skipped = 0
    for p in paths:
        webp_path = os.path.splitext(p)[0] + ".webp"
        before = os.path.getsize(p)
        total_before += before
        if os.path.exists(webp_path):
            skipped += 1
            total_after += os.path.getsize(webp_path)
            continue
        if APPLY:
            img = Image.open(p)
            if img.mode in ("P", "CMYK"):
                img = img.convert("RGBA" if img.mode == "P" and "transparency" in img.info else "RGB")
            quality = 85 if p.lower().endswith(".png") else 82
            img.save(webp_path, "WEBP", quality=quality, method=6)
            after = os.path.getsize(webp_path)
        else:
            after = before  # unknown until converted; dry run just reports candidates
        total_after += after
        converted += 1
        rel = os.path.relpath(p, BASE)
        if APPLY:
            print(f"  {rel}: {before//1024}KB -> {after//1024}KB")
        else:
            print(f"  would convert: {rel} ({before//1024}KB)")

    mode = "APPLIED" if APPLY else "DRY RUN"
    print(f"\n=== optimize_images — {mode} ===")
    print(f"candidates: {converted} | already had .webp: {skipped}")
    if APPLY:
        print(f"total: {total_before//1024}KB -> {total_after//1024}KB source+webp "
              f"(pages will only ship the webp once wired in)")


if __name__ == "__main__":
    main()
