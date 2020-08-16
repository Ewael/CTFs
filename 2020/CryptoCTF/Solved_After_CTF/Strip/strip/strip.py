#!/usr/bin/python

from Crypto.Util.number import *
from secret import flag, r

def a(n): # WARNING: very slow implementation...
	if n <= 2:
		return n
	elif n == 3:
		return 24
	else:
		return (6*a(n-1)**2*a(n-3) - 8*a(n-1)*a(n-2)**2) // (a(n-2)*a(n-3))

def strip(n):
	return int(bin(n)[2:].rstrip('0'), 2)

def encrypt(msg, r):
	n = strip(a(r))
	return pow(bytes_to_long(msg.encode('utf-8')), 0x10001 + 0x02, n)

print(encrypt(flag, r))