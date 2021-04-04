#!/usr/bin/env python3

import base64

exp = 'x2JlwWFmz2w0vWpgY210M2Y1vaVpYqN1Y2xaZ3B5wC0cyTAayqVuNTFrNXVuZaNmwmpaLXJgvTN3NWt1M2JbwTNmuWx='
key = 'buggy-m255'
lkey = len(key)

def do(ipt, index, buff):
    l = len(ipt)
    b = buff
    if index < l:
        buff[index * 2] = ipt[index]
        buff[index * 2 + 1] = key[index % lkey]
        b = do(ipt, index + 1, buff)
    return b

def dorec(ipt, buff):
    l = len(ipt)
    for i in range(l):
        buff[i * 2] = ipt[i]
        buff[i * 2 + 1] = key[i % lkey]
    return buff

def undo(buff):
    flag = b''
    for i in range(len(buff)):
        if not i % 2:
            flag += bytes([buff[i]])
    return flag

ipt = 'shaktictf{just_t3st1ng}'
buf = [' '] * 0x50

r = ''.join(dorec(ipt, buf))
enc = base64.b64encode(r.encode('utf-8'))
print(f'r = {r}')
print(f'enc = {enc}')

print(f'exp = {exp}')
dec = base64.b64decode(exp.encode('utf-8'))
print(f'dec = {dec}')

flag = b'sbhuagkgtyi-cmt3f5{5db3ucg3gpyt-1m03n5_51b5u_g3gvy3-rmy3w5h53bru3g}g'
flag = undo(flag)
print(f'flag = {flag}')
