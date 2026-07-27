#!/usr/bin/env python3
"""Replace templated meta descriptions with copy drawn from each page.

40 pages carried the same generated sentence — "ZenoHosp is an advanced Hospital
Management System (HMS). Discover <title> for your healthcare facility." — which
tells a searcher nothing and gives Google no page-specific signal. Several are
the module and blog pages that should be pulling in commercial traffic.

Each page already opens with a lead paragraph that summarises it well, so the
description is built from that, falling back to the H1 for context when the
lead is too short to stand alone.

Pass --dry-run to review the generated copy before writing.
"""

import html as H
import pathlib
import re
import sys

BOILERPLATE = re.compile(
    r"^ZenoHosp is an advanced Hospital Management System \(HMS\)\. Discover "
)

# Descriptions scraped from the page furniture by an earlier generator. The docs
# and module pages wrap their sidebar in <div class="doc-sidebar"> rather than a
# <nav>, so whatever produced these walked straight into the menu and emitted
# "Back to Finance Dashboard Finance Bank Accounts HMS Billing ..." as the
# description. Google shows that verbatim in the SERP.
NAV_TEXT = re.compile(
    r"^(Back to |HMS Inventory Asset|HMS End-to-end|Products Solutions)", re.I
)

# Wrong page's copy: the about-us description was pasted onto unrelated pages.
MISPLACED = {"Meet the team behind ZenoHosp."}


def needs_rewrite(desc):
    d = desc.strip()
    return bool(BOILERPLATE.match(d)) or bool(NAV_TEXT.match(d)) or d in MISPLACED
SKIP_DIRS = {".git", "node_modules", "scripts", "components"}
MAX_LEN = 158

DESC_TAG = re.compile(r'(<meta\s+name="description"\s*\n?\s*content=")([^"]*)(")', re.I)
H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S | re.I)
PARA = re.compile(r"<p[^>]*>(.*?)</p>", re.S | re.I)

# Chrome that appears before the article body on some templates.
NOISE = re.compile(r"^(read more|share|book a|request a|\d+ min read)", re.I)

# Anywhere in the text, not just at the start. The cross-post notice matters:
# on three blog posts it precedes the real lead, and using it would advertise
# LinkedIn inside our own search snippet.
REJECT_ANYWHERE = re.compile(r"originally published|all rights reserved", re.I)

# Some templates leave an unclosed <picture>/<img>, so the first <p> match runs
# past its own paragraph and swallows layout markup. Those spans are not prose.
BLOCK_MARKUP = re.compile(r"<(section|div|picture|img|source|figure)\b", re.I)


def text_of(fragment):
    return " ".join(H.unescape(re.sub(r"<[^>]+>", " ", fragment)).split())


def strip_chrome(html):
    """Drop nav, footer, script and style so lead-paragraph detection is honest."""
    for tag in ("script", "style", "nav", "footer", "header"):
        html = re.sub(rf"<{tag}\b.*?</{tag}>", " ", html, flags=re.S | re.I)
    # Docs pages build their sidebar from divs, so tag-based stripping misses it.
    # Cut from the sidebar opener to the content <h1>, which always follows it.
    html = re.sub(r'<div[^>]*class="[^"]*doc-sidebar[^"]*".*?(?=<h1)', " ", html,
                  flags=re.S | re.I)
    return html


def truncate(text, limit=MAX_LEN):
    text = text.strip()
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:—-")
    return cut + "…"


MODULE_NAMES = {
    "hms": "Hospital Management System",
    "inventory": "Inventory",
    "asset": "Asset Management",
    "ot-room": "OT Room",
    "finance": "Finance",
    "pharmacy": "Pharmacy",
    "lab": "Laboratory",
    "people": "HR & Payroll",
}


def module_pricing_description(rel_parts):
    """Pricing pages share one lead paragraph, so name the module explicitly.

    Without this every apps/<module>/pricing/ page ends up with byte-identical
    copy — trading one duplication problem for another.
    """
    if len(rel_parts) < 3 or rel_parts[0] != "apps" or rel_parts[2] != "pricing":
        return None
    module = MODULE_NAMES.get(rel_parts[1])
    if not module:
        return None
    return truncate(
        f"ZenoHosp {module} module pricing for Indian hospitals. Buy the module on its own "
        f"or as part of the Essential Pack — priced per location, per month, in INR."
    )


def build_description(html):
    body = strip_chrome(html)

    h1 = H1.search(body)
    heading = text_of(h1.group(1)) if h1 else ""

    lead = ""
    start = h1.end() if h1 else 0
    for m in PARA.finditer(body, start):
        if BLOCK_MARKUP.search(m.group(1)):
            continue
        candidate = text_of(m.group(1))
        if len(candidate) < 60:
            continue
        if NOISE.match(candidate) or REJECT_ANYWHERE.search(candidate):
            continue
        # A paragraph ending in a colon introduces a list; on its own it reads as
        # a truncated sentence in the SERP. Prefer the next real paragraph.
        if candidate.rstrip().endswith(":"):
            continue
        lead = candidate
        break

    if not lead:
        return None
    if len(lead) < 90 and heading:
        lead = f"{heading}. {lead}"
    return truncate(lead)


def main():
    dry = "--dry-run" in sys.argv
    root = pathlib.Path(__file__).resolve().parent.parent
    changed = skipped = 0

    for path in sorted(root.rglob("*.html")):
        if SKIP_DIRS & set(path.relative_to(root).parts):
            continue
        html = path.read_text(encoding="utf-8")
        m = DESC_TAG.search(html)
        if not m or not needs_rewrite(m.group(2)):
            continue

        rel_parts = path.relative_to(root).parts
        desc = module_pricing_description(rel_parts) or build_description(html)
        if not desc:
            print(f"  SKIP (no usable lead paragraph): {path.relative_to(root)}")
            skipped += 1
            continue

        safe = desc.replace('"', "&quot;")
        print(f"  {path.relative_to(root)}\n      {safe}")
        if not dry:
            html = DESC_TAG.sub(lambda mm: mm.group(1) + safe + mm.group(3), html, count=1)
            # og:/twitter: descriptions mirror the meta description on this site.
            for prop in ("og:description", "twitter:description"):
                html = re.sub(
                    rf'(property="{prop}" content=")[^"]*(")',
                    lambda mm: mm.group(1) + safe + mm.group(2),
                    html,
                )
            path.write_text(html, encoding="utf-8")
        changed += 1

    verb = "would rewrite" if dry else "rewrote"
    print(f"\n{verb} {changed} descriptions, skipped {skipped}")


if __name__ == "__main__":
    sys.exit(main())
