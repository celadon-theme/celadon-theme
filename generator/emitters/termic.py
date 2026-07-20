"""termic: theme JSON for ~/.config/termic/themes/, one <slug>.json per
theme. The ui block maps the field ramp (bg → bg-3) and brand accents
(accent = the celadon green, ok = cyan so it reads apart from the accent);
the terminal block is the same honest ANSI mapping as every terminal port.
rgba() strings put alpha over role hexes — formatting, not new colors.
"""
import json


def filename(slug):
    return f"{slug}.json"


def _rgba(hx, a):
    r, g, b = (int(hx[i:i+2], 16) for i in (1, 3, 5))
    return f"rgba({r},{g},{b},{a})"


def emit(slug, p):
    doc = {
        'name': slug.replace('-', ' ').title(),
        'colorScheme': 'light' if slug == 'celadon-sky' else 'dark',
        'ui': {
            'bg': p['base'], 'bg-1': p['surface'], 'bg-2': p['overlay'],
            'bg-3': p['overlay2'],
            'fg': p['text'], 'fg-dim': p['subtle'], 'fg-faint': p['muted'],
            'border': p['muted'], 'border-soft': p['overlay'],
            'hover': _rgba(p['text'], 0.05),
            'sel': _rgba(p['green'], 0.22),
            'accent': p['green'], 'accent-soft': _rgba(p['green'], 0.22),
            'accent-deep': p['green_deep'], 'accent-fg': p['base'],
            'ok': p['cyan'], 'ok-fg': p['base'],
            'warn': p['yellow'], 'err': p['red'],
        },
        'terminal': {
            'background': p['base'], 'foreground': p['text'],
            'cursor': p['subtle'], 'cursorAccent': p['base'],
            'selectionBackground': p['overlay'],
            'black': p['overlay'], 'red': p['red'], 'green': p['green'],
            'yellow': p['yellow'], 'blue': p['blue'], 'magenta': p['magenta'],
            'cyan': p['cyan'], 'white': p['text'],
            'brightBlack': p['muted'], 'brightRed': p['br_red'],
            'brightGreen': p['br_green'], 'brightYellow': p['br_yellow'],
            'brightBlue': p['br_blue'], 'brightMagenta': p['br_magenta'],
            'brightCyan': p['br_cyan'], 'brightWhite': p['text'],
        },
    }
    return json.dumps(doc, indent=2) + '\n'
