#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import bytes_to_long

hub = {
0xadc52d: 'fun_4cd',
0x560729d: 'fun_652',
0x48c5ccc6: 'fun_438',
0x542010a0: 'fun_590',
0xbdecfe55: 'fun_7bb',
0x41f93b4b: 'fun_7d4',
0x5e64bb6c: 'fun_7ea',
0xed4e2cfb: 'fun_835',
0x180bc12d: 'fun_866',
0x5a0f38fc: 'fun_8f9',
0x27497906: 'fun_98c_exit',
0xba1116a9: 'fun_9a2',
0xfa83fa5e: 'fun_9de',
0x818cd6b5: 'fun_a1d',
0x8d67bae1: 'fun_a64',
0xd1450d67: 'fun_abf_putchar',
0x8ea45b38: 'fun_b46',
0xf00bb6c1: 'fun_b03',
0x5991ba22: 'fun_b89',
0x43ae1f53: 'fun_724',
0x8960888a: 'fun_be5',
0x1f0a8e6f: 'fun_c41',
0x466a54d9: 'fun_c8e_exit',
0xfb521a9c: 'fun_ca4',
0xc650f15d: 'fun_cf7'
}

b64 = open('b64strings/2.decoded', 'rb').read()
step = 4
chunks = [b64[i:i+step][::-1] for i in range(0, len(b64), step)]
chunks = [bytes_to_long(chunks[i]) for i in range(len(chunks))]

for i in range(0, len(chunks), 2):
    chunk = chunks[i]
    associated_chunk = chunks[i + 1]
    if chunk not in hub:
        print(f'chunk {hex(chunk)} not in chunks')
        continue
    fun = hub[chunk]
    print(f'chunk {hex(chunk)} -> {fun} | associated chunk = {hex(associated_chunk)}')

'''
[2*14] => 0xadc52d => changes
never reaches 0x795bf373
'''
