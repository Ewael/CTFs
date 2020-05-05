#!/usr/bin/env python3

import base64

get = open("GET.enc", "r").read()
get = base64.b64decode(get)

wantedget = open("wantedget", 'r').read()

dico = open("crunch_01")

key = ""
for word in dico:
    word = word[:-1]
    key = ""
    arr = list(wantedget)
    for i in range(16):
        arr[i] = str(word[i])
    n = min(len(get), len(arr))
    for i in range(n):
        key += chr(ord(arr[i%n]) ^ get[i%n])
    print('[+] prefix = {}'.format(word))
    if key[:16] == key[16:32]:
        print("Found key : {}".format(key))
        break

print("[+] Bruteforce over")
