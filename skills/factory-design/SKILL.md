---
name: factory-design
description: >-
  Factory (Droid) design language and official brand kit, independent of any
  language, framework, or medium: dark industrial surfaces, hairline borders,
  near-square corners, uppercase monospace labels, numbered orange eyebrows, a
  sparing Factory-orange accent, plus verified color/type/radius tokens
  (tokens.json), official logos, rotor mark, halftone and guild imagery, logo
  rules, and the Factory Guild community guidelines pulled from
  factory.com/guild/resources. Use whenever anything should look or feel like
  Factory made it: any app, website, CLI/TUI, slide, README, diagram, icon,
  document, or AI-generated image; restyling an existing design; looking up a
  Factory color, font, logo, or brand rule; or when the user says "make it look
  like Factory built it", "Factory / Droid style", "Factory-native", or asks
  for the Factory brand kit.
---

# Factory design language

A medium-neutral design language and brand resource for Factory (the company
behind Droid). It is not tied to a stack: the same rules apply to a web page,
a native app, a terminal UI, a slide deck, a diagram, an icon, or a prompt for
an image model.

Contents of this skill:

| What | Where |
|---|---|
| Design rules (this file) | `SKILL.md` |
| Machine-readable tokens | `tokens.json` |
| Token provenance and re-verification | `tokens.md` |
| Per-medium application guide, image-generation prompts, restyle checklist | `references/applying.md` |
| Official logos, rotor mark, usage and clear-space rules | `references/brand-kit.md`, `assets/logos/` |
| Backgrounds and imagery | `assets/backgrounds/` |
| Community guidelines (brand, public posts, submissions) | `references/community-guidelines.md` |
| Guild FAQ and where to get help | `references/guild-faq-and-help.md` |

The brand kit, guidelines, FAQ, and help content were pulled from
<https://factory.com/guild/resources> on 2026-10-25. Tokens were verified
against factory.com's live CSS on the same date.

## What do you need?

| Request | Start here |
|---|---|
| Build or style something new, in any medium | The rules below, then `references/applying.md` for that medium. |
| Restyle an existing design | `references/applying.md` → "Restyling an existing design". |
| A color, font, radius, or motion value | `tokens.json` (or `tokens.md` for context). |
| A logo, mark, or background file | `assets/`, and `references/brand-kit.md` for which file and the usage rules. |
| An AI-generated image or illustration | `references/applying.md` → "Image generation and illustration". |
| Policy or "can I say/use X" questions | `references/community-guidelines.md`, `references/brand-kit.md`, `references/guild-faq-and-help.md`. |

## The design language

Factory has two moods. **Marketing chrome is light industrial** (`#F5F5F5`
page, near-black text, black-filled buttons). **Product surfaces are dark**
(`#020202` base, light text, light-filled buttons). Default to the dark
product treatment for apps, tools, terminals, and screenshots. Use the light
set for landing pages, docs, print, and anything that should read as Factory
marketing. Everything below applies to both.

Rules, in priority order:

1. **Surfaces.** Dark: base `#020202`, panel `#0A0A0A`, raised `#101010`.
   Light: page `#F5F5F5`, raised `#FFFFFF`, sunken `#EBEBEB`. Flat fills only:
   **no gradients, no glows, no blur halos, no shadows for depth**. Ambient
   glow and gradient buttons are the biggest tell of a non-Factory design.
   Strip them when restyling.
2. **Borders.** 1px hairlines everywhere. Dark: `white @ 9%` default,
   `white @ 18%` for interactive or strong. Light: `black @ 6%`. Hairline
   horizontal rules separate header bands from content, like the site nav.
3. **Corners.** Near-square: about 3px (the site uses 2–6px). Pills and
   10–14px radii read as generic SaaS, not Factory.
4. **Text.** Dark mode: primary `#EEEEEE`, secondary `#8C8C8C`, tertiary
   `white @ 32%`. Light mode: `#020202`. Body font is Geist. If unavailable,
   a system sans is fine, but **chrome text is monospace**.
5. **Uppercase monospace labels.** Buttons, section labels, status lines, and
   badges are UPPERCASE Geist Mono (or system mono) with letter tracking
   (0.5–1.6px). Keep symbols like `⌘↩` outside uppercase-transformed labels.
6. **Numbered eyebrows.** Section headers read `01 REPOSITORY`: a
   Factory-orange index plus a tracked uppercase gray label, about 10px mono
   semibold.
7. **Accent = Factory orange, used sparingly.** `#EE6018` primary,
   `#EF6F2E` bright (hover), `#D15010` deep (pressed). Use for eyebrow
   indexes, focus rings, hover border/text shifts, active-state icons, live
   counters, and a single highlighted element in a diagram or chart. Never
   for large fills or button backgrounds.
8. **Buttons invert against their surface.** On dark, the primary CTA is
   light-filled (`#EEEEEE` fill, `#020202` uppercase mono label) with a
   trailing `→`, like the site's "START BUILDING →". On light, it is
   black-filled with a light label. Secondary buttons are surface-filled
   with hairline borders; on hover the border and text shift toward orange.
9. **Iconography.** Minimal, thin, monochrome. The rotor (pinwheel droid
   mark) replaces decorative icons such as sparkles for empty states, AI
   affordances, and branding.
10. **Motion.** Quick and mechanical: 120–180ms ease-out (site default 150ms,
    `cubic-bezier(.4,0,.2,1)`) on hover and press. No springs, bounces, or
    shimmer.
11. **Imagery.** Either flat and industrial (halftone dots, hairline grids,
    the rotor) or brutalist editorial collage (see
    `assets/backgrounds/guild-graphic.jpg`). Never glossy, 3D, or
    glassmorphic.
12. **Honesty.** Show real work and real proof. Don't invent Factory features,
    partnerships, or endorsements. See `references/community-guidelines.md`.

## Logos and brand assets

Use the files in `assets/` as-is. Do not recolor, redraw, stretch, or
re-typeset them. Never ask an image model to draw the logo; composite the
official file instead.

| Surface | Lockup | Mark only | `factory.ai` dot logo |
|---|---|---|---|
| Dark | `assets/logos/factory-lockup-white.svg` | `assets/logos/rotor-white.svg` | `assets/logos/dot-logo-dark.svg` |
| Light | `assets/logos/factory-lockup-black.svg` | `assets/logos/rotor-black.svg` | `assets/logos/dot-logo-light.svg` |

Every logo also has a transparent PNG with the same name. Keep clear space of
at least the height of the mark around any logo. Don't combine it with another
logo or imply Factory endorses a project. Full rules, dimensions, and
membership guidance are in `references/brand-kit.md`.

Decorative textures: `assets/backgrounds/bg-halftone-rotor.png` (black halftone
on transparent: invert or lower opacity on dark) and
`assets/backgrounds/guild-graphic.jpg` (reference collage).

## Workflow

1. **Pick the mood** (dark product or light marketing) from the surface the
   output lives on.
2. **Define tokens first** in the form the target uses, from `tokens.json`.
3. **Compose from the rules**, using `references/applying.md` for medium-specific
   guidance. Don't introduce gradients, glows, or pills in the first place.
4. **Use official assets** from `assets/` instead of redrawing them.
5. **Verify visually.** Render or screenshot the real output and confirm:
   uppercase mono labels, orange numbered indexes, hairline borders, near-square
   corners, flat fills, no glow. Confirm you captured the new output, not a stale
   instance or cached build.
6. **Re-verify tokens only if the brand may have changed.** `tokens.md` has the
   exact commands. Trap: `--factory-orange` and `--factory-border` appear in
   class names but are never assigned; the real accent variables are
   `--accent-100/200/300`.
