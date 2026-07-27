#!/usr/bin/env python3
"""Describe the Essential Pack accurately — there is no HMS-only plan.

History of this file, because it has changed direction twice:

1. The pricing page title advertised "from ₹5,000/month" while the page body
   showed nothing below ₹9,000. First pass changed the title to ₹9,000 to match.
2. Told that ₹5,000 was real, an earlier version of this script rewrote 15 pages
   to say "from ₹5,000 for HMS with its dependent apps, or ₹9,000 for the full
   Essential Pack" — inventing a standalone HMS tier.
3. That tier does not exist. "HMS + Inventory + Asset + Finance + People" IS the
   Essential Pack, sold as one bundle, with module add-ons on top.

So this pass removes the fictitious HMS-only plan and restates every claim
around the single bundle. It uses ₹9,000, which is what the live page, its
calculator and its OfferCatalog schema all currently serve — NOT because that
figure is confirmed, but because publishing a number the page contradicts is
what caused this mess twice already.

UNRESOLVED, and blocking: the owner states the bundle is ₹5,000/month; the page
states ₹9,000 for the 35-80 bed tier. Until that is settled — along with the
other three tier rates if the ladder has moved — no price should be changed
again. The pricing page title is left at ₹5,000 and is the one remaining
inconsistency, deliberately visible rather than papered over.
"""

import pathlib
import sys

SKIP_DIRS = {".git", "node_modules", "scripts", "components"}

# Longest-first so no phrasing is partly consumed by a shorter prefix.
REPLACEMENTS = [
    (
        "starts at ₹5,000 per month for HMS with its dependent apps, or ₹9,000 per month for the "
        "full Essential Pack — ₹8,000 per month billed annually — plus GST",
        "starts at ₹9,000 per month for the Essential Pack — HMS, Inventory, Asset, Finance and "
        "People — or ₹8,000 per month billed annually, plus GST",
    ),
    (
        "from ₹5,000 per month for HMS with its dependent apps, or ₹9,000 for the full Essential "
        "Pack (₹8,000 billed annually), plus GST, scaling by bed tier with no per-user fee",
        "₹9,000 per month for the Essential Pack — HMS, Inventory, Asset, Finance and People — "
        "or ₹8,000 billed annually, plus GST, scaling by bed tier with no per-user fee",
    ),
    (
        "from ₹5,000 per month for HMS with its dependent apps, rising to ₹9,000 for the full "
        "Essential Pack (₹8,000 billed annually), with add-ons itemised and no per-user fee",
        "₹9,000 per month for the Essential Pack — HMS, Inventory, Asset, Finance and People — "
        "₹8,000 billed annually, with add-on modules itemised and no per-user fee",
    ),
    (
        "from ₹5,000 per month for HMS with its dependent apps and ₹9,000 for the full Essential "
        "Pack, scaling by bed tier rather than by user, so hiring more front-desk staff does not "
        "raise the bill",
        "₹9,000 per month for the Essential Pack, scaling by bed tier rather than by user, so "
        "hiring more front-desk staff does not raise the bill",
    ),
    # Schema copy carries the ASCII spelling.
    (
        "starts at Rs 5,000 per month for HMS with its dependent apps, or Rs 9,000 per month for "
        "the full Essential Pack - Rs 8,000 per month billed annually - plus GST",
        "starts at Rs 9,000 per month for the Essential Pack - HMS, Inventory, Asset, Finance and "
        "People - or Rs 8,000 per month billed annually, plus GST",
    ),
    (
        "ZenoHosp publishes its pricing from Rs 5,000 per month",
        "ZenoHosp publishes its pricing from Rs 9,000 per month",
    ),
    (
        "ZenoHosp publishes its rates. HMS can be licensed with its dependent apps from Rs 5,000 "
        "per month. The full Essential Pack covering HMS, Inventory, Asset, Finance and People is "
        "Rs 9,000 per month",
        "ZenoHosp publishes its rates. The Essential Pack covering HMS, Inventory, Asset, Finance "
        "and People is Rs 9,000 per month",
    ),
    (
        "ZenoHosp starts at <strong>₹5,000 per month</strong> for HMS with its dependent apps. "
        "The full Essential Pack — HMS, Inventory, Asset, Finance and People — is",
        "ZenoHosp's Essential Pack — HMS, Inventory, Asset, Finance and People — is",
    ),
    # Cost guide rate-card row for a plan that does not exist.
    (
        """                        <tr>
                            <td><strong>HMS</strong><br>Hospital management with its dependent apps</td>
                            <td>from ₹5,000 / month</td>
                            <td>annual rate on request</td>
                        </tr>
""",
        "",
    ),
]


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    changed = 0
    for path in sorted(root.rglob("*.html")):
        if SKIP_DIRS & set(path.relative_to(root).parts):
            continue
        # The pricing page title stays at ₹5,000 on purpose — see module docstring.
        html = path.read_text(encoding="utf-8")
        original = html
        for old, new in REPLACEMENTS:
            html = html.replace(old, new)
        if html != original:
            path.write_text(html, encoding="utf-8")
            print(f"  {path.relative_to(root)}")
            changed += 1
    print(f"\nupdated {changed} pages")


if __name__ == "__main__":
    sys.exit(main())
