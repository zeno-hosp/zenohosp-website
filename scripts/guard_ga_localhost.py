#!/usr/bin/env python3
"""
Gates the Google Analytics (gtag) tag so it only initializes on the real
zenohosp.com domain, not on localhost/127.0.0.1 during local dev/testing.

Without this guard, every page load during local development or QA
(headless browser screenshots, curl smoke tests, etc.) fires a real
pageview and event stream to the production GA4 property, since the
gtag snippet has no environment check.

Usage:
    python3 scripts/guard_ga_localhost.py          # apply
    python3 scripts/guard_ga_localhost.py --check  # dry run, report only

Safe to re-run: skips any file that already has the guard.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKER = "zenohosp\\.com$/.test(location.hostname)"

PATTERN = re.compile(
    r'<script async(?:="")? src="https://www\.googletagmanager\.com/gtag/js\?id=G-27WDP0T7BZ"></script>\n'
    r'([ \t]*)<script>\n'
    r'[ \t]*window\.dataLayer = window\.dataLayer \|\| \[\];\n'
    r"[ \t]*function gtag\(\)\s*\{\s*dataLayer\.push\(arguments\);?\s*\}\n"
    r"[ \t]*gtag\('js', new Date\(\)\);\n"
    r"[ \t]*gtag\('config', 'G-27WDP0T7BZ'\);\n"
    r"[ \t]*</script>"
)


def build_replacement(indent):
    return (
        f"{indent}<script>\n"
        f"{indent}  window.dataLayer = window.dataLayer || [];\n"
        f"{indent}  function gtag(){{dataLayer.push(arguments);}}\n"
        f"{indent}  if (/(^|\\.)zenohosp\\.com$/.test(location.hostname)) {{\n"
        f"{indent}    var gtagScript = document.createElement('script');\n"
        f"{indent}    gtagScript.async = true;\n"
        f"{indent}    gtagScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-27WDP0T7BZ';\n"
        f"{indent}    document.head.appendChild(gtagScript);\n"
        f"{indent}    gtag('js', new Date());\n"
        f"{indent}    gtag('config', 'G-27WDP0T7BZ');\n"
        f"{indent}  }}\n"
        f"{indent}</script>"
    )


def main():
    check_only = "--check" in sys.argv
    html_files = [p for p in ROOT.rglob("*.html") if ".git" not in p.parts]
    updated, skipped, no_match = 0, 0, []

    for path in html_files:
        text = path.read_text(encoding="utf-8")

        if MARKER in text:
            skipped += 1
            continue

        match = PATTERN.search(text)
        if not match:
            if "googletagmanager.com/gtag/js?id=G-27WDP0T7BZ" in text:
                no_match.append(str(path.relative_to(ROOT)))
            continue

        if check_only:
            updated += 1
            continue

        indent = match.group(1)
        new_text = text[: match.start()] + build_replacement(indent) + text[match.end():]
        path.write_text(new_text, encoding="utf-8")
        updated += 1

    label = "Would update" if check_only else "Updated"
    print(f"{label}: {updated}")
    print(f"Already guarded (skipped): {skipped}")
    if no_match:
        print(f"Has gtag but pattern didn't match, needs manual fix ({len(no_match)}):")
        for p in no_match:
            print(f"  - {p}")


if __name__ == "__main__":
    main()
