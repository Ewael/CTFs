#!/usr/bin/env python3

from base128 import base128

def createEnc(msg):
    obj = []
    s = 8
    for i in range(0, len(msg), s):
        block = msg[i:i+s]
        obj.append(block)
    if len(obj[-1]) != 7:
        obj.append([len(obj[-1]) - 1])
    return obj

def b128decode(msg):
    obj = createEnc(msg)
    b = base128()
    return b''.join(b.decode(obj))

def test():
    c1 = b'1~p-otq{dsYBKTD;L?=,?6W\'?66h_kcvY(:Z4ipq,%CHT<HHAI'
    print(b128decode(c1))
