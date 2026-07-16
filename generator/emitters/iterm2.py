"""iTerm2: XML plist, one `<slug>.itermcolors` per theme. Import via
Settings → Profiles → Colors → Color Presets… → Import.

Same ANSI mapping as every port: 1=red 2=green 3=yellow 4=blue 5=magenta
6=cyan; brights 9-14 use the br_* tier. Key set matches the
iTerm2-Color-Schemes gallery layout (Badge/Bold/Link/Tab/Underline included)
so the file is gallery-submittable as-is. plistlib keeps output stable and
identical in shape to iTerm2's own exports.
"""
import plistlib


def filename(slug):
    return f"{slug}.itermcolors"


def _color(hx, alpha=1.0):
    r, g, b = (int(hx[i:i+2], 16)/255 for i in (1, 3, 5))
    return {'Alpha Component': alpha, 'Blue Component': b, 'Color Space': 'sRGB',
            'Green Component': g, 'Red Component': r}


def emit(slug, p):
    ansi = [p['overlay'], p['red'], p['green'], p['yellow'], p['blue'], p['magenta'],
            p['cyan'], p['text'], p['muted'], p['br_red'], p['br_green'], p['br_yellow'],
            p['br_blue'], p['br_magenta'], p['br_cyan'], p['text']]
    d = {f'Ansi {i} Color': _color(hx) for i, hx in enumerate(ansi)}
    d.update({
        'Background Color': _color(p['base']),
        'Badge Color': _color(p['red'], 0.5),
        'Bold Color': _color(p['text']),
        'Cursor Color': _color(p['subtle']),
        'Cursor Guide Color': _color(p['blue'], 0.25),
        'Cursor Text Color': _color(p['base']),
        'Foreground Color': _color(p['text']),
        'Link Color': _color(p['blue']),
        'Selected Text Color': _color(p['text']),
        'Selection Color': _color(p['overlay']),
        'Tab Color': _color(p['base']),
        'Underline Color': _color(p['blue']),
    })
    return plistlib.dumps(d, sort_keys=True).decode('ascii')
