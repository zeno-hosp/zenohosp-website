#!/usr/bin/env python3
"""Repair canonical tags that point somewhere the page is not.

Every one of these tells Google "don't index me, index that instead", so the
affected pages are handing their authority away — including three blog posts
that name LinkedIn as the original. That leaks domain authority off-site, which
is the same authority the homepage needs to win brand queries.

Three unambiguous classes are repaired here:

  apps/<module>/       canonical -> /<module>/, which 301s straight back to
                       /apps/<module>/. A canonical must never name a URL that
                       redirects.
  blog posts           canonical -> a linkedin.com/pulse republication of the
                       same article, i.e. the site deindexes its own original
                       in favour of a third-party copy.
  partners, resources  canonical -> /about-us/, an unrelated page.

Deliberately NOT touched (flagged for a human, since consolidation may be
intended): apps/*/pricing/ all canonicalise to /pricing/, and
blog/post-template.html canonicalises to a real post.
"""

import pathlib
import re
import sys

BASE = "https://www.zenohosp.com"

# Pages whose canonical must simply be themselves.
SELF_CANONICAL = [
    "apps/asset/index.html",
    "apps/finance/index.html",
    "apps/hms/index.html",
    "apps/inventory/index.html",
    "apps/lab/index.html",
    "apps/ot-room/index.html",
    "apps/people/index.html",
    "apps/pharmacy/index.html",
    "blog/inventory-money-missing.html",
    "blog/patient-wait-times-discharge.html",
    "blog/revenue-left-on-table.html",
    "partners/index.html",
    "resources/index.html",
    "resources/roi-calculator/index.html",
]

CANONICAL = re.compile(r'<link[^>]*rel="canonical"[^>]*>|<link[^>]*canonical[^>]*>', re.IGNORECASE)
HREF = re.compile(r'href="([^"]*)"', re.IGNORECASE)


def canonical_url(rel_path):
    """The URL this file is actually served at, given cleanUrls + trailingSlash."""
    if rel_path == "index.html":
        return BASE + "/"
    if rel_path.endswith("/index.html"):
        return f"{BASE}/{rel_path[: -len('index.html')]}"
    return f"{BASE}/{rel_path[: -len('.html')]}/"


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    changed = 0

    for rel in SELF_CANONICAL:
        path = root / rel
        if not path.exists():
            print(f"  skip (missing): {rel}")
            continue

        html = path.read_text(encoding="utf-8")
        want = canonical_url(rel)

        m = CANONICAL.search(html)
        if not m:
            print(f"  skip (no canonical tag): {rel}")
            continue

        old_href = HREF.search(m.group(0))
        old = old_href.group(1) if old_href else "?"
        if old.rstrip("/") == want.rstrip("/"):
            continue

        new_tag = HREF.sub(f'href="{want}"', m.group(0), count=1)
        html = html[: m.start()] + new_tag + html[m.end():]

        # og:url and twitter:url advertise the same page identity; realign any
        # that still name the old address.
        html = html.replace(f'property="og:url" content="{old}"', f'property="og:url" content="{want}"')
        html = html.replace(f'property="twitter:url" content="{old}"', f'property="twitter:url" content="{want}"')

        path.write_text(html, encoding="utf-8")
        print(f"  {rel}\n      {old}  ->  {want}")
        changed += 1

    print(f"\nrepaired {changed} canonical tags")


if __name__ == "__main__":
    sys.exit(main())
