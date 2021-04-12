#!/usr/bin/env python3

import os
import zlib
from Crypto.Util.number import bytes_to_long, long_to_bytes

def keystream(key):
    index = 0
    while 1:
        index += 1
        if index >= len(key):
            key += zlib.crc32(key).to_bytes(4,'big')
        yield key[index]

def encrypt(pt, key):
    ciphertext = []
    k = keystream(key)
    ck = []
    for i in range(len(pt)):
        ck.append(next(k))
    for i in range(len(pt)):
        ciphertext.append(pt[i] ^ ck[i])
    ciphertext = bytes(ciphertext)
    return ciphertext, bytes(ck)

def decrypt(enc, key):
    return encrypt(enc, key)

def rshift(s, n):
    shifted = (s * 3)[len(s) - n:2 * len(s) - n]
    return shifted

def getCiphers(s, key):
    ciphers = []
    for i in range(len(s) - len(b'actf{') + 1):
        sh = rshift(s, i)
        ct, _ = encrypt(sh, key)
        cipher = ct[i:i+len(b'actf{')]
        ciphers.append(cipher)
        # print(f'sh = {sh}, cipher = {cipher}')
    return ciphers

def bf(enc, offset=0):
    n = 0
    for i in range(offset, 0xffff + 1):
        key = long_to_bytes(i)
        ciphers = getCiphers(b'actf{' + b'A' * (len(enc) - 5), key)
        # print(f'trying key {key}')
        for k in range(len(ciphers)):
            if ciphers[k] in enc:
                print(f'success, key = {key}, shift = {k}')
                return key
        n += 1
    print(f'tried {n} keys')
    return None

enc = open('given_enc.txt', 'rb').read()[:-1]
# pt = b'hello here i am again, get ur flag: actf{a}'
# enc, k = encrypt(pt, b'\x13\x37')
# exp = enc[-7:-2]
# print(f'enc = {enc}\nexp = {exp}\nk = {k}\n---')

offset = 0
while True:
    key = bf(enc, offset)
    flag, k = decrypt(enc, key)
    print(f'flag = {flag}\nk = {k}')
    cont = input('continue ? yes/no : ')
    if cont == 'yes':
        offset = bytes_to_long(key) + 1
    else:
        break

# actf{low_entropy_keystream}
