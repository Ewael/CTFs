#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes
import gmpy2

p = 6722156186149423473586056936189163112345526308304739592548269432948561498704906497631759731744824085311511299618196491816929603296108414569727189748975204102209646335725406551943711581704258725226874414399572244863268492324353927787818836752142254189928999592648333789131233670456465647924867060170327150559233
ct = 5602276430032875007249509644314357293319755912603737631044802989314683039473469151600643674831915676677562504743413434940280819915470852112137937963496770923674944514657123370759858913638782767380945111493317828235741160391407042689991007589804877919105123960837253705596164618906554015382923343311865102111160

# build list of 'x' as 'ct = x [p]'
i = 254995058
while 1:
    pt = gmpy2.isqrt(ct + (p * i))
    pt = long_to_bytes(pt)
    print("[+] len = {}, i = {}".format(len(list(pt)), i))
    if b'TWCTF' in pt:
        break
    i += 1

print(pt)