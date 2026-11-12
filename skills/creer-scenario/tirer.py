#!/usr/bin/env python3
"""Tire une main dans palettes.md, au vrai hasard, et la note dans jets.log.

Usage, depuis le dossier de la campagne :
  python3 tirer.py          une main complète pour une campagne nouvelle
  python3 tirer.py --arc    seulement un genre, ce qui porte l'arc et une humeur
"""
import os
import random
import re
import sys
from datetime import datetime

ICI = os.path.dirname(os.path.realpath(__file__))
CAMPAGNE = ["Mondes", "Quêtes de campagne", "Genres", "Échelle", "Humeur"]
ARC = ["Genres", "Ce qui porte l'arc", "Humeur"]


def urnes():
    with open(os.path.join(ICI, "palettes.md"), encoding="utf-8") as h:
        texte = h.read()
    res = {}
    for titre, corps in re.findall(r"^## (.+?)\n(.+?)(?=\n## |\Z)", texte, flags=re.S | re.M):
        items = [re.sub(r"^et ", "", i.strip(" .\n")) for i in corps.replace("\n", " ").split(",")]
        res[titre.strip()] = [i for i in items if i]
    return res


def main():
    u, de = urnes(), random.SystemRandom()
    arc = "--arc" in sys.argv
    main_ = [(t, de.choice(u[t])) for t in (ARC if arc else CAMPAGNE) if t in u]
    if not arc:
        main_ += [("Premier arc, " + t.lower(), de.choice(u[t])) for t in ARC[:2] if t in u]
    for t, v in main_:
        print(f"{t} : {v}")
    with open(os.path.join(os.getcwd(), "jets.log"), "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M} [MJ] main tirée ({'arc' if arc else 'campagne'}) : "
                + " · ".join(f"{t} = {v}" for t, v in main_) + "\n")


if __name__ == "__main__":
    main()
