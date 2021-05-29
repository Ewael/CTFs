#!/usr/bin/env python3

from gdbpython import *

def pba(offset):
    exc(f'pie breakpoint *{hex(offset)}')

def pbc(offset):
    pba(offset)
    cont()

exc('file ./secureAuthV2')
exc('pie breakpoint *0x1bf6') # main

l = 0x40
charset = getCharset()
flag = 'NORZH{'
pwd = 'A' * (l - len(flag) - 1)
pwd += '}'
pwd = charset[:l]
os.system(f'echo {pwd} > pwd.txt')

exc(f'pie run < pwd.txt')
setFork('child')
exc('handle all pass nostop')

# https://stackoverflow.com/questions/58851/can-i-set-a-breakpoint-on-memory-access-in-gdb
exc('rwatch *0x555555556048') # 'Failed !'
#exc('watch *0x55555555810c') # nb_ptrace
#exc('rwatch *0x7fffffffddd0') # input

pba(0x1bfe) # fork

# child bp
pba(0x18a3) # child
#pba(0x19b5) # execve
#pba(0x1956) # sigaction
pba(0x187a) # sig handler
pba(0x199c) # raise

# parent bp
pba(0x13dc) # fgets
pba(0x14c9) # send input
#pba(0x1703) # xor
#pba(0x1727) # ptrace after xor
pba(0x1804) # final wait? -> https://code.woboq.org/gcc/include/bits/waitstatus.h.html
pba(0x1835) # success ptrace

cont()
print(context())

'''
# calling convention rdi, rsi, rdx, rcx

i = 0x0000555555554000 + 0x410c = 0x55555555810c
'''
