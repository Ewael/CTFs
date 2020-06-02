#!/usr/bin/env python3

import string

pt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÂÊÎÔÛŶÁÉÍÚÓÝ"
ct = "GOW4ÎÓDLT19ÉAIQY6ÛCKS08ÁBJRZ7ŶHPX5ÔÝEMU2ÂÍFNV3ÊÚ"

res = [None] * 48
per = [None] * 48
for i in range(48):
    per[i] = pt.index(ct[i])
    res[per[i]] = ct[i]
print(pt)
print(''.join(res))
print(per)

ct = "SCNTGET0SKV3CTNESYS2ISL7AF4I0SC0COM5ORS31RR3AYN1"
res = [None] * 48
per = [6, 14, 22, 30, 38, 46, 3, 11, 19, 27, 35, 43, 0, 8, 16, 24, 32, 40, 2, 10, 18, 26, 34, 42, 1, 9, 17, 25, 33, 41, 7, 15, 23, 31, 39, 47, 4, 12, 20, 28, 36, 44, 5, 13, 21, 29, 37, 45]
for i in range(48):
    res[per[i]] = ct[i]
print(''.join(res))
