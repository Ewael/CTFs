#!/usr/bin/env python3

# from https://blog.cryptohack.org/cryptoctf2020#classic

import string
from collections import Counter
from cipher_solver.simple import SimpleSolver

with open('enc.txt') as f:
    ctext = f.read().strip().replace(' ', '')

def chunks(l, n):
    n = max(1, n)
    return [l[i:i+n] for i in range(0, len(l), n)]

# 1. We suspect that groupings of 5 are there to confuse us.
# Let's break chars into groups of different sizes and look at
# the size of the set
for i in range(1,10):
    unique = len(set(chunks(ctext, i)))
    print(f"{unique} unique groups when split into groups of length {i}")

# 2. Breaking into groups of 3 (trigrams) gives much less unique chars
chunked = chunks(ctext, 3)
freq = Counter(chunked).most_common()
print(freq)

# 3. Build a substitution table for each trigram to a different letter
# only important thing is that the most frequent trigram corresponds to a space
subs = {}
alphabet = " " + string.ascii_lowercase + string.ascii_uppercase
cur = 0
for trigram in freq:
    subs[trigram[0]] = alphabet[cur]
    cur += 1
print(subs)

# 4. Make the substitutions
substituted = "".join([subs[c] for c in chunked])
print(substituted)

# 5. Use any algorithm for solving substitution ciphers (quipqiup also works)
s = SimpleSolver(substituted)
s.solve()

# 6. It's readable and the flag is visible after a couple of manual
# substitutions
ptext = s.plaintext()
ptext = ptext.replace('z', 'T')
ptext = ptext.replace('q', '_')
print(ptext)
