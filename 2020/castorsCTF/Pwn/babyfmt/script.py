#!/usr/bin/env python3

import binascii

chaine = "0x4373726f74736163-0x5f6b34336c7b4654-0x3468745f6b34336c-0x74346d7230665f74-0x5f366e317274735f-0x7d6b34336c"
arr = chaine.split('-')

for i in range(len(arr)):
    if len(arr[i]) == 18:
        tmp = ""
        tmp += arr[i][16]+arr[i][17]
        tmp += arr[i][14]+arr[i][15]
        tmp += arr[i][12]+arr[i][13]
        tmp += arr[i][10]+arr[i][11]
        tmp += arr[i][8]+arr[i][9]
        tmp += arr[i][6]+arr[i][7]
        tmp += arr[i][4]+arr[i][5]
        tmp += arr[i][2]+arr[i][3]
        arr[i] = binascii.unhexlify(tmp).decode()
    if len(arr[i]) == 12:
        tmp = ""
        tmp += arr[i][8]+arr[i][9]
        tmp += arr[i][6]+arr[i][7]
        tmp += arr[i][4]+arr[i][5]
        tmp += arr[i][2]+arr[i][3]
        arr[i] = binascii.unhexlify(tmp).decode()

print(''.join(arr))
