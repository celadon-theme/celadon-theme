# Celadon for Alacritty

Four themes: `celadon` (dark, the default), `celadon-powder` (dark, low
contrast), `celadon-jade` (dark, high contrast), `celadon-sky` (light).

## Install

```sh
curl --create-dirs -o ~/.config/alacritty/themes/celadon.toml \
  https://raw.githubusercontent.com/celadon-theme/celadon-theme/main/ports/alacritty/celadon.toml
```

Then in `~/.config/alacritty/alacritty.toml`:

```toml
[general]
import = ["~/.config/alacritty/themes/celadon.toml"]
```

(On Alacritty 0.13, `import` is top-level rather than under `[general]`.)

These files are generator output — don't edit them; if a color looks wrong,
[open an issue](https://github.com/celadon-theme/celadon-theme/issues).
