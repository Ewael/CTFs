#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, isPrime

flag = 'TWCTF{F4k3_fL4GG_'
flag += "A" * (42-len(flag)-1) + '}'
p = 6722156186149423473586056936189163112345526308304739592548269432948561498704906497631759731744824085311511299618196491816929603296108414569727189748975204102209646335725406551943711581704258725226874414399572244863268492324353927787818836752142254189928999592648333789131233670456465647924867060170327150559233

def encrypt(pt, k, p):
    return pow(pt, 1 << k, p)

assert flag.startswith("TWCTF{")
assert len(flag) == 42
assert isPrime(p)

k = 64
pt = bytes_to_long(flag.encode())
ct = encrypt(pt, k, p)

print('[+] pt: {}'.format(pt))
print('[+] 1 << k: {}'.format(1<<k))
print('[+] p: {}'.format(p))
print('[+] ct: {}'.format(ct))

# ct = pt ^ (1<<k) % p
# ct = pt ^ (2^64) % p
