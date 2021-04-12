#!/usr/bin/env python3

ipt = open("challenge.hex", "r").read()
out = open("decoded", "w")

chat = ipt.replace('.', '').split('\n')

hexa = ''
for line in chat:
    hexa += line[9:]
out.write(hexa)

# from hex + remove trash in flag
# MCTF{Th3_Al4Rm_Ha$_G0n3_0ff}
