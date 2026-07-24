"""Neovim: lua palette modules, one <slug>.lua per theme — the generated
half of celadon-theme/nvim. That repo's highlight mapping is hand-written
and consumes these; no hex exists there outside its palette/ dir, which is
copied from ports/nvim/ (manual sync, per the decided model). Includes the
derived tints and the decorative orange/indigo accents — editor syntax is
where the extra hues earn their keep.
"""

ROLES = ['base', 'surface', 'overlay', 'overlay2', 'muted', 'subtle', 'text',
         'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
         'br_red', 'br_green', 'br_yellow', 'br_blue', 'br_magenta', 'br_cyan',
         'orange', 'indigo', 'br_orange', 'br_indigo',
         'diff_add', 'diff_add_dim', 'diff_add_word',
         'diff_del', 'diff_del_dim', 'diff_del_word',
         'magenta_tint', 'magenta_deep']


def filename(slug):
    return f"{slug}.lua"


def emit(slug, p):
    lines = [
        f"-- {slug} · calm green. honest color.",
        "-- https://github.com/celadon-theme/celadon-theme — generated, do not edit",
        "return {",
        f'  appearance = "{"light" if slug == "celadon-sky" else "dark"}",',
        *[f'  {r} = "{p[r]}",' for r in ROLES],
        "}",
    ]
    return "\n".join(lines) + "\n"
