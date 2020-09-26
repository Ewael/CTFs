#!/usr/bin/env python3

from Crypto.Util.number import getStrongPrime, getRandomRange

N = 1024
flag = "A"*70

def generateKey():
    p = getStrongPrime(N)
    q = (p - 1) // 2
    x = getRandomRange(2, q)
    g = 2
    h = pow(g, x, p)
    pk = (p, q, g, h)
    sk = x
    return (pk, sk)

def encrypt(m, pk):
    (p, q, g, h) = pk
    r = getRandomRange(2, q)
    c1 = pow(g, r, p)
    c2 = m * pow(h, r, p) % p
    return (c1, c2)

pk, sk = generateKey()

for m in flag:
    c = encrypt(ord(m), pk)
    print(f"{c}")

print(f"p = {pk[0]}")
print(f"q = {pk[1]}")
print(f"g = {pk[2]}")
print(f"h = {pk[3]}")
