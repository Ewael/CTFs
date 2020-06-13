#!/usr/bin/env python3

from pwn import *

host = "jh2i.com"
port = 50034

r = remote(host, port)

def caesar(text, shift):
    res = ""
    for i in range(len(text)):
        char = text[i]
        if 97 <= ord(char) <= 122:
            res += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            res += char
    return res

flag = ['*']*31 # got len with tests
log.info("Building file")

while '*' in flag:
    rec = r.recv().decode()
    shift = 0
    for i in range(26):
        if caesar(rec[:4], i) == "send":
            shift = i
            break
    data = caesar(rec, shift)
    if len(data) > 58:
        index = int(data[-22:-20])
        flag[index] = data[-3:-2]
        print(''.join(flag))
    r.send(data)
