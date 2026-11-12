#!/usr/bin/env python3
"""Compte, sans rien en montrer, ce qu'une idée partage avec les autres campagnes.

Usage, depuis le dossier de la campagne :
  python3 recoupe.py mot1 mot2 ...   avant d'écrire, avec les mots propres à l'idée (au singulier)
  python3 recoupe.py                 après, les mots sont pris dans la campagne écrite

N'affiche que des nombres : ni nom de dossier, ni ligne de texte des autres campagnes.
Un mot « pèse » dans un dossier s'il y revient 20 fois, ou 10 fois pour 10 000 mots.
"""
import os
import re
import sys
from collections import Counter

MOT = re.compile(r"[a-zàâäçéèêëîïôöùûüœ]{3,}")
MARQUES = ("etat_actuel.md", "personnage.md", "journal.md", "intrigues.md", "regles.md", "monde", "scenario", "arcs")
ICI = os.path.dirname(os.path.realpath(__file__))


def compter(dossier):
    c = Counter()
    for base, sous, fichiers in os.walk(dossier):
        sous[:] = [d for d in sous if not d.startswith(".")]
        for f in fichiers:
            if f.endswith(".md"):
                try:
                    with open(os.path.join(base, f), encoding="utf-8", errors="ignore") as h:
                        c.update(MOT.findall(h.read().lower()))
                except OSError:
                    pass
    return c


def nb(c, mot):
    """Occurrences du mot, pluriel compris."""
    return c[mot] + c[mot + "s"] + c[mot + "x"]


def est_campagne(p):
    return (os.path.isdir(p) and os.path.basename(p) != "campagne-modele"
            and sum(os.path.exists(os.path.join(p, m)) for m in MARQUES) >= 2)


def autres_campagnes(ici):
    """Les dossiers voisins de la campagne, et leurs sous-dossiers (archives), qui ont l'air d'une campagne."""
    parent, trouvees = os.path.dirname(ici), []
    for nom in sorted(os.listdir(parent)):
        p = os.path.join(parent, nom)
        if nom.startswith(".") or not os.path.isdir(p) or os.path.realpath(p) == ici:
            continue
        if est_campagne(p):
            trouvees.append(p)
            continue
        try:
            trouvees += [q for q in (os.path.join(p, n) for n in sorted(os.listdir(p)) if not n.startswith("."))
                         if est_campagne(q) and os.path.realpath(q) != ici]
        except OSError:
            pass
    return trouvees


def pese(n, total):
    return n >= 20 or (n >= 5 and n * 10000 / max(total, 1) >= 10)


def main():
    ici = os.path.realpath(os.getcwd())
    autres = [compter(p) for p in autres_campagnes(ici)]
    autres = [c for c in autres if sum(c.values()) > 3000]   # un dossier qui n'a que le modèle ne compte pas
    if not autres:
        sys.exit("Aucune autre campagne à côté de celle-ci : rien à compter.")
    totaux = [sum(c.values()) for c in autres]
    print(f"{len(autres)} autres dossiers de campagne comptés, sans les lire.")

    auto = len(sys.argv) == 1
    if not auto:
        mots = [m.lower() for m in sys.argv[1:]]
    else:
        # Les mots du système (skills, modèle de campagne) ne disent rien d'une idée.
        systeme = compter(os.path.dirname(ICI)) + compter(os.path.join(os.path.dirname(os.path.dirname(ICI)), "campagne-modele"))
        moi, mots = compter(ici), []
        for m in moi:
            if len(m) < 5 or m in systeme or (m[-1] in "sx" and m[:-1] in moi) or nb(moi, m) < 8:
                continue
            if len(autres) < 4 or sorted(nb(c, m) for c in autres)[1] <= 2:   # presque absent de deux dossiers : pas un mot-outil
                mots.append(m)

    lignes = []
    for m in mots:
        occ = [nb(c, m) for c in autres]
        lignes.append((sum(pese(n, t) for n, t in zip(occ, totaux)), m, sorted(occ, reverse=True)))
    if auto:
        lignes = sorted((l for l in lignes if l[0] >= 2), key=lambda l: (-l[0], -sum(l[2])))[:20]

    print(f"{'mot':<16}{'pèse dans':<12}occurrences par dossier, du plus au moins")
    for k, m, occ in lignes:
        print(f"{m:<16}{str(k) + ' / ' + str(len(autres)):<12}{' '.join(map(str, occ))}")
    if auto:
        print(f"\n{len(lignes)} mot(s) de cette campagne, sur {len(mots)} examinés, pèsent dans au moins deux autres dossiers.")
    else:
        un, deux = sum(l[0] >= 1 for l in lignes), sum(l[0] >= 2 for l in lignes)
        print(f"\n{un} mot(s) sur {len(mots)} pèsent dans au moins un autre dossier, {deux} dans au moins deux.")


if __name__ == "__main__":
    main()
