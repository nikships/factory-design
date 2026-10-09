# factory-design

An agent skill for building and restyling UI in the [Factory](https://factory.ai) design language: dark industrial surfaces, hairline borders, near-square corners, uppercase monospace labels, numbered eyebrows, and a sparingly used Factory-orange accent.

## Install

```bash
npx skills add nikships/factory-design
```

Works with Droid, Claude Code, Cursor, and other agents supported by the [`skills`](https://www.npmjs.com/package/skills) CLI.

## Usage

Invoke it by name (`/factory-design`) or ask for something that should "look like Factory built it", for example:

- "Build a settings page in the Factory style"
- "Restyle this SwiftUI app to match factory.ai"
- "Make a README banner with the Factory lockup"

## What's inside

```
factory-design/
├── assets/        Official lockup, rotor, and halftone PNGs, plus the pinwheel SVG and reference renders
├── templates/     SwiftUI (Theme.swift, LogoView.swift) and CSS (tokens.css) starters
├── SKILL.md       Design rules and the build / restyle workflow
└── tokens.md      Verified colors, type, and radii, with steps to re-verify against the live site
```

## Disclaimer

Unofficial. The Factory name, logo, and brand assets belong to Factory. Design tokens were extracted from the public factory.ai site.
