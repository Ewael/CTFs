# GroceryList

To begin with, we have a base 64 string:

```
UmV2ZXJzZSBHcm9jZXJ5UGxhY2UKCnZpY2h5c3NvaXNlICAgICAgICAgICAgIAptYW5nbyAgICAgICAgICAgICAgICAgICAKdmVybW91dGgKenVjb3R0bwpzYW5kd2ljaApsYW1iCnZlYWwKeW9ndXJ0CnZlcm1pY2VsbGkKenVjY2hpbmkKc2FsbW9uCmZlbm5lbCBzZWVkcwppY2UgY3JlYW0KY2Fycm90cwp1bmFnaQppbmNhIGJlcnJpZXMKY2FiYmFnZQp1cG1hCmdyYXBlcwpuYWFuCmFwcGxlcwpiYW5hbmFzCmFsbW9uZHMKYmFzaWwKZmVudWdyZWVrCnBvdGF0b2VzCnBpZQpzb3kgYmVhbnMKZWdncwp0dW5hZmlzaAoKRmluZCB0aGUgaW5wdXQgdG8gdGhlIGZvbGxvd2luZyBvdXRwdXQuCk9VVFBVVDogNGN1bTc3aXRRZEt5NHI3Y35ybTV1MDVwbE4=
```

Once decoded, we get:

```
Reverse GroceryPlace

vichyssoise
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
tunafish

Find the input to the following output.
OUTPUT: 4cum77itQdKy4r7c~rm5u05plN
```

I spent a LOT of time searching for any hint about what to do with the list. I eventually found this reading abot esoteric languages: [esolang](https://esolangs.org/wiki/Grocery_List) and [progopedia](http://progopedia.com/language/grocery-list). And BOTH SITES HAVE MISTAKES. The worst one being *progopedia* which does not event precise when to pop before an operation, and *esolang* having some typos but being much much more trustable.

As you may notice, this language has no online interpreter, so I decided to code one in Python.

```python
#!/usr/bin/env python3

import string

x = '''vichyssoise
mango
[...]
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

charset = string.ascii\_letters + string.punctuation + string.digits
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
```

Playing a bit with the input, we can easily notice that for each pair of character, we have

```
(x, y) => (y + 4, x)
```

Reversing the expected output gives us the flag:

```
shaktictf{c0mp73tedMyGr0c3ry5h0pp1Ng}
```
