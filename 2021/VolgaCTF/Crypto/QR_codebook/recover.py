#!/usr/bin/env python3

from PIL import Image
import sys, cv

# pix[x, y] = pix[x][y] = column y, line x
white = (255, 255, 255)
black = (0, 0, 0)

if len(sys.argv) == 1:
    print(f'please provide encrypted png to decrypt')
    exit(1)

def printBlock(block):
    for i in range(len(block)):
        for j in range(len(block[0])):
            try:
                print(f'{block[i][j][0]}'.ljust(3), end=' ')
            except:
                print(f'{block[i][j]}'.ljust(3), end=' ')
        print('')
    print('---')

def getParams():
    qr = Image.open('qr.png')
    qrpix = qr.load()
    xor = Image.open('xored.png')
    xorpix = xor.load()
    flag = Image.open(sys.argv[1])
    pix = flag.load()
    blockSize = (16, 22)
    return qr, qrpix, xor, xorpix, flag, pix, blockSize

def getBlock(pix, coords):
    block = [[None for _ in range(blockSize[1])] for _ in range(blockSize[0])]
    x1, x2 = coords[0] * blockSize[0], (coords[0] + 1) * blockSize[0]
    y1, y2 = coords[1] * blockSize[1], (coords[1] + 1) * blockSize[1]
    for x in range(x1, x2): # lines
        for y in range(y1, y2): # columns
            try:
                block[x % blockSize[0]][y % blockSize[1]] = [pix[y, x][0], pix[y, x][1], pix[y, x][2]]
            except:
                block[x % blockSize[0]][y % blockSize[1]] = pix[y, x]
    return block

def fixBlock(pix, block, coords):
    x1, x2 = coords[0] * blockSize[0], (coords[0] + 1) * blockSize[0]
    y1, y2 = coords[1] * blockSize[1], (coords[1] + 1) * blockSize[1]
    for x in range(x1, x2): # lines
        for y in range(y1, y2): # columns
            try:
                pix[y, x][0] = block[x % blockSize[0]][y % blockSize[1]][0]
                pix[y, x][1] = block[x % blockSize[0]][y % blockSize[1]][1]
                pix[y, x][2] = block[x % blockSize[0]][y % blockSize[1]][2]
            except:
                pix[y, x] = block[x % blockSize[0]][y % blockSize[1]]

qr, qrpix, xor, xorpix, flag, pix, blockSize = getParams()
coords = (0, 0)
xorblock = getBlock(xorpix, coords)
printBlock(xorblock)
fixBlock(pix, xorblock, coords)

flag.save('flag.png')
