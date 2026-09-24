# Celadon for Slack

All four variants ship as generated, comma-separated legacy theme strings:

| Variant | Theme file |
|---|---|
| Celadon · default | [celadon.txt](celadon.txt) |
| Sky · light | [celadon-sky.txt](celadon-sky.txt) |
| Powder · dark, low contrast | [celadon-powder.txt](celadon-powder.txt) |
| Jade · dark, high contrast | [celadon-jade.txt](celadon-jade.txt) |

## Install

1. Open a theme file above and copy its entire line of colors.
2. In Slack on desktop, click your profile picture → **Preferences** →
   **Appearance** → **Custom theme**.
3. Next to **Theme Colors**, choose **Import theme**, paste the line into
   **Paste your legacy theme colors**, and click **Apply**.

Some Slack versions put these controls under **Themes**. Choose light mode
for Sky and dark mode for the other variants. Window gradient and darker
sidebar preferences can also affect the result.

See Slack's [theme instructions](https://slack.com/help/articles/205166337-Change-your-Slack-theme).

## Compatibility

Current Slack maps legacy theme colors to its built-in palette, so the
import is an approximation of Celadon. The four variants may look less
distinct after import. Exact palette colors and the generator's contrast
guarantees do not carry over to Slack's rendered theme. This limitation is
also documented by the [Catppuccin Slack port](https://github.com/catppuccin/slack).

## Color mapping

The ten legacy slots, in order:

| Slack slot | Celadon role |
|---|---|
| Column background | `base` |
| Menu background | `surface` |
| Active item | `magenta` |
| Active item text | `base` |
| Hover item | `overlay` |
| Text color | `text` |
| Active presence | `green` |
| Mention badge | `red` |
| Top navigation background | `surface` |
| Top navigation text | `text` |

These files are generated; don't edit the hex values by hand. Regenerate
with `python3 generator/build_celadon.py --emit slack`.
