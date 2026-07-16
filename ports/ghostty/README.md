# Celadon for Ghostty

Four themes: `celadon` (dark, the default), `celadon-powder` (dark, low
contrast), `celadon-jade` (dark, high contrast), `celadon-sky` (light).

## Install

Copy the theme file(s) into Ghostty's themes directory:

```sh
mkdir -p ~/.config/ghostty/themes
curl -o ~/.config/ghostty/themes/celadon \
  https://raw.githubusercontent.com/celadon-theme/celadon-theme/main/ports/ghostty/celadon
```

Then set it in your Ghostty config (`~/.config/ghostty/config`):

```
theme = celadon
```

To follow the system appearance, grab `celadon-sky` too and use:

```
theme = light:celadon-sky,dark:celadon
```

These files are generator output — don't edit them; if a color looks wrong,
[open an issue](https://github.com/celadon-theme/celadon-theme/issues).
