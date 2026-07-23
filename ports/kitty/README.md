# Celadon for kitty

Four themes: `celadon` (dark, the default), `celadon-powder` (dark, low
contrast), `celadon-jade` (dark, high contrast), `celadon-sky` (light).

## Install

```sh
curl --create-dirs -o ~/.config/kitty/themes/celadon.conf \
  https://raw.githubusercontent.com/celadon-theme/celadon-theme/main/ports/kitty/celadon.conf
```

Then either add to `~/.config/kitty/kitty.conf`:

```
include themes/celadon.conf
```

or pick it interactively — custom themes show up in
`kitty +kitten themes`.

These files are generator output — don't edit them; if a color looks wrong,
[open an issue](https://github.com/celadon-theme/celadon-theme/issues).
