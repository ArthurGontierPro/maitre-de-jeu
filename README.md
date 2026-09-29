# Maître de jeu

Deux skills Claude Code pour mener une campagne de jeu de rôle en solo, en français, où **les fichiers font foi** d'une session à l'autre.

| Skill | Quand | Ce qu'il fait |
|---|---|---|
| `creer-scenario` | hors partie | construit un arc : grand secret en pièces de puzzle, carte des lieux, PNJ, antagoniste qui agit, horloge, issues, calibrage de la difficulté ; écrit les fichiers de campagne |
| `jouer` | en session | lit les fichiers, fait le « Précédemment », narre, fait parler les PNJ, lance les dés, tient l'horloge, met les fichiers à jour |

Les deux se parlent par les fichiers de la campagne, dont la structure est dans `campagne-modele/`.

## Installation

```bash
git clone git@github.com:ArthurGontierPro/maitre-de-jeu.git ~/mj
~/mj/install.sh ~/ma-campagne
```

`install.sh` lie `<campagne>/.claude/skills` vers `skills/` (les skills sont donc disponibles dans ce dossier, et se mettent à jour avec le dépôt) et, si le dossier est vide, y copie le modèle de campagne. Il reste à remplir `CLAUDE.md` (titre, personnage, ton) et `personnage.md`, puis à lancer Claude Code dans le dossier et demander de préparer le premier arc.

Pour rendre les skills disponibles partout plutôt que dans une seule campagne : `ln -sfn ~/mj/skills/creer-scenario ~/.claude/skills/creer-scenario` (et de même pour `jouer`).

## Structure d'une campagne

```
ma-campagne/
  CLAUDE.md          rôle du MJ, quel skill utiliser quand
  etat_actuel.md     où on en est maintenant (réécrit)
  personnage.md      la fiche, seulement ce que le personnage a maintenant
  regles.md          le système d100 et les règles maison connues du joueur
  intrigues.md       ce que le joueur sait
  secrets_mj.md      le caché : vérités, secret, carte, PNJ, antagoniste, horloge
  journal.md         un résumé par session
  retours_joueur.md  ce que le joueur a dit de la partie, hors jeu
  monde/             univers, lieux et PNJ tels que le joueur les connaît
  arcs/<arc>/        archives des arcs terminés, avec RESUME.md
  des.py, jets.log   lanceur de dés d100 et historique
```

## Le système
d100 sous la valeur (stat ou compétence), critiques sur 1-5 et 96-100, modificateurs de ±10 à ±30, 20 PV. Détail dans `campagne-modele/regles.md`. Le lanceur : `python3 des.py 60 +10`, `python3 des.py 2d6`, `--cache` pour un jet caché du MJ.

## Historique
`archive/` contient le système v1 (un `CLAUDE.md` unique) et les raisons du passage aux deux skills.
