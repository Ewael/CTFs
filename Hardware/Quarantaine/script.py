#!/usr/bin/env python3

a = 454088092903

print("{0:b}".format(a))
print(''.join(reversed("0110100110111001110000100110110011100111")))

# 1110011100
# 1101100100
# 0011100111
# 0110010110

b1 = ''.join(reversed("1110000100"))
b2 = ''.join(reversed("1111001000"))
b3 = ''.join(reversed("1000101001"))
b4 = ''.join(reversed("0011101111"))

b = b4 + b3 + b2 + b1

print(b)
print(int(b, 2))
