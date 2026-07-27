#!/usr/bin/env python3
"""Embed the product walkthrough video on the homepage.

Uses a facade rather than a raw <iframe>. A YouTube iframe pulls well over a
megabyte of script and CSS on page load whether or not anyone presses play, and
this sits high on the homepage — the page whose Core Web Vitals matter most. So
the section ships a locally hosted 14KB poster and a play button, and the iframe
is only created on click. Nothing from youtube.com is requested until a visitor
actually asks for the video.

Also adds VideoObject schema. Google needs name, description, thumbnailUrl and
uploadDate to consider a page for video rich results, and "hospital management
software demo" is exactly the kind of query where a video result outranks text.

Metadata is taken from the video itself (oEmbed plus the watch page), not
invented: title, channel, upload date 2026-07-24 and duration 106s / PT1M46S.
"""

import json
import pathlib
import re
import sys

VIDEO_ID = "tbBu8-okHTc"
TITLE = "ZenoHosp — Hospital Management Software for Indian Hospitals | Full Platform Walkthrough"
DESCRIPTION = (
    "A full walkthrough of the ZenoHosp platform for Indian hospitals — how the eight "
    "connected apps work together, from patient registration and clinical workflows through "
    "billing, pharmacy, lab and radiology, operation theatre, inventory, assets and accounts."
)
UPLOAD_DATE = "2026-07-24"
DURATION = "PT1M46S"

SECTION = """
  <!-- Product walkthrough video (scripts/add_product_video.py) -->
  <section class="home-video-section reveal" id="walkthrough">
    <div class="container">
      <div class="home-video-header">
        <h2>See the whole platform in under two minutes</h2>
        <p>One walkthrough across all eight apps — registration to discharge, billing, pharmacy,
          lab, theatre, inventory, assets and accounts.</p>
      </div>

      <div class="video-facade" data-video-id="VIDEO_ID_PLACEHOLDER">
        <button type="button" class="video-facade-btn"
          aria-label="Play the ZenoHosp platform walkthrough, 1 minute 46 seconds">
          <picture>
            <source srcset="/images/video-walkthrough-poster.webp" type="image/webp">
            <img src="/images/video-walkthrough-poster.jpg" alt="ZenoHosp platform walkthrough"
              width="480" height="270" loading="lazy" decoding="async">
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

# Inline so it ships with the section rather than loading on every page.
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

CSS = """

/* Product walkthrough video — facade pattern (scripts/add_product_video.py) */

.home-video-section {
  padding: 100px 0;
  background: #0a0a08;
}

.home-video-header {
  max-width: 720px;
  margin: 0 auto 48px;
  text-align: center;
}

.home-video-header h2 {
  font-size: clamp(2rem, 4vw, 2.75rem);
  font-weight: 800;
  color: #fff;
  letter-spacing: -0.02em;
  margin-bottom: 16px;
  line-height: 1.15;
}

.home-video-header p {
  font-size: 1.1rem;
  line-height: 1.7;
  color: rgba(255, 255, 255, .62);
  margin: 0;
}

.video-facade {
  position: relative;
  max-width: 900px;
  margin: 0 auto;
  aspect-ratio: 16 / 9;
  border-radius: 20px;
  overflow: hidden;
  background: #11110d;
  box-shadow: 0 24px 60px rgba(0, 0, 0, .45);
}

.video-facade iframe {
  width: 100%;
  height: 100%;
  border: 0;
  display: block;
}

.video-facade-btn {
  all: unset;
  display: block;
  position: relative;
  width: 100%;
  height: 100%;
  cursor: pointer;
}

.video-facade-btn img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform .4s ease;
}

.video-facade-btn:hover img,
.video-facade-btn:focus-visible img {
  transform: scale(1.03);
}

.video-facade-btn:focus-visible {
  outline: 3px solid #d1f470;
  outline-offset: 3px;
}

.video-facade-play {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.video-facade-play-bg {
  fill: rgba(17, 17, 13, .78);
  transition: fill .25s ease;
}

.video-facade-btn:hover .video-facade-play-bg,
.video-facade-btn:focus-visible .video-facade-play-bg {
  fill: #d1f470;
}

.video-facade-btn:hover .video-facade-play path:last-child,
.video-facade-btn:focus-visible .video-facade-play path:last-child {
  fill: #11110d;
}

.video-facade-duration {
  position: absolute;
  right: 12px;
  bottom: 12px;
  padding: 3px 8px;
  border-radius: 6px;
  background: rgba(17, 17, 13, .85);
  color: #fff;
  font-size: .8rem;
  font-weight: 600;
  letter-spacing: .02em;
  pointer-events: none;
}

.home-video-note {
  text-align: center;
  margin: 32px 0 0;
  font-size: .98rem;
  color: rgba(255, 255, 255, .55);
}

.home-video-note a {
  color: #d1f470;
  font-weight: 600;
}

@media (max-width: 640px) {
  .home-video-section {
    padding: 64px 0;
  }

  .video-facade {
    border-radius: 14px;
  }

  .video-facade-play svg {
    width: 54px;
    height: 38px;
  }
}
"""


def main():
    root = pathlib.Path(__file__).resolve().parent.parent

    css_path = root / "css" / "main.css"
    css = css_path.read_text(encoding="utf-8")
    if ".video-facade" not in css:
        css_path.write_text(css + CSS, encoding="utf-8")
        print("appended video styles to css/main.css")

    page = root / "index.html"
    html = page.read_text(encoding="utf-8")

    if "video-facade" in html:
        print("homepage already has the video section")
        return

    # Sits after the trust strip and before the deployment block: high on the
    # page, and directly ahead of the eight-app grid the video walks through.
    marker = '<section class="home-deployment-section reveal"'
    idx = html.index(marker)
    line_start = html.rfind("\n", 0, idx) + 1
    section = SECTION.replace("VIDEO_ID_PLACEHOLDER", VIDEO_ID)
    html = html[:line_start] + section + html[line_start:]

    # Player bootstrap goes at the end of body, after the markup exists.
    html = html.replace("</body>", SCRIPT + "</body>", 1)

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": TITLE,
        "description": DESCRIPTION,
        "thumbnailUrl": [f"https://i.ytimg.com/vi/{VIDEO_ID}/hqdefault.jpg"],
        "uploadDate": UPLOAD_DATE,
        "duration": DURATION,
        "embedUrl": f"https://www.youtube-nocookie.com/embed/{VIDEO_ID}",
        "contentUrl": f"https://www.youtube.com/watch?v={VIDEO_ID}",
        "publisher": {
            "@type": "Organization",
            "name": "ZenoHosp",
            "logo": {
                "@type": "ImageObject",
                "url": "https://www.zenohosp.com/images/zenohosp-b.svg",
            },
        },
    }, indent=2, ensure_ascii=False)
    html = html.replace(
        "</head>",
        f'  <script type="application/ld+json">\n{schema}\n</script>\n</head>',
        1,
    )

    page.write_text(html, encoding="utf-8")
    print("added walkthrough video section + VideoObject schema to index.html")


if __name__ == "__main__":
    sys.exit(main())
