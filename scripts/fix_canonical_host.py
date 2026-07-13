#!/usr/bin/env python3
"""
fix_canonical_host.py — align every absolute self-URL with production's real
URL format.

Production (Vercel, cleanUrls + trailingSlash + www as primary domain) serves
exactly one 200 form:   https://www.zenohosp.com/<path>/
Everything else 308-redirects:  apex -> www,  /x.html -> /x/,  /x -> /x/.

But canonicals, og:url, JSON-LD URLs, sitemap.xml and robots.txt were written
as https://zenohosp.com/<path>.html — every SEO signal pointed at a URL that
redirects twice. This script rewrites all absolute zenohosp.com URLs to the
final form:

    https://zenohosp.com/a/b.html        -> https://www.zenohosp.com/a/b/
    https://zenohosp.com/a/index.html    -> https://www.zenohosp.com/a/
    https://zenohosp.com/a/              -> https://www.zenohosp.com/a/
    https://zenohosp.com/img/x.png       -> https://www.zenohosp.com/img/x.png

Idempotent. Covers *.html, sitemap.xml, robots.txt.

Usage:  python3 scripts/fix_canonical_host.py [--apply]
"""
import glob, os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLY = "--apply" in sys.argv
ASSET_EXT = (".png", ".jpg", ".jpeg", ".svg", ".webp", ".avif", ".ico", ".css",
             ".js", ".pdf", ".xml", ".txt", ".json", ".webmanifest")

URL_RE = re.compile(r"https://(?:www\.)?zenohosp\.com([^\s\"'<>\\)]*)")


def transform(m):
    path = m.group(1) or "/"
    low = path.lower()
    if low.endswith("/index.html"):
        path = path[: -len("index.html")]
    elif low.endswith(".html"):
        path = path[: -len(".html")] + "/"
    elif not path.endswith("/") and not low.endswith(ASSET_EXT) and "#" not in path and "?" not in path:
        path = path + "/"
    return "https://www.zenohosp.com" + path


def main():
    files = [p for p in glob.glob(os.path.join(BASE, "**", "*.html"), recursive=True)
             if os.sep + ".git" + os.sep not in p and "google8d5ba0a9486bf4c0" not in p]
    files += [os.path.join(BASE, "sitemap.xml"), os.path.join(BASE, "robots.txt")]
    changed = 0
    total_urls = 0
    for p in files:
        try:
            h = open(p, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        out, n = URL_RE.subn(transform, h)
        if n and out != h:
            changed += 1
            total_urls += n
            if APPLY:
                open(p, "w", encoding="utf-8").write(out)
    print(f"=== fix_canonical_host — {'APPLIED' if APPLY else 'DRY RUN'} ===")
    print(f"files changed: {changed} | URLs rewritten: {total_urls}")


if __name__ == "__main__":
    main()
