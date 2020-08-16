#!/usr/bin/env python3

from Crypto.Util.number import *
from functools import reduce
import operator

def comb(n, k):
    if k > n :
        return 0
    k = min(k, n - k)
    u = reduce(operator.mul, range(n, n - k, -1), 1)
    #print("u = {}".format(u))
    d = reduce(operator.mul, range(1, k + 1), 1)
    #print("d = {}".format(d))
    print("comb({}, {}) = {}".format(n, k, u // d))
    return u // d

def encrypt(msg, n, k):
    msg = bytes_to_long(msg.encode('utf-8'))
    print("msg = {}".format(msg))
    if msg >= comb(n, k):
        return -1
    m = ['1'] + ['0' for i in range(n - 1)]
    for i in range(1, n + 1):
        if msg >= comb(n - i, k):
            m[i-1]= '1'
            msg -= comb(n - i, k)
            print("msg = {}".format(msg))
            print(m)
            k -= 1
    m = int(''.join(m), 2)
    i, z = 0, [0 for i in range(n - 1)]
    c = 0
    while (m > 0):
        if m % 4 == 1:
            c += 3 ** i
            m -= 1
        elif m % 4 == 3:
            c += 2 * 3 ** i
            m += 1
        m //= 2
        i += 1
    return c

flag = "CCTF{I_aM_ThE_fLaG}"
n = 500
k = 240

enc = encrypt(flag, n, k)
print('enc =', enc)
