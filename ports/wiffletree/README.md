# Celadon for Wiffletree

Four themes: `celadon` (dark, the default), `celadon-powder` (dark, low
contrast), `celadon-jade` (dark, high contrast), `celadon-sky` (light).

[Wiffletree](https://github.com/Vyttle-LLC/wiffletree) theme files — the
interface colors from the generated palette plus Figtree and JetBrains Mono
at 14 pt. Each file carries one variant: Sky appears in Wiffletree's Light
theme menu, the other three in its Dark theme menu. Needs a Wiffletree
version with theme file support.

## Install

Copy a theme into Wiffletree's themes folder:

```sh
mkdir -p ~/Library/Application\ Support/Wiffletree/themes
curl -o ~/Library/Application\ Support/Wiffletree/themes/celadon.json \
  https://raw.githubusercontent.com/celadon-theme/celadon-theme/main/ports/wiffletree/celadon.json
```

Then pick it in **Settings › Appearance** (Light theme / Dark theme).

The themes use Figtree and JetBrains Mono. If they aren't installed,
Wiffletree falls back to the system fonts and the colors still apply:

```sh
brew install --cask font-figtree font-jetbrains-mono
```

These files are generator output — don't edit them; if a color looks wrong,
[open an issue](https://github.com/celadon-theme/celadon-theme/issues).
