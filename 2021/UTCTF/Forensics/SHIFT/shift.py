#!/usr/bin/env python3

from PIL import Image
from collections import deque

im = Image.open('SHIFT.png')
pix = im.load()
h, w = 136, 1967

rows = []
for x in range(h):
    row = []
    for y in range(w):
        row.append(pix[y, x])
    rows.append(row)

for i in range(h):
    items = deque(rows[i])
    items.rotate(-(h - i*6))
    rows[i] = list(items)

for x in range(h):
    for y in range(w):
        pix[y, x] = rows[x][y]

im.save('shifted.png')
