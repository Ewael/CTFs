#!/usr/bin/env python3

# pt = https://www.hackworks.com/en/housinghack/teams/innovation.etc

import string

def encrypt(flag, shift, key):
    stdalph = string.ascii_lowercase
    rkey = ""
    for i in key:
        if i not in rkey:
            rkey += i
    for i in stdalph:
        if i not in rkey:
            rkey += i
    rkey = rkey[-shift:] + rkey[:-shift]
    enc = ""
    for a in flag:
        if a in stdalph:
            enc += rkey[stdalph.index(a)]
        else:
            enc += a
    print(f'--\nkey = {key}\nrkey = {rkey}\nstda = {stdalph}\nenc = {enc}')
    return enc

def decrypt(enc, rkey):
    stdalph = string.ascii_lowercase
    dec = ""
    for a in enc:
        if a in rkey:
            dec += stdalph[rkey.index(a)]
        else:
            dec += a
    return dec

def getKey(ct, pt):
    stdalph = string.ascii_lowercase
    rkey = list(stdalph)
    for i in range(len(pt)):
        if pt[i] in stdalph:
            rkey[stdalph.index(pt[i])] = ct[i]
    rkey = ''.join(rkey)
    print(f'rkey = {rkey}')
    return rkey

pt = open('plain.txt', 'r').read()[:-1]
ct = open('out.txt', 'r').read()[:-1]
print(f'pt len = {len(pt)}')
print(f'ct len = {len(ct)}')
rkey = getKey(ct, pt)
flag = decrypt('qufx{awowvuqwdqcrtcwibawdgsdfbfgfbtm}', rkey)
print(f'flag = {flag}')

# actf{keyedcaesarmorelikesubstitution}
