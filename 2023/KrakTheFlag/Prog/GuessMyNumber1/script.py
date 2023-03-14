#!/usr/bin/env python3

import time
import random
import datetime

from pwn import *

host, port = "chall06.ctf.bde-kraken.com", 55781

r = remote(host, port)

print(r.recv())
print(r.recv())
print(r.recv())
print(r.recv())
print(r.recv())
print(r.recv())

seed = int(time.time()) - 5
random.seed(seed)
number = random.randint(1, 1000000000)

r.sendline(str(number).encode())

print(r.recv())

"""
HDCTF{r4nd0m_numb3rssss}
"""
