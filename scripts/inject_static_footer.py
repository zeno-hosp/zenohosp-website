#!/usr/bin/env python3
"""
inject_static_footer.py — server-side-render the footer for SEO.

The site footer is a client-side web component (<zeno-footer> filled in by
js/components/footer.js), so crawlers reading raw HTML see ZERO footer links —
the site-wide internal link graph is invisible to them. This script extracts the
template literal from footer.js (single source of truth) and inlines it as
static child content of every <zeno-footer> element. When JS runs,
connectedCallback overwrites it with identical markup, so there is no visual or
behavioural change — but crawlers now see all footer links in the raw HTML.

Idempotent: re-running replaces the previously injected block with the current
footer.js template, so footer.js edits propagate by re-running this script.

Usage:
    python3 scripts/inject_static_footer.py            # dry run
    python3 scripts/inject_static_footer.py --apply    # write
"""
import glob, os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLY = "--apply" in sys.argv


def footer_template():
    js = open(os.path.join(BASE, "js", "components", "footer.js"), encoding="utf-8").read()
    m = re.search(r"this\.innerHTML\s*=\s*`(.*?)`;", js, re.S)
    if not m:
        sys.exit("could not find template literal in footer.js")
    return m.group(1).strip()


def main():
    tpl = footer_template()
    pages = [p for p in sorted(glob.glob(os.path.join(BASE, "**", "*.html"), recursive=True))
             if os.sep + ".git" + os.sep not in p and os.sep + "components" + os.sep not in p]
    changed = 0
    for p in pages:
        h = open(p, encoding="utf-8", errors="ignore").read()
        if "<zeno-footer" not in h:
            continue
        out = re.sub(r"<zeno-footer>.*?</zeno-footer>",
                     "<zeno-footer>\n" + tpl + "\n</zeno-footer>",
                     h, flags=re.S)
        if out != h:
            changed += 1
            if APPLY:
                open(p, "w", encoding="utf-8").write(out)
    print(f"=== inject_static_footer — {'APPLIED' if APPLY else 'DRY RUN'} ===")
    print(f"pages updated: {changed}")


if __name__ == "__main__":
    main()
