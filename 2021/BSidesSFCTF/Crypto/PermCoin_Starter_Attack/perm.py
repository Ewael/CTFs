#!/usr/bin/python3

import binascii

N = 64
C = 16
B = 296

final = [
    19,
    51,
    8,
    10,
    33,
    40,
    59,
    61,
    43,
    15,
    20,
    3,
    41,
    56,
    62,
    46,
    60,
    34,
    16,
    54,
    1,
    7,
    31,
    29,
    0,
    35,
    24,
    17,
    28,
    42,
    49,
    52,
    37,
    48,
    18,
    55,
    39,
    14,
    13,
    11,
    57,
    6,
    30,
    9,
    58,
    45,
    2,
    12,
    27,
    53,
    22,
    5,
    50,
    38,
    23,
    4,
    63,
    36,
    26,
    44,
    25,
    47,
    21,
    32,
]

gens = [
    [
        63,
        62,
        40,
        42,
        34,
        32,
        61,
        22,
        27,
        28,
        23,
        10,
        29,
        45,
        5,
        19,
        16,
        24,
        46,
        33,
        17,
        14,
        8,
        47,
        18,
        44,
        25,
        26,
        53,
        38,
        21,
        52,
        15,
        1,
        31,
        0,
        59,
        36,
        56,
        6,
        37,
        41,
        58,
        51,
        54,
        11,
        2,
        50,
        55,
        4,
        12,
        39,
        35,
        13,
        43,
        3,
        30,
        7,
        9,
        48,
        57,
        60,
        20,
        49,
    ],  # 0
    [
        0,
        39,
        59,
        31,
        9,
        41,
        52,
        1,
        25,
        55,
        15,
        37,
        28,
        48,
        43,
        58,
        40,
        38,
        24,
        18,
        10,
        60,
        44,
        63,
        20,
        57,
        26,
        27,
        45,
        4,
        54,
        46,
        51,
        42,
        47,
        29,
        6,
        11,
        16,
        35,
        32,
        49,
        5,
        53,
        30,
        8,
        56,
        19,
        50,
        2,
        23,
        34,
        14,
        3,
        12,
        22,
        13,
        17,
        21,
        33,
        62,
        61,
        36,
        7,
    ],  # 1
    [
        10,
        12,
        52,
        42,
        7,
        36,
        13,
        57,
        61,
        44,
        39,
        22,
        32,
        17,
        8,
        59,
        27,
        29,
        2,
        38,
        46,
        21,
        0,
        4,
        5,
        6,
        62,
        58,
        9,
        48,
        45,
        16,
        1,
        35,
        3,
        31,
        23,
        54,
        56,
        41,
        49,
        24,
        33,
        40,
        50,
        63,
        43,
        25,
        37,
        11,
        53,
        55,
        15,
        26,
        60,
        20,
        18,
        34,
        47,
        30,
        14,
        51,
        28,
        19,
    ],  # 2
    [
        6,
        58,
        45,
        55,
        14,
        37,
        32,
        8,
        4,
        53,
        13,
        16,
        47,
        0,
        23,
        19,
        49,
        10,
        30,
        52,
        3,
        21,
        27,
        60,
        48,
        12,
        9,
        11,
        50,
        39,
        56,
        40,
        25,
        46,
        51,
        43,
        54,
        24,
        15,
        17,
        35,
        29,
        20,
        33,
        26,
        18,
        42,
        1,
        41,
        31,
        62,
        57,
        63,
        28,
        5,
        34,
        59,
        61,
        22,
        38,
        36,
        7,
        44,
        2,
    ],  # 3
    [
        34,
        60,
        50,
        25,
        9,
        40,
        21,
        26,
        29,
        59,
        1,
        44,
        42,
        15,
        23,
        48,
        57,
        27,
        55,
        6,
        11,
        33,
        35,
        38,
        51,
        16,
        53,
        14,
        52,
        47,
        49,
        5,
        54,
        4,
        12,
        18,
        61,
        24,
        3,
        43,
        0,
        36,
        45,
        17,
        62,
        63,
        28,
        58,
        37,
        13,
        8,
        31,
        56,
        19,
        10,
        39,
        30,
        41,
        20,
        22,
        32,
        2,
        7,
        46,
    ],  # 4
    [
        61,
        32,
        35,
        18,
        48,
        47,
        11,
        19,
        3,
        44,
        39,
        21,
        52,
        43,
        50,
        1,
        51,
        4,
        34,
        16,
        7,
        54,
        36,
        2,
        22,
        9,
        28,
        20,
        62,
        14,
        31,
        55,
        38,
        13,
        42,
        58,
        41,
        33,
        15,
        0,
        27,
        23,
        53,
        57,
        6,
        30,
        60,
        29,
        46,
        26,
        45,
        56,
        8,
        59,
        25,
        37,
        63,
        10,
        49,
        17,
        5,
        40,
        12,
        24,
    ],  # 5
    [
        61,
        57,
        0,
        32,
        37,
        30,
        7,
        28,
        14,
        17,
        21,
        27,
        18,
        58,
        40,
        33,
        54,
        13,
        2,
        42,
        35,
        44,
        53,
        29,
        55,
        8,
        20,
        59,
        48,
        52,
        51,
        16,
        46,
        11,
        39,
        24,
        36,
        4,
        41,
        31,
        60,
        43,
        62,
        10,
        6,
        34,
        56,
        47,
        38,
        45,
        23,
        63,
        26,
        49,
        1,
        3,
        12,
        19,
        5,
        25,
        15,
        22,
        9,
        50,
    ],  # 6
    [
        18,
        41,
        21,
        26,
        10,
        13,
        32,
        51,
        33,
        16,
        54,
        28,
        25,
        45,
        11,
        39,
        56,
        37,
        42,
        2,
        57,
        31,
        4,
        9,
        24,
        43,
        27,
        59,
        29,
        6,
        17,
        20,
        44,
        23,
        22,
        34,
        53,
        35,
        52,
        19,
        0,
        63,
        30,
        61,
        7,
        38,
        49,
        48,
        60,
        1,
        46,
        5,
        55,
        50,
        8,
        3,
        40,
        58,
        36,
        15,
        62,
        47,
        14,
        12,
    ],  # 7
    [
        43,
        28,
        21,
        62,
        39,
        35,
        33,
        30,
        63,
        57,
        26,
        8,
        19,
        32,
        23,
        6,
        16,
        38,
        5,
        60,
        53,
        56,
        37,
        3,
        48,
        11,
        18,
        34,
        22,
        25,
        0,
        46,
        47,
        52,
        51,
        59,
        42,
        9,
        24,
        31,
        50,
        61,
        2,
        20,
        15,
        29,
        17,
        1,
        49,
        40,
        55,
        13,
        4,
        12,
        10,
        41,
        14,
        58,
        54,
        7,
        36,
        27,
        44,
        45,
    ],  # 8
    [
        21,
        9,
        57,
        35,
        19,
        41,
        3,
        8,
        30,
        47,
        42,
        23,
        52,
        18,
        15,
        59,
        11,
        37,
        54,
        25,
        53,
        51,
        56,
        44,
        16,
        46,
        26,
        12,
        43,
        2,
        28,
        14,
        38,
        29,
        10,
        61,
        1,
        45,
        7,
        39,
        13,
        6,
        27,
        5,
        60,
        22,
        17,
        4,
        49,
        55,
        36,
        0,
        62,
        63,
        31,
        32,
        24,
        48,
        40,
        34,
        33,
        20,
        58,
        50,
    ],  # 9
    [
        43,
        45,
        51,
        26,
        10,
        9,
        18,
        55,
        3,
        33,
        38,
        59,
        32,
        35,
        0,
        41,
        15,
        25,
        60,
        44,
        57,
        61,
        52,
        4,
        24,
        47,
        54,
        58,
        34,
        36,
        30,
        12,
        42,
        53,
        46,
        8,
        20,
        14,
        6,
        39,
        2,
        7,
        27,
        21,
        29,
        50,
        48,
        31,
        40,
        11,
        49,
        17,
        1,
        28,
        22,
        23,
        19,
        5,
        56,
        62,
        13,
        16,
        63,
        37,
    ],  # A
    [
        12,
        9,
        28,
        13,
        29,
        63,
        10,
        39,
        48,
        15,
        32,
        0,
        19,
        1,
        34,
        25,
        46,
        50,
        45,
        2,
        22,
        33,
        26,
        7,
        58,
        20,
        27,
        11,
        18,
        21,
        59,
        62,
        14,
        52,
        40,
        8,
        23,
        57,
        38,
        41,
        35,
        5,
        4,
        49,
        31,
        60,
        37,
        16,
        61,
        51,
        6,
        56,
        36,
        43,
        54,
        55,
        24,
        17,
        3,
        42,
        53,
        44,
        30,
        47,
    ],  # B
    [
        29,
        62,
        32,
        17,
        52,
        13,
        34,
        46,
        48,
        51,
        54,
        20,
        3,
        63,
        41,
        56,
        19,
        44,
        16,
        58,
        6,
        37,
        59,
        0,
        28,
        33,
        53,
        47,
        21,
        12,
        9,
        25,
        40,
        26,
        4,
        1,
        61,
        42,
        60,
        18,
        10,
        31,
        2,
        7,
        49,
        23,
        45,
        15,
        11,
        30,
        39,
        8,
        50,
        55,
        24,
        14,
        43,
        27,
        36,
        57,
        38,
        35,
        5,
        22,
    ],  # C
    [
        52,
        31,
        10,
        18,
        59,
        33,
        63,
        44,
        1,
        61,
        28,
        5,
        39,
        26,
        34,
        12,
        56,
        16,
        15,
        43,
        13,
        2,
        55,
        9,
        37,
        8,
        11,
        0,
        42,
        50,
        36,
        51,
        54,
        48,
        22,
        23,
        46,
        32,
        60,
        47,
        24,
        4,
        40,
        17,
        19,
        30,
        49,
        29,
        62,
        58,
        27,
        35,
        57,
        20,
        21,
        6,
        3,
        41,
        7,
        14,
        38,
        45,
        25,
        53,
    ],  # D
    [
        48,
        49,
        22,
        56,
        5,
        43,
        25,
        9,
        37,
        19,
        28,
        55,
        54,
        59,
        31,
        46,
        40,
        11,
        30,
        8,
        4,
        61,
        51,
        18,
        24,
        57,
        15,
        17,
        44,
        58,
        42,
        3,
        47,
        60,
        27,
        39,
        33,
        20,
        62,
        35,
        45,
        23,
        36,
        2,
        13,
        10,
        1,
        0,
        6,
        38,
        53,
        14,
        63,
        16,
        29,
        52,
        7,
        12,
        34,
        26,
        50,
        21,
        41,
        32,
    ],  # E
    [
        26,
        14,
        56,
        29,
        51,
        61,
        15,
        54,
        2,
        63,
        30,
        40,
        62,
        27,
        52,
        4,
        0,
        21,
        13,
        38,
        33,
        53,
        5,
        8,
        39,
        36,
        47,
        57,
        58,
        43,
        7,
        60,
        1,
        9,
        25,
        28,
        24,
        55,
        23,
        41,
        45,
        49,
        12,
        10,
        22,
        35,
        11,
        6,
        50,
        16,
        32,
        31,
        44,
        37,
        48,
        42,
        46,
        59,
        34,
        3,
        18,
        20,
        17,
        19,
    ],
]  # F

class PermHash:
    def __init__(self):
        self.state = [0] * N

    def init(self):
        for i in range(N):
            self.state[i] = i

    def apply_perm(self, perm):
        tmp = [0] * N
        for i in range(N):
            tmp[i] = self.state[perm[i]]
        self.state = list(tmp)

    def update(self, ptext):
        for b in ptext:
            u = (b & 0xF0) >> 4
            l = b & 0x0F
            self.apply_perm(gens[u])
            self.apply_perm(gens[l])

    def finalize(self):
        self.apply_perm(final)

    def hash(self, ptext):
        self.init()
        self.update(ptext)
        self.finalize()

    def hash_hex(self, ptext):
        self.init()
        self.update(ptext)
        self.finalize()
        return binascii.hexlify(self.to_binary()).decode("ascii")

    def to_binary(self):
        pint = 0
        nval = [0] * N
        for i in range(N):
            nval[i] = i

        for i in range(N, 1, -1):
            pint += nval[self.state[N - i]]
            pint *= i - 1
            for j in range(self.state[N - i], N):
                nval[j] -= 1

        return pint.to_bytes(37, byteorder="big")

def computeHash(msg):
    return h.hash_hex(binascii.unhexlify(msg))

def chall1():
    ipt = input('chall1 - message to hash = ')
    print(computeHash(ipt))

def chall2():
    f = open('hashes.txt', 'w')
    dico = open('/usr/share/wordlists/words_alpha.txt', 'r')
    for line in dico.readlines():
        l = line[:-1]
        msg = binascii.hexlify(l.encode('utf-8'))
        hsh = computeHash(msg)
        print(f'{msg} : {hsh}')
        f.write(hsh + '\n')

def chall3():
    dico = open('/usr/share/wordlists/rockyou.txt', errors='ignore')
    for line in dico.readlines():
        l = line[:-1]
        if l == '':
            continue
        msg = binascii.hexlify(l.encode('utf-8'))
        hsh = computeHash(msg)
        print(f'{msg} : {hsh}')
        if hsh == computeHash(""):
            print(f'{msg} has same hash as empty string')
            break

h = PermHash()
h.init()

chall1() # uncomment to input msg to hash

# chall2() # deeded and def -> 646565646564 and 646566 (see collisions.txt)
# to see all the collisions in dico:
# for line in `sort hashes.txt | uniq -cd | cut -d' ' -f 8`; do for n in `grep -n $line hashes.txt | cut -d':' -f 1`; do sed -n "$n"p /usr/share/wordlists/words_alpha.txt; done; echo ""; done
print("chall2 - 646565646564 and 646566")

# chall3() # 323233323233 (223223)
print("chall3 - 323233323233")

# CTF{permutation_attacks_no_joke_one_more_collision_ill_go_broke}
