#!/usr/bin/env python3
"""Setzt das echte Fahrschul-Logo perspektivisch auf die Autos der KI-Fotos.

Regel: Jedes Auto trägt das echte Logo (nie vom Bildgenerator gezeichnet).
Das Logo wird auf ein Viereck auf der Tür verzerrt und multiplizierend eingerechnet,
damit Licht und Schatten der Tür erhalten bleiben (wirkt wie eine Folie).

Quelle: assets-src/fotos-ki/strauch-ki-*.png (Abacus AI Studio, GPT Image 2.5)
Ziel:   assets-src/fotos-ki/final/<name>.png, danach npm run images
Aufruf: python3 scripts/fotos.py
"""
import os

from PIL import Image, ImageChops, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'assets-src', 'fotos-ki')
OUT = os.path.join(SRC, 'final')
LOGO = Image.open(os.path.join(ROOT, 'assets-src', 'brand', 'logo.png')).convert('RGBA')


def quad(cx, cy, w, slope=0.0, near=1.0, far_left=True):
    """Viereck für das Logo: Mitte, Breite, Neigung (dy/dx) und Verkürzung der fernen Seite."""
    h = w * LOGO.height / LOGO.width
    hl, hr = (h * near, h) if far_left else (h, h * near)
    x0, x1 = cx - w / 2, cx + w / 2
    y0, y1 = cy - slope * w / 2, cy + slope * w / 2
    # Reihenfolge: oben links, oben rechts, unten rechts, unten links
    return [(x0, y0 - hl / 2), (x1, y1 - hr / 2), (x1, y1 + hr / 2), (x0, y0 + hl / 2)]


# Bild: (Variante, [Logo-Vierecke])
JOBS = {
    # echter VW Tiguan der Fahrschule (Referenz: assets-src/fotos-ki/referenz/tiguan.jpg)
    'hero': ('echt-hero-c', [quad(1700, 726, 166, slope=-0.13, near=0.93, far_left=False)]),
    'klasse-b': ('echt-klasse-b-b', [quad(452, 682, 158, slope=0.0, near=0.97)]),
    'klasse-be': ('echt-klasse-be-b', [quad(343, 656, 106, slope=0.0, near=0.98, far_left=False)]),
    'b197': ('b197-a', []),  # Innenraum, kein Auto von außen
    'bf17': ('bf17-a', []),
    'lkw': ('lkw-b', [quad(335, 758, 220, slope=0.07, near=0.9)]),
    'theorie': ('theorie-b', []),
}


def coeffs(dst, src):
    """Koeffizienten für Image.transform(PERSPECTIVE): bildet dst-Punkte auf src-Punkte ab."""
    import numpy as np
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y])
        B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()


def place(img, q):
    w, h = img.size
    src = [(0, 0), (LOGO.width, 0), (LOGO.width, LOGO.height), (0, LOGO.height)]
    warped = LOGO.transform((w, h), Image.PERSPECTIVE, coeffs(q, src), Image.BICUBIC)
    warped = warped.filter(ImageFilter.GaussianBlur(0.35))
    base = img.convert('RGB')
    mult = ImageChops.multiply(base, warped.convert('RGB'))
    alpha = warped.getchannel('A').point(lambda a: int(a * 0.95))
    return Image.composite(mult, base, alpha)


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, (variant, quads) in JOBS.items():
        img = Image.open(os.path.join(SRC, f'strauch-ki-{variant}.png')).convert('RGB')
        for q in quads:
            img = place(img, q)
        img.save(os.path.join(OUT, f'{name}.png'), optimize=True)
        print(f'✓ {name}: {img.size[0]}×{img.size[1]}, Logos {len(quads)}')


if __name__ == '__main__':
    main()
