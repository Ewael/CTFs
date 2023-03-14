#!/usr/bin/env python3

#   Le principe du challenge est d'utiliser la génération aléatoire qui a une graine prévisible (le temps) pour prévoir le nombre en avance

import time
import random
import datetime

FLAG = "HDCTF{FAKE FLAG1}"

scoreboard = """
Tableau des scores (plus le score est petit, mieux c'est):
Helyosis - 2
Max - 7
AAAAA - 8
Hexagons - 10
Joe - 12
Alfred - 42
"""

seed = int(time.time())
date = datetime.datetime.utcfromtimestamp(seed)
random.seed(seed)

print(f"Il est {date}.")
print("Il est temps de jouer à un jeu !")
print("Je vais penser à un nombre aléatoire entre 1 et 1 000 000 000 (inclus), essaie de trouver le plus vite possible :P")
print(scoreboard)

number = random.randint(1, 1000000000)
for _ in range(5):
    time.sleep(1)
    print(".", end = "", flush=True)
print()
print("J'ai trouvé mon nombre ! A toi de trouver")
nb_guess = 0
while True:
    guess = int(input("> "))
    nb_guess += 1
    if guess == number:
        break
    if guess < number:
        print("Mon nombre est supérieur.")
    if guess > number:
        print("Mon nombre est inférieur.")

assert guess == number

print(f"Bien joué ! C'était bien {number}, tu as trouvé en {nb_guess} essai{'s' if nb_guess > 0 else ''}.")
if nb_guess > 1:
    print("C'est un bon nombre d'essais mais tu peux faire mieux ! Essaie d'être le premier sur le tableau des scores !")
else:
    print("Tu as trouvé le nombre en un nombre impressionnant d'essais")
    print(FLAG)
