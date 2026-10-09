---
name: factory-design
description: >-
  Factory (factory.ai) design language and brand kit: dark industrial
  surfaces, Factory-orange accents, uppercase monospace labels, numbered
  section eyebrows, hairline borders, the pinwheel droid glyph, plus official
  logo/rotor/halftone assets and verified color, type, and radius tokens. Use
  whenever anything should look or feel like Factory made it: building a new
  app, page, slide, README, diagram, icon, or UI from scratch; restyling or
  redesigning an existing one; picking Factory colors, fonts, or logos; or when
  the user says "make it look like Factory built it", "factory.ai style /
  theme / aesthetic", or "Factory-native". Includes SwiftUI and CSS starter
  templates, token re-verification against the live site, and a screenshot
  verification loop.
---

# Factory design language

The Factory (factory.ai) visual system, for **anything you build or restyle**:
new apps and pages from scratch, redesigns of existing UI, docs, slides,
READMEs, diagrams, icons, and marketing assets. It has three parts:

- **Design language** — the rules below (surfaces, borders, type, accent,
  buttons, iconography, motion).
- **Brand kit** — official logo, rotor, and halftone files in `assets/`, plus
  verified tokens in `tokens.md`.
- **Starter code** — `templates/` for SwiftUI and CSS.

The tokens were extracted from factory.ai's live CSS and verified visually in
Aug 2026; `tokens.md` records provenance and how to re-verify if the brand
evolves.

## Choosing a mode

| Situation | Start here |
|---|---|
| Building something new | Apply the design language directly. Copy `templates/` for the stack, then compose views from the rules. |
| Restyling an existing app | Follow the **Restyle workflow** below: swap tokens first, then convert component by component. |
| Just need brand pieces (logo, color, font, background texture) | Skip the workflow. Take files from `assets/` and values from `tokens.md`. |
| Non-UI output (slides, README, diagrams, social images) | Use the palette, type, hairline, and accent rules plus the matching `assets/` files. Ignore the app-specific button and window-chrome guidance. |

## The design language

Factory's site has two moods: **marketing chrome is light industrial**
(`#f5f5f5` page, near-black text, black-filled buttons) and **product
surfaces are dark** (`#020202` base, light text, light-filled CTAs). Apps
and tools should default to the **dark product treatment** — it's what
Factory's own desktop app and CLI screenshots use. Use the light marketing
set (`tokens.md`, `templates/tokens.css`) for landing pages, docs, print, and
anything that should read as Factory marketing. Everything else below applies
to both moods.

Core rules, in priority order:

1. **Surfaces.** Base `#020202`, panels `#0A0A0A`, raised elements `#101010`.
   Flat fills only — **no gradients, no glows, no blur halos, no shadows for
   depth**. Ambient glow and gradient buttons are the single biggest tell of
   a non-Factory design; never introduce them, and strip them when restyling.
2. **Borders.** 1pt hairlines everywhere: `white @ 9%` default, `white @ 18%`
   for interactive/strong. Hairline horizontal rules separate header bands
   from content (like the site nav).
3. **Corners.** Near-square: ~3pt radius (site uses 2–6px). Rounded-rect
   pills and 10–14pt radii read as generic-SaaS, not Factory.
4. **Text.** Primary `#EEEEEE`, secondary ~`#8C8C8C`, tertiary `white @ 32%`.
   Body font is Geist; if unavailable (native apps), system fonts are fine for
   body, but **UI chrome text is monospace**.
5. **Monospace uppercase labels.** Buttons, section labels, status lines, and
   badges are UPPERCASE monospace with letter tracking (0.5–1.6pt). Keep
   symbols like `⌘↩` *outside* uppercase-transformed labels (textCase
   mangles adjacent styling; put hints in a separate tertiary Text).
6. **Numbered eyebrows.** Section headers are `01 REPOSITORY`-style: a
   Factory-orange index + tracked uppercase gray label, 10pt mono semibold.
7. **Accent = Factory orange, used sparingly.** `#EE6018` (bright hover
   variant `#EF6F2E`, deep `#D15010`). Use for: eyebrow indexes, focus rings,
   hover border/text shifts, active-state icons, live counters. Never for
   large fills or button backgrounds.
8. **Buttons invert against their surface.** On dark: primary CTA is
   **light-filled** (`#EEE` fill, black uppercase mono label) with a trailing
   `→` arrow — like the site's "START BUILDING →". Secondary/ghost buttons
   are dark-filled with hairline borders; on hover the border and text shift
   toward orange.
9. **Iconography.** Minimal. The Factory pinwheel droid glyph (template
   rendered, inherits foreground color) replaces decorative icons like
   sparkles for empty states and branding. Wordmark centered in the title
   bar/header band. Simple SF Symbols (`arrow.right`, `folder.fill`, `cpu`)
   at small sizes are fine.
10. **Motion.** Quick and mechanical: 0.12–0.18s easeOut on hover/press.
    No springy bounces, no shimmer.

## Workflow

### Building something new

1. Start from the matching template (`templates/Theme.swift` for SwiftUI,
   `templates/tokens.css` for web). For other stacks, port the values from
   `tokens.md`.
2. Define the tokens file first, then build views from the design-language
   rules. Don't introduce gradients, glows, or rounded-pill shapes in the
   first place.
3. Pull logo, rotor, and halftone files from `assets/` (see Assets) instead
   of redrawing them.
4. Run **Build and verify visually** (step 4 below) before calling it done.

### Restyling an existing app

Steps 1–4 below. Step 1 is optional, and steps 2–3 are where existing
generic styling gets converted.

### 1. (Optional) Re-verify tokens against the live site

Only needed if you suspect the brand changed — otherwise trust `tokens.md`.
`FetchUrl` on factory.ai returns markdown with **zero visual tokens**; you
must read the CSS. Two ways (see `tokens.md` for exact commands):

- Grep the `/_next/static/css/*.css` files' `:root` block for
  `--dark-base-*`, `--light-base-*`, `--accent-*`.
- Or `agent-browser open https://factory.ai/` + `eval` computed styles.

**Trap:** `--factory-orange` / `--factory-border` are referenced in class
names but never assigned a value — the real accent vars are
`--accent-100/200/300`. Don't burn time grepping for factory-orange.

### 2. Replace the theme tokens first

Do the tokens file in one pass before touching views. For SwiftUI, start from
`templates/Theme.swift`; for web, `templates/tokens.css`. When replacing an
existing theme, delete gradient definitions entirely so stale references fail
the build and get caught.

### 3. Restyle per component

Work through each view applying the rules above. Typical conversions from a
generic dark theme (also a checklist of what to avoid when building new):

| Before (generic) | After (Factory) |
|---|---|
| Gradient primary button + glow shadow | Light-filled `PrimaryButtonStyle`, uppercase mono, `→` |
| `sparkles` icons | `DroidGlyph` pinwheel (templates/LogoView.swift) |
| 10–14pt corner radii | `Theme.corner` (3pt) |
| Plain `SectionLabel("PROMPT")` | Numbered eyebrow `SectionLabel(index: "02", text: "Prompt")` |
| Ambient background glow ellipse | Flat `Theme.background` |
| Orange system `.orange` error banners | `ERR` mono prefix in danger red `#EF4444`-ish, hairline border |
| Purple/indigo accent | Factory orange `#EE6018` |

Also style the window chrome (macOS): transparent titlebar, hidden title,
`fullSizeContentView`, window background `#020202`, wordmark centered in the
header band with a hairline rule below it.

### 4. Build and verify visually

Build, launch (or render), screenshot, and compare against the rules —
uppercase mono labels, orange indexes, square corners, and no glow should all
be visible. For web or static output, open it in a browser and screenshot it
the same way.

macOS gotchas hit in practice:

- **Stale instances:** if the app was already running, your screenshot may
  capture the *old* design. `ps aux | grep <AppName>` and kill old PIDs, or
  target the fresh one explicitly:
  `orca computer get-app-state --app pid:<newpid> --restore-window --json`
  (screenshot path is at `result.screenshot.path`).
- Don't use `osascript`/JXA `CGWindowListCopyWindowInfo` for window IDs — it
  segfaults. Use orca computer-use (or `screencapture -l` only if you already
  have a window number).

## Templates

- `templates/Theme.swift` — SwiftUI tokens + `SurfaceStyle`,
  `PrimaryButtonStyle`, `GhostButtonStyle`, `SectionLabel`. Drop in and fix
  call sites.
- `templates/LogoView.swift` — `LogoView` (full FACTORY wordmark + pinwheel)
  and `DroidGlyph` (pinwheel alone), both template-rendered NSImages from
  inline SVG so they paint in the current foreground color.
- `templates/tokens.css` — the same palette as CSS custom properties for web
  apps, both dark-product and light-marketing sets.

## Assets

### Official brand files (prefer these)

Official Factory brand PNGs with **transparent backgrounds**. Pick the color
by surface: `-white` files go on dark surfaces (the default for apps), `-black`
files go on light surfaces (marketing chrome, light-mode docs). Note that a
`-white` file looks blank when previewed on a white background.

- `assets/factory-lockup-white.png` / `assets/factory-lockup-black.png` — full
  lockup: pinwheel + `FACTORY` wordmark, 2048×307. Use for headers, title
  bars, README banners, and splash screens.
- `assets/rotor-white.png` / `assets/rotor-black.png` — the pinwheel droid
  glyph alone (the "rotor"), 1932×2048. Use for empty states, app icons,
  favicons, and loading indicators.
- `assets/bg-halftone-rotor.png` — halftone dot-pattern rendering of the
  rotor, 738×738, black dots on transparent. Decorative background texture for
  hero areas and empty states; it is black-on-transparent, so invert it (or
  lower its opacity) before using it on dark surfaces. Keep it subtle,
  consistent with the no-glow, flat-fill rules above.

For native apps that need the mark to follow the foreground color, still use
the template-rendered `LogoView` / `DroidGlyph` in `templates/LogoView.swift`;
use the PNGs when a raster is fine (web, docs, marketing, app icons).

### Reference and source files

Raw source and reference renders of the Factory pinwheel droid glyph. Reach
for these when you need the glyph outside `templates/LogoView.swift` — web
apps, app icons, other toolkits — or when you want a visual ground truth to
compare your own rendering against.

- `assets/_pinwheel.svg` — the pinwheel glyph as a standalone SVG: `#EEEEEE`
  path centered on a `#020202` 1024×1024 canvas. Drop-in for web; the path
  data is the same geometry inlined in `templates/LogoView.swift`.
- `assets/_glyph-ref.svg` / `assets/_glyph-ref.png` — reference render of the
  same glyph at a slightly larger scale (2048×2048 PNG); use as the visual
  ground truth when screenshot-verifying your glyph rendering.
- `assets/_glyph-magick.png` — the SVG rasterized via ImageMagick
  (1024×1024); a second opinion when a renderer's output looks off.
- `assets/_logo-check.png` — 800×120 render of the full wordmark + pinwheel
  lockup, for checking overall logo proportions against Factory's branding.
