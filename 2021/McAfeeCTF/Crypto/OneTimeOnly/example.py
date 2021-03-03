#!/usr/bin/python3

# this is the same script with an example from
# https://thusithathilina.medium.com/reused-key-vulnerability-in-one-time-pad-for-ctf-9e1fc04015c
# to test the methodology

from pwn import *
import string
import binascii
from colorama import Fore, Style

def h(msg):
    return binascii.hexlify(msg)

def hs(msg):
    return binascii.hexlify(msg.encode('utf-8'))

def getParams():
    hc1 = b"02036109340314070d131510141c06077a0b646d7f671a0b0d151403120463050b761b3241282f41312d20282f35243935412e2f412c38412524322a352e2d"
    hc2 = b"0b0d0a025b0775001b08166211017f1e711c1d0409711c1d7f1875011777641d64630a24323241233435412420323841352e4133242c242c2324334040405c"
    c1 = binascii.unhexlify(hc1)
    c2 = binascii.unhexlify(hc2)
    x12 = h(xor(c1, c2, cut='min'))
    return c1, c2, hc1, hc2, x12

def printParams(params):
    c1, c2, hc1, hc2, x12 = params
    print(f'enc1 = {c1}')
    print(f'enc2 = {c2}')
    print("---------")
    print(f'hc1 = {hc1}')
    print(f'hc2 = {hc2}')
    print("---------")
    print(f'x12 = {x12}')

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
    c1, c2, hc1, hc2, x12 = params
    for plain in plaintexts:
        print(f'{Fore.RED}\n============ Solving for plaintext = {plain}{Fore.RESET}')
        print(f'{Fore.BLUE}\n-- processing c1 and c2 with plaintext = {plain}{Fore.RESET}')
        solve(x12, plain)

def processPlain(params, plaintexts):
    c1, c2, hc1, hc2, x12 = params
    for plain in plaintexts:
        print(f'{Fore.RED}\n============ Solving for plaintext = {plain}{Fore.RESET}')
        print(f'{Fore.BLUE}\n-- processing c1 with plaintext = {plain}{Fore.RESET}')
        solve(hc1, plain)
        print(f'{Fore.BLUE}\n-- processing c2 with plaintext = {plain}{Fore.RESET}')
        solve(hc2, plain)

params = getParams()
printParams(params)
plaintexts = [b'FLAG{']
# plaintexts = [b'ATR[', b'Nebakanezzer', b'AcidicZero']
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

processXored(params, plaintexts)
# processXored(params, guesses)
processPlain(params, plaintexts)
