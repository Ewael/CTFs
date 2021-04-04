#!/usr/bin/env python3

from pwn import *
import os
import time

os.system('crunch 8 8 012345 -t 231@4@0@ > cracklist')
codes = open('cracklist', 'r').readlines()[::-1]
l = len(codes)
i = 0
for code in codes:
    code = code[:-1]
    p = i / l * 100
    log.info(f'trying {code} ------------------------------------- {str(p)[:4]}%')
    os.system('rm -f check')
    r = process('./nosleep')
    r.recvuntil('Enter the code:')
    r.sendline(code)
    time.sleep(0.1)
    res = r.clean()
    if not b'Not there yet' in res:
        log.success(f'found code: {code}')
        break
    r.close()
    i += 1

# code was 23144105
# shaktictf{p4r3nt_ch1ld_Ch17d_wut?_0n3_m0r3!}
