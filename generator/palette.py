"""Color math: OKLCH → sRGB with gamut fitting, and APCA contrast.

Pure functions, stdlib only. Everything the generator knows about color
science lives here; build_celadon.py holds the design decisions.
"""
import math


def _lin(L, C, h):
    """OKLCH → linear sRGB (may be out of gamut)."""
    hr = math.radians(h)
    a, b = C*math.cos(hr), C*math.sin(hr)
    l_ = L + 0.3963377774*a + 0.2158037573*b
    m_ = L - 0.1055613458*a - 0.0638541728*b
    s_ = L - 0.0894841775*a - 1.2914855480*b
    l, m, s = l_**3, m_**3, s_**3
    r = +4.0767416621*l - 3.3077115913*m + 0.2309699292*s
    g = -1.2684380046*l + 2.6097574011*m - 0.3413193965*s
    bb = -0.0041960863*l - 0.7034186147*m + 1.7076147010*s
    return r, g, bb


def in_gamut(L, C, h):
    return all(-0.001 <= v <= 1.001 for v in _lin(L, C, h))


def to_hex(L, C, h):
    """OKLCH → sRGB hex, walking chroma down until the color fits the gamut."""
    while C > 0 and not in_gamut(L, C, h):
        C -= 0.002
    def enc(x):
        x = max(0.0, min(1.0, x))
        return 12.92*x if x <= 0.0031308 else 1.055*(x**(1/2.4)) - 0.055
    r, g, b = (enc(v) for v in _lin(L, C, h))
    return '#%02x%02x%02x' % (round(r*255), round(g*255), round(b*255))


def apca_y(hexstr):
    r = int(hexstr[1:3], 16)/255; g = int(hexstr[3:5], 16)/255; b = int(hexstr[5:7], 16)/255
    Y = 0.2126729*(r**2.4) + 0.7151522*(g**2.4) + 0.0721750*(b**2.4)
    if Y < 0.022: Y += (0.022 - Y)**1.414
    return Y


def apca_lc(txt, bg):
    """APCA lightness contrast |Lc| between text and background hexes."""
    Yt, Yb = apca_y(txt), apca_y(bg)
    lc = (Yb**0.56 - Yt**0.57)*1.14 if Yb > Yt else (Yb**0.65 - Yt**0.62)*1.14
    return abs(lc*100)
