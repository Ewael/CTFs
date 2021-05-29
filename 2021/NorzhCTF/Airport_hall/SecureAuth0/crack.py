#!/usr/bin/env python3

from pwn import *

exp = b'''c-n|TD^zJFp|I'q"VCj7.mNj4'''
#print(xor('aaaa', 'Gt]|'[::-1]))
#print(xor('bbbb', 'Hu^}'[::-1]))
#print(xor('cccc', 'Iv_~'[::-1]))
#print(xor('dddd', 'Jw`\177'[::-1]))

off = [-26, -76, -4, 27, -26, 19, -4, 27, -26, 19, -4, 27, -26, -76, -4, -68, -26, 19, -4]
out = b''
for i in range(len(off)):
    n = exp[i] - off[i]
    if n > 256 or n < 0:
        n = (-n) % 256
    out += bytes([n])
print(out[::-1])
print(exp)

'''
main scanf 0x462bf6d
mod input call 0x46f9484
mod input 0x31b8c40
strcmp 0x3a2486f

strlen:
strlen 0x35bb213

call mod input 0x38f090b

format NORZH{...}

xxd -ps secureAuth0 | sed 's/90//g' | tr -d '\n' > patched.hex
xxd -ps -r patched.hex > patched.out
'''

# NORZH{n0pfuscat3d_b1nary}
