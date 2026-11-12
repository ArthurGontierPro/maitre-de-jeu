#!/usr/bin/env python3
"""Lanceur de dés pour la campagne.

Usage :
  python3 des.py               -> d100 brut
  python3 des.py 60            -> test contre 60 (réussite si le dé <= 60)
  python3 des.py 60 +10        -> test contre 60 avec un bonus de +10
  python3 des.py 60 -20        -> test contre 60 avec un malus de -20
  python3 des.py d6 | 2d6 | 3d10+2   -> dés quelconques (dégâts, etc.)
  --cache                      -> jet caché du MJ (noté [MJ] dans jets.log)

Critiques, quelle que soit la valeur : 1-10 = réussite critique (1 = effet bonus extrême),
91-100 = échec critique (100 = effet catastrophique). Le seuil est donc borné à 90.
Chaque jet est enregistré dans jets.log.
"""
import os
import random
import re
import sys
from datetime import datetime

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jets.log")


def log(ligne, cache):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M} {'[MJ] ' if cache else ''}{ligne}\n")


def des_libres(expr):
    m = re.fullmatch(r"(\d*)d(\d+)([+-]\d+)?", expr.lower())
    if not m:
        return None
    n, faces, bonus = int(m.group(1) or 1), int(m.group(2)), int(m.group(3) or 0)
    tirages = [random.randint(1, faces) for _ in range(n)]
    total = sum(tirages) + bonus
    detail = " + ".join(map(str, tirages)) + (f" {bonus:+d}" if bonus else "")
    return f"{expr} : [{detail}] = {total}"


def test(valeur, modif):
    seuil = max(1, min(90, valeur + modif))
    de = random.randint(1, 100)
    if de == 1:
        verdict = "RÉUSSITE CRITIQUE EXTRÊME !"
    elif de <= 10:
        verdict = "RÉUSSITE CRITIQUE !"
    elif de == 100:
        verdict = "ÉCHEC CATASTROPHIQUE !"
    elif de >= 91:
        verdict = "ÉCHEC CRITIQUE !"
    elif de <= seuil:
        verdict = "Réussite"
    else:
        verdict = "Échec"
    mod_txt = f" ({valeur} {modif:+d})" if modif else ""
    return f"d100 = {de}  vs  {seuil}{mod_txt}  ->  {verdict}"


def main():
    args = sys.argv[1:]
    cache = "--cache" in args
    args = [a for a in args if a != "--cache"]

    if not args:
        res = f"d100 = {random.randint(1, 100)}"
    elif "d" in args[0].lower():
        res = des_libres(args[0])
        if res is None:
            sys.exit(f"Expression invalide : {args[0]}")
    else:
        try:
            valeur = int(args[0])
            modif = int(args[1]) if len(args) > 1 else 0
        except ValueError:
            sys.exit(__doc__)
        res = test(valeur, modif)

    print(res)
    log(res, cache)


if __name__ == "__main__":
    main()
