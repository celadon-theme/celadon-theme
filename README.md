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

## License

[MIT](LICENSE)
