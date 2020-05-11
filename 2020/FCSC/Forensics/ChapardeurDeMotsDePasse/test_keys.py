#!/usr/bin/env python3

import base64

get = open("GET.enc", "r").read()
get = base64.b64decode(get).decode()

dico = open("keys")
plaintexts = open("plaintexts", "w")

plain = ""
for word in dico:
    word = word[:-1]
    plain = ""
    for i in range(len(get)):
        plain += chr(ord(word[i%16]) ^ ord(get[i]))
    plaintexts.write('key = {} =>\n{}\n---\n'.format(word, plain))
    print("[+] Trying: {}".format(word))

print("[+] Bruteforce over")
