#!/usr/bin/env python3
"""
Rolls out the Meta Pixel + LinkedIn Insight Tag scaffold (see index.html)
to every HTML page on the site, once real account IDs exist.

Usage:
    python3 scripts/rollout_pixel_tracking.py META_PIXEL_ID LINKEDIN_PARTNER_ID

Where to get the IDs:
    Meta Pixel ID:        Meta Business Suite > Events Manager > Data Sources > Add > Pixel
    LinkedIn Partner ID:  LinkedIn Campaign Manager > Account Assets > Insight Tag

Safe to re-run: skips any file that already has the active tracking block.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKER = "<!-- Meta Pixel (Facebook/Instagram) -->"

GTAG_ANCHOR = re.compile(
    r"(gtag\('config', 'G-27WDP0T7BZ'\);\s*\n\s*</script>)"
)

BLOCK_TEMPLATE = """
  <!-- Meta Pixel (Facebook/Instagram) -->
  <script>
    !function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
    document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', '{meta_pixel_id}');
    fbq('track', 'PageView');
  </script>
  <noscript><img height="1" width="1" style="display:none"
    src="https://www.facebook.com/tr?id={meta_pixel_id}&ev=PageView&noscript=1" /></noscript>

  <!-- LinkedIn Insight Tag -->
  <script type="text/javascript">
    _linkedin_partner_id = "{linkedin_partner_id}";
    window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
    window._linkedin_data_partner_ids.push(_linkedin_partner_id);
  </script>
  <script type="text/javascript">
    (function(l) {{
    if (!l){{window.lintrk = function(a,b){{window.lintrk.q.push([a,b])}};
    window.lintrk.q=[]}}
    var s = document.getElementsByTagName("script")[0];
    var b = document.createElement("script");
    b.type = "text/javascript";b.async = true;
    b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
    s.parentNode.insertBefore(b, s);}})(window.lintrk);
  </script>
  <noscript>
    <img height="1" width="1" style="display:none;" alt=""
      src="https://px.ads.linkedin.com/collect/?pid={linkedin_partner_id}&fmt=gif" />
  </noscript>
"""


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    meta_pixel_id, linkedin_partner_id = sys.argv[1], sys.argv[2]
    block = BLOCK_TEMPLATE.format(
        meta_pixel_id=meta_pixel_id, linkedin_partner_id=linkedin_partner_id
    )

    html_files = [p for p in ROOT.rglob("*.html") if ".git" not in p.parts]
    updated, skipped, no_anchor = 0, 0, []

    for path in html_files:
        text = path.read_text(encoding="utf-8")

        if MARKER in text and "fbq('init'," in text:
            skipped += 1
            continue

        # index.html carries a commented-out reference copy of the scaffold;
        # strip it out exactly (by literal start/end markers, not regex,
        # since the block itself contains nested "-->" sequences that make
        # a single non-greedy regex match the wrong closing tag) so we don't
        # end up with both a dead comment and the live block in the file.
        scaffold_start = "  <!--\n    Meta Pixel (Facebook/Instagram) — SCAFFOLD"
        scaffold_end = '  <meta charset="UTF-8">'
        if scaffold_start in text:
            start = text.index(scaffold_start)
            end = text.index(scaffold_end, start)
            text = text[:start] + text[end:]

        match = GTAG_ANCHOR.search(text)
        if not match:
            no_anchor.append(str(path.relative_to(ROOT)))
            continue

        text = text[: match.end()] + block + text[match.end():]
        path.write_text(text, encoding="utf-8")
        updated += 1

    print(f"Updated: {updated}")
    print(f"Already had tracking (skipped): {skipped}")
    if no_anchor:
        print(f"No gtag anchor found, needs manual insertion ({len(no_anchor)}):")
        for p in no_anchor:
            print(f"  - {p}")


if __name__ == "__main__":
    main()
