#!/usr/bin/env python3

from pwn import *

host = "chals20.cybercastors.com"
port = 14429

r = remote(host, port)
r.recv()
r.sendline("")

one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9

while True:
    resp = r.recv().decode()
    if not "What" in resp:
        print("-----Over-----")
        print(resp)
        break
    print(resp[:-1])
    cal = ""
    on = False
    for i in range(1, len(resp)):
        if resp[i-1]+resp[i] == "is":
            on = True
        if on:
            cal += resp[i]
        if resp[i] == '?':
            on = False
    cal = cal[2:-2]
    if "multiplied-by" in cal:
        cal = cal.split(' ')
        cal[1] = '*'
        cal = ''.join(cal)
    if "plus" in cal:
        cal = cal.split(' ')
        cal[1] = '+'
        cal = ''.join(cal)
    if "minus" in cal:
        cal = cal.split(' ')
        cal[1] = '-'
        cal = ''.join(cal)
    if "divided-by" in cal:
        cal = cal.split(' ')
        cal[1] = '//'
        cal = ''.join(cal)
    res = str(eval(cal))
    print(res)
    r.sendline(res)
    print(r.recv().decode())
