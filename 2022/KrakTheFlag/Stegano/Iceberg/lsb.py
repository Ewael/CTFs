#!/usr/bin/env python3

from PIL import Image
import binascii
from Crypto.Util.number import long_to_bytes

def getlsb(path):
    im = Image.open(path)
    pix_val = list(im.getdata())
    lsbs=""

    for idx,val in enumerate(pix_val):
        # Converting each rgb values into binary and keeping only the Least Significant Bit
        lsbs=lsbs+'{0:08b}'.format(val[0])[-1]
        lsbs=lsbs+'{0:08b}'.format(val[1])[-1]
        lsbs=lsbs+'{0:08b}'.format(val[2])[-1]

    n=int(lsbs,2)
    # Converting binary to ascii
    print(long_to_bytes(n))

getlsb('iceberg.png')

# D4v1D_F0r3V3r
