#!/usr/bin/env python3

import gmpy2

# Enter N here
N = 3349683240683303752040100187123245076775802838668125325785318315004398778586538866210198083573169673444543518654385038484177110828274648967185831623610409867689938609495858551308025785883804091

def fermat_factor(n):
    assert n % 2 != 0

    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n

    print("[+] Working...")
    while not gmpy2.is_square(b2):
        a += 1
        print("[x] a = {}".format(a))
        b2 = gmpy2.square(a) - n

    p = a + gmpy2.isqrt(b2)
    q = a - gmpy2.isqrt(b2)

    return int(p), int(q)

if __name__ == "__main__":
    (p, q) = fermat_factor(N)

    print("[+] p = {}".format(p))
    print("[+] q = {}".format(q))
