#!/usr/bin/env python3

import codecs

a = 0x3767384d797b665a
b = 0x253246706345774c
c = 0x2930412d28476444
d = 0x535e36767254657a
e = 0x4f4262344a35506a
f = 0x246d6b6f59616e73
g = 0x3378496c48715558
h = 0x524e4b6943683175
i = 0x7d74395f51572a56

L = [a, b, c, d, e, g, h, i]

for n in L:
    n = hex(n)[2:]
    print(bytearray.fromhex(n).decode())
