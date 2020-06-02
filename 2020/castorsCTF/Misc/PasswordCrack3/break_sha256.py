#!/usr/bin/env python3

import hashlib

dico = open("wrapped_rockyou", "r", encoding="utf-8", errors="ignore")

for word in dico:
    word = word[:-1].encode()
    sha = hashlib.sha256(word).hexdigest()
    print("[x] Trying {} = {}".format(word, sha))
    if sha == "7adebe1e15c37e23ab25c40a317b76547a75ad84bf57b378520fd59b66dd9e12":
        print("Found: {}".format(word))
        break
