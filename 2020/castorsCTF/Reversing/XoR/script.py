#!/usr/bin/env python3

chaine = "gh}w_{aPDSmk$ch&r+Ah-&F|"+chr(0x14)+'z'+chr(0x11)+'P'+ \
          chr(0x15)+chr(0x10)+chr(0x1d)+'R'+chr(0x1e)
res = ""

for i in range(len(chaine)):
    res += chr((ord(chaine[i]) + 2) ^ i + 10)

print(res)
