"""Alacritty: TOML color sections, one <slug>.toml per theme, pulled in via
`[general] import` (Alacritty ≥ 0.13). Same ANSI mapping as every terminal
port: 1=red … 6=cyan on an overlay black, brights from the br_* tier.
"""

ORDER = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']


def filename(slug):
    return f"{slug}.toml"


def emit(slug, p):
    normal = dict(black=p['overlay'], white=p['text'],
                  **{a: p[a] for a in ORDER[1:7]})
    bright = dict(black=p['muted'], white=p['text'],
                  **{a: p['br_' + a] for a in ORDER[1:7]})
    lines = [
        f"# {slug} · calm green. honest color.",
        "# https://github.com/celadon-theme/celadon-theme — generated, do not edit",
        "",
        "[colors.primary]",
        f'background = "{p["base"]}"',
        f'foreground = "{p["text"]}"',
        "",
        "[colors.cursor]",
        f'text = "{p["base"]}"',
        f'cursor = "{p["subtle"]}"',
        "",
        "[colors.selection]",
        f'text = "{p["text"]}"',
        f'background = "{p["overlay"]}"',
        "",
        "[colors.normal]",
        *[f'{k} = "{normal[k]}"' for k in ORDER],
        "",
        "[colors.bright]",
        *[f'{k} = "{bright[k]}"' for k in ORDER],
    ]
    return "\n".join(lines) + "\n"
