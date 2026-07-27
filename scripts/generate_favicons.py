#!/usr/bin/env python3
"""Rasterise the ZenoHosp mark into the favicon formats Google indexes.

Google's favicon crawler wants a stable URL, a square image that is a multiple
of 48px, and a raster fallback. Shipping only an SVG is why the SERP shows a
generic globe next to zenohosp.com instead of the brand mark.

Outputs (mirroring images/favicon.svg):
  favicon.ico                    16/32/48 multi-resolution, root URL
  images/favicon-48.png          Google's minimum indexable size
  images/favicon-192.png         Android home screen / PWA
  images/apple-touch-icon.png    180px, iOS home screen
"""

from PIL import Image, ImageDraw, ImageFont

BG = "#111111"
FG = "#D1F470"
FONT = "/System/Library/Fonts/Helvetica.ttc"
FONT_BOLD_INDEX = 1  # Helvetica Bold within the .ttc collection

# Ratios lifted from images/favicon.svg (64px box, rx=16, font-size 36).
RADIUS_RATIO = 16 / 64
FONT_RATIO = 36 / 64

SUPERSAMPLE = 8  # draw big, downsample for clean antialiased corners


def render(size: int) -> Image.Image:
    s = size * SUPERSAMPLE
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([(0, 0), (s - 1, s - 1)], radius=s * RADIUS_RATIO, fill=BG)

    font = ImageFont.truetype(FONT, int(s * FONT_RATIO), index=FONT_BOLD_INDEX)
    # Centre on the glyph's ink box rather than its metrics, so the Z sits
    # optically centred the way it does in the SVG.
    left, top, right, bottom = draw.textbbox((0, 0), "Z", font=font)
    draw.text(
        ((s - (right - left)) / 2 - left, (s - (bottom - top)) / 2 - top),
        "Z",
        font=font,
        fill=FG,
    )
    return img.resize((size, size), Image.LANCZOS)


def main() -> None:
    render(48).save("images/favicon-48.png")
    render(192).save("images/favicon-192.png")
    # iOS composites over its own background; flatten so corners aren't black.
    render(180).convert("RGB").save("images/apple-touch-icon.png")
    render(256).save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print("wrote favicon.ico, images/favicon-48.png, images/favicon-192.png, images/apple-touch-icon.png")


if __name__ == "__main__":
    main()
