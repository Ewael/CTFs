#!/usr/bin/env python3

# d2j-dex2jar Jakarta.apk
# jd-gui

import string

enc = [11, 152, 177, 51, 145, 152, 153, 185, 26, 156,
      177, 19, 177, 50, 156, 26, 156, 35, 176, 159,
      185, 185, 185, 26, 19, 152, 177, 50, 144, 144,
      176, 177, 26, 184, 190, 50, 11, 26, 51, 26,
      26, 156, 19, 58, 148, 19, 176, 51, 26, 177,
      58, 58, 144, 139, 152, 50, 185, 153, 177, 153,
      144, 26, 176, 144, 50, 156, 145, 153, 156, 156]

flag = 'FCSC{bebfb1b880d802cb96be0bb256f4239c27971310cdfd1842083fbe16b3a2dcf7}'
l = len(flag)
arr = [0] * l
charset = string.ascii_letters + string.digits

for i in range(l):
    for lt in charset:
        j = (i * 37 + 1) % l
        c = ord(lt)
        for c1 in range(7, -1, -1):
            arr[i] = arr[i] ^ (c >> c1 & True) << (c1 * 5 + 3) % 8
        if arr[i] == enc[i]:
            flag = list(flag)
            flag[j] = lt
            flag = ''.join(flag)
            break
        else:
            arr[i] = 0

print(enc)
print(arr)
print(flag)

valid = [(1 if enc[i] == arr[i] else 0) for i in range(l)]
print(f'{valid.count(1)} / 70')

# FCSC{6df723aa33b1aa8d604069a693e5990d411a7f7a7169b70e694b0bdf4d26aa9e}
