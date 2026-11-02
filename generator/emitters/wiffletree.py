"""wiffletree: theme JSON for ~/Library/Application Support/Wiffletree/themes/,
one <slug>.json per theme. Each file carries one variant — celadon-sky is
light-only, the other three dark-only — so Wiffletree lists it in the matching
theme menu. Mapping follows termic's ui block: the field ramp (base, surface,
overlay), text and subtle, edge = muted (termic's border), accent = magenta
(the family's focus chrome, so green stays honest), on-accent = base, focus =
cyan, and green/red/yellow/blue/magenta are the honest hues. Fonts are
celadontheme.com's body and mono faces; size is points.
"""
import json


def filename(slug):
    return f"{slug}.json"


def emit(slug, p):
    variant = {
        'base': p['base'], 'surface': p['surface'], 'overlay': p['overlay'],
        'text': p['text'], 'subtle': p['subtle'], 'edge': p['muted'],
        'accent': p['magenta'], 'on-accent': p['base'], 'focus': p['cyan'],
        'green': p['green'], 'red': p['red'], 'yellow': p['yellow'],
        'blue': p['blue'], 'magenta': p['magenta'],
    }
    doc = {
        'version': 1,
        'name': slug.replace('-', ' ').title(),
        'fonts': {'ui': 'Figtree', 'mono': 'JetBrains Mono', 'size': 14},
        'variants': {'light' if slug == 'celadon-sky' else 'dark': variant},
    }
    return json.dumps(doc, indent=2) + '\n'
