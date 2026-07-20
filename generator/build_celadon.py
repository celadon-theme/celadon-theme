#!/usr/bin/env python3
"""Celadon — the shipping generator. Four themes from one set of OKLCH numbers:

  celadon-powder  dark, low contrast   (pivot-scale of celadon, factor 0.80)
  celadon         dark, medium         (the reference palette)
  celadon-jade    dark, high contrast  (pivot-scale of celadon, factor 1.18)
  celadon-sky     light, sage paper    (its own definition — light physics differ)

Palette LOCKED 2026-07-16. Design rules baked in:
  - sage-green tint on both dark (base L0.21) and light (base L0.96) fields
  - dark accents: L~0.80, chroma ≤0.13 (gamut-clamped), APCA 66-72 —
    visible AND rich
  - light accents: one uniform chroma budget (cap 0.11, L 0.48-0.58) — a dusty
    family sharing the field's calm, not vivid primaries
  - every build gated: `python3 generator/build_celadon.py --check` exits
    non-zero if any gate fails

CLI:  --check          gates (text/accent APCA, accent distinctness) + CVD info
      --emit [port ..] write ports/<port>/<file> for every theme
      --json           slug → role → hex dump (the website + tooling feed)
"""
import json, math, os, sys
from palette import to_hex, apca_lc, in_gamut
from distinctness import hex_to_lin, lin_to_oklab, dist
import emitters

HUE = 140                      # sage anchor
PIVOT = 0.55
ACC_ROLES = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
ACC_HUE = dict(red=25, green=132, yellow=92, blue=240, magenta=338, cyan=185)


def maxC(L, h):
    C = 0.0
    while C < 0.4 and in_gamut(L, C+0.002, h): C += 0.002
    return C


def to_oklch(hx):
    L, a, b = lin_to_oklab(hex_to_lin(hx))
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


# ---- dark medium: the reference palette -----------------------------------
def dark_medium():
    p = {}
    for role, (L, C) in dict(base=(0.21, 0.022), surface=(0.24, 0.027), overlay=(0.29, 0.033),
                             muted=(0.58, 0.026), subtle=(0.69, 0.025), text=(0.86, 0.024)).items():
        p[role] = to_hex(L, C, HUE)
    for a in ACC_ROLES:                       # L 0.80, chroma target 0.13 (clamped)
        h = ACC_HUE[a]; L = 0.80; C = min(0.13, maxC(L, h)*0.94)
        p[a] = to_hex(L, C, h); p['br_'+a] = to_hex(L+0.07, C*0.95, h)
    return p


# ---- contrast siblings: scale the whole L range around the pivot ----------
def pivot_scale(pal, factor):
    out = {}
    for role, hx in pal.items():
        L, C, h = to_oklch(hx); out[role] = to_hex(PIVOT + (L-PIVOT)*factor, C, h)
    return out


# ---- light: dusty uniform accents on sage paper ----------------------------
def light():
    p = {}
    for role, (L, C) in dict(base=(0.960, 0.022), surface=(0.930, 0.030), overlay=(0.890, 0.037),
                             muted=(0.60, 0.020), subtle=(0.50, 0.022), text=(0.37, 0.016)).items():
        p[role] = to_hex(L, C, HUE)
    LA = dict(red=(0.51, 27), green=(0.52, 142), yellow=(0.58, 80), blue=(0.48, 250),
              magenta=(0.49, 338), cyan=(0.51, 192))
    for a, (L, h) in LA.items():              # uniform chroma budget: family, not primaries
        C = min(0.11, maxC(L, h)*0.90)
        p[a] = to_hex(L, C, h); p['br_'+a] = to_hex(L-0.08, min(C*1.05, maxC(L-0.08, h)), h)
    return p


med = dark_medium()
THEMES = {'celadon-powder': pivot_scale(med, 0.80), 'celadon': med,
          'celadon-jade': pivot_scale(med, 1.18), 'celadon-sky': light()}


# ---- derived tones: computed tints for rich ports --------------------------
def tints(p):
    """Accent-tinted fields and depth steps that rich ports need (claude-code,
    termic; nvim later): diff backgrounds, a field step past overlay, a deep
    accent. Computed from each theme's own base — dark themes tint upward,
    light themes downward — never hand-picked.
    """
    L, _, _ = to_oklch(p['base'])
    d = 1 if L < 0.5 else -1
    out = {}
    for name, role in (('add', 'green'), ('del', 'red')):
        h = ACC_HUE[role]
        out[f'diff_{name}'] = to_hex(L + d*0.055, 0.035, h)
        out[f'diff_{name}_dim'] = to_hex(L + d*0.030, 0.025, h)
        out[f'diff_{name}_word'] = to_hex(L + d*0.105, 0.050, h)
    out['magenta_tint'] = to_hex(L + d*0.050, 0.025, ACC_HUE['magenta'])
    Lo, Co, ho = to_oklch(p['overlay'])
    out['overlay2'] = to_hex(Lo + d*0.05, Co, ho)
    La, Ca, ha = to_oklch(p['green'])
    out['green_deep'] = to_hex(La - 0.18, min(Ca, 0.09), ha)  # capped C: deep, not loud
    return out


for _p in THEMES.values():
    _p.update(tints(_p))

# Hard gate floors — just under the locked values, so the locked build always
# passes but a param change that genuinely regresses fails CI. Conformance to
# the exact locked hexes is the drift check's job (regenerate + diff ports/).
GATES = dict(text_lc=65, accent_lc=54, minpair=0.080)


def check():
    ok = True
    for name, p in THEMES.items():
        band = [apca_lc(p[a], p['base']) for a in ACC_ROLES]
        text = apca_lc(p['text'], p['base'])
        npair = min(dist(p[a], p[b]) for i, a in enumerate(ACC_ROLES) for b in ACC_ROLES[i+1:])
        cvd = min(min(dist(p[a], p[b], k) for k in ('protan', 'deutan', 'tritan'))
                  for i, a in enumerate(ACC_ROLES) for b in ACC_ROLES[i+1:])
        fails = []
        if text < GATES['text_lc']: fails.append(f"text APCA {text:.0f} < {GATES['text_lc']}")
        if min(band) < GATES['accent_lc']: fails.append(f"accent APCA {min(band):.0f} < {GATES['accent_lc']}")
        if npair < GATES['minpair']: fails.append(f"minpair {npair:.3f} < {GATES['minpair']}")
        status = 'FAIL: ' + '; '.join(fails) if fails else 'ok'
        print(f"{name:15s} base {p['base']}  text APCA {text:.0f}  "
              f"accents {min(band):.0f}-{max(band):.0f}  minpair {npair:.3f}  "
              f"worstCVD {cvd:.3f} (info)  {status}")
        ok = ok and not fails
    return ok


def emit(ports):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for port in ports:
        mod = emitters.PORTS[port]
        outdir = os.path.join(root, 'ports', port)
        os.makedirs(outdir, exist_ok=True)
        for name, p in THEMES.items():
            path = os.path.join(outdir, mod.filename(name))
            with open(path, 'w') as f:
                f.write(mod.emit(name, p))
            print('wrote', os.path.relpath(path, root))


if __name__ == '__main__':
    if '--check' in sys.argv:
        sys.exit(0 if check() else 1)
    elif '--emit' in sys.argv:
        named = [a for a in sys.argv[1:] if not a.startswith('--')]
        emit(named or list(emitters.PORTS))
    else:
        print(json.dumps(THEMES))
