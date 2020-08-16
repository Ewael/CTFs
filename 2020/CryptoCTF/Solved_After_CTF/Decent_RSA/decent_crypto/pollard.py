#!/usr/bin/env python3

# Python code for Pollard p-1
# factorization Method

# Driver code - CHANGE N HERE
n = 31973912565930840183966476557514486967105734963490863850242883813184363077890247373353346311197244652164393947531225033913089540524508960337859521594971267299801046318823852855678220562983993746120365799161402319433119943409550637861054248792884967164024537194083317326043002215575735008275047537805378975239548031416843476640326890142850615245392184058602194672466707234505010060517043706542794833490218200030153606086208410372554126103395033388764862282497594446045727336858065181330686078548554317618028148145081341511574658757428258020937703703371498976906228288914164074403171127516885244682134581893201619939353

# importing "math" for
# calculating GCD
import math

# importing "sympy" for
# checking prime
import sympy

# function to generate
# prime factors
def pollard(n):
    # defining base
    a = 2
    # defining exponent
    i = 2

    # iterate till a prime factor is obtained
    while(True):
        # recomputing a as required
        a = (a**i) % n
        # finding gcd of a-1 and n
        # using math function
        d = math.gcd((a-1), n)
        # check if factor obtained
        if (d > 1):
            #return the factor
            return d
            break
        # else increase exponent by one
        # for next round
        i += 1


# temporarily storing n
num = n
# list for storing prime factors
ans = []

# iterated till all prime factors
# are obtained
while(True):
    # function call
    d = pollard(num)
    # add obtained factor to list
    ans.append(d)
    # reduce n
    r = int(num/d)
    # check for prime using sympy
    if(sympy.isprime(r)):
        # both prime factors obtained
        ans.append(r)
        break
    # reduced n is not prime, so repeat
    else:
        num = r

# print the result
print("Prime factors of", n, "are", *ans)
