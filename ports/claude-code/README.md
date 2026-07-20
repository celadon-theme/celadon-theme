# Celadon for Claude Code

Four themes: `celadon` (dark, the default), `celadon-powder` (dark, low
contrast), `celadon-jade` (dark, high contrast), `celadon-sky` (light).

Full theme JSON for the Claude Code CLI: brand accents, prompt/permission
chrome, diff and message backgrounds, subagent labels — all from the
generated palette (diff tints are computed by the generator, not
hand-picked).

## Install

Copy a theme into Claude Code's themes directory:

```sh
mkdir -p ~/.claude/themes
curl -o ~/.claude/themes/celadon.json \
  https://raw.githubusercontent.com/celadon-theme/celadon-theme/main/ports/claude-code/celadon.json
```

Then pick it with the `/theme` command (custom themes appear in the theme
picker).

These files are generator output — don't edit them; if a color looks wrong,
[open an issue](https://github.com/celadon-theme/celadon-theme/issues).
