#!/usr/bin/env python3
"""
add_breadcrumb_schema.py — inject BreadcrumbList JSON-LD into every app page that
lacks it, so Google can render breadcrumb rich results and better understand the
site hierarchy (Home > App > Page).

Idempotent: skips any page that already has a BreadcrumbList block.

Usage:
    python3 scripts/add_breadcrumb_schema.py            # dry run
    python3 scripts/add_breadcrumb_schema.py --apply    # write
"""
import glob, re, os, sys, json, html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.zenohosp.com"
APPLY = "--apply" in sys.argv
APP_NAMES = {
    "hms": "HMS", "inventory": "Inventory", "asset": "Asset", "ot-room": "OT Room",
    "finance": "Finance", "pharmacy": "Pharmacy", "lab": "Lab", "people": "People",
}


def url_for(rel):
    u = SITE + "/" + rel.replace(os.sep, "/")
    if u.endswith("/index.html"):
        return u[: -len("index.html")]
    return u[: -len(".html")] + "/" if u.endswith(".html") else u


def page_name(h):
    m = re.search(r"<title>(.*?)</title>", h, re.S)
    if not m:
        return None
    t = html.unescape(re.sub(r"\s+", " ", m.group(1)).strip())
    return t.split(" | ")[0].split(" - ")[0].strip()  # drop brand suffix


def build(rel, h):
    parts = rel.split(os.sep)
    if len(parts) < 2 or parts[0] != "apps":
        return None
    app = APP_NAMES.get(parts[1])
    if not app:
        return None
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    app_url = f"{SITE}/apps/{parts[1]}/"
    items.append({"@type": "ListItem", "position": 2, "name": f"{app} Software", "item": app_url})
    this_url = url_for(rel)
    if this_url.rstrip("/") != app_url.rstrip("/"):
        name = page_name(h) or app
        items.append({"@type": "ListItem", "position": 3, "name": name, "item": this_url})
    data = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(data, ensure_ascii=False, indent=2)
        + "\n</script>"
    )


def main():
    pages = [p for p in sorted(glob.glob(os.path.join(BASE, "apps", "**", "*.html"), recursive=True))]
    added = 0
    sample = []
    for p in pages:
        rel = os.path.relpath(p, BASE)
        h = open(p, encoding="utf-8", errors="ignore").read()
        if "BreadcrumbList" in h or "</head>" not in h:
            continue
        block = build(rel, h)
        if not block:
            continue
        out = h.replace("</head>", "  " + block + "\n</head>", 1)
        added += 1
        if APPLY:
            open(p, "w", encoding="utf-8").write(out)
        if len(sample) < 4:
            names = [i["name"] for i in json.loads(block[block.find("{"): block.rfind("}") + 1])["itemListElement"]]
            sample.append((rel, " > ".join(names)))
    print(f"=== breadcrumb schema — {'APPLIED' if APPLY else 'DRY RUN'} ===")
    print(f"pages to receive BreadcrumbList: {added}\n")
    for rel, trail in sample:
        print(f"• {rel}\n    {trail}")
    if not APPLY:
        print("\nRe-run with --apply to write.")


if __name__ == "__main__":
    main()
