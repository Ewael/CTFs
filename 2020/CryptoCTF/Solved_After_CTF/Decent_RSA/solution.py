#!/usr/bin/env python3

# from https://blog.cryptohack.org/cryptoctf2020#decent-rsa

from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long

flag = bytes_to_long(open("flag.enc","rb").read())
key = RSA.import_key(open("mykey.pem").read())
n = Integer(key.n)

poly = sum(e * x^i for i,e in enumerate(Integer(key.n).digits(11)))
(p, _), (q, _) = poly.factor_list()
p, q = p(x=11), q(x=11)
assert p*q == n

d = inverse_mod(key.e, (p-1)*(q-1))
print(long_to_bytes(pow(flag, d, n)))
