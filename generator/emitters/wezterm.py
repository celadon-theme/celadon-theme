"""WezTerm: color-scheme TOML, one <slug>.toml per theme, dropped into
~/.config/wezterm/colors/ and selected with `color_scheme = "<slug>"`.
Same ANSI mapping as every terminal port; ansi/brights arrays are the
0-7 / 8-15 slots in order.
"""

ACC = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']


def filename(slug):
    return f"{slug}.toml"


def _arr(vals):
    return "[" + ", ".join(f'"{v}"' for v in vals) + "]"


def emit(slug, p):
    ansi = [p['overlay']] + [p[a] for a in ACC] + [p['text']]
    brights = [p['muted']] + [p['br_' + a] for a in ACC] + [p['text']]
    lines = [
        f"# {slug} · calm green. honest color.",
        "# https://github.com/celadon-theme/celadon-theme — generated, do not edit",
        "",
        "[colors]",
        f'background = "{p["base"]}"',
        f'foreground = "{p["text"]}"',
        f'cursor_bg = "{p["subtle"]}"',
        f'cursor_fg = "{p["base"]}"',
        f'cursor_border = "{p["subtle"]}"',
        f'selection_bg = "{p["overlay"]}"',
        f'selection_fg = "{p["text"]}"',
        f"ansi = {_arr(ansi)}",
        f"brights = {_arr(brights)}",
        "",
        "[metadata]",
        f'name = "{slug}"',
        'author = "Celadon"',
        'origin_url = "https://github.com/celadon-theme/celadon-theme"',
    ]
    return "\n".join(lines) + "\n"
