#!/usr/bin/env python3

import random
import time
from mt19937predictor import MT19937Predictor
from pwn import *

host, port = "chall06.ctf.bde-kraken.com", 55782

r = remote(host, port)

def rec():
    time.sleep(0.05)
    received = r.recv().decode()
    return received

def send(msg):
    time.sleep(0.05)
    r.sendline(msg.encode())

def solve():
    inf = 0
    sup = 4294967296
    n = (sup - inf) // 2

    print(f'Sending {n}')

    for i in range(100):
        received = rec()
        if 'sup' in received:
            inf = n
            n += (sup - inf) // 2 + 1
        elif 'inf' in received:
            sup = n
            n -= (sup - inf) // 2 + 1
        elif 'Bien' in received:
            print(received)
            return n
        if n <= inf:
            n = inf + 1
        if n >= sup:
            n = sup - 1
        print(f"inf = {inf}, n = {n}, sup = {sup}")
        send(str(n))

def collect_numbers():
    predictor = MT19937Predictor()
    for i in range(624):
        n = solve()
        print(f"{i} - Found {n}")
        send('Y')
        predictor.setrandbits(n, 32)
    return predictor.getrandbits(32)

print(rec())
n = collect_numbers()
print(f"Next number is {n}")
r.interactive()

"""
HDCTF{Y0U_can_pr3diCT_ALL_MYNUMBERS}
"""
