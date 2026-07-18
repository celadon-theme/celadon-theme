#!/usr/bin/env python3
"""Artifact lint: prove the committed port files are well-formed, not just
drift-free. The drift check can't catch a broken emitter — broken output
matches broken output — so this parses every artifact for real:

  ghostty     all 16 palette slots + required keys, values are hexes
  iterm2      plist parses; Ansi 0-15 + Background/Foreground; components in [0,1]
  json        parses; slug matches; all 18 roles present, values are hexes
  oh-my-posh  TOML parses; palette values are named ANSI slots; NO hex
              anywhere in the file (the follow-the-terminal contract)
  svg cards   XML parses

Stdlib only. Exits non-zero listing every failure.  Usage:
  python3 generator/lint_ports.py
"""
import json, os, plistlib, re, sys, tomllib
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ['celadon', 'celadon-powder', 'celadon-jade', 'celadon-sky']
ROLES = ['base', 'surface', 'overlay', 'muted', 'subtle', 'text',
         'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
         'br_red', 'br_green', 'br_yellow', 'br_blue', 'br_magenta', 'br_cyan']
HEX = re.compile(r'^#[0-9a-f]{6}$')
ANSI_NAMES = {'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
              'white', 'darkGray', 'lightRed', 'lightGreen', 'lightYellow',
              'lightBlue', 'lightMagenta', 'lightCyan', 'lightWhite',
              'default', 'transparent'}
errors = []


def err(path, msg):
    errors.append(f"{os.path.relpath(path, ROOT)}: {msg}")


def read(*parts):
    path = os.path.join(ROOT, *parts)
    if not os.path.exists(path):
        err(path, 'missing')
        return path, None
    with open(path, 'rb') as f:
        return path, f.read()


def lint_ghostty(slug):
    path, raw = read('ports', 'ghostty', slug)
    if raw is None: return
    kv = re.findall(r'^([\w-]+) = (.+)$', raw.decode(), re.M)
    slots = [v.split('=', 1) for k, v in kv if k == 'palette']
    if sorted(int(n) for n, _ in slots) != list(range(16)):
        err(path, 'palette slots are not exactly 0-15')
    bad = [v for _, v in slots if not HEX.match(v)]
    for k in ('background', 'foreground', 'cursor-color', 'cursor-text',
              'selection-background', 'selection-foreground'):
        vals = [v for kk, v in kv if kk == k]
        if len(vals) != 1: err(path, f'expected exactly one {k}')
        else: bad += [] if HEX.match(vals[0]) else [vals[0]]
    if bad: err(path, f'non-hex values: {bad}')


def lint_iterm2(slug):
    path, raw = read('ports', 'iterm2', f'{slug}.itermcolors')
    if raw is None: return
    try:
        p = plistlib.loads(raw)
    except Exception as e:
        return err(path, f'plist does not parse: {e}')
    for k in [f'Ansi {i} Color' for i in range(16)] + ['Background Color', 'Foreground Color']:
        c = p.get(k)
        if not isinstance(c, dict):
            err(path, f'missing {k}'); continue
        comps = [c.get(f'{ch} Component') for ch in ('Red', 'Green', 'Blue', 'Alpha')]
        if not all(isinstance(v, float) and 0.0 <= v <= 1.0 for v in comps):
            err(path, f'{k}: components not floats in [0,1]')


def lint_json(slug):
    path, raw = read('ports', 'json', f'{slug}.json')
    if raw is None: return
    try:
        d = json.loads(raw)
    except Exception as e:
        return err(path, f'does not parse: {e}')
    if d.get('slug') != slug: err(path, f"slug is {d.get('slug')!r}")
    pal = d.get('palette', {})
    if sorted(pal) != sorted(ROLES): err(path, 'palette roles != the 18 expected')
    bad = [v for v in pal.values() if not HEX.match(str(v))]
    if bad: err(path, f'non-hex values: {bad}')


def lint_omp():
    path, raw = read('ports', 'oh-my-posh', 'celadon.omp.toml')
    if raw is None: return
    try:
        cfg = tomllib.loads(raw.decode())
    except Exception as e:
        return err(path, f'TOML does not parse: {e}')
    for name, val in cfg.get('palette', {}).items():
        if val not in ANSI_NAMES:
            err(path, f'palette.{name} = {val!r} is not a named ANSI slot')
    for m in re.finditer(r'#[0-9a-fA-F]{3,8}\b', raw.decode()):
        err(path, f'hex color {m.group()!r} — this port must stay ANSI-only')


def lint_svg(slug):
    path, raw = read('assets', 'palette', f'{slug}.svg')
    if raw is None: return
    try:
        ET.fromstring(raw)
    except Exception as e:
        err(path, f'not valid XML: {e}')


if __name__ == '__main__':
    for slug in SLUGS:
        lint_ghostty(slug); lint_iterm2(slug); lint_json(slug); lint_svg(slug)
    lint_omp()
    for e in errors: print('FAIL', e)
    n = 4*len(SLUGS) + 1
    print(f'{n - len(errors)}/{n} artifacts clean' if not errors
          else f'{len(errors)} problem(s)')
    sys.exit(1 if errors else 0)
