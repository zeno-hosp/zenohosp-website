#!/usr/bin/env python3
"""Put the walkthrough video on the eight module pages.

Same facade as the homepage — local 14KB poster, nothing fetched from YouTube
until someone presses play — but framed per module, because a visitor on
/apps/pharmacy/ wants to know how pharmacy fits the whole, not a generic pitch.

Inserted before each page's id="features" section: after the hero has made its
claim, ahead of the feature deep-dive.

NO VideoObject schema here, deliberately. It is one video; marking it up on nine
URLs is the duplicate-video case Google warns about, and it splits the signal
rather than concentrating it. The schema stays on the homepage only.

NO timestamp deep-links either, though they would be the obvious win. The
description's chapters run to 02:20 on a 1:46 video, so they do not match the
actual edit. Once they are corrected, add a `start` parameter per module here
and `hasPart` clips to the homepage schema.
"""

import pathlib
import re
import sys

VIDEO_ID = "tbBu8-okHTc"

MODULES = {
    "hms": (
        "See HMS working with the rest of the platform",
        "Registration through discharge is the spine of the walkthrough — watch how a patient "
        "journey picks up charges from pharmacy, lab and theatre without anyone re-keying them.",
    ),
    "inventory": (
        "See Inventory working with the rest of the platform",
        "Stock is only half the problem. The walkthrough shows consumption posting against the "
        "patient bill as it leaves the store, which is where most hospitals lose the money.",
    ),
    "asset": (
        "See Asset working with the rest of the platform",
        "Equipment, maintenance schedules and room allocation sit alongside the clinical "
        "workflow in the walkthrough rather than in a separate register.",
    ),
    "ot-room": (
        "See OT Room working with the rest of the platform",
        "Watch a surgery move from scheduling to consumables to billing — the handoffs where "
        "theatre costs usually go unrecorded.",
    ),
    "finance": (
        "See Finance working with the rest of the platform",
        "Every department in the walkthrough posts to one ledger. That is the difference "
        "between a finance module and a reconciliation exercise at month end.",
    ),
    "pharmacy": (
        "See Pharmacy working with the rest of the platform",
        "Dispensing, FEFO stock movement and GST billing appear as one continuous flow in the "
        "walkthrough, not three systems handing paper between them.",
    ),
    "lab": (
        "See Lab working with the rest of the platform",
        "Test ordered from the EMR, sample tracked, result validated, report delivered — the "
        "walkthrough follows it end to end without a paper slip.",
    ),
    "people": (
        "See People working with the rest of the platform",
        "Rostering, attendance and payroll run against the same staff records the clinical "
        "modules use, so there is one source of truth for who worked when.",
    ),
}

SECTION = """
  <!-- Product walkthrough video (scripts/add_video_to_app_pages.py) -->
  <section class="home-video-section reveal" id="walkthrough">
    <div class="container">
      <div class="home-video-header">
        <h2>{heading}</h2>
        <p>{sub}</p>
      </div>

      <div class="video-facade" data-video-id="{vid}">
        <button type="button" class="video-facade-btn"
          aria-label="Play the ZenoHosp platform walkthrough, 1 minute 46 seconds">
          <picture>
            <source srcset="/images/video-walkthrough-poster.webp" type="image/webp">
            <img src="/images/video-walkthrough-poster.jpg" alt="ZenoHosp platform walkthrough"
              width="1200" height="675" loading="lazy" decoding="async">
          </picture>
          <span class="video-facade-play" aria-hidden="true">
            <svg viewBox="0 0 68 48" width="68" height="48" focusable="false">
              <path class="video-facade-play-bg"
                d="M66.52 7.74a8.6 8.6 0 0 0-6.05-6.09C55.08 0 34 0 34 0S12.92 0 7.53 1.65A8.6 8.6 0 0 0 1.48 7.74 90 90 0 0 0 0 24a90 90 0 0 0 1.48 16.26 8.6 8.6 0 0 0 6.05 6.09C12.92 48 34 48 34 48s21.08 0 26.47-1.65a8.6 8.6 0 0 0 6.05-6.09A90 90 0 0 0 68 24a90 90 0 0 0-1.48-16.26z" />
              <path d="M45 24 27 14v20z" fill="#fff" />
            </svg>
          </span>
          <span class="video-facade-duration" aria-hidden="true">1:46</span>
        </button>
      </div>

      <p class="home-video-note">
        Prefer a live demo on your own data?
        <a href="/contact-us/index.html">Book a walkthrough with our team</a>.
      </p>
    </div>
  </section>

"""

SCRIPT = """
  <script>
    // Swap the poster for the real player only when a visitor asks for it, so
    // no YouTube payload is fetched on page load.
    (function () {
      document.querySelectorAll('.video-facade').forEach(function (facade) {
        var button = facade.querySelector('.video-facade-btn');
        if (!button) return;
        button.addEventListener('click', function () {
          var id = facade.getAttribute('data-video-id');
          var frame = document.createElement('iframe');
          frame.src = 'https://www.youtube-nocookie.com/embed/' + id +
            '?autoplay=1&rel=0&modestbranding=1';
          frame.title = 'ZenoHosp platform walkthrough';
          frame.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
          frame.setAttribute('allowfullscreen', '');
          frame.setAttribute('loading', 'lazy');
          facade.classList.add('is-playing');
          facade.replaceChildren(frame);
          frame.focus();
        });
      });
    })();
  </script>
"""


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    added = 0

    for slug, (heading, sub) in MODULES.items():
        path = root / "apps" / slug / "index.html"
        if not path.exists():
            print(f"  missing: apps/{slug}/")
            continue

        html = path.read_text(encoding="utf-8")
        if "video-facade" in html:
            print(f"  already has video: apps/{slug}/")
            continue

        anchor = re.search(r'<section[^>]*id="features"', html)
        if not anchor:
            print(f"  no features anchor: apps/{slug}/")
            continue

        line_start = html.rfind("\n", 0, anchor.start()) + 1
        section = SECTION.format(heading=heading, sub=sub, vid=VIDEO_ID)
        html = html[:line_start] + section + html[line_start:]
        html = html.replace("</body>", SCRIPT + "</body>", 1)

        path.write_text(html, encoding="utf-8")
        print(f"  apps/{slug}/  —  {heading}")
        added += 1

    print(f"\nadded the walkthrough to {added} module pages")


if __name__ == "__main__":
    sys.exit(main())
