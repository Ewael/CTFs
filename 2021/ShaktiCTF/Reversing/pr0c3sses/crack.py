#!/usr/bin/env python3

from gdbpython import *
import os

os.system('rm -f check')

exc('file ./chall')
exc('b *0x5555554010e1') # main
exc('set follow-fork-mode parent')

code = '50101000' # 322-3224-321-3214-312-3124-311-3114-122-1224-121-1214-112-1124-111-1114
code = '50104000' # 322-3224-325-3254-312-3124-315-3154-122-1224-125-1254-112-1124-115-1154
code = '20104000' # 322-3224-325-3254-312-3124-315-3154-522-5224-525-5254-512-5124-515-5154
# we want --------- 322-3224-325-3254-312-3124-315-3154-522-5224-525-5254-512-5124-515-5154
# from now we can bruteforce

run(stdin=code)

# ba(0x555555401228) # inc 1st loop
tbc(0x555555401259) # first open
tbc(0x5555554012b9) # fprintf even
tbc(0x5555554012ca) # to reach check file
ba(0x555555401381) # inc 2nd loop
tb(0x55555540141e) # 2nd close
tb(0x5555554014b9) # strcmp

print(context())

'''
len code < 8

main 1010e1 -> 0x5555554010e1
strcmp 1014b9 -> 0x5555554014b9
getpid after close 1012ca -> 0x5555554012ca

first loop checks every even indexes 0, 2, 4...
second loop checks every odd indexes 1, 3, 5...

expected
322-3224-325-3254-312-3124-315-3154-522-5224-525-5254-512-5124-515-5154-
2+2+25+22+22+225+24+24+245+242+242+2425+5+5+55+52+52+525+54+54+545+542+542+5425+
'''
