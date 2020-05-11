#!/usr/bin/env python3

chaine = "56 64 6b 6b 1f 63 6e 6d 64 20 1f 53 67 64 1f 65 6b 60 66 1f 68 72 39 1f 45 42 52 42 7a 37 32 65 33 30 33 32 30 62 30 30 30 2f 35 31 63 2f 2f 32 63 63 2f 31 30 32 62 65 37 31 33 63 35 35 65 36 36 2f 60 2f 61 64 30 32 2f 34 64 31 37 30 32 65 30 34 63 63 36 35 34 2f 32 60 38 30 63 7c 00"

arr = chaine.split(" ")

for k in range(len(arr)):
    arr[k] = chr(int(arr[k], 16) + 0x01)

print(''.join(arr))
