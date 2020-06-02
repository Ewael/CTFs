#!/usr/bin/env python3

import os

os.system("echo '' > wrapped_rockyou")
dico = open("/usr/share/wordlists/rockyou.txt", encoding="utf-8", errors='ignore')
new_dico = open("wrapped_rockyou", "w")

for word in dico:
    word = word[:-2]
    print("[+] Copying {}".format(word))
    word = "castorsCTF{" + word + "}" + "\n"
    new_dico.write(word)
