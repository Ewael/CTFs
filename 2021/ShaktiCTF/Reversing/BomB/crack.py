#!/usr/bin/env python3

from gdbpython import *

exc('file BomB')
bs('main')

l = 9
code = '123456789'
code = '124432226'

run(stdin=code)
tbc(0x555555401010) # after len check
tbc(0x5555554010bd) # cmp check
tbc(0x55555540132b) # flag check

print(context())

"""
len is 9 - only numbers

"""
