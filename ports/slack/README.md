# Celadon for Slack

Each generated file contains one line of four comma-separated hex colors,
ordered as System navigation, Selected items, Presence indication, and
Notifications. Copy the entire line without adding labels or backticks.

| Variant | Theme file | Color mode |
|---|---|---|
| Celadon · default | [celadon.txt](celadon.txt) | Dark |
| Sky · light | [celadon-sky.txt](celadon-sky.txt) | Light |
| Powder · dark, low contrast | [celadon-powder.txt](celadon-powder.txt) | Dark |
| Jade · dark, high contrast | [celadon-jade.txt](celadon-jade.txt) | Dark |

## Install

1. Open a theme file above and copy its entire line.
2. In Slack on desktop, click your profile picture → **Preferences** →
   **Appearance**.
3. Set **Color Mode** to **Dark** for Celadon, Powder, or Jade; choose
   **Light** for Sky. **System** follows your OS appearance, so it can leave
   the message area white even when you enter a dark navigation color.
4. Open **Custom theme** → **Import**, paste the line, and click **Apply**.
   If your Slack version only accepts legacy strings there, enter the four
   values individually in the controls in the order listed below.
5. Turn **Window gradient** off for a solid background. Start with
   **Darker sidebars** on for the dark variants and off for Sky.
6. Save changes if prompted.

Some Slack versions put theme controls under **Themes**. See Slack's
[theme instructions](https://slack.com/help/articles/205166337-Change-your-Slack-theme).

The four-color string format and order follow the
[Codigrate Slack port](https://github.com/codigrate/slack-themes#theme-format).

## Color mapping

| Slack control | Celadon role |
|---|---|
| System navigation | `slack_navigation`: brighter, richer sage derived from the base |
| Selected items | `slack_selection`: mint derived from green and cyan |
| Presence indication | `green` |
| Notifications | `red` |

This adaptation puts more color into the navigation because Slack's gray
conversation surface occupies most of the window. The navigation is lighter
and more saturated than the terminal base; the selection is a cooler mint
instead of lime. Presence stays green and notifications stay coral. These
Slack-specific tones are generated without changing the core palette.

## Compatibility

The previous files used ten legacy import slots. The current UI exposes
only the four controls above; separate text, hover, menu, and top-navigation
text colors are not configurable here. Slack derives the remaining colors,
so this port approximates Celadon rather than reproducing its full palette.
The generator's contrast guarantees do not carry over to Slack's rendered
theme, and the variants may look less distinct in Slack.

Changing the theme colors does not select light or dark color mode.
Window gradient blends the navigation and selected-item colors. Selected
items use a derived mint to keep that blend in the green family instead of
introducing the previous magenta accent's pink or purple tint.
Darker sidebars adjusts sidebar
contrast independently of the message area's color mode.

These files are generated; don't edit the hex values by hand. Regenerate
with `python3 generator/build_celadon.py --emit slack`.
