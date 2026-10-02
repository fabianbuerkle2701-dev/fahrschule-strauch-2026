#!/usr/bin/env python3
"""Bereitet die generierten Illustrationen für die Website auf.

1. Setzt das echte Fahrschul-Logo (assets-src/brand/logo.png) auf Türen, Anhänger und Lkw.
2. Stellt den einfarbigen Hintergrund frei (nur vom Bildrand aus erreichbare Flächen,
   damit weiße Autoteile erhalten bleiben).
3. Schneidet auf den Inhalt zu und speichert nach assets-src/illustrationen/final/.

Aufruf: python3 scripts/illustrations.py
"""
import os
from collections import deque

from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'assets-src', 'illustrationen')
OUT = os.path.join(SRC, 'final')
LOGO = Image.open(os.path.join(ROOT, 'assets-src', 'brand', 'logo.png')).convert('RGBA')

# Logo-Platzierung: (Mittelpunkt x, Mittelpunkt y, Breite) in Pixeln des Quellbilds
JOBS = {
    'auto-seite': [(800, 360, 280)],
    'auto-anhaenger': [(605, 374, 250), (1240, 338, 300)],
    'begleitet-17': [(482, 482, 196)],
    'lkw': [(955, 300, 560)],
    'automatik-schaltung': [],
}


def place_logo(img, cx, cy, width):
    scale = width / LOGO.width
    logo = LOGO.resize((round(LOGO.width * scale), round(LOGO.height * scale)), Image.LANCZOS)
    if scale > 1:
        logo = logo.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
    img.alpha_composite(logo, (round(cx - logo.width / 2), round(cy - logo.height / 2)))


def remove_background(img, tol=22):
    """Flutfüllung vom Rand aus: Pixel nahe der Randfarbe werden transparent."""
    w, h = img.size
    px = img.load()
    corners = [px[0, 0], px[w - 1, 0], px[0, h - 1], px[w - 1, h - 1]]
    bg = tuple(sum(c[i] for c in corners) // 4 for i in range(3))
    near = lambda p: abs(p[0] - bg[0]) + abs(p[1] - bg[1]) + abs(p[2] - bg[2]) <= tol * 3
    mask = Image.new('L', (w, h), 0)
    m = mask.load()
    q = deque()
    for x in range(w):
        q.extend([(x, 0), (x, h - 1)])
    for y in range(h):
        q.extend([(0, y), (w - 1, y)])
    while q:
        x, y = q.popleft()
        if m[x, y] or not near(px[x, y]):
            continue
        m[x, y] = 255
        if x > 0: q.append((x - 1, y))
        if x < w - 1: q.append((x + 1, y))
        if y > 0: q.append((x, y - 1))
        if y < h - 1: q.append((x, y + 1))
    # weiche Kante: Maske leicht weichzeichnen, dann als Transparenz anwenden
    soft = mask.filter(ImageFilter.GaussianBlur(0.8))
    out = img.copy()
    a = out.getchannel('A').load()
    s = soft.load()
    for y in range(h):
        for x in range(w):
            if s[x, y]:
                a[x, y] = max(0, 255 - s[x, y])
    out.putalpha(Image.frombytes('L', (w, h), bytes(a[x, y] for y in range(h) for x in range(w))))
    return out, bg


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, logos in JOBS.items():
        img = Image.open(os.path.join(SRC, f'{name}.png')).convert('RGBA')
        img, bg = remove_background(img)
        for cx, cy, width in logos:
            place_logo(img, cx, cy, width)
        box = img.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()
        pad = 12
        box = (max(0, box[0] - pad), max(0, box[1] - pad), min(img.width, box[2] + pad), min(img.height, box[3] + pad))
        img = img.crop(box)
        img.save(os.path.join(OUT, f'{name}.png'), optimize=True)
        print(f'✓ {name}: {img.size[0]}×{img.size[1]}, Hintergrund {bg}, Logos {len(logos)}')


if __name__ == '__main__':
    main()
