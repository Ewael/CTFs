#!/usr/bin/env python3

from pwn import *

binary = './highest-power'
context.binary = binary
pwnlib.qemu.archname(arch='arm')

main = 0x10a40
bind = 0x109a0
retgetcode = 0x109e0
entry = 0x3feb2000
accept = 0x10ed4
after_acc = 0x10f08
call_sock = 0x10f44
send = 0x10bbc
nstr = 0x10be4
call_unpack = 0x109dc
call_r3 = 0x109e8

f_accept = 0x3feb2014
f_unpack = 0x3feb218c
new_unpacked = 0x3fead000

commands = f'''
set follow-fork-mode child
#b *{hex(main)}
#b *{hex(bind)}
#b *{hex(retgetcode)}
b *{hex(entry)}
#b *{hex(accept)}
#b *{hex(call_sock)}
#b *{hex(send)}
#b *{hex(nstr)}
#b *{hex(call_unpack)}
#b *{hex(call_r3)}
# from unpacked fun
b *{hex(f_accept+4)}
b *{hex(f_unpack+4)}
c
'''
r = gdb.debug(binary, commands)

r.interactive()

'''
open listening port on localhost 8000
reads http input char per char

HTTP/1.0 403 Forbidden

dump binary memory unpaked2.raw 0x3fead000 0x3feb17bc
'''
