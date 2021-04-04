#!/usr/bin/env python3

import string
import gdb

pl = 30
charset = string.ascii_letters + string.digits + "{}_-.?!"
ori = ""
still = pl - len(ori)
pwd = list(ori + "A" * still)
bp = 0x56555990

gdb.execute("file brute")
gdb.execute("b *{}".format(bp))

for i in range(len(ori), pl):
    for l in charset:
        pwd[i] = l
        spwd = "".join(pwd)

        print("-------------")
        print("[-] running ./brute with pwd {}".format(spwd))
        gdb.execute("run < <(python -c 'print \"{}\"')".format(spwd))

        for j in range(i):
            gdb.execute("c")

        # check ZF flag after CMP
        flags = gdb.execute("info reg eflags", to_string=True)
        print("[+] flags = {}".format(flags))
        if 'ZF' in flags:
            print("[+] worked, pwd = {}".format(spwd))
            break

        if l == charset[-1]:
            print("[x] fail, pwd = {}, i = {}".format(spwd, i))
            exit(1)

spwd = "".join(pwd)
print("[x] bruteforce over, pwd = {}".format(spwd))

# picoCTF{I_5D3_A11DA7_dd4ad7d3}
