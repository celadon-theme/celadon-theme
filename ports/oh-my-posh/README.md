# Celadon for oh-my-posh

The prompt from the Celadon screenshots: two lines, `╭─`/`╰─` frame, path +
git on the left, execution time + AWS profile pinned right, and a transient
`❯` so past commands stay compact.

Unlike the other ports there is **one file for all four variants, with no
hexes in it**. Every color is a named ANSI slot (`cyan`, `magenta`,
`darkGray`, …), so the prompt inherits whichever Celadon variant your
terminal runs — switch the terminal theme and the prompt follows. It also
looks right on any other theme with honest ANSI colors.

## Install

Requires [oh-my-posh](https://ohmyposh.dev) and Nerd Font symbols for the
folder / branch / nix glyphs (or swap them out in the config):

- **Ghostty**: nothing to install — Nerd Font symbols are built in.
- **iTerm2 and most others**: use a patched font, e.g.
  `brew install --cask font-monaspace-nf` and select **MonaspiceNe Nerd
  Font** (Nerd Fonts' renamed Monaspace Neon, the screenshot font), or any
  font from [nerdfonts.com](https://www.nerdfonts.com).

```sh
curl --create-dirs -o ~/.config/oh-my-posh/celadon.omp.toml \
  https://raw.githubusercontent.com/celadon-theme/celadon-theme/main/ports/oh-my-posh/celadon.omp.toml
```

Then init for your shell — zsh shown, other shells in the
[oh-my-posh docs](https://ohmyposh.dev/docs/installation/prompt) — by adding
to `~/.zshrc`:

```sh
eval "$(oh-my-posh init zsh --config ~/.config/oh-my-posh/celadon.omp.toml)"
```

This port is hand-written, not generator output — there are no hexes to
generate. Tweaks welcome by PR, but keep it ANSI-only: a hex here would
break the follow-the-terminal contract.
