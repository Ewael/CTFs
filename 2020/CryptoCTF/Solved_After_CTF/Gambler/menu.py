#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long

def encrypt(m, p, a, b):
    assert m < p and isPrime(p)
    return (m ** 3 + a * m + b) % p

#encrypt(bytes_to_long(flag)) = 7183306132330940243175185121671517011576846926591702688573767976840040618290005682066687696788701177257132537078406704803972575136037942297496950443150688

flag = b"."*1
print(bytes_to_long(flag))
