#!/usr/bin/env python3

f = open("corona.csv", "r")

maxi = 0
for line in f.readlines():
    arr = line.split(",")
    for n in arr:
        try:
            n = int(n)
        except ValueError:
            continue
        if (n > maxi):
            maxi = n
            print("maxi = {}".format(maxi))

print("over, maxi = {}".format(maxi))
