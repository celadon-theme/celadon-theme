#!/usr/bin/env python3
"""Render the four Celadon builds as truecolor ANSI in a real terminal —
the honest test. Palettes come live from build_celadon.py, never a file.

Usage:  python3 generator/preview.py                # all four builds
        python3 generator/preview.py celadon-sky    # one build
"""
import re
import sys

from build_celadon import THEMES

ORDER = ['celadon-powder', 'celadon', 'celadon-jade', 'celadon-sky']

def fg(hx): r,g,b = int(hx[1:3],16),int(hx[3:5],16),int(hx[5:7],16); return f"\x1b[38;2;{r};{g};{b}m"
def bg(hx): r,g,b = int(hx[1:3],16),int(hx[3:5],16),int(hx[5:7],16); return f"\x1b[48;2;{r};{g};{b}m"
R = "\x1b[0m"
W = 74
ANSI = re.compile(r'\x1b\[[0-9;]*m')


def block(name, p):
    B = bg(p['base'])
    def strip(s): return ANSI.sub('', s)
    def line(s=""):
        pad = W - len(strip(s))
        print(f"{B}  {s}{B}{' ' * max(0, pad)}{R}")

    t = lambda k: fg(p[k])
    line()
    line(f"{t('text')}\x1b[1m{name}{R}{B}   {t('muted')}base {p['base']}")
    line()
    line(f"{t('cyan')}~/dev/project {t('magenta')}main {t('muted')}› {t('text')}git diff --stat && npm test")
    line(f"{t('subtle')} src/auth/session.ts {t('muted')}| {t('green')}+18 {t('red')}-4")
    line(f"{t('green')}  ✓ {t('subtle')}refresh token rotates {t('muted')}(11ms)")
    line(f"{t('red')}  ✗ {t('text')}session expiry drift {t('muted')}— expected 3600, got 3611")
    line(f"{t('yellow')}  warn {t('subtle')}deprecated API, use the v2 client")
    line(f"{t('blue')}  info {t('subtle')}12 passed{t('muted')}, 1 failed, 2 skipped")
    line(f"{t('muted')}# comment / whisper layer     {t('subtle')}subtle / secondary     {t('text')}text / primary")
    sw = "  ".join(f"{bg(p[k])}{fg(p['base'])} {k[:3]} {R}{B}" for k in ('red','green','yellow','blue','magenta','cyan'))
    line(sw)
    sw2 = "  ".join(f"{bg(p['br_'+k])}{fg(p['base'])} b{k[:2]} {R}{B}" for k in ('red','green','yellow','blue','magenta','cyan'))
    line(sw2)
    line()
    print()


names = sys.argv[1:] or ORDER
for name in names:
    if name not in THEMES:
        sys.exit(f"unknown theme {name!r}: {sorted(THEMES)}")
    block(name, THEMES[name])
