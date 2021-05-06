#!/usr/bin/env python3

from gdbpython import *

def pba(offset):
    exc(f'pie breakpoint *{hex(offset)}')

def pbc(offset):
    pba(offset)
    cont()

exc('file ./vmv')
exc('pie breakpoint *0x1d44') # main

pwd = 'ABCDEF0123456789'

exc(f'pie run {pwd}')

# calling convention = rdi, rsi, rdx, rcx
pbc(0x1f87) # after unpacking
pbc(0x2028) # memcpy(decoded1_copy + 0x2f4c, argv[1], len)
pbc(0x12bc) # build_arr

pba(0x2061) # call return_decoded2 -> chunk for hub
pba(0x206e) # call choose_function
pba(0x207d) # call rdx

#pba(0x1abf) # putchar
#pba(0x1afb) # call putchar

print(context())

'''
check = 0x0000555555582550 size = 0x90 (144)
buff1 = 0x00005555555825f0 size = 0x400 * 4 (4096)
buff2 = 0x00007fffefce2010 size = 0x8000000 (134217728)
decoded2 = 0x0000555555572540 size = 0x3f10
decoded1_copy = 0x000055555556f5d0 size = 0x2f4c
input = decoded1_copy+0x2f4c = 0x55555557251c

# check[Y] means check+(8*Y) cuz it's array of x64 addresses
check[0x0] = buff1
check[0x5] = counter ou associated_chunk
check[0xb] = decoded2
check[0xc] = buff2
check[0xd] = associated_chunk
check[0xe] = decoded1_copy (decoded1 | input)
check[0xf] = 0x0
check[0x10] = 0x1
check[0x11] = 0x0

get_associated => return associated chunk

0x87ab3b0200000397 = 1.decoded
0x00000400ba1116a9 = 2.decoded

ça prend 4 bytes par 4 bytes en skippant
un block de 4 à chaque fois

dans le choose_function:
rax = block du decoded (4 bytes) little endian
rax = rax ** 2
rax = rax & 0x1ffff
rax = rax << 3
rax += rdx -> base_addr? (= 0x00007ffff7ce3010)
rax = [rax]
'''
