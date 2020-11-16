#!/usr/bin/env python3

def obfuscate(arg):
    ret = ''
    for i, c in enumerate(arg):
        ret += chr(ord(c) ^ 1 + i % 3)
    else:
        return ret

pwd = "M4j2l3GpQhUC"
desobf = obfuscate(pwd)

print(desobf)
print(obfuscate(desobf))
