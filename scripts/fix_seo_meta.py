#!/usr/bin/env python3
"""
fix_seo_meta.py — give every app sub-page a unique <title>, <meta description>,
and self-referencing <link rel="canonical">.

Problem it fixes: ~130 app deep-pages (docs/features/pricing/...) inherited the
generic homepage title + description, so Google treats them as duplicates. Many
feature pages ALSO already contain a good, unique og:title/og:description that a
previous SEO pass generated but never wired into the real <title>. This script:

  * feature pages  -> promote the existing specific og:title/og:description
  * docs/other     -> derive title from the page <h1>, description from 1st <p>
  * all            -> add a self-referencing canonical if missing, matching the
                      sitemap URL form (.html for non-index, trailing / for index)

Safety: only touches pages whose <title> is still the generic duplicate, so it is
idempotent (a second run is a no-op) and never overwrites already-good metadata.

Usage:
    python3 scripts/fix_seo_meta.py            # dry run (prints planned changes)
    python3 scripts/fix_seo_meta.py --apply    # write changes
"""
import glob, re, os, sys, html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
SITE = "https://zenohosp.com"
GENERIC_TITLE = "Hospital Management Software & Healthcare Solutions"
GENERIC_DESC = "Zenohosp is an advanced Hospital Management System"
APPLY = "--apply" in sys.argv

APP_NAMES = {
    "hms": "HMS", "inventory": "Inventory", "asset": "Asset", "ot-room": "OT Room",
    "finance": "Finance", "pharmacy": "Pharmacy", "lab": "Lab", "people": "People",
}


def clean(s):
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def canonical_for(rel):
    url = SITE + "/" + rel.replace(os.sep, "/")
    return url[: -len("index.html")] if url.endswith("/index.html") else url


def app_of(rel):
    parts = rel.split(os.sep)
    return APP_NAMES.get(parts[1], "") if len(parts) > 1 and parts[0] == "apps" else ""


def first_specific(pattern, head):
    for v in re.findall(pattern, head):
        if not clean(v).startswith(GENERIC_TITLE[:25]) and not clean(v).startswith(GENERIC_DESC[:25]):
            return html.unescape(v).strip()
    return None


def truncate(text, limit=158):
    text = clean(text)
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(" ,.;:") + "..."


def derive_title(head, body, app):
    og = first_specific(r'<meta property="og:title" content="([^"]*)"', head)
    if og:
        return og
    m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    if m:
        label = re.split(r"(?<=[.!?])\s", clean(m.group(1)))[0][:62].strip(" .")
        # avoid doubling the brand when the H1 already names ZenoHosp / the app
        if f"ZenoHosp {app}".lower() in label.lower() or label.lower().endswith(app.lower()):
            return label if "ZenoHosp" in label else f"{label} | ZenoHosp"
        return f"{label} | ZenoHosp {app}".strip()
    return None


def derive_desc(head, body, title, app):
    og = first_specific(r'<meta property="og:description" content="([^"]*)"', head)
    if og:
        return truncate(og)
    for p in re.findall(r"<p[^>]*>(.*?)</p>", body, re.S):
        t = clean(p)
        if len(t) >= 60 and "@type" not in t:
            return truncate(t)
    base = title.split(" | ")[0]
    return truncate(f"{base} in ZenoHosp {app}. Hospital {app.lower()} software built for Indian hospitals — GST-ready, ABDM-compliant, used by 75+ hospitals.")


def process(path):
    rel = os.path.relpath(path, BASE)
    h = open(path, encoding="utf-8", errors="ignore").read()
    split = h.find("</head>")
    head, body = h[:split], h[split:]

    mt = re.search(r"<title>(.*?)</title>", head, re.S)
    if not mt or not clean(mt.group(1)).startswith(GENERIC_TITLE[:25]):
        return None  # not a broken page — skip (idempotent)

    app = app_of(rel)
    new_title = derive_title(head, body, app)
    if not new_title:
        return None
    new_desc = derive_desc(head, body, new_title, app)
    canon = canonical_for(rel)

    out = h
    # 1) title
    out = re.sub(r"<title>.*?</title>", lambda m: f"<title>{html.escape(new_title)}</title>", out, count=1, flags=re.S)
    # 2) meta description (only the generic one)
    out = re.sub(
        r'(<meta name="description" content=")[^"]*(">)',
        lambda m: m.group(1) + html.escape(new_desc, quote=True) + m.group(2),
        out, count=1,
    )
    # 3) canonical — insert after the description tag if absent
    if 'rel="canonical"' not in out[: out.find("</head>")]:
        out = re.sub(
            r'(<meta name="description"[^>]*>)',
            lambda m: m.group(1) + f'\n  <link rel="canonical" href="{canon}">',
            out, count=1,
        )
    return rel, new_title, new_desc, canon, out, (out != h)


def main():
    pages = [p for p in sorted(glob.glob(os.path.join(BASE, "**", "*.html"), recursive=True))
             if os.sep + "components" + os.sep not in p and os.sep + ".git" + os.sep not in p]
    changed = promoted = derived = canon_added = 0
    samples = []
    for p in pages:
        r = process(p)
        if not r:
            continue
        rel, title, desc, canon, out, did = r
        if not did:
            continue
        changed += 1
        if "og:title" in open(p, encoding="utf-8", errors="ignore").read()[:3000] and " | ZenoHosp" not in title:
            promoted += 1
        else:
            derived += 1
        if APPLY:
            open(p, "w", encoding="utf-8").write(out)
        if len(samples) < 8:
            samples.append((rel, title, desc, canon))

    mode = "APPLIED" if APPLY else "DRY RUN (no files written)"
    print(f"=== fix_seo_meta — {mode} ===")
    print(f"pages fixed: {changed}\n")
    for rel, title, desc, canon in samples:
        print(f"• {rel}")
        print(f"    title : {title}")
        print(f"    desc  : {desc}")
        print(f"    canon : {canon}\n")
    if not APPLY:
        print("Re-run with --apply to write these changes.")


if __name__ == "__main__":
    main()
