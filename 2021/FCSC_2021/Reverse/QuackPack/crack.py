#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
import binascii

def unhex(h):
    return binascii.unhexlify(h)

def decodeStrings():
    enter_key = xor(unhex('270c16100718420e0342010e0704425868'), 0x62)
    print(enter_key)
    x1 = xor(unhex('270c16100718420e0342010e07044258681634251c3e35243d3419303f353d3400'), 0x51)
    print(x1)
    x2 = xor(unhex('cfedfcd8fae7ebc9ececfaedfbfb0000'), 0x88)
    print(x2)
    x3 = xor(unhex('c0ced9c5cec7989985cfc7c70000cfedfcd8fae7ebc9ececfaedfbfb0000'), 0xab)
    print(x3)
    x4 = xor(unhex('a39c8781809499b499999a9600c0ced9c5cec7989985cfc7c70000cfedfcd8fae7ebc9ececfaedfbfb00'), 0xf5)
    print(x4)
    x5 = xor(unhex('655a414746525f63415c4756504700'), 0x33)
    print(x5)
    x6 = xor(unhex('655a414746525f63415c47565047002f0d1c25070c1d040d2009060c040d00'), 0x68)
    print(x6)
    x7 = xor(unhex('6f4d5c785a474b694c4c5a4d5b5b00'), 0x28)
    print(x7)
    x8 = xor(unhex('131d0a161d144b4a561c1414006f4d5c785a474b694c4c5a4d5b5b00'), 0x78)
    print(x8)
    x9 = xor(unhex('d0e0f3e4fdb2b300'), 0x92)
    print(x9)
    x10 = xor(unhex('4a616c607d6a2f7a612f7b607a7b2f7f6a7b667b2f6a6969607d7b21212100'), 0xf)
    print(x10)

def decode_arr(buf1, buf2, l):
    res = [None] * l
    for i in range(l):
        c = buf1[i*2]
        c8ls = bytes_to_long(bytes(buf1[i*2:i*2+1])) >> 0x8
        if c == 0x13:
            res[i] = buf2[i] + c8ls
        elif c == ord('T'):
            res[i] = buf2[i] - c8ls
        elif c == ord('w'):
            res[i] = buf2[i] ^ c8ls
    return res

arr = [0x54, 0x5e, 0x13, 0xd, 0x77, 0x5f, 0x54, 99, 0x54, 0, 0x13, 0x19, 0x77, 8, 0x13, 0x4f, 0x54, 0x1c, 0x13, 0x2b, 0x13, 0x25, 0x13, 0x3e, 0x54, 0x2a, 0x77, 0x55, 0x13, 0x36, 0x77, 0x1d, 0x77, 0xd, 0x54, 0x26, 0x13, 0x3f, 0x13, 0x52, 0x13, 0x5a, 0x54, 0x59, 0x77, 4, 0x54, 0x18, 0x54, 0x36, 0x54, 0x2b, 0x54, 0x17, 0x13, 0xc, 0x77, 0x31, 0x54, 0x50, 0x54, 0x50, 0x54, 0x43, 0x77, 0x4a, 0x77, 0x58, 0x77, 5, 0x13, 0x56, 0x77, 0x4d, 0x77, 0x5b, 0x13, 0x4d, 0x54, 0xe, 0x77, 0x3b, 0x54, 0xe, 0x13, 0x45, 0x13, 0xe, 0x54, 0x16, 0x77, 0x61, 0x77, 0x1a, 0x13, 0x5a, 0x77, 0x2d, 0x77, 0x3e, 0x13, 8, 0x54, 0xe, 0x13, 0x18, 0x77, 0x11, 0xb3, 0x7e, 0xb3, 0xb4, 199, 0x2c, 0xf4, 0xb1, 0x1c, 0xd5, 0xdb, 0x4d, 0x6f, 0xa9, 5, 0x58, 1, 0xa3, 0xe0, 0x39, 0xf3, 0x61, 7, 0x65, 0x32, 0x3a, 0xd5, 5, 0xb2, 0x42, 0x75, 0xce, 0xf, 0x50, 6, 0xef, 0xb1, 0xd3, 0xc3, 0x99, 0x76, 10, 0x3e, 0xb3, 0x17, 0xe8, 0x57, 0xa2, 0xc6, 0xe7, 0x83, 0xf3, 0x45, 0xd2]
limit = arr.index(0xb3)
#r = decode_arr(arr[:limit], arr[limit:], 36)
r = binascii.unhexlify("51ec8b5500fc45c78b000000453bfc458b1f7d0c4d03084d11be0ffc8b25f283450308458b1088fcc183fc4dfc4d8901e58bd9eb0000c35d")
print(f'limit = {limit}')
print(f'r = {r}')

f = open('fun_decoded.hex', 'r').read()[:-1]
g = open('fun_decoded.raw', 'w')
L = [f[i:i+8] for i in range(0, len(f), 8)]
c = ''
for a in L:
    b = a[6:8] + a[4:6] + a[2:4] + a[0:2]
    c += b
g.write(c + '\n')
g.close()
# see y.c

# 1c170 -> 1c56f
arx = '00000000b71dc1046e3b8209d926430ddc7604136b6bc517b24d861a0550471eb8ed08260ff0c922d6d68a2f61cb4b2b649b0c35d386cd310aa08e3cbdbd4f3870db114cc7c6d0481ee09345a9fd5241acad155f1bb0d45bc2969756758b5652c836196a7f2bd86ea60d9b6311105a6714401d79a35ddc7d7a7b9f70cd665e74e0b6239857abe29c8e8da191399060953cc0278b8bdde68f52fba582e5e66486585b2bbeef46eaba3660a9b7817d68b3842d2fad3330eea9ea16ada45d0b6ca0906d32d42770f3d0fe56b0dd494b71d94c1b36c7fb06f7c32220b4ce953d75ca28803af29f9dfbf646bbb8fbf1a679fff4f63ee143ebffe59acdbce82dd07dec77708634c06d4730194b043dae56c539ab0682271c1b4323c53d002e7220c12acf9d8e1278804f16a1a60c1b16bbcd1f13eb8a01a4f64b057dd00808cacdc90c07ab9778b0b6567c69901571de8dd475dbdd936b6cc0526fb5e6116202fbd066bf469f5e085b5e5ad17d1d576660dc5363309b4dd42d5a490d0b1944ba16d84097c6a5ac20db64a8f9fd27a54ee0e6a14bb0a1bffcad60bb258b23b69296e2b22f2bad8a98366c8e41102f83f60dee87f35da9994440689d9d662b902a7bea94e71db4e0500075e4892636e93e3bf7ed3b6bb0f38c7671f7555032fae24df3fe5ff0bcc6e8ed7dc231cb3ecf86d6ffcb8386b8d5349b79d1edbd3adc5aa0fbd8eee00c6959fdcd6d80db8e6037c64f643296087a858bc97e5cad8a73ebb04b77560d044fe110c54b383686468f2b47428a7b005c3d66c158e4408255535d43519e3b1d252926dc21f0009f2c471d5e28424d1936f550d8322c769b3f9b6b5a3b26d6150391cbd40748ed970afff0560efaa011104dbdd014949b93192386521d0e562ff1b94beef5606dadf8d7706cfcd2202be2653deae6bc1ba9eb0b0668efb6bb27d701a6e6d3d880a5de6f9d64da6acd23c4ddd0e2c004f6a1cdb3eb60c97e8d3ebdc990ffb910b6bcb4a7ab7db0a2fb3aae15e6fbaaccc0b8a77bdd79a3c660369b717df79fa85bb4921f4675961a163288ad0bf38c742db081c330718599908a5d2e8d4b59f7ab085440b6c95045e68e4ef2fb4f4a2bdd0c479cc0cd43217d827b9660437f4f460072f85bc176fd0b86684a16476c93300461242dc565e94b9b115e565a1587701918306dd81c353d9f0282205e065b061d0bec1bdc0f51a69337e6bb52333f9d113e8880d03a8dd097243acd5620e3eb152d54f6d4297926a9c5ce3b68c1171d2bcca000eac8a550add6124d6cd2cb6b2fdf7c76eedbc1cba1e376d660e7aff023ea18ede2ee1dbda5f0aaa064f4738627f9c49be6fd09fdb889bee0798d67c63a80d0dbfb84d58bbc9a62967d9ebbb03e930cadff97b110b0af060d71abdf2b32a66836f3a26d66b4bcda7b75b8035d36b5b440f7b1'

# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -

arx = [arx[i:i+8] for i in range(0, len(arx), 8)]
for i in range(len(arx)):
    arx[i] = arx[i][6:8] + arx[i][4:6] + arx[i][2:4] + arx[i][0:2]
arx = ''.join(arx)
#arx = [int(arx[i], 16) for i in range(len(arx))]
#print([hex(a) for a in arx])

def getX(i, j, k, l):
    # 00d49e78 = input addr
    # bu 3e8f6f -> bu quackpack+0x8f71
    mask = 0xffffffff
    buff = [i, j, k, l]
    print(f'trying {buff}')
    i = 0
    for n in range(4):
        # mask = mask << 8 ^ (arx[mask >> 0x18 ^ buff[i]] * 4)
        print(f'--- loop {n}')
        eax = mask << 8 & 0xffffffff
        print(f'eax = {hex(eax)}')
        ecx = mask >> 0x18
        print(f'ecx = {hex(ecx)}')
        edx = buff[i]
        print(f'edx = {hex(edx)}')
        ecx = ecx ^ edx
        print(f'after xor ecx = {hex(ecx)}')
        ecx = ecx & 0xff
        print(f'after and ecx = {hex(ecx)}')
        ind = ecx * 4 * 2 # * 2 bcuz of hex
        print(f'ecx * 4 = {hex(ind)}')
        elt = int(arx[ind:ind+8], 16)
        gigaxor = eax ^ elt
        print(f'gigaxor(eax={hex(eax)}, elt={hex(elt)}) = {hex(gigaxor)}')
        mask = gigaxor
        print(f'mask = {hex(mask)}')
        i += 1
    return mask

def getBuff(mask):
    buff = [0x0, 0x0, 0x0, 0x0]
    for i in range(256):
        print(f'trying i = {i}')
        for j in range(256):
            for k in range(256):
                for l in range(256):
                    if getX(i, j, k, l) == mask:
                        return [i, j, k, l]

x = 0x966cd31b
#buff = getX(buff)
buff= [0xf5, 0x0b, 0x13, 0xa1]
print(f'success : {[hex(a) for a in buff]}')
print(f'got {hex(getX(buff[0], buff[1], buff[2], buff[3]))}')
s = 0xa113b0f5

pwd = 'fc5c' + 'a1130bf5'
print(f'pwd = {pwd}')

context.log_level='error'
charset = '0123456789abcdef'
for w in charset:
    for x in charset:
        for y in charset:
            for z in charset:
                newpwd = pwd+w+x+y+z
                p = process(['./checkpwd', newpwd])
                print(f'trying {newpwd}')
                if b'success' in p.recv():
                    print(f'pwd = {newpwd}')
                    exit(0)
                p.close()

'''
https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/getting-started-with-windbg
https://stackoverflow.com/questions/4946685/good-tutorial-for-windbg

no anti-debug

b quackpack+offset
main = bu quackpack+0x91c0
after gets = bu quackpack+0x951d
call1 = bu quackpack+0x9553
call fun_dec = bu quackpack+0x959f
decode_fun2 = bu quackpack+0x95ca
call getX = bu quackpack+0x968e

after Z = bu quackpack+0x960c
after X = bu quackpack+0x9693

fun_00025000 -> decoded by fun1/fun2
must ret != 0
from da5000 to da616a
n == 0x2b

for Z:
0x00d466f0 = input
0x00aff978 = copy first 4 bytes
int(input[:4], 16) == 0xfc5c

for X:
0963a = memcpy next 4 bytes
buff = strtoul(input[4:12])

Y = bu quackpack+0x959f
Z = bu quackpack+0x9604
X = bu quackpack+0x968e

keylen = 0x11 = 17
'''

# FCSC{3d9593ccd1400c61cd5b6e16f2b5d042cf1b24648c7497412060ef199a92bd61}
