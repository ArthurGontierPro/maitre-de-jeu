# Maître de jeu

Deux skills Claude Code pour mener une campagne de jeu de rôle en solo, en français, où **les fichiers font foi** d'une session à l'autre.

| Skill | Quand | Ce qu'il fait |
|---|---|---|
| `creer-scenario` | hors partie | construit le monde large en fiches, puis un arc : ce que les choses sont vraiment, ce qui porte l'arc (inventé à chaque fois, sous la forme qu'il appelle), comment il peut finir, ce qui bouge sans le joueur, lieux et PNJ ; peu d'invariants, le reste se choisit, avec une boîte à outils à part (`boite-a-outils.md`) ; écrit les fichiers de campagne |
| `jouer` | en session | lit les fichiers, fait le « Précédemment », narre, fait parler les PNJ, lance les dés, tient l'horloge, met les fichiers à jour |

Les deux se parlent par les fichiers de la campagne, dont la structure est dans `campagne-modele/`.

## Installation

```bash
git clone git@github.com:ArthurGontierPro/maitre-de-jeu.git ~/mj
~/mj/install.sh ~/ma-campagne
```

`install.sh` lie `<campagne>/.claude/skills` vers `skills/` (les skills sont donc disponibles dans ce dossier, et se mettent à jour avec le dépôt) et, si le dossier est vide, y copie le modèle de campagne. Il reste à remplir `CLAUDE.md` (titre, personnage) et `personnage.md`, puis à lancer Claude Code dans le dossier et demander de préparer le premier arc.

Pour rendre les skills disponibles partout plutôt que dans une seule campagne : `ln -sfn ~/mj/skills/creer-scenario ~/.claude/skills/creer-scenario` (et de même pour `jouer`).

## Structure d'une campagne

```
ma-campagne/
  CLAUDE.md          rôle du MJ, quel skill utiliser quand
  etat_actuel.md     où on en est maintenant (réécrit), avec des pointeurs vers les fiches
  personnage.md      la fiche, seulement ce que le personnage a maintenant
  regles.md          le système d100 et les règles maison connues du joueur
  intrigues.md       ce que le joueur sait
  journal.md         un résumé court par session de l'arc en cours
  retours_joueur.md  ce que le joueur a dit de la partie, hors jeu
  scenario/
    SCENARIO.md      l'arc en cours, caché et court : ce qui est vrai, comment ça finit,
                     ce qui bouge, et ce que l'arc demande ; il ne décrit rien, il pointe vers les fiches
  monde/
    INDEX.md         une ligne par fiche
    univers.md       le monde connu de tous, une page
    histoire.md      chronologie et « En ce moment, ailleurs »
    grand_dessin.md  les vérités à l'échelle de la campagne (caché)
    contrees/ factions/ anciens/ lieux/ pnj/   une fiche par élément
  arcs/<arc>/        archives des arcs terminés, avec RESUME.md
  des.py, jets.log   lanceur de dés d100 et historique
```

Le MJ lit à chaque session ce qui est court (état, scénario, index) et n'ouvre une fiche que quand la scène la touche. Le monde peut donc être vaste sans encombrer la partie, et le scénario dit toujours ce qui fait avancer l'intrigue.

## Le système
d100 sous la valeur (stat ou compétence), critiques sur 1-5 et 96-100, modificateurs de ±10 à ±30, 20 PV. Détail dans `campagne-modele/regles.md`. Le lanceur : `python3 des.py 60 +10`, `python3 des.py 2d6`, `--cache` pour un jet caché du MJ.

## Historique
`archive/` contient le système v1 (un `CLAUDE.md` unique) et les raisons du passage aux deux skills.

## Sources et remerciements
La méthode du skill `creer-scenario` s'inspire de maîtres de jeu qui ont partagé la leur en public, FibreTigre en premier. Qui a apporté quoi, et où le lire : `REMERCIEMENTS.md`.
