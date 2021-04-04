#!/usr/bn/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import md5
from os import urandom

flag = b'sharkyctf{hey_this_is_the_flag}'

keys = [md5(urandom(3)).digest() for _ in range(2)]

def bytexor(da,ta):
    return bytes(i ^ j for i, j in zip(da, ta))

def get_ciphers(iv1, iv2):
    return [
        AES.new(keys[0], mode=AES.MODE_CBC, iv=iv1),
        AES.new(keys[1], mode=AES.MODE_CFB, iv=iv2, segment_size=8*16),
    ]

def encrypt(m, iv1, iv2):
    m = pad(m, 32)
    ciphers = get_ciphers(iv1, iv2)
    c = m
    for cipher in ciphers:
        l = [c[i:i+32] for i in range(0, len(c), 32)]
        c = b''.join(i[16:] + bytexor(i[:16], cipher.encrypt(i[16:])) for i in l)
    return c

plaintext = f'finally now i am able to send my secret with double security and double trust, {flag}'.encode()
iv1, iv2 = urandom(16), urandom(16)

ciphertext = encrypt(plaintext, iv1, iv2)

iv1, iv2, ciphertext = iv1.hex().encode(), iv2.hex().encode(), ciphertext.hex().encode()
print(f'iv1 = {iv1}\niv2 = {iv2}\nciphertext = {ciphertext}')
