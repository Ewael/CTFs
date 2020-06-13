#!/usr/bin/env python3

from pwn import *

host = "jh2i.com"
port = 50031

r = remote(host, port)

print(r.recvuntil('>').decode())
r.sendline('6')
print(r.recvuntil(':').decode())
r.sendline('1')

for i in range(20000):
    print(r.recvuntil('>').decode())
    r.sendline('5')

r.interactive()
