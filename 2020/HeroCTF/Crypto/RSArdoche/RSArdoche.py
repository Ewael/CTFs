#!/usr/bin/env python3

from Crypto.Util.number import getPrime
from Crypto.Util.number import bytes_to_long
import os

p = getPrime(256)
q = getPrime(256)
e = 1
n = p * q

flag = b"F4ke_fk4G"
pt = bytes_to_long(flag)
ct = pow(pt, e, n)

print(f"n={n}", f"e={e}", f"ct={ct}", sep='\n')
