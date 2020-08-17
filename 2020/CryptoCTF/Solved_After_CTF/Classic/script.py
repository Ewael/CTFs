#!/usr/bin/env python3

import string
from collections import Counter
from cipher_solver.simple import SimpleSolver

with open("enc.txt") as f:
    text = f.read().strip().replace(' ', '')
#print(text)

def chunks(text, size):
    l = []
    for i in range(0, len(text), size):
        l.append(text[i:i+size])
    return l

for i in range(1, 10):
    # use set to remove duplicates
    nb = len(set(chunks(text, i)))
    print("[+] groups of length {}: {} unique groups".format(i, nb))

# keep len 3
chunked = chunks(text, 3)
# counter to count how many times each chunk appears
# most_commons() to have doublets (chunk, quantity)
freq = Counter(chunked).most_common()
print("----\nfrequences:\n")
print(freq)

# build substitution table
substitution_table = {}
alphabet = ' ' + string.ascii_letters
cur = 0
for chunk in freq:
    # assign a letter to each different chunk (trigram)
    substitution_table[chunk[0]] = alphabet[cur]
    cur += 1
print("----\nsubstitution table:\n")
print(substitution_table)

# make subs
sub_text = ''.join([substitution_table[c] for c in chunked])
print("-----\nnew text:\n\n" + sub_text)

# solve algo for subs cipher
s = SimpleSolver(sub_text)
s.solve()

# launch it several times until the flag appears
print("-----\nreadable:\n")
r = s.plaintext()
r = r.replace('q', '_')
r = r.replace('z', 'T')
r = r.replace('d', 'p')
r = r.replace('k', '')
r = r.replace('E', 'C')
r = r.replace('G', 'F')
r = r.replace('B', '{')
r = r.replace('D', '}')
r = r.replace('j', 'v')
print(r)
