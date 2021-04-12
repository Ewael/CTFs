#!/usr/bin/env python3

from pwn import *
import binascii
from Crypto.Util.number import long_to_bytes, bytes_to_long
import string

def add(c, i):
    l = c + i
    x = l >> 4
    y = l << 4
    return x ^ y

def crypt(pt):
    enc = []
    for i in range(len(pt)):
        c = add(pt[i], i) & 0xff
        c = xor(c, 0x69)
        c = long_to_bytes(bytes_to_long(c) + 0x42)
        c = xor(c, 0x7f)
        c = long_to_bytes(bytes_to_long(c) & 0xff)
        enc.append(c)
    return enc

charset = (string.printable).encode('utf-8')
exp = b'801031409f40332e2f43b16ece9fdee30ecf405f200f3eddfe5f702cc1407fdf5c116dfcfe2d413c0ffa614ddf7ab2a20000000000000000'
exp = binascii.unhexlify(exp)
flag = b'X' * len(exp)
log.info(f'exp = {exp}')

for i in range(len(exp)):
    for l in charset:
        arr = list(flag)
        arr[i] = l
        flag = bytes(arr)
        enc = crypt(flag)
        if bytes_to_long(enc[i]) == exp[i]:
            log.info(f'flag = {flag}')
            break
        if l == charset[-1]:
            log.warn(f'fail at char {i}')
            exit(1)

# MCTF{D0_n0T_TrU$T_7h3_SyMb0l5,_Th3y_Ar3_Ly1nG}
