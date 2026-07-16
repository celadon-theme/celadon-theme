#!/usr/bin/env python3
"""Palette cards for the README: one SVG per theme in assets/palette/.

Self-theming — every color in a card comes from the palette it shows, hex
labels included, so the README never states a hex. Generated output; CI's
drift check keeps these in sync with the generator.

Usage:  python3 generator/swatches.py
"""
import os
from build_celadon import THEMES

ROWS = [('field', ['base', 'surface', 'overlay', 'muted', 'subtle', 'text']),
        ('accents', ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']),
        ('bright', ['br_red', 'br_green', 'br_yellow', 'br_blue', 'br_magenta', 'br_cyan'])]

CELL_W, CELL_H, GAP, PAD = 112, 44, 12, 20
W = PAD*2 + 6*CELL_W + 5*GAP
ROW_H = CELL_H + 34
MONO = "ui-monospace, SFMono-Regular, Menlo, monospace"


def card(slug, p):
    H = 52 + len(ROWS)*ROW_H + PAD - 10
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" role="img" aria-label="{slug} palette">',
         f'  <rect width="{W}" height="{H}" rx="10" fill="{p["base"]}"/>',
         f'  <text x="{PAD}" y="34" font-family="{MONO}" font-size="15" '
         f'font-weight="bold" fill="{p["text"]}">{slug}</text>']
    for r, (label, roles) in enumerate(ROWS):
        y = 52 + r*ROW_H
        for c, role in enumerate(roles):
            x = PAD + c*(CELL_W + GAP)
            s += [f'  <rect x="{x}" y="{y}" width="{CELL_W}" height="{CELL_H}" rx="6" '
                  f'fill="{p[role]}" stroke="{p["muted"]}" stroke-opacity="0.45"/>',
                  f'  <text x="{x}" y="{y + CELL_H + 14}" font-family="{MONO}" '
                  f'font-size="10" fill="{p["subtle"]}">{role}</text>',
                  f'  <text x="{x}" y="{y + CELL_H + 26}" font-family="{MONO}" '
                  f'font-size="10" fill="{p["text"]}">{p[role]}</text>']
    s.append('</svg>')
    return '\n'.join(s) + '\n'


if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    outdir = os.path.join(root, 'assets', 'palette')
    os.makedirs(outdir, exist_ok=True)
    for slug, p in THEMES.items():
        path = os.path.join(outdir, f'{slug}.svg')
        with open(path, 'w') as f:
            f.write(card(slug, p))
        print('wrote', os.path.relpath(path, root))
