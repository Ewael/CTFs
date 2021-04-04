#!/usr/bin/env python3

from pwn import *
import binascii

code = b'..4..2..6'
code = b'674332666' # flag
assert len(code) == 9
check = p64(0x000313176d171310) + p64(0x000007050201034b)
check = list(check)[:15]
check[14] = 0
print(check)

print(f'code = {code.decode("utf-8")}')
for i in range(15):
    check[i] ^= code[i % 9]
scheck = ''.join([chr(a) for a in check])
print(f'check = {scheck}')
assert scheck[2] == '#'
assert scheck[5] == '!'
assert scheck[8] == '}'

buf = [0x55, 0x4c, 0x42, 0x35, 0x50, 0x48, 0x76, 0x62, 0x3b, 0x4e, 0x62, 0x7e, \
        5, 0x6b, 100, 0x4b, 0x6e, 0x3c, 0x7b, 0x10, 0x11, 0x69, 0x39, 6, 0x77, \
        0x55, 0x62, 0x5d, 0x70, 0x10, 0x57, 0x6d, 0x60, 0x7e, 0x52, 100, 0x4e, \
        1, 0x62, 0x69, 0x41, 4, 0x74, 0x4f, 2, 0x23]

a = 'shaktiCTF{'
b = buf[:10]
x1 = xor(a, b)
print(f'x1 = {x1}')
x2 = xor(x1, check[:10])
print(f'x2 = {x2}')

flag = []
for i in range(len(buf)):
    flag.append(check[i % 0xe] ^ buf[i])
sflag = ''.join([chr(a) for a in flag])
print(sflag)

assert sflag[:10] == 'shaktiCTF{'
assert sflag[-1] == '}'
assert sflag[0xb] == 'H'

"""
tmaltiGPF|QH4_EjMe_1 [D4DcSiQ1t4D_cV33Q_p0Un!z
tmaltiGPF|QH4_EjMe_1 [D4DcSiQ1t4D_cV33Q_p0Un!z
"""

# shaktiCTF{TH3_BoMb_1$_D3AcTiV4t3D_gR34T_w0Rk!}
