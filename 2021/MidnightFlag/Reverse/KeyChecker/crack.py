#!/usr/bin/env python3

from gdbpython import *

pwd = list('A' * 30)
charset = getCharset() + '{}'
print(f'charset = {charset}')
init('./key_checker')
bp = 0x401277 # bt
ba(bp)

for i in range(1):
    for l in charset:
        pwd[i] = l
        spwd = ''.join(pwd)

        print(f'[-] spwd = {spwd}')
        run(stdin=spwd)
        cont()
        cont()
        cont()

        c = context()
        if not 'not running' in context():
            cont()
            c = context()
            if not 'not running' in context():
                cont()
                c = context()
                if not 'not running' in context():
                    print(f'[v] success, spwd = {spwd}')
                    break

        if l == charset[-1]:
            print("[x] fail, pwd = {}, i = {}".format(spwd, i))
            exit(1)

spwd = "".join(pwd)
print("[x] bruteforce over, pwd = {}".format(spwd))

# could not solve this one, still keeping the script
# and the chall to come back on it, was nice tho
