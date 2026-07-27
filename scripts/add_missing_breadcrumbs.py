#!/usr/bin/env python3
"""Add BreadcrumbList schema to pages that lack it.

144 of 214 pages already carry breadcrumb markup from an earlier pass; the
remaining 70 — including every blog post, the compare cluster and the city
pages — do not. Breadcrumbs change how the URL line renders in search results
(a readable trail instead of a raw path) and give Google an explicit statement
of where a page sits in the hierarchy.

The trail is derived from the URL path, with human labels for known segments.
Pages that should not be indexed at all are skipped.
"""

import html as H
import json
import pathlib
import re
import sys

BASE = "https://www.zenohosp.com"
SKIP_DIRS = {".git", "node_modules", "scripts", "components"}

# Pages deliberately kept out of the index — no breadcrumbs needed.
SKIP_FILES = {
    "google8d5ba0a9486bf4c0.html",
    "blog/post-template.html",
    "thank-you/index.html",
}

LABELS = {
    "apps": "Products",
    "hms": "HMS",
    "ot-room": "OT Room",
    "hms-software": "HMS by City",
    "compare": "Compare",
    "resources": "Resources",
    "blog": "Blog",
    "customers": "Customers",
    "solutions": "Solutions",
    "services": "Services",
    "about-us": "About Us",
    "contact-us": "Contact Us",
    "for-doctors": "For Doctors",
    "for-founders": "For Founders",
    "trust-center": "Trust Center",
    "privacy-policy": "Privacy Policy",
    "terms-of-service": "Terms of Service",
    "cookie-policy": "Cookie Policy",
    "why-us": "Why Us",
    "india": "Built for India",
    "help": "Help Centre",
    "docs": "Docs",
    "pricing": "Pricing",
    "careers": "Careers",
    "partners": "Partners",
    "security": "Security",
    "status": "Status",
    "features": "Features",
}


# Title-casing a slug mangles the acronyms this domain is full of: "abdm" must
# not become "Abdm". Restored after title-casing.
ACRONYMS = {
    "Abdm": "ABDM", "Hms": "HMS", "Ot": "OT", "Gst": "GST", "Fifo": "FIFO",
    "Fefo": "FEFO", "Ipd": "IPD", "Opd": "OPD", "Emr": "EMR", "Hr": "HR",
    "Roi": "ROI", "Nabh": "NABH", "Tpa": "TPA", "Amc": "AMC", "Lis": "LIS",
    "Pacs": "PACS", "Abha": "ABHA", "Dpdp": "DPDP", "Ai": "AI", "Vs": "vs",
    "Ent": "ENT", "Dss": "DSS", "Grn": "GRN", "Po": "PO", "Pf": "PF",
    "Esi": "ESI", "Pt": "PT", "Mis": "MIS", "Faq": "FAQ", "Hipaa": "HIPAA",
}


def titleise(slug):
    words = slug.replace("-", " ").title().split()
    return " ".join(ACRONYMS.get(w, w) for w in words)


def label_for(segment, html):
    """Prefer a known label, then the page's own <h1>, then a title-cased slug."""
    if segment in LABELS:
        return LABELS[segment]
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    if h1:
        # Unescape: the label goes into JSON-LD, where "&amp;" would be literal.
        text = " ".join(H.unescape(re.sub(r"<[^>]+>", " ", h1.group(1))).split())
        # Long editorial headlines make poor breadcrumb labels, and some case
        # studies use a customer pull-quote as the H1 — neither names the page.
        if text and len(text) <= 70 and not text.lstrip().startswith(('"', "\u201c", "'")):
            return text
    return titleise(segment)


def crumbs_for(rel, html):
    parts = rel.split("/")
    if parts[-1] == "index.html":
        parts = parts[:-1]
    else:
        parts[-1] = parts[-1][: -len(".html")]

    trail = [{"name": "Home", "url": BASE + "/"}]
    acc = ""
    for i, seg in enumerate(parts):
        acc += "/" + seg
        last = i == len(parts) - 1
        trail.append({
            "name": label_for(seg, html) if last else LABELS.get(seg, titleise(seg)),
            "url": f"{BASE}{acc}/",
        })
    return trail


def main():
    dry = "--dry-run" in sys.argv
    root = pathlib.Path(__file__).resolve().parent.parent
    added = 0

    for path in sorted(root.rglob("*.html")):
        rel = path.relative_to(root).as_posix()
        if SKIP_DIRS & set(pathlib.Path(rel).parts) or rel in SKIP_FILES:
            continue
        html = path.read_text(encoding="utf-8")
        if "BreadcrumbList" in html or rel == "index.html":
            continue

        trail = crumbs_for(rel, html)
        if len(trail) < 2:
            continue

        schema = json.dumps({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": c["name"], "item": c["url"]}
                for i, c in enumerate(trail)
            ],
        }, indent=2, ensure_ascii=False)

        print(f"  {rel}\n      {' > '.join(c['name'] for c in trail)}")
        if not dry:
            html = html.replace(
                "</head>",
                f'  <script type="application/ld+json">\n{schema}\n</script>\n</head>',
                1,
            )
            path.write_text(html, encoding="utf-8")
        added += 1

    print(f"\n{'would add' if dry else 'added'} breadcrumbs to {added} pages")


if __name__ == "__main__":
    sys.exit(main())
