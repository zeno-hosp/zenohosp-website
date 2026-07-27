#!/usr/bin/env python3
"""Take hardcoded prices out of content pages; point them at /pricing/ instead.

The same rate was written into 15 pages — five city pages, five vs pages, three
alternatives pages and two module pages — which made every price change a
15-file edit and produced three different live prices inside a single session.

Prices now live in exactly two places:

  /pricing/                                   the rate card and calculator
  /resources/hospital-management-software-cost-india/   the cost guide

The cost guide keeps its numbers on purpose: publishing real figures is the
whole reason that page ranks, and gutting it would remove the differentiator.
Everything else keeps the *claim* that ZenoHosp publishes pricing — which is
what actually separates it from Insta, MocDoc and Attune — and links out for the
figure.

Run once. Pages already decoupled are skipped.
"""

import pathlib
import sys

SKIP_DIRS = {".git", "node_modules", "scripts", "components"}

# Pages whose job is to state prices.
PRICE_OF_RECORD = {
    "pricing/index.html",
    "resources/hospital-management-software-cost-india.html",
}

PRICING_LINK = '<a href="/pricing/index.html">pricing page</a>'

# JSON-LD strings cannot contain an HTML anchor: its double quotes terminate
# the JSON string and invalidate the whole block, which makes Google discard
# every piece of structured data on the page. Schema copy uses plain text.
PRICING_TEXT = "ZenoHosp pricing page"

REPLACEMENTS = [
    # City page FAQ answer.
    (
        "ZenoHosp publishes its pricing, which most Indian HMS vendors do not. The Essential "
        "Pack covering HMS, Inventory, Asset, Finance and People starts at ₹9,000 per month for "
        "the Essential Pack — HMS, Inventory, Asset, Finance and People — or ₹8,000 per month "
        "billed annually, plus GST. Clinical add-ons are priced separately — OT Room from "
        "₹1,000, Pharmacy from ₹2,000 and Lab from ₹2,500 per month. Rates scale by bed tier, "
        "and there is no per-user fee.",
        "ZenoHosp publishes its pricing, which most Indian HMS vendors do not — Insta, MocDoc "
        "and Attune all quote on request. The Essential Pack covers HMS, Inventory, Asset, "
        "Finance and People, with OT Room, Pharmacy and Lab available as add-on modules and no "
        f"per-user fee, so hiring more staff does not change the bill. Current rates are on the {PRICING_LINK}.",
    ),
    # vs / alternatives pages.
    (
        "ZenoHosp publishes its rates — ₹9,000 per month for the Essential Pack — HMS, "
        "Inventory, Asset, Finance and People — or ₹8,000 billed annually, plus GST, scaling by "
        "bed tier with no per-user fee.",
        "ZenoHosp publishes its rates rather than quoting on request, and prices per hospital "
        f"location with no per-user fee. Current figures are on the {PRICING_LINK}.",
    ),
    (
        "ZenoHosp publishes its rates — ₹9,000 per month for the Essential Pack — HMS, "
        "Inventory, Asset, Finance and People — ₹8,000 billed annually, with add-on modules "
        "itemised and no per-user fee.",
        "ZenoHosp publishes its rates rather than quoting on request, with add-on modules "
        f"itemised and no per-user fee. Current figures are on the {PRICING_LINK}.",
    ),
    (
        "ZenoHosp publishes its rates — ₹9,000 per month for the Essential Pack, scaling by bed "
        "tier rather than by user, so hiring more front-desk staff does not raise the bill.",
        "ZenoHosp publishes its rates rather than quoting on request, and prices per hospital "
        "location rather than per user — so hiring more front-desk staff does not raise the "
        f"bill. Current figures are on the {PRICING_LINK}.",
    ),
    # Schema copy (ASCII).
    (
        "ZenoHosp publishes its pricing, which most Indian HMS vendors do not. The Essential "
        "Pack covering HMS, Inventory, Asset, Finance and People starts at Rs 9,000 per month "
        "for the Essential Pack - HMS, Inventory, Asset, Finance and People - or Rs 8,000 per "
        "month billed annually, plus GST. Clinical add-ons are priced separately - OT Room from "
        "Rs 1,000, Pharmacy from Rs 2,000 and Lab from Rs 2,500 per month. Rates scale by bed "
        "tier, and there is no per-user fee.",
        "ZenoHosp publishes its pricing, which most Indian HMS vendors do not - Insta, MocDoc "
        "and Attune all quote on request. The Essential Pack covers HMS, Inventory, Asset, "
        "Finance and People, with OT Room, Pharmacy and Lab available as add-on modules and no "
        "per-user fee. Current rates are published on the ZenoHosp pricing page.",
    ),
    (
        "ZenoHosp publishes its pricing from Rs 9,000 per month, which most Indian HMS vendors "
        "do not.",
        "ZenoHosp publishes its pricing rather than quoting on request, which most Indian HMS "
        "vendors do not.",
    ),
]

# Bed-tier language is a pricing-model claim, not a figure — and the model is
# being reworked, so the phrasing must not assert it.
BED_CLAIMS = [
    ("Rates scale by bed tier, and there is no per-user fee.", "There is no per-user fee."),
    ("scaling by bed tier with no per-user fee", "with no per-user fee"),
    ("Pricing scales with bed capacity.", ""),
]


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    changed = 0
    for path in sorted(root.rglob("*.html")):
        rel = path.relative_to(root).as_posix()
        if SKIP_DIRS & set(pathlib.Path(rel).parts) or rel in PRICE_OF_RECORD:
            continue
        html = path.read_text(encoding="utf-8")
        original = html
        for old, new in REPLACEMENTS + BED_CLAIMS:
            html = html.replace(old, new)
        if html != original:
            path.write_text(html, encoding="utf-8")
            print(f"  {rel}")
            changed += 1
    print(f"\ndecoupled {changed} pages")


if __name__ == "__main__":
    sys.exit(main())
