# Ports

Flat-file ports live here, one directory per app:

```
ports/
  ghostty/
  iterm2/
  alacritty/
  ...
```

Each port ships all four variants — `celadon`, `celadon-sky`,
`celadon-powder`, `celadon-jade` — in whatever format the app expects.
These files are **build output from the generator**: install them, don't
edit them. If a color looks wrong, [open an issue](../../../issues)
instead — see [CONTRIBUTING.md](../CONTRIBUTING.md).

Ports installed by a plugin manager from a repo root (Neovim, tmux, …)
live in their own repos under the
[`celadon-theme`](https://github.com/celadon-theme) org, not here.

Available now: [Ghostty](ghostty/) · [iTerm2](iterm2/) ·
[Alacritty](alacritty/) · [kitty](kitty/) · [WezTerm](wezterm/) ·
[Windows Terminal](windows-terminal/) · [oh-my-posh](oh-my-posh/) ·
[Claude Code](claude-code/) · [termic](termic/).

Two exceptions to the "generated, one file per variant" rule:

- [`oh-my-posh/`](oh-my-posh/) is **hand-written and variant-less** — it
  contains no hexes at all, only named ANSI slots, so the one file follows
  whichever Celadon variant the terminal runs.
- [`json/`](json/) is the machine-readable palette (slug → role → hex) that
  the website and tooling consume — not an app port, but committed for the
  same reason: one source of truth, curl-able at a stable ref.
