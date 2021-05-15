#!/usr/bin/env python3

import binascii
import string
from pwn import *
from itertools import permutations

def initArr():
    exp = [0xb4d8846071ac9ee5, 0x1e1ff00814e134fe, 0x6b198e7941b7002e, 0xbc6fa839efe36443, 0xc3c71ad9a664b6c3, 0x5692a2f09c98d986, 0xf084a1a59cd01e68, 0xbc52e78a7e4df2df, 0xda219d93290b91a8, 0x5703d0286fa5d32f, 0x6274b1b118da82b2, 0xa746ebfb0954ebbc, 0x5f6df7bd4f1967a2, 0x16d5b5bdee98cf8e, 0x52e8b6df7e62e39a, 0x99f9455fb0c8d933, 0x5ffd82d53af933d, 0xff9084a16ff0141c, 0xe17c5f0781d52f9b, 0x1a0f4431548e51d1, 0xf2e8573d8f0f01dd, 0x250039177f4def91, 0x8851491ecbc7af7c, 0xad427c6695b91d24, 0x5e0071d97d98d094, 0x264dda52b0c37b03, 0xa5811271d6d7c428, 0xe0133fc719f34136, 0xe508ace2412b2633, 0x74321a3e9face34c, 0xff5b8a59e8ebf70b, 0x76275a516f88c986, 0x1604d76f74599cc4, 0xf744bcd8f2016f58, 0xa0b6a7a0239e4ea7, 0xf1efc57f15cb9ab4, 0xb0d1ad4fb4ed946a, 0x81ca31324d48e689, 0xe6a9979c51869f49, 0xa666637ee4bc2457, 0x6475b6ab4884b93c, 0x5c033b1207da898f, 0xb66dc7e0dec3443e, 0xe4899c99cfa0235c, 0x3b7fd8d4d0dcaf6b, 0xb1a4690db34a7a7c, 0x8041d2607129adab, 0xa6a1294a99894f1a, 0xdde37a1c4524b831, 0x3bc8d81de355b65c, 0x6c61ab15a63ad91e, 0x8fa4e37f4a3c7a39, 0x268b598404e773af, 0x74f4f040ae13f867, 0x4df78e91fd682404, 0xabe1fc425a9a671a, 0x1bb06615c8a31dd5, 0x9f56e9aef2fa5d55, 0x239dcf030b3ce09b, 0x24556a34b61ca998]
    arr1 = [0xdeadbeeffeedbeef, 0x1badb002facecafe, 0xfeedface08920892, 0xcafefeed12401240]
    arr2 = [0x9e3779b917181920, 0x9e3779b912881288]
    arr = [0 for i in range(len(exp))]
    sbuf = '00000000020000000b000000060000000400000005000000030000000700000008000000090000000a000000010000000c00000016000000180000000f0000001100000010000000120000001300000017000000140000000d000000150000000e0000001d0000001c0000001b0000001a00000019000000'
    buf = []
    for j in range(0, len(sbuf), 8):
        n = sbuf[j:j+8]
        m = n[6:8] + n[4:6] + n[2:4] + n[0:2]
        l = int(m, 16)
        buf.append(l)
    return arr1, arr2, arr, buf, exp

def fun2(arr2, arr, j, arr1):
    arr1_ = arr1.copy()
    arr2_ = arr2.copy()
    for i in range(0x10):
        #print(f'--- loop {i} :')
        # a = arr1_[0] + arr1_[1] + (arr1_[2] + arr1_[3] ^ arr1_[0] << (arr1_[2] & 0x3f))
        w1 = (arr1_[2] & 0x3f) & 0xffffffffffffffff
        w2 = (arr1_[0] << w1) & 0xffffffffffffffff
        w3 = (arr1_[2] + arr1_[3]) & 0xffffffffffffffff
        w4 = (w3 ^ w2) & 0xffffffffffffffff
        a = arr1_[0] + arr1_[1] + w4
        a &= 0xffffffffffffffff
        arr1_[i & 3] = a
        lVar1 = arr1_[i & 3];

        # b = arr2_[0] + ((lVar1 + arr2_[1]) * 0x200 ^ lVar1 - arr2_[1] ^ lVar1 + arr2_[1] >> 0xe)
        x1 = (lVar1 + arr2_[1]) & 0xffffffffffffffff
        x2 = (x1 * 0x200) & 0xffffffffffffffff
        x3 = (lVar1 - arr2_[1]) & 0xffffffffffffffff
        x4 = (lVar1 + arr2_[1]) & 0xffffffffffffffff
        x5 = (x4 >> 0xe) & 0xffffffffffffffff
        x6 = (x5 ^ x3) & 0xffffffffffffffff
        x7 = (x6 ^ x2) & 0xffffffffffffffff
        b = arr2_[0] + x7
        b &= 0xffffffffffffffff
        #print(f'x1 = {hex(x1)}\nx2 = {hex(x2)}\nx3 = {hex(x3)}\nx4 = {hex(x4)}\nx5 = {hex(x5)}\nx6 = {hex(x6)}\nx7 = {hex(x7)}\narr2_[0] = {hex(arr2_[0])}')
        arr2_[0] = b

        # c = arr2_[1] + ((lVar1 + arr2_[0]) * 0x200 ^ lVar1 - arr2_[0] ^ lVar1 + arr2_[0] >> 0xe);
        y1 = (lVar1 + arr2_[0]) & 0xffffffffffffffff
        y2 = (y1 * 0x200) & 0xffffffffffffffff
        y3 = (lVar1 - arr2_[0]) & 0xffffffffffffffff
        y4 = (lVar1 + arr2_[0]) & 0xffffffffffffffff
        y5 = (y4 >> 0xe) & 0xffffffffffffffff
        y6 = (y5 ^ y3) & 0xffffffffffffffff
        y7 = (y6 ^ y2) & 0xffffffffffffffff
        c = arr2_[1] + y7
        c &= 0xffffffffffffffff
        arr2_[1] = c
        #print(f'a = {hex(a)}\nb = {hex(b)}\nc = {hex(c)}')

    arr[j] = arr2_[0]
    arr[j + 1] = arr2_[1]
    #log.info(f'arr[{j}:{j+2}] = {[hex(a) for a in arr[j:j+2]]}' + f'\nexp[{j}:{j+2}] = {[hex(a) for a in exp[j:j+2]]}')

def fun(flag, l, arr1, arr2, arr):
    j = 0
    for i in range(l):
        a = flag[i + 2] << 0x10
        a &= 0xffffff
        b = flag[i + 1] << 0x8
        b &= 0xffff
        c = flag[i]
        c &= 0xffffffffffffffff
        arr2[0] = a | b | c | 0xaabbccdd11000000
        arr2[0] &= 0xffffffffffffffff
        #print(f'--- i = {i} :\nflag[0:3] = {[hex(i) for i in flag[0:3]]}\na = {hex(a)}\nb = {hex(b)}\nc = {hex(c)}\nbig or = {hex(arr2[0])}')
        fun2(arr2, arr, j, arr1)
        j += 2

def newflag(flag, buf):
    flag = list(flag)
    j = 0
    for i in range(0x1d):
        j = i
        while -1 < buf[j]:
            flag[i], flag[buf[j]] = flag[buf[j]], flag[i]
            c = buf[j]
            buf[j] -= 0x1e
            j = c
    return flag

def getflag(flag):
    flag = list(flag)
    j = 0
    for i in range(0x1d):
        j = i
        while -1 < buf[j]:
            flag[i], flag[buf[j]] = flag[buf[j]], flag[i]
            c = buf[j]
            buf[j] -= 0x1e
            j = c
    return ''.join(flag)

triples = [0, 11, 1,
        6, 4, 5,
        3, 7, 8,
        9, 10, 2,
        12, 22, 24,
        15, 17, 16,
        18, 19, 21,
        23, 13, 20,
        14, 29, 28,
        27, 26, 25]

l = 30
#flag = string.ascii_letters[:l]
#flag = 'ptm{' + '.' * (l-5) + '}'
#flag = '.' * l
flag = 'put...........................'

charset = string.ascii_letters + string.digits + '_-{}@#$&*'
#charset = charset[:2]
arr1, arr2, arr, buf, exp = initArr()
spld = [ord(c) for c in newflag(flag, buf)]
a = ''.join(chr(a) for a in spld)
b = flag
#for i in range(len(a)):
#    print(f'{i} = {a[i]}:{a.index(a[i])} <-> {b[i]}:{a.index(b[i])}')
log.info(f'ori = {b}\nmod = {a}')
log.info(f'{[hex(ord(i)) for i in a]}')
#print([b.index(c) for c in a])
#fun(spld, l, arr1, arr2, arr)
#exit(0)

j = 2
for i in range(flag.index('.'), len(flag)):
    pld = list(flag)
    good = False
    for a in charset:
        pld[i] = a

        arr1, arr2, arr, buf, exp = initArr()
        spld = ''.join(pld)
        oldspld = spld

        spld += spld[0] + spld[1]
        spld = spld.encode('utf-8')

        fun(spld, l, arr1, arr2, arr)
        #log.info(f'flag = {bytearray(spld)}' + f'\ngot : arr[{i}] = {hex(arr[i])}, arr[{i+1}] = {hex(arr[i+1])}' + f'\nexp : exp[{i}] = {hex(exp[i])}, exp[{i+1}] = {hex(exp[i+1])}')

        if arr[:j+2] == exp[:j+2]:
            flag = oldspld
            log.success(f'flag = {flag} - spld = {"".join(chr(a) for a in spld)}')
            j += 2
            good = True
            break

        if good:
            break
        if a == charset[-1]:
            log.warn(f'error at index {i}')
            exit(1)

log.success(f'masterclass over -> flag = {getflag(flag)}')

'''
exp = 0xb4d8846071ac9ee5
got = 0xee315bad8321fc79

pmu{5m0l_chtnk5_5m0lc_35ur17y} (bug in script)
-> ptm{5m0l_chunk5_5m0l_53cur17y}
'''
