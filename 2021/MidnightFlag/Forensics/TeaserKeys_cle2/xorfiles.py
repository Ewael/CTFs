#!/usr/bin/env python3

from pwn import xor

f1 = open('./Documents/Projects/download.dat', 'rb').read()
f2 = open('./WINDOWS_BACKUP/MES-VMS.PWL', 'rb').read()

r = xor(f1, f2)

out = open('output.txt', 'wb')
out.write(r)
out.close()
