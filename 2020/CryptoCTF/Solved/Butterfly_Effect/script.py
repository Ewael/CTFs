#!/usr/bin/env python3

from pwn import *
import string
import hashlib

host = "05.cr.yp.toc.tf"
port = 3371

def puzzle(cry, end, l):
    fun = print
    if cry == 'sha256':
        fun = hashlib.sha256
    elif cry == 'sha1':
        fun = hashlib.sha1
    elif cry == 'md5':
        fun = hashlib.md5
    elif cry == 'sha512':
        fun = hashlib.sha512
    elif cry == 'sha384':
        fun = hashlib.sha384
    elif cry == 'sha224':
        fun = hashlib.sha224
    else:
        print("Impossible case")
        return "dslMeansSorry"

    if l == 10:
        for i in string.printable:
            for j in string.printable:
                for k in string.printable:
                    for l in string.printable:
                        for a in string.printable:
                            for b in string.printable:
                                for c in string.printable:
                                    for d in string.printable:
                                        for e in string.printable:
                                            for h in string.printable:
                                                ch = i+j+k+l+a+b+c+d+e+h
                                                if fun(ch.encode('utf-8')).hexdigest()[-6:] == end:
                                                    return ch

    elif l == 15:
        for i in string.printable:
            for j in string.printable:
                for k in string.printable:
                    for l in string.printable:
                        for a in string.printable:
                            for b in string.printable:
                                for c in string.printable:
                                    for d in string.printable:
                                        for e in string.printable:
                                            for h in string.printable:
                                                for o in string.printable:
                                                    for m in string.printable:
                                                        for p in string.printable:
                                                            for z in string.printable:
                                                                for r in string.printable:
                                                                    ch = i+j+k+l+a+b+c+d+e+h+o+m+p+z+r
                                                                    if fun(ch.encode('utf-8')).hexdigest()[-6:] == end:
                                                                        return ch

l = 0
while l != 10 and l != 15:
    r = remote(host, port)
    line = r.recvuntil("\n").decode()
    print(line)
    offset = line.find('(')
    cry = line[46:offset]
    end = line[offset+11:offset+17]
    l = int(line[-3:-1])
    print("sha = {}\nend = {}\nlen = {}\n".format(cry, end, l))
    if l != 10 and l != 15:
        r.close()

h = puzzle(cry, end, l)
print("hash = {}\n".format(h))
r.sendline(h)
print(r.recvuntil('\n'))
print(r.recvuntil('\n'))
print(r.recvuntil('\n'))
print(r.recvuntil('\n'))
print(r.recvuntil('\n'))
print(r.recvuntil('\n'))
r.interactive()
