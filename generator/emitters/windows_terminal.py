"""Windows Terminal: one scheme object per <slug>.json, pasted into the
`schemes` array of settings.json (or shipped as a settings fragment).
Windows Terminal names slot 5 "purple" — it still holds the magenta role;
the mapping stays the honest ANSI one used by every terminal port.
"""
import json


def filename(slug):
    return f"{slug}.json"


def emit(slug, p):
    doc = {
        'name': slug,
        'background': p['base'],
        'foreground': p['text'],
        'cursorColor': p['subtle'],
        'selectionBackground': p['overlay'],
        'black': p['overlay'],
        'red': p['red'],
        'green': p['green'],
        'yellow': p['yellow'],
        'blue': p['blue'],
        'purple': p['magenta'],
        'cyan': p['cyan'],
        'white': p['text'],
        'brightBlack': p['muted'],
        'brightRed': p['br_red'],
        'brightGreen': p['br_green'],
        'brightYellow': p['br_yellow'],
        'brightBlue': p['br_blue'],
        'brightPurple': p['br_magenta'],
        'brightCyan': p['br_cyan'],
        'brightWhite': p['text'],
    }
    return json.dumps(doc, indent=2) + '\n'
