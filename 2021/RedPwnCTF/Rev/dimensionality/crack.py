#!/usr/bin/env python3

from gdbpython import *
import string
import os

base = 0x0000555555554000

init('./dimensionality', entry=base+0x1080) # main

def bf_check():
    charset = string.ascii_letters + string.digits + "{}_-.?!"
    l = 0x1c
    ori = ''
    pld = ori + 'X' * (l - len(ori))
    r12 = 0

    for i in range(l):
        for c in charset:
            pld = list(pld)
            pld[i] = c
            pld = ''.join(pld)

            print(f'i = {i} -> running with pld = {pld}')
            run(stdin=pld)
            pbc(0x14bc) # mustbe3 check with 0
            if i != 1:
                for j in range(i):
                    print(f'[+] skipping char {j}')
                    cont()

            print(context())
            r12 = int(exc('info reg r12').split(' ')[12][2:])
            print(f'[+] r12 = {r12}')
            if r12 != 0:
                print(f'[+] pld = {pld}')
                os.system(f'echo {pld} > tempo.txt')
                break
            if c == charset[-1]:
                print(f'[x] fail, i = {i}, pld = {pld}')
                exit(1)

    print(f'[x] bf over, pld = {pld}')
    os.system(f'echo {pld} > tempo.txt')
    return pld

#pld = bf_check()
pld = 'adalaaafaaabaaafaaabaaafaaab'

run(stdin=pld)
pbc(0x10ba) # call check_input
pbc(0x14bc) # mustbe3 check with 0

print(context())

'''
adalaaafaaabaaafaaabaaafaaab
'''

# solved by tanguy -> flag{star_/_so_bright_/_car_/_site_-ppsu}
