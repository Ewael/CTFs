#!/usr/bin/env python3

import os
from Crypto.Util.number import long_to_bytes
from Crypto.Util.strxor import strxor
import binascii

def encrypt():
    FLAG = open("flag.txt", "rb").read()
    key = os.urandom(4) * 20
    c = strxor(FLAG, key[:len(FLAG)])
    print(c.hex())

cipher = open('output.txt', 'r').read()[:-1]
cipher = binascii.unhexlify(cipher)
key = strxor(b'FCSC', cipher[:4])
print(f'key = {key}')
key *= 20
dec = strxor(cipher, key[:len(cipher)])
print(dec)
