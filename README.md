<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/celadon-logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/celadon-logo-light.svg">
    <img src="assets/celadon-logo-universal.svg" alt="Celadon logo — a crackle-glaze tile" width="120">
  </picture>
</p>

<h1 align="center">Celadon</h1>

<p align="center"><em>calm green. honest color.</em></p>

---

A sage-green theme family for terminals and editors, named for the pale
grey-green ceramic glaze.

Celadon keeps the field calm — low-saturation sage, dark or light — while the
accents stay **honest to their ANSI meaning**: red is red, green is green, so
diffs, test output, and prompts read the way they should. Accents sit in a
tight loudness band so syntax never outranks your content.

The palettes are **generated, not hand-tuned**: a small set of OKLCH parameters
and rules, with every build gated on APCA contrast and accent-distinctness
checks.

## Variants

One graded family, light → dark: **sky → powder → celadon → jade**.

| variant | field | for |
|---|---|---|
| `celadon sky` | light · sage paper | daytime |
| `celadon powder` | dark · low contrast | night, dim rooms |
| `celadon` | dark · medium contrast | **the default** |
| `celadon jade` | dark · high contrast | bright rooms, glare |

## Status

🚧 **Early days.** The palette is in final validation; first ports (Ghostty,
iTerm2) land here, with Neovim and friends to follow in their own repos under
this org.

## Repo layout

This is the hub repo for the [`celadon-theme`](https://github.com/celadon-theme)
org. It holds the palette generator (the source of truth), flat-file ports
under [`ports/<app>/`](ports/), and logo/screenshot assets. Ports that a
plugin manager installs from a repo root (Neovim, tmux, …) get their own
repos under the org.

## Contributing

Issues — port requests, color problems, screenshots — are the most useful
thing right now. Before touching any hex value, read
[CONTRIBUTING.md](CONTRIBUTING.md): the palettes are generated, so fixes go
through the generator, never through hand-edited output.

## License

[MIT](LICENSE)
