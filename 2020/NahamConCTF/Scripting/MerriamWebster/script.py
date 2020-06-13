#!/usr/bin/env python3

from pwn import *
import enchant

host = "jh2i.com"
port = 50012

r = remote(host, port)
d = enchant.Dict("en_US")

while(True):
    try:
        rec = r.recvuntil("\n", timeout=1).decode()
    except EOFError:
        print(r.clean())
        break
    print(rec)
    if "NOT" in rec:
        real = False
    else:
        real = True
    if "CHRONOLOGICAL" in rec:
        chrono = True
    else:
        chrono = False
    if "many" in rec:
        many = True
    else:
        many = False
    words = r.recvuntil(">").decode()[:-2]
    print(words)
    words = words.split(" ")
    resp = []
    count = 0
    for word in words:
        if not d.check(word) and not real:
            resp.append(word)
            count += 1
        if d.check(word) and real:
            resp.append(word)
            count += 1
    if not chrono:
        resp = sorted(resp)
    resp = ' '.join(resp)
    if not many:
        print(resp)
        r.send(resp)
    else:
        print(count)
        r.send(str(count))
    print(r.recvuntil("\n"))
