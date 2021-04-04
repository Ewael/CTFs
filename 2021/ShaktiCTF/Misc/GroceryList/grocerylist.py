#!/usr/bin/env python3

import string

x = '''vichyssoise
mango
vermouth
zucotto
sandwich
lamb
veal
yogurt
vermicelli
zucchini
salmon
fennel seeds
ice cream
carrots
unagi
inca berries
cabbage
upma
grapes
naan
apples
bananas
almonds
basil
fenugreek
potatoes
pie
soy beans
eggs
tunafish'''

s = x.split('\n')[:]

def debug(msg):
    if d:
        print(f'[*] {msg}')

def push(v):
    L.insert(0, v)

def pop():
    return L.pop(0)

def add():
    a = pop()
    b = pop()
    push(a + b)
    debug(f'add {a} + {b}')

def bring():
    v = L.pop()
    push(v)
    debug(f'bring {v}')

def copy():
    push(L[0])
    debug(f'copy')

def endloop():
    global j
    j = save
    debug(f'end loop -> returning to j={save}')

def flip():
    L[0], L[1] = L[1], L[0]
    debug(f'flip')

def gt():
    s0 = pop()
    s1 = pop()
    if s0 > s1:
        push(1)
    else:
        push(0)
    debug(f'greater than')

def ipt():
    global i
    if i >= len(pld):
        push(0)
        debug(f'input: pushing 0 (end of input)')
    else:
        push(ord(pld[i]))
        debug(f'input: pushing {pld[i]}')
        i += 1

def loop():
    global save
    save = j
    debug(f'loop starting')
    if not L or L[0] == 0:
        return True
    return False

def number():
    push(len(s[j]))
    debug(f'number with {s[j]}')

def p():
    global output
    c = chr(pop())
    if c not in charset:
        return True
    output += c
    print(f'output = {c} -> {output}')
    return False

def sub():
    a = pop()
    b = pop()
    push(a - b)
    debug(f'sub {a} - {b}')

def terminate():
    return

def unbring():
    L.append(pop())
    debug(f'unbring')

def value():
    global j
    push(ord(prog[j + 1]))
    j += 1
    debug(f'value: pushing {prog[j]}')

def interpret(l):
    ret = False
    if l == 'a': add()
    elif l == 'b': bring()
    elif l == 'c': copy()
    elif l == 'e': endloop()
    elif l == 'f': flip()
    elif l == 'g': gt()
    elif l == 'i': ipt()
    elif l == 'l': ret = loop()
    elif l == 'n': number()
    elif l == 'p': ret = p()
    elif l == 's': sub()
    elif l == 't': terminate()
    elif l == 'u': unbring()
    elif l == 'v': value()
    elif l == 'w': push(100)
    else:
        print('critical error on letter {l}')
        exit(1)
    return ret

charset = string.ascii_letters + string.punctuation + string.digits
prog = ''.join([w[0] for w in s])
L = [] # stack
i = 0
j = 0
save = 0
pld = 'c0mp73tedMyGr0c3ry5h0pp1Ng'
d = False
output = ''

while j < len(prog) and prog[j] != 't':
    ret = interpret(prog[j])
    j += 1
    # print(f'i = {i}, j = {j}', prog[j:], L)
    if ret:
        break

out = '4cum77itQdKy4r7c~rm5u05plN'
print(f'prog = {prog}, len = {len(prog)}')
print(f'ipt = {pld}')
print(f'got = {output}')
print(f'exp = {out}')

# shaktictf{c0mp73tedMyGr0c3ry5h0pp1Ng}
