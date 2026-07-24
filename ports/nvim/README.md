# Celadon palette for Neovim

These are **not** the Neovim theme — install that from
[`celadon-theme/nvim`](https://github.com/celadon-theme/nvim).

Each `<slug>.lua` here is the generated palette module (roles + derived
tints) that the nvim repo's hand-written highlight mapping consumes; they
are copied into its `lua/celadon/palette/` verbatim. One source of truth:
if a color changes, it changes here first, through the generator.
