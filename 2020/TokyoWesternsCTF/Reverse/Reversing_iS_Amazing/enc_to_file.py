#!/usr/bin/env python3

import binascii

enc_flag = open("enc_flag", "r")
enc_input = open("enc_input", "r")

file_flag = open("file_flag", "wb")
file_input = open("file_input", "wb")

for line in enc_flag.readlines():
    hexas = line[16:-1].split('\t')
    for hexa in hexas:
        little = ''.join(list(hexa[2:])[::-1])
        to_bytes = binascii.unhexlify(little)
        file_flag.write(to_bytes)

for line in enc_input.readlines():
    hexas = line[16:-1].split('\t')
    for hexa in hexas:
        little = ''.join(list(hexa[2:])[::-1])
        to_bytes = binascii.unhexlify(little)
        file_input.write(to_bytes)
