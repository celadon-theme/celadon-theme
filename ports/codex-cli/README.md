# Codex CLI

All four Celadon variants as TextMate (`.tmTheme`) syntax themes.

## Install

From the repository root:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/themes"
cp ports/codex-cli/*.tmTheme "${CODEX_HOME:-$HOME/.codex}/themes/"
```

Or download just the default variant:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/themes"
curl -fL -o "${CODEX_HOME:-$HOME/.codex}/themes/celadon.tmTheme" \
  https://raw.githubusercontent.com/celadon-theme/celadon-theme/main/ports/codex-cli/celadon.tmTheme
```

Start Codex and run **`/theme`**. Choose `celadon`, `celadon-powder`,
`celadon-jade`, or `celadon-sky`. The picker saves the selection as `tui.theme`
in `$CODEX_HOME/config.toml` (normally `~/.codex/config.toml`).

These themes color fenced code blocks and file diffs. They do not replace
the terminal's overall background or ANSI palette: use the matching Celadon
[terminal port](../) for a consistent interface. Match `celadon-sky` with a
light terminal background and the other variants with their dark backgrounds.

Syntax uses green strings, magenta keywords, blue functions, yellow types,
and orange constants. Added and removed content stays green and red.
No font family or size is set.

[Official CLI customization documentation](https://learn.chatgpt.com/docs/cli-customization).
For desktop appearance imports, use the [desktop port](../codex/).

Regenerate with `python3 generator/build_celadon.py --emit codex-cli`.
Do not hand-edit the generated files.
