# Archive : le système v1

`CLAUDE_v1.md` est le fichier d'instructions unique qui a servi de MJ pour les arcs 1 et 2 de *Les Marches du Sablier* (sessions 1 à 4). Il mélangeait la préparation et la conduite de partie.

## Pourquoi on l'a remplacé
- Préparer et jouer demandent deux façons de penser : prendre son temps et vérifier la cohérence d'un côté, répondre vite en 200 mots et laisser le joueur agir de l'autre.
- Le v1 ne disait rien de la **difficulté** : l'arc 2 (une enquête) s'est révélé trop facile, avec une seule suspecte crédible et des indices qui s'accumulaient tous dans le même sens.
- Il ne décrivait pas comment construire un arc d'**exploration** (carte de lieux, découvertes par l'observation, ressources).

## Ce qui a changé (v2)
- Deux skills : `creer-scenario` (hors partie) et `jouer` (en session), dans `skills/`.
- Un modèle de campagne (`campagne-modele/`) avec la structure de fichiers que les deux skills se partagent, dont un `secrets_mj.md` à sections fixes et un `retours_joueur.md`.
- Le `CLAUDE.md` d'une campagne se limite au rôle et au choix du skill.
