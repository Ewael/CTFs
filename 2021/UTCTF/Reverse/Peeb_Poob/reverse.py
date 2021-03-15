#!/usr/bin/env python3

import string

def encode(flag):
    for i in range(len(flag)):
        j = 0
        # j = ((i ^ -j) + j & 3 ^ -j) + j
        j = i % 4
        if j == 0:
            flag[i] ^= 0x21
        elif j == 1:
            flag[i] ^= 0x7
        elif j == 2:
            flag[i] ^= 0x23
        elif j == 3:
            flag[i] ^= 5
        if i + 1 < len(flag):
            flag[i + 1] ^= flag[i]

flag = '54 27 62 0b 4b 2b 73 14 06 32 61 3b 78 4f 5c 29 57 20 30 06 45 1d 4e 7b 6a 0f 51 5e 00 00 00 00'.split(' ')
flag = [int(x, 16) for x in flag]
charset = string.punctuation + string.ascii_letters + string.digits
ipt = list('utflag{' + '?' * (len(flag) - 7))

for i in range(7, len(flag)):
    for c in charset:
        ipt[i] = c
        arr = [ord(a) for a in ipt]
        encode(arr)
        if arr[i] == flag[i]:
            break
print(''.join(ipt))
