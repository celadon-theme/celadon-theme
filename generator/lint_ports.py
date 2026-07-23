#!/usr/bin/env python3
"""Artifact lint: prove the committed port files are well-formed, not just
drift-free. The drift check can't catch a broken emitter — broken output
matches broken output — so this parses every artifact for real:

  ghostty      all 16 palette slots + required keys, values are hexes
  iterm2       plist parses; Ansi 0-15 + Background/Foreground; components in [0,1]
  json         parses; slug matches; all 18 roles present, values are hexes
  claude-code  parses; base is dark/light; every override is a hex
  termic       parses; colorScheme is dark/light; ui/terminal values are hex
               or rgba(); terminal block carries all 16 ANSI slots
  alacritty    TOML parses; primary/cursor/selection/normal/bright complete, hexes
  kitty        required keys + color0-15 present, values are hexes
  wezterm      TOML parses; ansi/brights are 8 hexes each; metadata.name = slug
  windows-terminal  parses; full scheme key set, values are hexes
  oh-my-posh   TOML parses; palette values are named ANSI slots; NO hex
               anywhere in the file (the follow-the-terminal contract)
  svg cards    XML parses

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
RGBA = re.compile(r'^rgba\(\d{1,3},\d{1,3},\d{1,3},0?\.\d+\)$')
TERM_KEYS = (['background', 'foreground', 'cursor', 'cursorAccent', 'selectionBackground']
             + [c for b in ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
                for c in (b, 'bright' + b[0].upper() + b[1:])])
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


def lint_claude(slug):
    path, raw = read('ports', 'claude-code', f'{slug}.json')
    if raw is None: return
    try:
        d = json.loads(raw)
    except Exception as e:
        return err(path, f'does not parse: {e}')
    if d.get('base') not in ('dark', 'light'): err(path, f"base is {d.get('base')!r}")
    bad = [f'{k}={v!r}' for k, v in d.get('overrides', {}).items() if not HEX.match(str(v))]
    if bad: err(path, f'non-hex overrides: {bad}')


def lint_termic(slug):
    path, raw = read('ports', 'termic', f'{slug}.json')
    if raw is None: return
    try:
        d = json.loads(raw)
    except Exception as e:
        return err(path, f'does not parse: {e}')
    if d.get('colorScheme') not in ('dark', 'light'):
        err(path, f"colorScheme is {d.get('colorScheme')!r}")
    for block in ('ui', 'terminal'):
        bad = [f'{k}={v!r}' for k, v in d.get(block, {}).items()
               if not (HEX.match(str(v)) or RGBA.match(str(v)))]
        if bad: err(path, f'{block}: bad values: {bad}')
    missing = [k for k in TERM_KEYS if k not in d.get('terminal', {})]
    if missing: err(path, f'terminal block missing: {missing}')


ANSI8 = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']


def lint_alacritty(slug):
    path, raw = read('ports', 'alacritty', f'{slug}.toml')
    if raw is None: return
    try:
        c = tomllib.loads(raw.decode()).get('colors', {})
    except Exception as e:
        return err(path, f'TOML does not parse: {e}')
    for sect, keys in (('primary', ['background', 'foreground']),
                       ('cursor', ['text', 'cursor']),
                       ('selection', ['text', 'background']),
                       ('normal', ANSI8), ('bright', ANSI8)):
        vals = c.get(sect, {})
        missing = [k for k in keys if k not in vals]
        if missing: err(path, f'colors.{sect} missing {missing}')
        bad = [v for v in vals.values() if not HEX.match(str(v))]
        if bad: err(path, f'colors.{sect} non-hex: {bad}')


def lint_kitty(slug):
    path, raw = read('ports', 'kitty', f'{slug}.conf')
    if raw is None: return
    kv = dict(re.findall(r'^(\w+) (\S+)$', raw.decode(), re.M))
    need = (['background', 'foreground', 'cursor', 'cursor_text_color',
             'selection_background', 'selection_foreground', 'url_color']
            + [f'color{i}' for i in range(16)])
    missing = [k for k in need if k not in kv]
    if missing: err(path, f'missing keys: {missing}')
    bad = [f'{k}={v}' for k, v in kv.items() if not HEX.match(v)]
    if bad: err(path, f'non-hex values: {bad}')


def lint_wezterm(slug):
    path, raw = read('ports', 'wezterm', f'{slug}.toml')
    if raw is None: return
    try:
        d = tomllib.loads(raw.decode())
    except Exception as e:
        return err(path, f'TOML does not parse: {e}')
    c = d.get('colors', {})
    for k in ('background', 'foreground', 'cursor_bg', 'cursor_fg',
              'cursor_border', 'selection_bg', 'selection_fg'):
        if not HEX.match(str(c.get(k, ''))): err(path, f'{k} missing or non-hex')
    for arr in ('ansi', 'brights'):
        v = c.get(arr, [])
        if len(v) != 8 or not all(HEX.match(str(x)) for x in v):
            err(path, f'{arr} is not 8 hexes')
    if d.get('metadata', {}).get('name') != slug: err(path, 'metadata.name != slug')


def lint_wt(slug):
    path, raw = read('ports', 'windows-terminal', f'{slug}.json')
    if raw is None: return
    try:
        d = json.loads(raw)
    except Exception as e:
        return err(path, f'does not parse: {e}')
    if d.get('name') != slug: err(path, f"name is {d.get('name')!r}")
    need = (['background', 'foreground', 'cursorColor', 'selectionBackground']
            + [c for b in ('black', 'red', 'green', 'yellow', 'blue', 'purple',
                           'cyan', 'white')
               for c in (b, 'bright' + b[0].upper() + b[1:])])
    missing = [k for k in need if k not in d]
    if missing: err(path, f'missing keys: {missing}')
    bad = [f'{k}={v}' for k, v in d.items() if k != 'name' and not HEX.match(str(v))]
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
        lint_ghostty(slug); lint_iterm2(slug); lint_json(slug)
        lint_claude(slug); lint_termic(slug); lint_svg(slug)
        lint_alacritty(slug); lint_kitty(slug); lint_wezterm(slug); lint_wt(slug)
    lint_omp()
    for e in errors: print('FAIL', e)
    n = 10*len(SLUGS) + 1
    print(f'{n - len(errors)}/{n} artifacts clean' if not errors
          else f'{len(errors)} problem(s)')
    sys.exit(1 if errors else 0)
