"""Vector Sydney skyline (Harbour Bridge + Opera House + sun) used where we have no photo.
draw(stroke, sail_fill, sun_fill, sw) returns an inline <svg> sized by its container."""


def _sail(x, w, h, right=True, base=200):
    ax = x + (w * 0.86 if right else w * 0.14)
    ay = base - h
    if right:
        outer = f"Q {x + w * 0.12:.1f} {base - h * 0.75:.1f} {ax:.1f} {ay:.1f} Q {x + w * 0.98:.1f} {base - h * 0.45:.1f} {x + w:.1f} {base}"
    else:
        outer = f"Q {x + w * 0.02:.1f} {base - h * 0.45:.1f} {ax:.1f} {ay:.1f} Q {x + w * 0.88:.1f} {base - h * 0.75:.1f} {x + w:.1f} {base}"
    rib = f"M {ax:.1f} {ay:.1f} Q {x + w * 0.5:.1f} {base - h * 0.35:.1f} {x + w * (0.62 if right else 0.38):.1f} {base}"
    return f"M {x} {base} {outer} Z", rib


SAILS = [(214, 96, 150, True), (286, 84, 122, True), (346, 64, 88, True),
         (392, 74, 112, False), (446, 58, 82, False), (490, 46, 56, False)]


def draw(stroke="#1B1714", sail_fill="#FBF8F5", sun_fill="#EC5B39", sw=4, water=True, cls="", style=""):
    sails = "".join(
        f'<path d="{p}" fill="{sail_fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
        f'<path d="{r}" fill="none" stroke="{stroke}" stroke-width="{sw * .6:.1f}" stroke-linecap="round"/>'
        for p, r in (_sail(*s) for s in SAILS))
    hangers = "".join(
        f'<path d="M {x} {176} L {x} {176 - (1 - ((x - 105) / 85) ** 2) * 88:.1f}" stroke="{stroke}" stroke-width="{sw * .5:.1f}"/>'
        for x in range(35, 180, 14))
    bridge = (f'<path d="M 20 176 Q 105 0 190 176" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"/>'
              f'<path d="M 34 176 Q 105 30 176 176" fill="none" stroke="{stroke}" stroke-width="{sw * .7:.1f}"/>'
              f'{hangers}<path d="M -10 176 L 214 176" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"/>'
              f'<rect x="4" y="138" width="22" height="58" fill="{sail_fill}" stroke="{stroke}" stroke-width="{sw}"/>'
              f'<rect x="184" y="138" width="22" height="58" fill="{sail_fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    base = (f'<path d="M 196 200 L 548 200 L 556 216 L 188 216 Z" fill="{sail_fill}" stroke="{stroke}" '
            f'stroke-width="{sw}" stroke-linejoin="round"/>')
    waves = ""
    if water:
        waves = "".join(
            f'<path d="M {x0} {y} q 12 -8 24 0 t 24 0 t 24 0 t 24 0" fill="none" stroke="{stroke}" '
            f'stroke-width="{sw * .6:.1f}" stroke-linecap="round"/>'
            for x0, y in [(40, 240), (250, 236), (420, 246), (150, 262), (340, 268)])
    sun = f'<circle cx="470" cy="70" r="42" fill="{sun_fill}"/>'
    return (f'<svg class="{cls}" style="{style}" viewBox="-20 0 600 280" xmlns="http://www.w3.org/2000/svg" '
            f'overflow="visible">{sun}{bridge}{sails}{base}{waves}</svg>')
