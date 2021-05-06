#!/usr/bin/env python3

part1 = 'FCSC{'
print(part1)

part2 = '\x65\x37\x35\x35\x32\x63\x66\x36'
print(part2)

arr1 = [0x34, 99, 0x65, 0x32, 0x65, 0x35, 0x61, 100]
part3 = ''.join(chr(l) for l in arr1)
print(part3)

arr2 = [0x30, 0x62, 0x62, 0x30, 0x39, 0x35, 0x34, 0x66]
part4 = ''.join(chr(l) for l in arr2)
print(part4)

arr3 = [1, 0x54, 0x55, 0x51, 9, 7, 0x57, 0]
part5 = ''.join(chr(arr2[i] ^ arr3[i]) for i in range(8))
print(part5)


print(f'flag = {part1+part2+part3+part4+part5}' + '}')
