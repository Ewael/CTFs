#!/usr/bin/env python3

s = 4
y = []
Z = []
res = []
expected="uh27bio:uY<xrA."

def printFlag(inp):
    st = []
    for i in range(len(inp)):
        st.append(chr(ord(inp[i]) - i + 4))
    print(''.join(st) + "}")

def decode2(inp):
    for i in range(len(inp)):
        if len(inp) < 8:
            Z.append(chr(ord(inp[i]) - 1 + i))
        else:
            Z.append(chr(ord(inp[i]) + 4))
    return ''.join(Z)

def reverse2(inp):
    res = ''
    for i in range(len(inp)):
        res += chr(ord(inp[i]) - 4)
    return res

def decode1(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isnumeric():
            result += chr(ord(char) - 1)
        elif char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr(ord(char) ^ 1)
    return result

def reverse1(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isnumeric():
            result += chr(ord(char) + 1)
        elif char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr(ord(char) ^ 1)
    return result

x2 = reverse2(expected)
print(f'reversed 2 = {x2}')
x1 = reverse1(x2, s)
print(f'reversed 1 = {x1}')

flag = x1
dec = decode1(flag, s)
print(f'decoded = {dec}')
res = decode2(dec)
print(f'res = {res}')
print(f'expected = {expected}')

if expected == res:
    print("Yoo.. looks like your flag is complete!!")
    printFlag(flag)
else:
    print("try again:/ ")

# th15_ch4lL3ng3!}
