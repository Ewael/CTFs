#!/usr/bin/env python3

# On continue avec la partie mais cette fois on utilise la génération de nombre pseudo aléatoires qui est faussée avec la libraire random python par défaut (Mersenne-Twister)
# https://mersenne-twister-predictor.readthedocs.io

import random
import time

FLAG = "HDCTF{FAKE FLAG2}"

scoreboard = """
=== Tableau des scores (plus le score est petit, mieux c'est) ====
Helyosis - 2
Max - 7
AAAAA - 8
Hexagons - 10
Joe - 12
Alfred - 42
============
"""

changelog = """
=== CHANGELOG ===
- Changement de la seed pour être imprévisible
- Ajoute la possibilité de recommencer une partie
- Diminution du délai pour trouver le nombre aléatoire
=================
"""

print(changelog)

print("Il est temps de jouer à un jeu !")
print("Je vais penser à un nombre aléatoire de 32 bits ! Essaie de trouver le plus vite possible :P")
print(scoreboard)

while True:
    number = random.getrandbits(32)
    for _ in range(5):
        time.sleep(0.01)
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
        print("C'est un bon nombre d'essais mais tu peux faire mieux !")
    else:
        print("Tu as trouvé le nombre en un nombre impressionnant d'essais")
        print(FLAG)

    ans = input("Veux-tu continuer à jouer ? (Y/n) ")
    if len(ans) > 0 and ans[0].upper() == "N":
        break
