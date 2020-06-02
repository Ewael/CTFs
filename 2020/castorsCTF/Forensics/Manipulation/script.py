#!/usr/bin/env python3

import binascii

f = open("test", "r").readlines()
res = ""
for line in f:
    res += line[10:50]
res = ''.join(res.split(' '))
output = open("image.jpg", "wb")
output.write(binascii.unhexlify(res))
