# Règles

## Principe
Tout se joue au **d100**, sous la valeur testée : `python3 des.py <valeur> [bonus/malus]`.
- **Dé ≤ valeur (modifiée)** : réussite. **Dé > valeur** : échec.
- **1 à 10** : réussite critique (effet bonus). Sur 1, effet bonus extrême.
- **91 à 100** : échec critique (effet malus). Sur 100, effet catastrophique.

## Statistiques (sur 100)
| Stat | Sert à… |
|---|---|
| **Force** | soulever, enfoncer, retenir, encaisser, frapper sans technique |
| **Intelligence** | déduire, se souvenir, comprendre un mécanisme, connaissances |
| **Perception** | observer l'environnement, chercher quelque chose |
| **Discrétion** | se cacher, se faufiler, passer inaperçu |
| **Mentir-Convaincre** | persuader, baratiner, négocier |
| **Intimidation** | intimider, menacer |
| **Courir-Sauter** | fuir, poursuivre, grimper, esquiver, agilité en général |


## Compétences
Apprises en jeu (auprès d'un PNJ, par l'expérience, un livre…). Elles ont leur propre valeur sur 100 et **remplacent la stat** quand elles s'appliquent.

## Bonus et malus (décidés par le MJ)
- Situation favorable (bon outil, préparation, aide) : **+10 à +30**
- Situation défavorable (blessé, pressé, dans le noir, cible méfiante) : **−10 à −30**
- Action quasi impossible : **−40 ou plus**. Action triviale : pas de jet.

## Santé
- **PV : 20**. Dégâts typiques : poing 1d4, arme 1d10, chute 1d6 par 3 m.
- **À 5 PV ou moins** : blessé grave, malus −20 sur tout.
- **À 0** : inconscient, en danger de mort. Le MJ ne tue pas bêtement, mais la mort reste possible.
- Repos : +2 PV par nuit, +5 avec des soins.

## Combat
Pas de tour rigide. Le joueur décrit son action, jet (corps à corps : Force ou la compétence ; esquive et fuite : Courir-Sauter). Un PNJ agit en réponse ; le MJ lance ses jets avec `--cache` si besoin. La fuite et la parole sont des options.

## Quand lancer les dés
- **Pas de jet** si l'action est simple pour le personnage dans la situation, ou si l'échec ne changerait rien. On ne lance que quand il y a un vrai doute **et** un enjeu.
- Un seul jet par enjeu : pas de chaîne de jets pour une même action.
- Un échec fait avancer l'histoire (complication, prix), il ne la bloque pas.
- Dégâts : `python3 des.py 1d4` (poing), `1d10` (arme), `1d6` (chute).

## Monnaie et ressources
_(À définir par le monde : le skill `creer-scenario` les écrit ici.)_
