#!/usr/bin/env python3
"""Give each page one distinct search intent instead of four fighting over one.

Four pages were titled for near-identical queries around "best hospital
management software in India". Google picks a single URL per query, so
splitting the signal across four leaves all four weak.

The comparison page is made the sole target for the head commercial term,
because every result on that SERP is comparison content rather than a vendor
product page. That frees the homepage to lead with the brand — which also feeds
the separate problem of Google not recognising "Zeno Hosp" as an entity.

  homepage    -> brand-led, category second
  comparison  -> owns "best hospital management software in India"
  apps/hms    -> product/module specification, not a "best" claim
"""

import pathlib
import re
import sys

RETITLE = {
    "index.html": {
        "title": "ZenoHosp — Hospital Management Software (HMS) for Indian Hospitals",
        "description": (
            "ZenoHosp is cloud hospital management software built in India. Unify OPD, IPD, "
            "billing, pharmacy, lab, OT and EMR on one platform. Trusted by 75+ hospitals."
        ),
    },
    "resources/best-hospital-management-software-india-2026.html": {
        "title": "Best Hospital Management Software in India (2026 Comparison)",
        "description": (
            "An objective 2026 comparison of the leading hospital management software in India "
            "for 25–500 bed hospitals — features, deployment, ABDM compliance and pricing model."
        ),
    },
    "apps/hms/index.html": {
        "title": "Hospital Management System & EMR Modules | ZenoHosp",
        "description": (
            "ZenoHosp HMS covers OPD and IPD workflows, ward and bed management, EMR, discharge "
            "summaries and consolidated billing for Indian hospitals with 35+ beds."
        ),
    },
    "blog/top-10-hospital-management-software-india.html": {
        "title": "Top 10 Hospital Management Software in India (2026) | ZenoHosp",
        "description": (
            "A side-by-side look at 10 hospital management software platforms used in India in "
            "2026 — who each one suits, what it is strongest at, and how to shortlist."
        ),
    },
}


def attr_safe(text):
    return text.replace('"', "&quot;")


def set_title(html, title):
    esc = title.replace("&", "&amp;")
    html = re.sub(r"<title>.*?</title>", f"<title>{esc}</title>", html, flags=re.S)
    for prop in ("og:title", "twitter:title"):
        html = re.sub(
            rf'(property="{prop}" content=")[^"]*(")',
            lambda m: m.group(1) + attr_safe(esc) + m.group(2),
            html,
        )
    return html


def set_description(html, desc):
    safe = attr_safe(desc)
    html = re.sub(
        r'(<meta\s+name="description"\s*\n?\s*content=")[^"]*(")',
        lambda m: m.group(1) + safe + m.group(2),
        html,
        flags=re.IGNORECASE,
    )
    for prop in ("og:description", "twitter:description"):
        html = re.sub(
            rf'(property="{prop}" content=")[^"]*(")',
            lambda m: m.group(1) + safe + m.group(2),
            html,
        )
    return html


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    for rel, spec in RETITLE.items():
        path = root / rel
        if not path.exists():
            print(f"  missing: {rel}")
            continue
        html = path.read_text(encoding="utf-8")
        html = set_description(set_title(html, spec["title"]), spec["description"])
        path.write_text(html, encoding="utf-8")
        print(f"  {rel}\n      {spec['title']}")
    print("\nretitled 4 pages")


if __name__ == "__main__":
    sys.exit(main())
