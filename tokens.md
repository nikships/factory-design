# Verified factory.ai design tokens

Extracted 2026-08-09 from the live site's compiled Tailwind CSS
(`https://factory.ai/_next/static/css/<hash>.css`) and confirmed via
computed styles in a live browser session.

## Color tokens (exact values from `:root`)

| Variable | Value | Meaning |
|---|---|---|
| `--dark-base-primary` | `#020202` | Dark product background |
| `--dark-base-secondary` | `#101010` | Dark raised surface |
| `--light-base-primary` | `#eee` | Light text on dark / light-mode surface |
| `--light-base-secondary` | `#fafafa` | Light-mode raised surface |
| `--accent-100` | `#ef6f2e` | Factory orange (bright / hover) |
| `--accent-200` | `#ee6018` | Factory orange (primary) |
| `--accent-300` | `#d15010` | Factory orange (deep / pressed) |
| `--surface-page` | `#f5f5f5` | Light marketing page background |
| `--surface-raised` | `#fff` | Light marketing card |
| `--surface-sunken` | `#ebebeb` | Light marketing inset |
| `--docs-grid-line` | `#b4b3b014` dark / `#0000000f` light | Hairline grid rules |

Computed on the marketing page: `body` background `rgb(245,245,245)`,
color `rgb(2,2,2)` — the marketing chrome is **light**; the dark values are
used on product surfaces, CTA panels, and the footer.

## Typography

- `bodyFont`: `Geist, "Geist Fallback"` (`--font-geist-sans`)
- Mono: `--font-geist-mono` — used for buttons, nav items, eyebrows, labels,
  all rendered UPPERCASE with tracking
- Display: `--font-geist-pixel-square` exists for pixel-style hero text
- Radii scale is small: `--radius-xs .125rem` … `--radius-3xl .75rem`;
  observed UI uses the 2–6px end
- Transitions: `--default-transition-duration: .15s`,
  `cubic-bezier(.4,0,.2,1)`

## Derived app tokens (used in templates)

| Token | Value | Rationale |
|---|---|---|
| background | `#020202` | `--dark-base-primary` |
| surface | `#0A0A0A` | midpoint panel between base and raised |
| surfaceRaised | `#101010` | `--dark-base-secondary` |
| border | `white @ 9%` | matches `--docs-grid-line` weight |
| borderStrong | `white @ 18%` | interactive borders |
| textPrimary | `#EEEEEE` | `--light-base-primary` |
| textSecondary | `#8C8C8C` | observed secondary gray |
| textTertiary | `white @ 32%` | hints/placeholders |
| accent | `#EE6018` | `--accent-200` |
| accentBright | `#EF6F2E` | `--accent-100`, hover |
| danger | `#EF4444` | tailwind red-500 family present in their palette |
| corner | 3pt | near-square observed radii |

## How to re-verify (if the brand may have changed)

`FetchUrl`/markdown readers return **no visual tokens** — read the CSS.

```bash
# 1. Find the CSS bundles
curl -s https://factory.ai/ -o /tmp/factory.html
grep -o 'href="[^"]*\.css[^"]*"' /tmp/factory.html

# 2. Grep the :root token block
curl -s "https://factory.ai/<css-path>" -o /tmp/f.css
grep -o -- '--dark-base-[^;]*\|--light-base-[^;]*\|--accent-[0-9]*:[^;]*\|--surface-[a-z]*:#[0-9a-f]*' /tmp/f.css | sort -u
```

Or via live computed styles (catches vars set by JS/themes):

```bash
agent-browser open https://factory.ai/ && agent-browser wait --load networkidle
cat <<'EOF' | agent-browser eval --stdin
const s = getComputedStyle(document.documentElement);
const vars = ["--accent-100","--accent-200","--accent-300",
  "--dark-base-primary","--dark-base-secondary",
  "--light-base-primary","--light-base-secondary"];
const out = {};
for (const v of vars) out[v] = s.getPropertyValue(v).trim();
out.bodyFont = getComputedStyle(document.body).fontFamily;
out.bodyBg = getComputedStyle(document.body).backgroundColor;
JSON.stringify(out, null, 2)
EOF
```

**Traps found in practice:**

- `--factory-orange`, `--factory-border`, `--factory-footer` appear in
  class names (`.border-factory-orange` etc.) but are **never assigned**
  in the served CSS — greps for their values exit 1. The real accent
  variables are `--accent-100/200/300`.
- The homepage hero and most sections are light; scroll to the footer CTA
  ("Ready to build the software of the future?") or product screenshots to
  see the dark treatment.
