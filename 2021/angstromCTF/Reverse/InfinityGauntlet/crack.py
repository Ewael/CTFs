#!/usr/bin/env python3

from pwn import *
import time
import binascii

# r = (c + 1) * b + a
def bar(a, b, c):
    return (c + 1) * b + a
def bar_a(r, b, c):
    return r - (c + 1) * b
def bar_b(r, a, c):
    return (r - a) / (c + 1)
def bar_c(r, a, b):
    return (r - a) / b - 1

# r = y + 1 ^ x ^ 0x539
def foo(x, y):
    return y + 1 ^ x ^ 0x539
def foo_x(r, y):
    for i in range(100000):
        if r == y + 1 ^ i ^ 0x539:
            return i
    return None
def foo_y(r, x):
    for i in range(100000):
        if r == i + 1 ^ x ^ 0x539:
            return i
    return None

def round():
    try:
        log.info(p.recvuntil("===\n", timeout=1).decode('utf-8'))
        return p.recvuntil('\n')[:-1]
    except:
        log.success(p.clean().decode('utf-8'))
        exit(0)

def parseBar(rnd):
    v1 = rnd.find(',')
    v2 = rnd.find(',', v1 + 1)
    p = rnd.find(')')
    a = rnd[4:v1]
    b = rnd[v1 + 2:v2]
    c = rnd[v2 + 2:p]
    r = rnd[p + 4:]
    inc = 0
    log.info(f'before: a = {a}, b = {b}, c = {c}, r = {r}')
    if r == '?':
        r = bar(int(a), int(b), int(c))
        inc = r
    if a == '?':
        a = bar_a(int(r), int(b), int(c))
        inc = a
    if b == '?':
        b = bar_b(int(r), int(a), int(c))
        inc = b
    if c == '?':
        c = bar_c(int(r), int(a), int(b))
        inc = c
    log.info(f'bar: a = {a}, b = {b}, c = {c}, r = {r} || inc = {inc}')
    assert bar(int(a), int(b), int(c)) == int(r)
    return inc

def parseFoo(rnd):
    v1 = rnd.find(',')
    p = rnd.find(')')
    x = rnd[4:v1]
    y = rnd[v1 + 2:p]
    r = rnd[p + 4:]
    inc = 0
    log.info(f'before: x = {x}, y = {y}, r = {r}')
    if r == '?':
        r = foo(int(x), int(y))
        inc = r
    if x == '?':
        x = foo(int(r), int(y))
        inc = x
    if y == '?':
        y = foo_y(int(r), int(x))
        inc = y
    log.info(f'after: x = {x}, y = {y}, r = {r} || inc = {inc}')
    exp = foo(int(x), int(y))
    assert exp == int(r), f'x = {x}, y = {y}, r = {r}, exp = {exp}'
    return inc

def resolve():
    for i in range(50):
        rnd = round().decode('utf-8')
        log.info(f'rnd {i} = {rnd}')
        res = 0
        if rnd[:3] == 'bar':
            res = int(parseBar(rnd))
        if rnd[:3] == 'foo':
            res = int(parseFoo(rnd))
        log.success(f'? = {str(res)}')
        time.sleep(0.1)
        p.sendline(str(res))
        i += 1

    flag = ['00'] * l
    maxrnd = 220
    for i in range(50, maxrnd):
        rnd = round().decode('utf-8')
        log.info(f'rnd {i} = {rnd}')
        res = 0
        if rnd[:3] == 'bar':
            res = int(parseBar(rnd))
        if rnd[:3] == 'foo':
            res = int(parseFoo(rnd))
        res = str(res)
        log.success(f'? = {res}')
        time.sleep(0.1)
        p.sendline(res)
        res = hex(int(res))[2:]
        char = res[-2:]
        assert len(char) == 2, f'res = {res}, char = {char}, pos = {hex(pos)}'
        pos = int(res[:-2], 16) - i - 1
        log.success(f'res = {res}, char = {char}, pos = {hex(pos)} -> flag[{pos}] = {char}')
        log.success(f'flag = {"".join(flag)}')
        flag[pos] = char
        if not '00' in flag:
            return ''.join(flag)

    return ''.join(flag)

def decode(flag):
    flag = binascii.unhexlify(flag)
    c = 0
    res = ''
    i = 0
    while c != ord('}') * 0x11 and i < len(flag):
        xor = hex(flag[i] ^ c)[2:].zfill(2)
        res += xor[-2:]
        c += 0x11
        i += 1
    return res

commands = '''
b *0x555555555294
b *0x555555555504
'''
# p = gdb.debug('./infinity_gauntlet', commands)
# p, l = process('./infinity_gauntlet'), 39 # flag len
p, l = remote('shell.actf.co', 21700), 26 # flag len

flag = resolve()
flag = decode(flag)
flag = binascii.unhexlify(flag)
log.success(f'flag = {flag}')

"""
4c42674802610d44d7ffc68f8b9a93
the answer is created from the flag
x = (y % len + round & 0xff) << 8 | buf[y % len];
"""

# actf{snapped_away_the_end}
