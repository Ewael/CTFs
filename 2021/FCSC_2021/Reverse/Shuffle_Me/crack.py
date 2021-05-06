#!/usr/bin/env python3

from gdbpython import *

init('./shuffleMe')

secret = '255'
charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!'
#charset = '01234fdd46bfc8105cb28e04988f904049dd60be1245718ffef5b9bbf9b509d5'
pld = 'FCSC{' + charset + '}'

run(stdin=pld, args=[secret])
tbc(0x401172) # main
tbc(0x401230) # check

#ba(0x40124b) # loop start
ba(0x40127b) # jmp rcx

def getX():
    x = []
    cont()
    for i in range(0x46):
        cont()
        cont()
        exc('si')
        x1 = int(exc('x/i $rip').split(',')[-1][2:-1], 16)
        cont()
        exc('si')
        x2 = int(exc('p $rsi').split(' ')[-1][2:-1], 16)
        x.append((x1, x2))
        for j in range(4):
            cont()
    for (x1, x2) in x:
        print(f'({hex(x1)}, {hex(x2)}),')

#cont()
#cont()
#cont()

getX()

ba(0x401205) # after check
#print(context())

'''
(((secret * 0x5b + 0xd9) % 0x200) << 0x4) + 0x000000000040127d

index 0:
    4024bd: 8a 1f                 mov    (%rdi),%bl

0x40236d                  mov    bl, BYTE PTR [rdi+0x19]
0x4019bd                  mov    bh, bl
0x40204d                  xor    bx, 0x3922
0x40241d                  xor    rbx, rsi

0x4017dd                  mov    bl, BYTE PTR [rdi+0x1a]
0x402ced                  mov    bh, bl
0x40313d                  xor    bx, 0x65d0
0x401dcd                  xor    rbx, rsi

len pld = 0x46

take the 11th letter and concat it to itself
5 -> 55
xor 0x6783 -> 0x52b6
xor 0x01e5 -> 0x5353

after first iteration
| r9 (starts to 0)
+ 0x0002000200020002

} -> }}
xor 0x7cdb -> 0x01a6
xor 0x01a6 -> 0x0000

at the end -> xor rax, 0x1234
r9 | r11 = returned value
'''
