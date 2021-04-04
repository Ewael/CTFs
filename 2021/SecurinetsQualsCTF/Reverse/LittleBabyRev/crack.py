#!/usr/bin/env python3

import string
import gdb

def ex(cmd):
    gdb.execute(cmd)

ex('file warmup')
ex('start')

ex('b *0x00005555555666e5') # decode1
ex('b *0x000055555556673c') # decode2
ex('b *0x00005555555667bf') # streq with input len

ex('r')

# Securinets{Nimper0r_The_aNimAtor}
