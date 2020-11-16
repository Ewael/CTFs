#!/usr/bin/env

from PIL import Image

image = Image.open("image.png")

count = 0
for i in range(500):
    for j in range(500):
        pixel = image.getpixel((i, j))
        if not pixel == (0, 0, 0):
            count += 1

print("Hero{{{0}}}".format(count))
