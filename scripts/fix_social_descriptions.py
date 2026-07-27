#!/usr/bin/env python3
"""Restore the best available og:/twitter: title and description per page.

fix_brand_entity_seo.py collapses duplicate Open Graph blocks by letting the
later tag win. That is right for the homepage but wrong for the app feature
pages, where the later block is generic boilerplate ("ZenoHosp is an advanced
Hospital Management System (HMS). Discover ...") and the earlier one was the
hand-written, page-specific copy.

This pass repairs that. It gathers every candidate description the page has
ever carried — including the ones in git HEAD, before the collapse — and picks
the most useful, preferring copy that is neither boilerplate nor truncated.
Titles are simply mirrored from <title>, which is always page-specific.
"""

import pathlib
import re
import subprocess
import sys

BOILERPLATE = re.compile(
    r"^ZenoHosp is an advanced Hospital Management System \(HMS\)\. Discover ",
)

SKIP_DIRS = {".git", "node_modules", "scripts", "components"}

TITLE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
META_DESC = re.compile(r'<meta\s+name="description"\s*\n?\s*content="([^"]*)"', re.I)
OG_DESC_ANY = re.compile(
    r'(?:property="og:description"\s*\n?\s*content="([^"]*)"'
    r'|content="([^"]*)"\s*\n?\s*property="og:description")',
    re.I,
)


def score(text):
    """Higher is better. Boilerplate and truncated copy are last resorts."""
    if not text:
        return (-1, 0)
    tier = 2
    if text.rstrip().endswith("..."):
        tier = 1
    if BOILERPLATE.match(text):
        tier = 0
    return (tier, len(text))


def git_head(rel):
    try:
        return subprocess.run(
            ["git", "show", f"HEAD:{rel}"],
            capture_output=True, text=True, check=True,
        ).stdout
    except subprocess.CalledProcessError:
        return ""


def attr_safe(text):
    """Make a value safe to sit inside a double-quoted HTML attribute."""
    return text.replace('"', "&quot;")


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    changed = 0

    for path in sorted(root.rglob("*.html")):
        rel = path.relative_to(root).as_posix()
        if SKIP_DIRS & set(pathlib.Path(rel).parts):
            continue

        html = path.read_text(encoding="utf-8")
        if 'property="og:description"' not in html and 'property="og:title"' not in html:
            continue

        original = html

        # --- title: mirror <title> ---
        t = TITLE.search(html)
        if t:
            title = attr_safe(" ".join(t.group(1).split()))
            html = re.sub(
                r'(property="og:title" content=")[^"]*(")',
                lambda m: m.group(1) + title + m.group(2),
                html,
            )
            html = re.sub(
                r'(property="twitter:title" content=")[^"]*(")',
                lambda m: m.group(1) + title + m.group(2),
                html,
            )

        # --- description: best candidate across current file and git HEAD ---
        candidates = []
        for src in (html, git_head(rel)):
            if not src:
                continue
            m = META_DESC.search(src)
            if m:
                candidates.append(m.group(1))
            for om in OG_DESC_ANY.finditer(src):
                candidates.append(om.group(1) or om.group(2))

        candidates = [c for c in candidates if c]
        if candidates:
            best = attr_safe(max(candidates, key=score))
            html = re.sub(
                r'(property="og:description" content=")[^"]*(")',
                lambda m: m.group(1) + best + m.group(2),
                html,
            )
            html = re.sub(
                r'(property="twitter:description" content=")[^"]*(")',
                lambda m: m.group(1) + best + m.group(2),
                html,
            )

        if html != original:
            path.write_text(html, encoding="utf-8")
            changed += 1

    print(f"repaired social title/description on {changed} pages")


if __name__ == "__main__":
    sys.exit(main())
