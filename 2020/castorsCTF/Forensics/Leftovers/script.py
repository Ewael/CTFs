#!/usr/bin/env python3

f = open('data', 'r')
g = open('betterFormat_data', 'w')

i = 1
for a in f:
    i += 1
    if i % 2 == 0:
        line = a[0:2] + ':' + a[2:4] + ':' + a[4:6] + ':' + a[6:8] + ':' + a[8:10] + '\n'
        g.write(line)
