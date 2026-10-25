# Factory brand kit

Official brand kit from the Factory Guild resources page
(<https://factory.com/guild/resources#brand>), pulled 2026-10-25. All files
are in `../assets/` byte-for-byte as downloaded from
`https://factory.com/guild/brand/...`. Use them as-is; never recolor, redraw,
stretch, or re-typeset them.

## Logos (`assets/logos/`)

Every logo ships as SVG (preferred: scalable, crisp) and PNG (transparent
background).

| File | Pixels (PNG) | Use |
|---|---|---|
| `factory-lockup-white.{svg,png}` | 2048×307 | Full wordmark (mark + FACTORY) for **dark** backgrounds. |
| `factory-lockup-black.{svg,png}` | 2048×307 | Full wordmark for **light** backgrounds. |
| `rotor-white.{svg,png}` | 1932×2048 | The mark alone ("Factory mark" / pinwheel droid / rotor), for avatars and small spaces on **dark** backgrounds. |
| `rotor-black.{svg,png}` | 1932×2048 | The mark alone, for **light** backgrounds. |
| `dot-logo-dark.{svg,png}` | 2048×385 | The `factory.ai` wordmark with the orange dot (`#EF6F2E`), for **dark** backgrounds. |
| `dot-logo-light.{svg,png}` | 2048×385 | The `factory.ai` wordmark with the orange dot (`#EF6F2E`), for **light** backgrounds. |

Naming trap: "white" and "dark" both mean *the logo is light-colored and goes
on a dark surface*. "black" and "light" mean *the logo is dark and goes on a
light surface*. A white logo previewed on a white page looks blank, which is
expected.

SVG viewBoxes: lockup `0 0 1459 218`, rotor `0 0 613 650`, dot logo
`0 0 847 159`. The SVGs carry `width="100%" height="100%"`, so size them with
their container (CSS, layout frame, or the host tool's size setting).

## Backgrounds and imagery (`assets/backgrounds/`)

| File | Size | Notes |
|---|---|---|
| `bg-halftone-rotor.png` | 738×738 PNG | Halftone dot rendering of the rotor, black dots on transparent. Decorative texture for heroes and empty states. Invert it or lower opacity on dark surfaces. Keep it subtle. |
| `guild-graphic.jpg` | 1024×590 JPG | Guild campaign collage: oversized `[GUILD]` bracketed type, the rotor in light gray on black, a red-tinted keyboard photograph, a sky-blue panel with red multilingual "Building Together" copy, a halftone dot grid. Shows the editorial/collage side of the brand. Treat as reference imagery, not a template. |

## Logo rules

Applies to materials that represent Factory or could look like they came
officially from Factory: workshop materials, presentations, event assets,
templates, and other branded resources.

- Use the provided logo files as-is: **white on dark backgrounds, black on
  light ones**.
- Keep clear space around the logo of **at least the height of the mark**.
- Do not change the colors or the shape.
- Do not combine the Factory logo with your own logo or suggest Factory
  endorses your project.
- Creative versions of the logo made for fun and posted as such are fine. They
  are not official Factory materials and do not imply endorsement.
- If something is borderline, check with the Guild Council before publishing.

### Showing membership (Guild members)

| What | How |
|---|---|
| Bio line | `@FactoryAI Guild Member`, for bios on X, LinkedIn, GitHub. |
| Tag Factory | Tag `@FactoryAI` when sharing something built with Droid. |
| Log it | Log the post on the Guild Contributions page to earn points. |

## When the task is not official Factory material

If you are only borrowing Factory's visual language for your own product, do
not use the logo files at all, or use them only when the user confirms the
material is Factory's own. The design language (see `../SKILL.md`) can be
applied without the logos.
