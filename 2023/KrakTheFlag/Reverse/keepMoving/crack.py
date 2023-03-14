#!/usr/bin/env python3

from gdbpython import *

init('challenge')

dico = string.ascii_letters + string.digits + '}'
flag = 'H'

ba(0x804a2f8) # where comparison is done

while flag[-1] != '}':

    run(args = [flag + 'X'])
    cont()

    for i in range(len(flag) + 1):
        print(f"{flag=}")
        cont()
        cont()

    edx = int(get('edx').split(' ')[-1], 16)
    letter = chr(edx)

    flag += letter
    print(f"{flag=}")

print(context())
print(f"{flag=}")


"""
0x804af7d -> we see correct

0x804b751 -> end of main = SIGILL

flag check letter at 0x804976a -> mov edx, DWORD PTR [edx*4+0x81f5390]
where edx is index ?

0x804a2f8 -> flag letter in edx so we can bruteforce

HDCTF{M0V3_IS_TUR1NG_C0MPLETE}
"""
