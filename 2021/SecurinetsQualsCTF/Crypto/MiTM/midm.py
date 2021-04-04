#!/usr/bin/env python3

# https://www.researchgate.net/figure/The-man-in-the-middle-attack-against-a-Diffie-Hellman-like-key-exchange-The_fig1_224342226
# https://www.youtube.com/watch?v=PPt7yvBtGRI

# n-th party DH attack page 44
# https://calhoun.nps.edu/bitstream/handle/10945/4509/09Sep_Geary.pdf

from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long, isPrime
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import hashlib, random, os, time, gmpy2

r = remote(f'crypto1.q21.ctfsecurinets.com', 1337)

g = 2
p = 169622824183424820825728324890204115101468714952998142585574034795946851153950475569207215681807529286667189170420372861538287664283023804761495759297626394111153684529019990561684722443184304549649494421130078368098045597169822975289983997491594344239614944483399038130689027660812095676588300142576532463429

def findR(p):
    limit = 100_000_000_000
    log.info(f'computing R with limit {limit}')
    for R in range(2, limit, 2):
        q = (p - 1) / R
        if not q.is_integer():
            continue
        q = int(q)
        if isPrime(q):
            return q, R
    log.warn(f'could not find R with limit {limit}')
    exit(1)

q, R = findR(p)
assert p == q * R + 1
log.success(f'p = Rq + 1:')
log.success(f'q = {q}')
log.success(f'R = {R}')
d = q

time.sleep(0.2)
r.recvuntil(f'Alice sends to Bob: ')
ga = int(r.recvuntil('\n'))
log.info(f'from alice: g^a = {ga}')
gda = pow(ga, d, p)
log.info(f'to bob: g^da = {gda}')
r.sendline(str(gda))

r.recvuntil(f'Bob sends to Carol: ')
gdab = int(r.recvuntil('\n'))
log.info(f'from bob to carol: g^dab = {gdab}')
r.sendline(str(gdab))

r.recvuntil(f'Bob sends to Carol: ')
gb = int(r.recvuntil('\n'))
log.info(f'from bob: g^b = {gb}')
gdb = pow(gb, d, p)
log.info(f'to bob: g^db = {gdb}')
r.sendline(str(gdb))

r.recvuntil(f'Carol sends to Alice: ')
gdbc = int(r.recvuntil('\n'))
log.info(f'from carol to alice: g^dbc = {gdbc}')
r.sendline(str(gdbc))

r.recvuntil(f'Carol sends to Alice: ')
gc = int(r.recvuntil('\n'))
log.info(f'from carol: g^c = {gc}')
gdc = pow(gc, d, p)
log.info(f'to bob: g^dc = {gdc}')
r.sendline(str(gdc))

r.recvuntil(f'Alice sends to Bob: ')
gdca = int(r.recvuntil('\n'))
log.info(f'from alice to bob: g^dca = {gdca}')
r.sendline(str(gdca))

r.recvuntil('\n')
msg = r.recvuntil('\n')[:-1]
log.success(f'msg = {msg}')

iv = binascii.unhexlify(msg[:32])
cipher = binascii.unhexlify(msg[32:])
debug = 1
for i in range(1, R+1):
    secret = pow(g, q*i, p)
    key = hashlib.sha1(long_to_bytes(secret)).digest()[:16]
    aes = AES.new(key, AES.MODE_CBC, iv)
    flag = aes.decrypt(cipher)
    if debug:
        log.info(f'computing secret for i = {i}')
        log.info(f'flag = {flag}')
    if b'Securinets' in flag:
        log.success(f'decrypted flag = {flag}')
        break
