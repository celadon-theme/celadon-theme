#!/usr/bin/env python3
"""Pairwise distinguishability audit: OKLab distance between every accent pair,
under normal vision and simulated protanopia/deuteranopia/tritanopia
(Machado et al. 2009, severity 1.0). Flags pairs likely to be confused.

Thresholds (OKLab euclidean distance):
  < 0.035  FAIL — likely confusable at a glance
  < 0.055  WARN — distinguishable side by side, risky in isolation

The audit is informational: it prints on --check but only accent minpair under
normal vision gates the build (see build_celadon.py).
"""
import math
import sys


def hex_to_lin(hx):
    def lin(c):
        c = c/255
        return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
    return [lin(int(hx[i:i+2], 16)) for i in (1, 3, 5)]


def lin_to_oklab(rgb):
    r, g, b = (max(0.0, min(1.0, v)) for v in rgb)
    l = 0.4122214708*r + 0.5363325363*g + 0.0514459929*b
    m = 0.2119034982*r + 0.6806995451*g + 0.1073969566*b
    s = 0.0883024619*r + 0.2817188376*g + 0.6299787005*b
    l, m, s = l**(1/3), m**(1/3), s**(1/3)
    return (0.2104542553*l + 0.7936177850*m - 0.0040720468*s,
            1.9779984951*l - 2.4285922050*m + 0.4505937099*s,
            0.0259040371*l + 0.7827717662*m - 0.8086757660*s)


CVD = {
 'protan': [[0.152286,1.052583,-0.204868],[0.114503,0.786281,0.099216],[-0.003882,-0.048116,1.051998]],
 'deutan': [[0.367322,0.860646,-0.227968],[0.280085,0.672501,0.047413],[-0.011820,0.042940,0.968881]],
 'tritan': [[1.255528,-0.076749,-0.178779],[-0.078411,0.930809,0.147602],[0.004733,0.691367,0.303900]],
}


def simulate(rgb, kind):
    m = CVD[kind]
    return [sum(m[i][j]*rgb[j] for j in range(3)) for i in range(3)]


def dist(h1, h2, kind=None):
    """OKLab distance between two hexes, optionally under a CVD simulation."""
    a, b = hex_to_lin(h1), hex_to_lin(h2)
    if kind: a, b = simulate(a, kind), simulate(b, kind)
    return math.dist(lin_to_oklab(a), lin_to_oklab(b))


ACCENTS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
FAIL, WARN = 0.035, 0.055

if __name__ == '__main__':
    from build_celadon import THEMES
    names = sys.argv[1:] or list(THEMES)
    for name in names:
        p = THEMES[name]
        pairs = [(a, b) for i, a in enumerate(ACCENTS) for b in ACCENTS[i+1:]]
        pairs += [(a, 'text') for a in ACCENTS]
        rows = []
        for a, b in pairs:
            d = {'normal': dist(p[a], p[b])}
            for kind in CVD: d[kind] = dist(p[a], p[b], kind)
            worst = min(d, key=d.get)
            if d[worst] < WARN:
                lvl = 'FAIL' if d[worst] < FAIL else 'warn'
                rows.append((d[worst], f"  {lvl}  {a:8s}~{b:8s} min {d[worst]:.3f} ({worst})  normal {d['normal']:.3f}"))
        print(f"{name}: {len(rows)} flagged of {len(pairs)} pairs")
        for _, r in sorted(rows): print(r)
