#!/usr/bin/env python3

from pwn import *
import string, os

binary = './automatic'

context.binary = binary
pwnlib.qemu.archname(arch='aarch64')

base = 0x0000005500000000
main = base + 0x9dc
ipt = base + 0x1268
check = base + 0x1304
call_fun = base + 0x12d0
fun = base + 0xc70
loop = base + 0x142c
a = base + 0x1498
b = base + 0x14e8
c = base + 0x1528
orr = base + 0xc7c
buf = base + 0xbac
call_fun2 = base + 0xcf4
bmod = base + 0x1268
mod = base + 0x126c
cpy = base + 0xb50
i_2 = base + 0xc84
i_1 = base + 0xc9c
i_0 = base + 0xcb8

commands = f'''
set follow-fork-mode child
#b *{hex(ipt)}
#b *{hex(call_fun)}
#b *{hex(fun)}
#b *{hex(buf)}
#b *{hex(orr)}
#b *{hex(loop)}
#b *{hex(a)}
#b *{hex(b)}
#b *{hex(c)}
#b *{hex(call_fun2)}
#b *{hex(bmod)}
#b *{hex(mod)}
b *{hex(i_2)}
b *{hex(i_1)}
b *{hex(i_0)}
b *{hex(check)}
c
'''

#flag = 'ptm{' + string.ascii_uppercase[:23] + '}'
flag = string.ascii_letters[:30]
#flag = 'ptm{5a0a...u..................}'

r = gdb.debug(binary, commands)
print(r.recv(timeout=0.01))
r.sendline(flag)
r.interactive()

log.info(f'flag = {flag}')

'''
ABCDEFGH -> 0xee315bad8321fc79
ABCDEFGHI -> 0xee315bad8321fc79
BBCDEFGH -> 0xee315bad8321fc79

it checks 2 bytes per 2 bytes
'''
