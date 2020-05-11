#!/usr/bin/env python3

import base64

get = open("GET.enc", "r").read()
get = base64.b64decode(get).decode()

dico = open("crunch_01")
keys = open("keys", "w")

key = ""
for word in dico:
    word = word[:-1]
    key = ""
    for i in range(16):
        key += chr(ord(word[i]) ^ ord(get[i]))
    keys.write(key + '\n')
    print("[+] Trying: {}".format(word))

print("[+] Bruteforce over")
