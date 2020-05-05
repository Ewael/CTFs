#!/usr/bin/env python3

from pwn import *

host = "challenges2.france-cybersecurity-challenge.fr"
port = 3001

r = remote(host, port)

while True:
    try:
        resp = r.recvuntil("name: ", timeout = 1)
    except EOFError:
        print(resp)
        print(r.clean())
        break
    user = r.recvuntil(">>>").decode()[:-4]
    print("user = {}".format(user))
    serial = ""
    for i in user:
        serial += chr(ord(i) ^ int('1f', 16))
    serial = ''.join(reversed(serial))
    print("serial = {}".format(serial))
    r.sendline(serial)
