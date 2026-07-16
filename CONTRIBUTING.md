# Contributing to Celadon

Thanks for your interest! Celadon is young — the palette is locked and
the first ports are out — so the most useful contributions right now are
issues: port requests, color problems you spot in real use, and
screenshots.

## How Celadon is built (read this before touching hexes)

The palettes are **generated, not hand-tuned**. A small set of OKLCH
parameters and rules produces every hex, and each build is gated on
APCA contrast and accent-distinctness checks.

That means:

- **Don't hand-edit hex values** — not in the palette, not in a port.
  A tweaked hex silently breaks the contrast/distinctness guarantees
  the theme is built on.
- If a color looks wrong somewhere, **open an issue** describing where
  and how (screenshots help a lot). Fixes go through the generator so
  every variant and port stays consistent.
- CI enforces this mechanically: every push re-runs the gates
  (`generator/build_celadon.py --check`) and regenerates all committed
  output — a hand-edited port or swatch fails the drift check.

## Repo layout

This is the hub repo for the [`celadon-theme`](https://github.com/celadon-theme)
org:

- **`generator/`** — the palette source of truth, build gates, and one
  emitter per port format.
- **`ports/<app>/`** — flat-file ports (Ghostty, iTerm2, Alacritty,
  Kitty, WezTerm, …): config files you copy or curl. These are build
  output, committed for easy install.
- **`assets/`** — logos and screenshots.

Ports that a plugin manager installs from a repo root (Neovim, tmux, …)
live in their own repos under the org.

## Adding a port

Open a **port request** issue first so we can agree on scope. A port
should:

- ship **all four variants** — file slugs `celadon`, `celadon-sky`,
  `celadon-powder`, `celadon-jade`;
- keep the **ANSI mapping honest** — red is red, green is green; don't
  remap accents to taste;
- be **generated** where possible: flat-file ports are emitted by the
  build, so a new port usually means a new emitter, not a hand-written
  config. An emitter is one module in `generator/emitters/` exposing
  `filename(slug)` and `emit(slug, palette)`, plus a registry entry —
  see `ghostty.py` for the shape. Regenerate with
  `python3 generator/build_celadon.py --emit`.

## Pull requests

- One port or fix per PR.
- Include a screenshot for anything visual.
- Regenerated files should come from the generator — note the command
  you ran in the PR description.

## Code of conduct

Be kind. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
