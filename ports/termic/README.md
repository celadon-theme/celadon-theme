# Celadon for termic

Four themes: `celadon` (dark, the default), `celadon-powder` (dark, low
contrast), `celadon-jade` (dark, high contrast), `celadon-sky` (light).

Full [termic](https://github.com/simion/termic) theme JSON — the `ui` field
ramp and accents plus an honest-ANSI `terminal` block, all from the
generated palette.

## Install

Copy a theme into termic's themes directory:

```sh
mkdir -p ~/.config/termic/themes
curl -o ~/.config/termic/themes/celadon.json \
  https://raw.githubusercontent.com/celadon-theme/celadon-theme/main/ports/termic/celadon.json
```

It appears in the theme picker (custom themes list at the bottom). If it
doesn't show up, launch termic from a terminal and look for
`[themes] skipping ...`.

These files are generator output — don't edit them; if a color looks wrong,
[open an issue](https://github.com/celadon-theme/celadon-theme/issues).
