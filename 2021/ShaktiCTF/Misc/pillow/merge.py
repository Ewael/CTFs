#!/usr/bin/env python3

from PIL import Image

def printBlock(pix, i):
    print(f'block {i}')
    for x in range(10):
        for y in range(10):
            print(str(pix[y, x]).ljust(3), end=' ')
        print('')
    print('---')

def placeBlock(flagpix, impix, i):
    printBlock(impix, i)
    i -= 1
    y = (i // 50) * 10
    x = (i % 50) * 10
    for u in range(x, x + 10):
        for v in range(y, y + 10):
            pix = impix[v % 10, u % 10]
            flagpix[u, v] = (pix, pix, pix)

doss = './60x50/'
flag = Image.new('RGB', (500, 600), 'red')
flagpix = flag.load()

for i in range(1, 3001):
    im = Image.open(f'{doss}{i}.jpg')
    impix = im.load()
    placeBlock(flagpix, impix, i)

flag.save('flag.png')

# shaktictf{pill0w_l1k3_a_g00d_c0nscience}
