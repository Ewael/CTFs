#!/usr/bin/env python3

a = "\x63\x6f\x6e\x6d\x56\x6d\x40\x53"
a += "\x4c\x4f\x7a\x41\x5c\x44\x5b\x54"
b = ""

for l in a:
    l = ord(l)
    l ^= 0x12
    l -= 0x41
    l ^= 0x78
    b += chr(l)

print(b)
