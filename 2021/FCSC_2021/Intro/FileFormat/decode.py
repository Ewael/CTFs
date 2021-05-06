#!/usr/bin/env python3

import binascii
import hashlib

f = open('challenge.iq', 'rb')
enc = f.read()
f.close()
l = len(enc)

phases = []
quadra = []
for j in range(0, l, 8):
    i = enc[j:j+4]
    q = enc[j+4:j+8]
    phases.append(i)
    quadra.append(q)

r1 = b''.join(i for i in phases)
r2 = b''.join(q for q in quadra)
res = r1 + r2
flag = 'FCSC{' + hashlib.sha256(res).hexdigest() + '}'
print(f'i_0 = {phases[0]}, q_0 = {quadra[0]}')
print(f'i_n = {phases[-1]}, q_n = {quadra[-1]}')
print(len(res))
print(flag)

# FCSC{843161934a8e53da8723047bed55e604e725160b868abb74612e243af94345d7}
