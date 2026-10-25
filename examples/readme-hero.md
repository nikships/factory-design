# README hero: how it was made

`readme-hero.png` (3200×1280, a 2x render of a 1600×640 banner) is a worked
example of the factory-design skill applied to image generation. The image
model drew only the abstract artwork. The logo and every word of text were
composited afterwards from official files and real fonts.

## 1. Background artwork

- Generator: Grok Imagine, model `grok-imagine-image-2.0`, through the local
  DroidProxy endpoint (the `grok-imagine` skill).
- Settings: `aspect_ratio: "20:9"`, `resolution: "2k"`, `n: 3`. Output was
  3 PNGs at 3200×1440.
- Negative prompt: none. Grok Imagine has no negative-prompt field, so the
  exclusions from `references/applying.md` are stated at the end of the prompt
  instead.

Prompt (the style core from `references/applying.md`, adapted to a banner):

> Flat, industrial, minimalist abstract banner artwork on a solid near-black
> background (#020202). On the right half of the frame, a large field of
> off-white (#EEEEEE) halftone dots on a precise square grid, the dots growing
> and shrinking in size to form a bold geometric machine-like disc shape, like
> a printed technical diagram. Thin 1px hairline grid lines in dim gray cross
> the composition, with a few rectangular hairline outline frames, small
> crosshair registration marks and tick-mark rulers along the edges, like an
> engineering drawing. The left half of the frame is completely empty flat
> black with only faint hairline grid lines, leaving space for type. Strictly
> monochrome black, gray and off-white, flat ink, no text, no letters, no
> logos, no gradients, no glow, no shadows, no 3D.

The prompt asks for no orange on purpose: the single orange accent is added
in compositing, so the model cannot spend it.

```bash
jq -n --arg p "$PROMPT" '{model:"grok-imagine-image-2.0", prompt:$p,
  aspect_ratio:"20:9", resolution:"2k", n:3, response_format:"b64_json"}' > req.json
curl -sS http://localhost:8317/v1/images/generations \
  -H "Content-Type: application/json" -H "Authorization: Bearer dummy-not-used" \
  -d @req.json > resp.json
jq -r '.data[0].b64_json' resp.json | base64 -d > g1_0.png
```

The right panel of the chosen candidate was cropped and saved as
`readme-hero-bg.png` (generation is not deterministic, so the source is kept):

```bash
uv run --with pillow python -c "from PIL import Image; \
  Image.open('g1_0.png').convert('L').crop((1760,80,3200,1360)) \
  .save('examples/readme-hero-bg.png', optimize=True)"
```

## 2. Compositing

`readme-hero.py` builds the final image with Pillow at 2x:

- Flat `#020202` canvas. The art panel sits right of a 1px divider at x=880
  (1x). Its grayscale is remapped so black is `#020202` and white is `#EEEEEE`,
  which also removes any stray color from the model.
- Hairlines in white at 9% (divider, header rule) and 18% (tag borders),
  flattened to opaque grays.
- Official `assets/logos/factory-lockup-white.png`, scaled to 32px tall (1x)
  with no other change. Clear space is at least 48px on every side, more than
  the mark height.
- `AGENT SKILL` header label, `01 DESIGN LANGUAGE` eyebrow (orange `#EE6018`
  index, gray label), a Geist headline and subline, and six tag boxes with
  3px corners. Labels are uppercase Geist Mono with 1.2–1.6px tracking.

Fonts: Geist Mono from the installed Geist Mono Nerd Font (Mono variant,
Medium and SemiBold). Geist sans static weights were instanced from
`Geist-Variable.woff2` ([vercel/geist-font](https://github.com/vercel/geist-font)):

```bash
uv run --with fonttools --with brotli python -c "
from fontTools.ttLib import TTFont; from fontTools.varLib import instancer
for w in (400, 500):
    f = instancer.instantiateVariableFont(TTFont('Geist-Variable.woff2'), {'wght': w})
    f.flavor = None; f.save(f'Geist-{w}.ttf')"

uv run --with pillow python examples/readme-hero.py \
  --bg examples/readme-hero-bg.png \
  --sans Geist-500.ttf --sans-regular Geist-400.ttf \
  --mono GeistMonoNerdFontMono-Medium.otf --mono-bold GeistMonoNerdFontMono-SemiBold.otf
```

## 3. Critique and fixes

- Rejected candidate 2 of 3: the disc was an irregular blob that ran into a
  stray tall rectangle on the right.
- Rejected candidate 3 of 3: the disc had clipped, stepped edges, and an
  outline box sat in the top center where the headline goes.
- Kept candidate 1, but its left half had hairline outline boxes where the
  lockup and headline go. Fixed by using only its right part as an art panel
  next to a flat type panel, split by a hairline.
- Checked the result against the skill rules: flat fills only, no gradient,
  glow, shadow or 3D; 1px hairlines; 3px corners; uppercase tracked mono
  labels; numbered orange eyebrow. A pixel scan confirmed the only colored
  pixels are the `01` index, so orange is used once. The lockup is the
  official file and the model drew no logo.
