#!/usr/bin/env python3

from Crypto.PublicKey import RSA
import os

files = os.listdir("keys")
pubkeys = []

for filename in files:
    filename = "keys/" + filename
    f = open(filename, "r")
    pubkey = RSA.importKey(f.read())
    pubkeys.append((filename, pubkey))

# e = 65537

def euclid_algo(x, y):
    if x < y:
        return euclid_algo(y, x)
    while y != 0:
        x, y = y, x % y
    return x

def find_weakness(pubkeys):
    nkeys = len(pubkeys)
    for i in range(nkeys):
        filenamex, keyx = pubkeys[i]
        nx = keyx.n
        ex = keyx.e

        for j in range(i + 1, nkeys):
            filenamey, keyy = pubkeys[j]
            ny = keyy.n
            ey = keyy.e

            print("computing between {} and {}".format(filenamex, filenamey))
            gcd = euclid_algo(nx, ny)
            if gcd != 1:
                print("key x = {}, key y = {}".format(filenamex, filenamey))
                print("found gcd = {}".format(gcd))
                return gcd

# key x = keys/420.pub, key y = keys/69.pub
gcd = 27325601508462946138018355480287302486465818420686814939811741814653681614104922945847457457476869105465869127086285056252887188911754204840595471114345495182167328748179822520824774875915217881107582127461486777445134672557821060455843482959541755561577188598824783370678109611190662490571382001051987694867735055214567775946340098549903777755759144867834634508409693066989382704359444448302079788057664501874415261114787408289904612614142915557847407388443181022658746437630511747455309708802234110812707130462162542880319922105522170315935564711196373058236989529036348793081426112001994820532148012768514320529441

key = open("keys/420.pub", "r")
key = RSA.importKey(key.read())
n = key.n
e = key.e

p = gcd
q = n // gcd

print("n = {}\ne = {}\np = {}\nq = {}".format(n, e, p, q))
