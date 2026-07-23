# Celadon for WezTerm

Four themes: `celadon` (dark, the default), `celadon-powder` (dark, low
contrast), `celadon-jade` (dark, high contrast), `celadon-sky` (light).

## Install

```sh
curl --create-dirs -o ~/.config/wezterm/colors/celadon.toml \
  https://raw.githubusercontent.com/celadon-theme/celadon-theme/main/ports/wezterm/celadon.toml
```

Then in `~/.wezterm.lua` (or `~/.config/wezterm/wezterm.lua`):

```lua
config.color_scheme = 'celadon'
```

To follow the system appearance, grab `celadon-sky` too and pick per
`wezterm.gui.get_appearance()` — see the WezTerm docs.

These files are generator output — don't edit them; if a color looks wrong,
[open an issue](https://github.com/celadon-theme/celadon-theme/issues).
