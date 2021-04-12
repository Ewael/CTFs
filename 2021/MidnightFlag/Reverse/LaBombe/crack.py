#!/usr/bin/env python3

from z3 import *

phase1 = "s3as0n4l"
print(phase1)

l = 5

out = [BitVec("{}".format(i), 8) for i in range(l)]
s = Solver()
s.add(out[2] == (out[0] + 1) * 2)
s.add(out[2] == out[1] + 0x10)
s.add(out[1] == out[0] + 0x22)
s.add(out[3] == out[2] + 0x7)
s.add(out[4] == out[3] + 0xb)

while s.check() == sat:
    model = s.model()
    res = ""
    for i in range(l):
        res += chr(model[out[i]].as_long())
    print(res)
    break

# phase 3 cmp at *phase_3 + 185

# s3as0n4l
# 0Rbit
# AcC3pt4nC3
# MCTF{s3as0n4l_0Rbit_AcC3pt4nC3}
