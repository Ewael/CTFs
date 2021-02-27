#!/usr/bin/python3

from pwn import *
import string
import binascii
from colorama import Fore, Style
from b128 import b128decode

def h(msg):
    return binascii.hexlify(msg)

def getParams():
    c1 = open("encryption1.txt", "r").read().encode('utf-8')
    c2 = open("encryption2.txt", "r").read().encode('utf-8')
    c3 = open("encryption3.txt", "r").read().encode('utf-8')
    # c1, c2, c3 = b128decode(c1), b128decode(c2), b128decode(c3)
    hc1 = h(c1)
    hc2 = h(c2)
    hc3 = h(c3)
    x12 = h(xor(c1, c2, cut='max'))
    x13 = h(xor(c1, c3, cut='max'))
    x23 = h(xor(c2, c3, cut='max'))
    return c1, c2, c3, hc1, hc2, hc3, x12, x13, x23

def printParams(params):
    c1, c2, c3, hc1, hc2, hc3, x12, x13, x23 = params
    print(f'enc1 = {c1}')
    print(f'enc2 = {c2}')
    print(f'enc3 = {c3}')
    print("---------")
    print(f'hc1 = {hc1}')
    print(f'hc2 = {hc2}')
    print(f'hc3 = {hc3}')
    print("---------")
    print(f'x12 = {x12}')
    print(f'x13 = {x13}')
    print(f'x23 = {x23}')
    print("---------")

def solve(xored, plain):
    xored = binascii.unhexlify(xored)
    charset = string.ascii_letters + string.digits + string.punctuation + " "
    i = 0;
    for i in range(len(xored) - len(plain) + 1):
        print(f'{Fore.MAGENTA}{i}{Fore.RESET}{" "*(3-len(str(i)))}', end='')
        copy = xored[:i] + plain + xored[i + len(plain):]
        lol = xor(xored, copy)
        count = 0
        for idx, c in enumerate(lol):
            if chr(c) in charset or False:
                print(f'{Fore.GREEN}{chr(c)}{Fore.RESET}', end='')
                count += 1
            else:
                print(f'{Fore.BLACK}#{Fore.RESET}', end='')
        if count == len(plain):
            print(f"  {Fore.YELLOW}{count}{Fore.RESET}")
        else:
            print(f"  {Fore.CYAN}{count}{Fore.RESET}")
        i += 1

def processXored(params, plaintexts):
    c1, c2, c3, hc1, hc2, hc3, x12, x13, x23 = params
    for plain in plaintexts:
        print(f'{Fore.RED}\n============ Solving for plaintext = {plain}{Fore.RESET}')
        print(f'{Fore.BLUE}\n-- processing c1 and c2 with plaintext = {plain}{Fore.RESET}')
        solve(x12, plain)
        print(f'{Fore.BLUE}\n-- processing c1 and c3 with plaintext = {plain}{Fore.RESET}')
        solve(x13, plain)
        print(f'{Fore.BLUE}\n-- processing c2 and c3 with plaintext = {plain}{Fore.RESET}')
        solve(x23, plain)

def processPlain(params, plaintexts):
    c1, c2, c3, hc1, hc2, hc3, x12, x13, x23 = params
    for plain in plaintexts:
        print(f'{Fore.RED}\n============ Solving for plaintext = {plain}{Fore.RESET}')
        print(f'{Fore.BLUE}\n-- processing c1 with plaintext = {plain}{Fore.RESET}')
        solve(hc1, plain)
        print(f'{Fore.BLUE}\n-- processing c2 with plaintext = {plain}{Fore.RESET}')
        solve(hc2, plain)
        print(f'{Fore.BLUE}\n-- processing c3 with plaintext = {plain}{Fore.RESET}')
        solve(hc3, plain)

def printXored(xored):
    indexes = []
    for i in range(0, len(xored), 2):
        if xored[i:i+2] == b'00':
            print(f'{Fore.RED}{xored[i:i+2].decode("utf-8")}{Fore.RESET}', end='')
            indexes.append(i)
        else:
            print(f'{xored[i:i+2].decode("utf-8")}', end='')
    print('')
    print(f'same chars at: {indexes}')

def printSpecial(params):
    c1, c2, c3, hc1, hc2, hc3, x12, x13, x23 = params
    printXored(x12)
    printXored(x13)
    printXored(x23)

params = getParams()
plaintexts = [b'ATR[', b'Nebakanezzer', b'AcidicZero']
guesses = [s.encode('utf-8') for s in """
T+}nn2hgl.[h
Tu*g9e=?ivhh
[-vkl0\gd;
AW{cal'P1h
Zh<q|xZ5`h
Mc7uyedWkf
QeWVpjDqrk
E03wen@
sNr}ul#>"f
""".split('\n')[1:-1]]

printParams(params)
# printSpecial(params)
processXored(params, plaintexts)
# processPlain(params, plaintexts)
# processXored(params, guesses)
# processPlain(params, guesses)
