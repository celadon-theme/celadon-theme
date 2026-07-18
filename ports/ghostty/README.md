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

## Fonts

The theme doesn't touch fonts. The screenshots use
[Monaspace Neon](https://monaspace.githubnext.com) — set it in your own
config if you want the same look:

```
font-family = Monaspace Neon
```

Glyph icons (e.g. from the [oh-my-posh port](../oh-my-posh/)) render with
any font here — Ghostty bundles Nerd Font symbols as a built-in fallback.

---

These files are generator output — don't edit them; if a color looks wrong,
[open an issue](https://github.com/celadon-theme/celadon-theme/issues).
