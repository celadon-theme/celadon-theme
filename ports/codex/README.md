# Codex desktop

All four Celadon variants as appearance share strings for the desktop app.
Generated from the same palette as the terminal ports.

## Install

1. Open **Settings → Appearance**.
2. Under **Dark theme**, click **Import** and paste the entire contents of
   [`celadon.txt`](celadon.txt), [`celadon-powder.txt`](celadon-powder.txt),
   or [`celadon-jade.txt`](celadon-jade.txt).
3. Under **Light theme**, import [`celadon-sky.txt`](celadon-sky.txt).
4. Choose **Light**, **Dark**, or **System** for the appearance mode.

The import slot must match the file's light/dark variant. On macOS, copy a
downloaded file with `pbcopy < celadon.txt`.

These themes set the background, foreground, green accent, red/green diff
colors, and magenta skill color. Powder, Celadon, and Jade use increasing
interface contrast. Windows are opaque to keep the palette consistent.

The share format requires font settings: importing resets UI and code fonts
to the app defaults. Reapply any custom fonts afterward. Code highlighting
uses the built-in **Codex** preset; desktop imports do not install custom
TextMate syntax themes. For those, use the [CLI port](../codex-cli/).

## Format and compatibility

Each file is a `codex-theme-v1:` prefix followed by JSON. The schema was
verified against the installed desktop app's share-string parser on
2026-09-24; it is not a published stable API. The picker may continue to
show **Codex** because that is the underlying code preset's name.

[Official appearance documentation](https://learn.chatgpt.com/docs/reference/settings#appearance).

Regenerate with `python3 generator/build_celadon.py --emit codex`.
Do not hand-edit the generated files.
