# factory-design

An agent skill that carries the [Factory](https://factory.com) (Droid) design language and official brand kit. It is language-, framework-, and medium-agnostic: use it for apps, websites, terminal UIs, slides, READMEs, diagrams, icons, and AI-generated images.

Dark industrial surfaces, hairline borders, near-square corners, uppercase monospace labels, numbered eyebrows, and a sparingly used Factory-orange accent.

## Install

```bash
npx skills add nikships/factory-design
```

Works with Droid, Claude Code, Cursor, and other agents supported by the [`skills`](https://www.npmjs.com/package/skills) CLI.

## Usage

Invoke it by name (`/factory-design`) or ask for something that should "look like Factory built it", for example:

- "Build a settings page in the Factory style"
- "Restyle this app to match factory.com"
- "Make a README banner with the Factory lockup"
- "Write an image prompt for a Factory-style hero illustration"

## What's inside

```
factory-design/
├── SKILL.md                         Design rules and workflow
├── tokens.json                      Verified colors, type, radii, motion (machine-readable)
├── tokens.md                        Same tokens with provenance and re-verification steps
├── assets/
│   ├── logos/                       Official lockup, rotor (mark), and factory.ai dot logo, SVG + PNG
│   └── backgrounds/                 Halftone rotor and Guild graphic
└── references/
    ├── applying.md                  Per-medium guide, image-generation prompts, restyle checklist
    ├── brand-kit.md                 Asset manifest and logo rules
    ├── community-guidelines.md      Factory Guild community guidelines
    └── guild-faq-and-help.md        Guild FAQ and where to get help
```

## Sources

Brand kit, guidelines, FAQ, and help content come from the [Factory Guild resources page](https://factory.com/guild/resources) (pulled 2026-10-25). Tokens were verified against factory.com's compiled CSS on the same date.

## Disclaimer

Unofficial. The Factory name, logo, and brand assets belong to Factory and are used under its published logo rules.
