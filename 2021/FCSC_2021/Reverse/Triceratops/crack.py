#!/usr/bin/env python3

from gdbpython import *

init('./triceratops')

username = 'thomas'
serial = 'abcdefghijklmnop' * 2 + 'AB'

creds = username + '\n' + serial + '\n'
f = open('creds.txt', 'w')
f.write(creds)
f.close()
run(stdin_file='creds.txt')

print(context())

'''
len serial = multiple de 3
'''
