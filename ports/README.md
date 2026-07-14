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

🚧 First ports (Ghostty, iTerm2) land once the palette is locked.
