#!/usr/bin/env pyhton3

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.number import long_to_bytes
import binascii

def encrypt():
    while False:
        pin = int(input(">>> PIN code (4 digits): "))
        if 0 < pin < 9999:
            break

    pin = 1111
    flag = b"FCSC{6a8024a83d9ec2d1a9c36c51d0408f15836a043ae0431626987ce2b8960a5937}"
    k = scrypt(long_to_bytes(pin), b"FCSC", 32, N = 2 ** 10, r = 8, p = 1)
    aes = AES.new(k, AES.MODE_GCM)
    c, tag = aes.encrypt_and_digest(flag)
    print(len(aes.nonce), len(c), len(tag))
    enc = aes.nonce + c + tag
    print(enc.hex())

def decrypt():
    cipher = open('output.txt', 'r').read()[:-1]
    nonce = cipher[:32]
    c = cipher[32:-32]
    tag = cipher[-32:]
    print(f'nonce = {nonce}\nc = {c}\ntag = {tag}')
    nonce = binascii.unhexlify(nonce)
    c = binascii.unhexlify(c)
    tag = binascii.unhexlify(tag)
    dec = b''
    pin = 0
    while dec[:5] != b'FCSC{':
        k = scrypt(long_to_bytes(pin), b"FCSC", 32, N = 2 ** 10, r = 8, p = 1)
        aes = AES.new(k, AES.MODE_GCM, nonce=nonce)
        dec = aes.decrypt(c)
        pin += 1
    print(dec)

decrypt()
