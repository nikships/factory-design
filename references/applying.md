# Applying the Factory design language by medium

The rules in `../SKILL.md` and the values in `../tokens.json` are
medium-neutral. This file translates them for common outputs. Each section
names the decisions that matter in that medium and leaves the implementation
(framework, toolkit, tool) to you.

## Contents

- Software UI (web, native, terminal)
- Documents, READMEs, and slides
- Diagrams and charts
- Icons, avatars, and favicons
- Image generation and illustration
- Restyling an existing design
- Verifying the result

## Software UI (web, native, terminal)

1. Define the tokens first, in whatever form the stack uses (CSS custom
   properties, a theme object, a design-token file, a config). Source of truth:
   `tokens.json`.
2. Build components from the rules: flat fills, 1px hairlines, ~3px corners,
   uppercase mono chrome labels, numbered eyebrows, orange used sparingly.
3. Buttons: primary is inverted against its surface (light fill, dark
   uppercase mono label, trailing `→` on dark; the reverse on light).
   Secondary buttons are surface-filled with a hairline border whose color and
   text shift toward orange on hover.
4. Focus rings and active-state icons use the orange accent.
5. Put keyboard hints (`⌘↩`) in a separate tertiary-colored element rather than
   inside an uppercase-transformed label, because text-case transforms mangle
   symbols.
6. Terminal UIs: `#020202` background and `#EEEEEE` text, orange for indexes
   and live counters, dim gray for secondary text, box-drawing hairlines
   instead of heavy borders, uppercase labels. Skip gradients and 256-color
   rainbow output.
7. Window chrome (desktop apps): flush header band with a hairline rule below
   it, wordmark or rotor centered or left-aligned in that band, no decorative
   title-bar imagery.

## Documents, READMEs, and slides

- Choose the mood by surface: light (`#F5F5F5` page, `#020202` text) for docs
  and print, dark (`#020202`) for product-style decks and hero slides.
- Headings in Geist (or the system sans); labels, captions, and section
  eyebrows in uppercase mono with tracking.
- Section eyebrows: `01 OVERVIEW`, `02 INSTALL`, with the index in
  Factory orange.
- Rules between sections are hairlines, not colored bars or boxes.
- READMEs: use `assets/logos/factory-lockup-white.svg` or the black variant
  (match the host's background; GitHub supports `<picture>` with
  `prefers-color-scheme` to serve both). Keep the logo's clear space at least
  the height of the mark.
- Slides: one idea per slide, left-aligned, generous empty space, one orange
  accent element at most.
- Only use Factory logos when the material is Factory's own or explicitly
  Factory-adjacent. See `brand-kit.md`.

## Diagrams and charts

- Background `#020202` (dark) or `#F5F5F5` (light), 1px hairline strokes at
  `white @ 18%` on dark, and `black @ 6%` (`--docs-grid-line`) or slightly
  stronger on light.
- Nodes are flat rectangles with ~3px corners, hairline borders, no shadows,
  no gradients.
- Labels in uppercase mono, 10–12px, tracked. Primary text `#EEEEEE`,
  secondary `#8C8C8C`.
- Use orange for the single thing the reader should look at (the critical path,
  the active node, the key metric). Everything else stays gray scale.
- Charts: grayscale series with one orange highlight. Avoid rainbow palettes.
  Use gridlines at hairline weight (`--docs-grid-line`).

## Icons, avatars, and favicons

- Prefer the rotor (`assets/logos/rotor-white.svg` / `rotor-black.svg`) for
  avatars, app icons, and favicons.
- Keep the rotor's shape and proportions. Place it on flat `#020202` (white
  rotor) or `#F5F5F5` / `#FFFFFF` (black rotor) with generous padding.
- Decorative icons are minimal: thin-stroke, monochrome, small. The rotor
  replaces generic sparkles and magic-wand icons for empty states and AI
  affordances.

## Image generation and illustration

When writing prompts for an image model, or briefing a designer, describe the
language, not a specific tool. Reusable prompt fragments:

**Style core**

> Flat, industrial, minimalist. Near-black background (#020202). Off-white
> (#EEEEEE) type and linework. Thin 1px hairline borders. Square or very
> slightly rounded (3px) corners. Uppercase monospaced labels with wide letter
> spacing. A single small accent in Factory orange (#EE6018). No gradients, no
> glows, no drop shadows, no 3D, no glassmorphism.

**Light variant**

> Flat, industrial, minimalist on a light gray page (#F5F5F5). Near-black
> (#020202) text and thin hairline rules. Square corners. Uppercase monospaced
> labels. One orange accent (#EE6018). No gradients, no shadows.

**Editorial/collage variant** (see `assets/backgrounds/guild-graphic.jpg`)

> Brutalist editorial collage: oversized grotesque type in square brackets,
> a halftone dot grid, high-contrast black panels, grainy photographic crops
> with red-orange tint, flat sky-blue panel with red type. Hard rectangular
> crops, no soft edges.

**Negative prompt** (when supported)

> gradient, glow, bloom, neon, lens flare, drop shadow, 3D render, glossy,
> glassmorphism, pill shapes, rounded cards, purple, indigo, cyan accent,
> sparkles, stock-photo smiles.

**Do not** ask a generation model to render the Factory logo or rotor. Models
distort them. Generate the artwork without the mark, then composite the
official SVG/PNG from `assets/logos/` on top, respecting clear space.

**Texture**: `assets/backgrounds/bg-halftone-rotor.png` works as a
low-opacity background layer or as a reference image for halftone style.

## Restyling an existing design

1. Swap tokens first, in one pass. Delete gradient and glow definitions
   entirely so stale references break loudly.
2. Convert component by component using this table (also a checklist of what
   to avoid when building new):

| Before (generic) | After (Factory) |
|---|---|
| Gradient primary button with glow shadow | Flat inverted button, uppercase mono label, `→` |
| Sparkle icons | The rotor, or no icon |
| 10–14px corner radii, pills | ~3px radii |
| Plain section label `PROMPT` | Numbered eyebrow `02 PROMPT`, orange index |
| Ambient background glow | Flat `#020202` |
| Colored error banners | `ERR` mono prefix in danger red `#EF4444`, hairline border |
| Purple or indigo accent | Factory orange `#EE6018`, sparingly |
| Drop shadows for elevation | Hairline border and a slightly lighter surface |

## Verifying the result

Render or screenshot the output and check against the rules. The design is
right when you can see all of: uppercase mono labels, orange numbered indexes,
square-ish corners, hairline borders, flat fills, and no glow.

- Make sure the screenshot is of the *new* output, not a stale running
  instance, cached build, or old export.
- Compare logo rendering against the official files in `assets/logos/`.
- For image-generation output, reject images containing gradients, glows, or
  a hallucinated logo and regenerate.
- To confirm tokens against the live brand, follow "How to re-verify" in
  `../tokens.md`.
