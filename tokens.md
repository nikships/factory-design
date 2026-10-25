# Verified Factory design tokens

Machine-readable copy: `tokens.json`. Re-verified **2026-10-25** against the
live site's compiled CSS (`https://factory.com/_next/static/css/<hash>.css`).
`factory.ai` now permanently redirects (308) to `factory.com`; the values were
unchanged from the original 2026-08-09 extraction.

## Color tokens (exact values from `:root`)

| Variable | Value | Meaning |
|---|---|---|
| `--dark-base-primary` | `#020202` | Dark product background |
| `--dark-base-secondary` | `#101010` | Dark raised surface |
| `--light-base-primary` | `#eee` | Light text on dark / light-mode surface |
| `--light-base-secondary` | `#fafafa` | Light-mode raised surface |
| `--accent-100` | `#ef6f2e` | Factory orange (bright / hover; also the dot in the `factory.ai` dot logo) |
| `--accent-200` | `#ee6018` | Factory orange (primary) |
| `--accent-300` | `#d15010` | Factory orange (deep / pressed) |
| `--surface-page` | `#f5f5f5` | Light marketing page background |
| `--surface-raised` | `#fff` | Light marketing card |
| `--surface-sunken` | `#ebebeb` | Light marketing inset |
| `--docs-grid-line` | `#b4b3b014` dark / `#0000000f` light | Hairline grid rules |

The marketing chrome is **light** (`body` background `rgb(245,245,245)`, text
`rgb(2,2,2)`). The dark values are used on product surfaces, CTA panels, and
the footer.

## Typography

- Body: `Geist` (`--font-geist-sans`)
- Mono: `Geist Mono` (`--font-geist-mono`), used for buttons, nav items,
  eyebrows, labels, all rendered UPPERCASE with tracking
- Display: `Geist Pixel Square` (`--font-pixel`) for pixel-style hero text
- Geist and Geist Mono are open source (SIL OFL) from Vercel. Where they are
  unavailable, use the system sans for body and the system monospace for
  chrome.
- Transitions: `--default-transition-duration: .15s`,
  `cubic-bezier(.4,0,.2,1)`

## Radii

Site scale: `xs .125rem`, `sm .1875rem`, `md .25rem`, `lg .375rem`,
`xl .5rem`, `2xl .625rem`, `3xl .75rem`. Observed UI uses the 2–6px end. The
design default is **3px**.

## Derived app tokens

Not CSS variables on the site. Derived from the observed UI so apps can copy
them directly.

| Token | Value | Rationale |
|---|---|---|
| background | `#020202` | `--dark-base-primary` |
| surface | `#0A0A0A` | midpoint panel between base and raised |
| surfaceRaised | `#101010` | `--dark-base-secondary` |
| border | `white @ 9%` (≈ `#191919` on background) | matches `--docs-grid-line` weight |
| borderStrong | `white @ 18%` (≈ `#303030`) | interactive borders |
| textPrimary | `#EEEEEE` | `--light-base-primary` |
| textSecondary | `#8C8C8C` | observed secondary gray |
| textTertiary | `white @ 32%` (≈ `#535353`) | hints, placeholders |
| accent | `#EE6018` | `--accent-200` |
| accentBright | `#EF6F2E` | `--accent-100`, hover |
| danger | `#EF4444` | Tailwind red-500 family present in their palette |
| corner | 3px | near-square observed radii |

## How to re-verify (if the brand may have changed)

Markdown readers and `FetchUrl` return **no visual tokens**. Read the CSS.
Any HTTP client plus `grep` works, so this is independent of language or
tooling.

```bash
# 1. Find the CSS bundles
curl -sL https://factory.com/ -o /tmp/factory.html
grep -o 'href="[^"]*\.css[^"]*"' /tmp/factory.html

# 2. Grep the :root token block (prefix the host to each CSS path)
curl -s "https://factory.com/<css-path>" -o /tmp/f.css
grep -o -- '--dark-base-[^;}]*\|--light-base-[^;}]*\|--accent-[0-9]*:[^;}]*\|--surface-[a-z]*:[^;}]*\|--radius-[a-z0-9]*:[^;}]*' /tmp/f.css | sort -u
```

Or read live computed styles in any browser tool (catches variables set by
JS or themes):

```js
const s = getComputedStyle(document.documentElement);
const vars = ["--accent-100","--accent-200","--accent-300",
  "--dark-base-primary","--dark-base-secondary",
  "--light-base-primary","--light-base-secondary"];
const out = Object.fromEntries(vars.map(v => [v, s.getPropertyValue(v).trim()]));
out.bodyFont = getComputedStyle(document.body).fontFamily;
out.bodyBg = getComputedStyle(document.body).backgroundColor;
JSON.stringify(out, null, 2)
```

**Traps found in practice:**

- `--factory-orange`, `--factory-border`, `--factory-footer` appear in class
  names (`.border-factory-orange` etc.) but are **never assigned** in the
  served CSS. The real accent variables are `--accent-100/200/300`.
- The homepage hero and most sections are light. Scroll to the footer CTA or
  product screenshots to see the dark treatment.
- Brand-kit assets and official brand guidance live on the Guild resources
  page (`https://factory.com/guild/resources`); see `references/brand-kit.md`.
