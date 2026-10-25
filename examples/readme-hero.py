"""Composite the README hero: Grok Imagine background panel + official lockup + type.

Usage:
  uv run --with pillow python examples/readme-hero.py \
    --bg examples/readme-hero-bg.png --sans Geist-500.ttf --sans-regular Geist-400.ttf \
    --mono GeistMono-Medium.otf --mono-bold GeistMono-SemiBold.otf
"""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
S = 2  # render at 2x: 3200x1280
W, H = 1600, 640

BASE = (2, 2, 2)
TEXT = (238, 238, 238)
TEXT_2 = (140, 140, 140)
ORANGE = (238, 96, 24)


def mix(alpha):
    """White at `alpha` over #020202, as an opaque color (hairlines need no alpha layer)."""
    return tuple(round(2 + (255 - 2) * alpha) for _ in range(3))


BORDER = mix(0.09)
BORDER_STRONG = mix(0.18)

ap = argparse.ArgumentParser()
ap.add_argument("--bg", required=True, help="Grok Imagine artwork, cropped right panel")
ap.add_argument("--sans", required=True)
ap.add_argument("--sans-regular", required=True)
ap.add_argument("--mono", required=True)
ap.add_argument("--mono-bold", required=True)
ap.add_argument("--out", default=str(ROOT / "examples/readme-hero.png"))
args = ap.parse_args()


def font(path, px):
    return ImageFont.truetype(path, px * S)


def tracked(draw, xy, text, fnt, fill, tracking):
    """Draw text with letter spacing (px at 1x). Returns the end x at 2x."""
    x, y = xy[0] * S, xy[1] * S
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += fnt.getlength(ch) + tracking * S
    return x - tracking * S


def tracked_width(text, fnt, tracking):
    return sum(fnt.getlength(c) for c in text) + tracking * S * (len(text) - 1)


img = Image.new("RGB", (W * S, H * S), BASE)
d = ImageDraw.Draw(img)

# Right art panel. Remap the generated grayscale so black lands on #020202 and
# white on #EEEEEE, which also strips any stray chroma the model introduced.
SPLIT = 880
art = Image.open(args.bg).convert("L")
art = art.point(lambda v: round(2 + v * 236 / 255))
img.paste(Image.merge("RGB", (art, art, art)), (SPLIT * S, 0))

# Vertical panel divider and header rule (1px hairlines at 1x).
d.rectangle([SPLIT * S, 0, SPLIT * S + S - 1, H * S], fill=BORDER)
d.rectangle([0, 128 * S, SPLIT * S, 128 * S + S - 1], fill=BORDER)

# Official lockup, scaled only. Clear space >= mark height (the lockup height).
LOGO_H, MX, MY = 32, 64, 48
logo = Image.open(ROOT / "assets/logos/factory-lockup-white.png").convert("RGBA")
lw = round(logo.width * LOGO_H * S / logo.height)
logo = logo.resize((lw, LOGO_H * S), Image.LANCZOS)
img.paste(logo, (MX * S, MY * S), logo)

mono_sm = font(args.mono, 12)
mono_eb = font(args.mono_bold, 14)

# Header label, right-aligned in the left panel.
label = "AGENT SKILL"
lw_ = tracked_width(label, mono_sm, 1.6)
tracked(d, ((SPLIT - 48) - lw_ / S, MY + 9), label, mono_sm, TEXT_2, 1.6)

# Numbered eyebrow: orange index, gray tracked label.
y = 196
x2 = tracked(d, (MX, y), "01", mono_eb, ORANGE, 1.6)
tracked(d, (x2 / S + 14, y), "DESIGN LANGUAGE", mono_eb, TEXT_2, 1.6)

# Headline.
head = font(args.sans, 58)
for i, line in enumerate(["Build anything that looks", "like Factory made it."]):
    d.text((MX * S, (y + 36 + i * 68) * S), line, font=head, fill=TEXT)

# Subline.
sub = font(args.sans_regular, 20)
d.text((MX * S, 396 * S), "The Factory (Droid) design language and brand kit, for any medium.",
       font=sub, fill=TEXT_2)

# Tag row: uppercase tracked mono in hairline boxes, ~3px corners.
x, ty, th, pad = MX, 520, 32, 14
for tag in ["APPS", "WEB", "CLI", "SLIDES", "DIAGRAMS", "IMAGES"]:
    tw = tracked_width(tag, mono_sm, 1.2) / S
    box = [x * S, ty * S, (x + tw + 2 * pad) * S, (ty + th) * S]
    d.rounded_rectangle(box, radius=3 * S, outline=BORDER_STRONG, width=S, fill=BASE)
    tracked(d, (x + pad, ty + 9), tag, mono_sm, TEXT, 1.2)
    x += tw + 2 * pad + 10

img.save(args.out, optimize=True)
print(args.out, img.size)
