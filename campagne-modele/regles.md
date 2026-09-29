# Règles

## Principe
Tout se joue au **d100**, sous la valeur testée : `python3 des.py <valeur> [bonus/malus]`.
- **Dé ≤ valeur (modifiée)** : réussite. **Dé > valeur** : échec.
- **1 à 5** : réussite critique (effet bonus, sans prix à payer).
- **96 à 100** : échec critique (complication sérieuse).
- La **marge** (valeur − dé) indique la qualité : grande marge = réussite éclatante, petite = de justesse.

## Statistiques (sur 100)
| Stat | Sert à… |
|---|---|
| **Force** | soulever, enfoncer, retenir, encaisser, frapper sans technique |
| **Intelligence** | observer, déduire, se souvenir, comprendre un mécanisme, connaissances |
| **Mentir-Convaincre** | persuader, baratiner, négocier, intimider, se déguiser |
| **Courir-Sauter** | fuir, poursuivre, grimper, esquiver, discrétion, agilité en général |

## Compétences
Apprises en jeu (auprès d'un PNJ, par l'expérience, un livre…). Elles ont leur propre valeur sur 100 et **remplacent la stat** quand elles s'appliquent.
- Une compétence nouvelle commence en général à **30** (ou à la stat liée −10 si c'est plus haut, au choix du MJ).
- **Progression** : après une réussite critique, ou après une scène marquante où la compétence a compté, le MJ peut accorder **+5**.

## Bonus et malus (décidés par le MJ)
- Situation favorable (bon outil, préparation, aide) : **+10 à +30**
- Situation défavorable (blessé, pressé, dans le noir, cible méfiante) : **−10 à −30**
- Action quasi impossible : **−40 ou plus**. Action triviale : pas de jet.

## Santé
- **PV : 20**. Dégâts typiques : poing 1d4, couteau 1d6, arme lourde 1d10, chute 1d6 par 3 m.
- **À 5 PV ou moins** : blessé grave, malus −20 sur tout.
- **À 0** : inconscient, en danger de mort. Le MJ ne tue pas bêtement, mais la mort reste possible.
- Repos : +2 PV par nuit, +5 avec des soins.

## Combat
Pas de tour rigide. Le joueur décrit son action, jet (corps à corps : Force ou la compétence ; esquive et fuite : Courir-Sauter). Un PNJ agit en réponse ; le MJ lance ses jets avec `--cache` si besoin. La fuite et la parole sont toujours des options.

## Quand lancer les dés
- **Pas de jet** si l'action est simple pour le personnage dans la situation, ou si l'échec ne changerait rien. On ne lance que quand il y a un vrai doute **et** un enjeu.
- Un seul jet par enjeu : pas de chaîne de jets pour une même action.
- Un échec fait avancer l'histoire (complication, prix), il ne la bloque pas.
- Dégâts : `python3 des.py 1d4` (poing), `1d6` (couteau, chute de 3 m), `1d10` (arme lourde).

## Monnaie et ressources
_(À définir par le monde : le skill `creer-scenario` les écrit ici.)_

## Règles maison (connues du joueur)
_(Vide au départ. Chaque arc y ajoute ses mécaniques propres : ressources, lieux à règles particulières, etc.)_
