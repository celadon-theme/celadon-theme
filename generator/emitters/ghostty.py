"""Ghostty: flat key = value config, one extensionless file per theme.

ANSI mapping keeps semantic hue identity: 1=red 2=green 3=yellow 4=blue
5=magenta 6=cyan. Brights (9-14) use the br_* tier, not duplicated normals.
"""


def filename(slug):
    return slug


def emit(slug, p):
    lines = [
        f"# {slug} · calm green. honest color.",
        "# https://github.com/celadon-theme/celadon-theme — generated, do not edit",
        f"palette = 0={p['overlay']}",
        f"palette = 1={p['red']}",
        f"palette = 2={p['green']}",
        f"palette = 3={p['yellow']}",
        f"palette = 4={p['blue']}",
        f"palette = 5={p['magenta']}",
        f"palette = 6={p['cyan']}",
        f"palette = 7={p['text']}",
        f"palette = 8={p['muted']}",
        f"palette = 9={p['br_red']}",
        f"palette = 10={p['br_green']}",
        f"palette = 11={p['br_yellow']}",
        f"palette = 12={p['br_blue']}",
        f"palette = 13={p['br_magenta']}",
        f"palette = 14={p['br_cyan']}",
        f"palette = 15={p['text']}",
        f"background = {p['base']}",
        f"foreground = {p['text']}",
        f"cursor-color = {p['subtle']}",
        f"cursor-text = {p['base']}",
        f"selection-background = {p['overlay']}",
        f"selection-foreground = {p['text']}",
    ]
    return "\n".join(lines) + "\n"
