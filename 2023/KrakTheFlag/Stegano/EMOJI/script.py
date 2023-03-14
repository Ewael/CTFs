#!/usr/bin/env python3

a = [1517, 1519, 1497, 1502, 1496, 1528, 1508]

for o in range(1350, 1490):
    p = ""
    for l in a:
        p += chr(l - o)
    print(p)
