#!/usr/bin/env python3
"""
optimize_images.py part 2 — wrap raster <img> tags in <picture> so browsers
fetch the WebP sibling first (falling back to the original PNG/JPG), and
lazy-load images below the first one on each page.

Scope, deliberately conservative:
  * Only <img> tags whose src resolves to a local images/*.png|jpg|jpeg that
    has a sibling .webp (produced by optimize_images.py) get wrapped.
  * SVGs and external (http) images are left untouched.
  * width/height attributes are NOT added in this pass: several pages size
    images via CSS (e.g. css/pages/blog.css's `.blog-card img{width:100%;
    height:200px}`) and a handful don't appear to constrain size via CSS at
    all. Guessing intrinsic width/height onto an unconstrained <img> could
    make it render at full pixel size and break a layout that currently
    relies on an implicit container width. That needs a visual pass per
    template, not a blind site-wide rewrite.
  * The FIRST matching raster <img> in each file is left eager (no loading
    attribute) on the assumption it's the most likely LCP candidate;
    every subsequent match gets loading="lazy". Purely a byte-size /
    fetch-priority change — no layout impact either way.

Idempotent: a <picture> already wrapping a given src is left alone.

Usage: python3 scripts/wrap_images_webp.py [--apply]
"""
import glob, os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLY = "--apply" in sys.argv
RASTER_EXT = (".png", ".jpg", ".jpeg")

IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
SRC_RE = re.compile(r'src="([^"]+)"', re.I)
PICTURE_RE = re.compile(r"<picture>.*?</picture>", re.S)


def resolve(src, html_dir):
    if src.startswith("http") or src.startswith("//"):
        return None
    path = os.path.join(BASE, src.lstrip("/")) if src.startswith("/") else os.path.join(html_dir, src)
    return os.path.normpath(path)


def process(path):
    html_dir = os.path.dirname(path)
    h = open(path, encoding="utf-8", errors="ignore").read()

    already_wrapped_srcs = set()
    for block in PICTURE_RE.findall(h):
        m = SRC_RE.search(block)
        if m:
            already_wrapped_srcs.add(m.group(1))

    count = 0
    first_seen = False

    def repl(m):
        nonlocal count, first_seen
        tag = m.group(0)
        sm = SRC_RE.search(tag)
        if not sm:
            return tag
        src = sm.group(1)
        if src in already_wrapped_srcs:
            first_seen = True
            return tag
        ext = os.path.splitext(src)[1].lower()
        if ext not in RASTER_EXT:
            return tag
        fs_path = resolve(src, html_dir)
        if not fs_path or not os.path.isfile(fs_path):
            return tag
        webp_fs = os.path.splitext(fs_path)[0] + ".webp"
        if not os.path.isfile(webp_fs):
            return tag
        webp_src = os.path.splitext(src)[0] + ".webp"

        new_tag = tag
        if first_seen:
            if "loading=" not in new_tag:
                new_tag = new_tag[:-1].rstrip("/") + ' loading="lazy" />' if new_tag.rstrip().endswith("/>") \
                    else new_tag[:-1] + ' loading="lazy">'
        else:
            first_seen = True

        count += 1
        return f'<picture><source srcset="{webp_src}" type="image/webp">{new_tag}</picture>'

    out = IMG_RE.sub(repl, h)
    return out, count


def main():
    files = [p for p in glob.glob(os.path.join(BASE, "**", "*.html"), recursive=True)
             if os.sep + ".git" + os.sep not in p and os.sep + "components" + os.sep not in p]
    total_files = total_wrapped = 0
    for p in files:
        out, count = process(p)
        if count:
            total_files += 1
            total_wrapped += count
            if APPLY:
                open(p, "w", encoding="utf-8").write(out)
            else:
                print(f"  {os.path.relpath(p, BASE)}: {count} image(s) to wrap")

    mode = "APPLIED" if APPLY else "DRY RUN"
    print(f"\n=== wrap_images_webp — {mode} ===")
    print(f"files changed: {total_files} | <img> tags wrapped: {total_wrapped}")


if __name__ == "__main__":
    main()
