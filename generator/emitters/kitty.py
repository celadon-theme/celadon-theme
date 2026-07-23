"""kitty: flat key-value .conf, one <slug>.conf per theme, used via
`include` or the `kitty +kitten themes` picker (the ## header block is that
kitten's metadata format). Same ANSI mapping as every terminal port.
"""

ACC = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']


def filename(slug):
    return f"{slug}.conf"


def emit(slug, p):
    name = slug.replace('-', ' ').title()
    appearance = 'light' if slug == 'celadon-sky' else 'dark'
    lines = [
        f"## name: {name}",
        "## author: Celadon",
        "## license: MIT",
        f"## blurb: calm sage-green {appearance} field, accents honest to their",
        "## ANSI meaning — generated, not hand-tuned.",
        "# https://github.com/celadon-theme/celadon-theme — generated, do not edit",
        "",
        f"background {p['base']}",
        f"foreground {p['text']}",
        f"cursor {p['subtle']}",
        f"cursor_text_color {p['base']}",
        f"selection_background {p['overlay']}",
        f"selection_foreground {p['text']}",
        f"url_color {p['blue']}",
        "",
        f"color0 {p['overlay']}",
        f"color8 {p['muted']}",
        *[line for i, a in enumerate(ACC, start=1)
          for line in (f"color{i} {p[a]}", f"color{i + 8} {p['br_' + a]}")],
        f"color7 {p['text']}",
        f"color15 {p['text']}",
    ]
    return "\n".join(lines) + "\n"
