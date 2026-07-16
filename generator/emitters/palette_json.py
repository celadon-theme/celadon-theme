"""Palette JSON: one `<slug>.json` per theme, role → hex. The website and
any tooling read these files (or the generator's --json dump) so no hex is
ever hand-copied. `appearance` is metadata for consumers (the site's variant
switcher), not color math.
"""
import json

ROLES = ['base', 'surface', 'overlay', 'muted', 'subtle', 'text',
         'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
         'br_red', 'br_green', 'br_yellow', 'br_blue', 'br_magenta', 'br_cyan']


def filename(slug):
    return f"{slug}.json"


def emit(slug, p):
    doc = {
        'slug': slug,
        'name': slug.replace('-', ' ').title(),
        'appearance': 'light' if slug == 'celadon-sky' else 'dark',
        'palette': {r: p[r] for r in ROLES},
    }
    return json.dumps(doc, indent=2) + '\n'
