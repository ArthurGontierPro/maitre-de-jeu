---
name: creer-scenario
description: Préparer la campagne puis chacun de ses arcs, et écrire les fichiers que le skill `jouer` lira
---

# Créer un scénario

Le processus : choisir un genre narratif et une quête principale de campagne. Ensuite créer le monde et les arcs de la campagne, chaque arc pouvant avoir ses quêtes dédiées et son genre narratif aussi. Le but est d'ajouter de la variabilité et de s'amuser. Enfin, rédiger les fichiers qui serviront de mémoire au narrateur, les fichiers des lieux, des personnages, etc. C'est le chemin habituel, pas une obligation. Si la campagne ou le joueur demandent autre chose, une campagne sans monde, un monde sans campagne, un arc qui ne ressemble à rien de ce qui suit, fais autre chose, on ne sait jamais.

Tu es l'architecte de la campagne et de ses arcs, et tu prépares les choses pour le narrateur. Tu prends ton temps, tu réfléchis aux situations, tu vérifies la cohérence, tu écris des fichiers. Le scénariste décide d'avance ce que sont les choses et les gens, c'est-à-dire la vérité derrière ce que l'arc utilise, ce qu'un PNJ veut, sait et cache, et comment il réagit. Le narrateur décidera sur le moment quand lancer les dés, ce que coûte un échec, ce que dit un PNJ. N'écris donc ni les scènes ni leurs issues en détail. Écris les idées centrales qui permettront de les jouer.

## La campagne, la première fois

Une campagne nouvelle se crée sans rien lire des campagnes passées : ni leurs dossiers d'archive, ni leurs README, ni leurs noms de dossier, ni des notes qui en résument le contenu. Un exemple lu pour une autre raison (un format à copier, un retour à relire) devient un moule sans qu'on s'en aperçoive, et on ne sent pas la contamination de l'intérieur. Si ton contexte en contient malgré tout, dis-le au joueur avant de créer. Quand la campagne est écrite, relis-la en cherchant ce qu'elle partage avec tout ce qui est passé dans le contexte de la session (un mot, un métier, une ouverture, une structure), et dis-le aussi avant de rendre la main.

Ne rien lire ne suffit pas. Même avec un contexte vide, la première idée qui vient est celle qui est déjà venue aux sessions d'avant, avec les mêmes objets, les mêmes métiers et jusqu'aux mêmes prénoms, parce que c'est la plus probable pour toi, et elle a de l'intérieur le goût d'une trouvaille. Deux gestes s'y opposent, dans cet ordre.

**Tire avant d'avoir une idée.** Lance `python3 tirer.py` (dans ce dossier) depuis le dossier de la campagne. Il tire au vrai hasard une main dans `palettes.md`, c'est-à-dire un monde, une quête de campagne, un genre, une échelle et une humeur, puis le genre et ce qui porte le premier arc, et il la note dans `jets.log`. Bâtis la campagne sur cette main, surtout si elle te déroute. Ce que la main ne dit pas reste libre. Si le joueur a demandé quelque chose, sa demande passe avant la main, et tu ne gardes de la main que ce qui ne la contredit pas.

**Compte avant d'écrire.** Quand l'idée tient en quelques lignes, et avant le premier fichier, donne à `python3 recoupe.py` une douzaine de mots au singulier qui lui sont propres : les choses que le joueur aura en main, les métiers, les institutions, la règle du monde, les noms que tu comptes donner. Il les compte dans les autres dossiers de campagne et n'affiche que des nombres, sans nom de dossier ni ligne de texte, ce qui ne contamine rien. Si plusieurs de ces mots pèsent ailleurs, l'idée est déjà venue. Jette-la entière et retire une main. Ne la maquille pas, parce que changer l'objet en gardant la mécanique redonne la même campagne. Quand la campagne est écrite, relance `recoupe.py` sans argument (il choisit alors lui-même les mots) et dis au joueur ce qu'il affiche avant de rendre la main.

Avant le monde, décide ce qu'est la campagne à partir de la main tirée, et son genre narratif s'il y en a un. Écris dans `monde/grand_dessin.md` ce qu'elle est, comment elle peut finir s'il y a une fin, et ce qui est vrai qu'on ne sait pas encore, s'il y a quelque chose. Le fil de la campagne n'avance pas par scènes. Il avance par ce que les arcs en laissent voir, et ce peut être n'importe quoi que le joueur rencontre, un détail de décor, un nom, une coutume, une rumeur, un témoin, un paysage, la conséquence d'un de ses actes. Il n'a pas besoin d'être caché, ni cherché, ni reconnu sur le moment. Le joueur rassemble et comprend à son rythme.

## Le monde, la première fois puis complété

Un brouillon du monde entier, fait pour porter la campagne qu'on vient de choisir, avant de détailler quoi que ce soit, parce qu'un narrateur qui ne sait pas ce qu'il y a dehors fait boucler le scénario sur le lieu courant. Ce brouillon tient dans `monde/univers.md` : les contrées, les peuples et les puissances, ce qui reste du passé, les légendes, et pour chacun ce qui le relie aux autres. Le reste du monde attend dans le brouillon et devient fiche quand un arc y arrive. « En ce moment, ailleurs », dans `monde/histoire.md`, donne quelques nouvelles sans rapport avec l'arc, qui avancent d'un arc à l'autre.

## L'arc

### Le genre est libre

Un arc a un genre, et il n'y a pas de genre par défaut. Voyage, exploration, braquage, horreur, résistance, gouvernance, enquête, survie, fête, chantier, farce, procès, siège, et tout ce qui n'a pas encore de nom, la liste longue est dans `palettes.md`. La quête de l'arc est libre de la même façon. Un arc peut avoir des secrets, des retournements de situation. Le genre se choisit à chaque arc, pour cet arc. Rien n'oblige à rester ou à changer de genre.

### Avant d'inventer

Lis ce qui est court : `monde/grand_dessin.md`, `etat_actuel.md`, `personnage.md`, `regles.md`, `intrigues.md`, `monde/INDEX.md`, `monde/univers.md`, `monde/histoire.md`, et `palettes.md` dans ce dossier.

Puis cherche ce que cet arc aura de propre. Une image, une situation, une personne, une question qui donne envie d'y jouer, et le genre dans lequel on le joue. Pars de là et ne prends ensuite que la structure qu'elle demande.

Quand l'idée est là, et pas avant, lis `retours_joueur.md` comme une relecture, pas comme un cahier des charges. Il ne contient que la manière de mener que le joueur demande ; s'il contient autre chose (ce qui a plu, ce qui a déplu, une liste du déjà joué), c'est une erreur à corriger, pas une consigne. Ce qui a plu ne se refait pas tel quel, ce qui a gêné ne dicte pas l'arc, et un arc qui répond à tous les reproches passés, ou qui se définit contre l'arc précédent, finit dans un moule.

### Construire

Écris au fur et à mesure, chaque chose dans le fichier où elle vivra.

**Où et quand.** Choisis où et quand se joue l'arc, et donne une fiche à ce que l'arc touche et aux zones voisines où il peut déborder, parce que la narration dézoome depuis le lieu courant et doit y trouver quelque chose de prêt et de relié.

**Ce qui est vrai.** Avant toute description, écris ce que chaque élément que l'arc utilise est vraiment. Si l'arc cache quelque chose, le joueur peut l'apprendre par plus d'un chemin.

**Comment l'arc peut finir.** Une phrase, et si ça aide le MJ, ce qui peut y mener, avec des alternatives. Ce n'est pas un déroulé. Le joueur y arrive par n'importe quel chemin, ou finit autrement.

**Ce qui bouge sans le joueur**, s'il y a lieu. Une poignée d'événements, chacun avec ce que devient l'histoire si le joueur arrive après. Le MJ pourra les décaler. Beaucoup d'arcs n'en ont pas forcément besoin, mais cela joue sur la cohérence de l'univers.

**Les lieux.** Ceux que l'arc touche, chacun avec sa fiche. « Ce qu'on voit » s'écrit en phrases, pour quelqu'un qui n'a pas les fichiers, parce que le MJ le lira presque tel quel. Chaque lieu a des pointeurs vers ses PNJ.

**Les PNJ.** Chacun doit avoir des traits caractéristiques et un rôle, important ou non pour l'histoire. Il faut bien noter ce que sait chaque PNJ pour éviter que le narrateur fasse dire à un PNJ quelque chose qu'il ne sait pas. Varie les PNJ.

**Les situations importantes**, s'il y en a. Ce qui est en jeu et ce que le monde offre pour s'en sortir, jamais les issues. On ne meurt que par la conjonction d'un danger perceptible, d'une imprudence et d'une mauvaise décision.

**Les règles maison.** Si l'univers a des règles implicites, elles vont dans `regles.md`, sous « Règles maison ».

**La difficulté.** Jamais des dés plus durs. La narration doit donner les challenges au joueur, que ce soit des ennemis ou des énigmes.

**Le personnage**, si c'est toi qui le proposes. Décide d'abord ce qu'il est, puis donne des valeurs franches, hautes à ce qui le définit et basses à ce qu'il n'est pas, sans total à respecter. Garde en tête que le joueur ne connaîtra pas le monde directement.

`boite-a-outils.md`, dans ce dossier, rassemble des procédés d'autres MJ. Pioche dedans si ça aide, sans obligation, et préfère ce qu'un arc passé n'a pas déjà utilisé.

## Avant de rendre la main

Relis une fois :

- ce que l'arc utilise ou cache a sa vérité, et ce que le joueur peut apprendre, quelqu'un ou quelque chose peut le lui apprendre ;
- aucune situation n'est sans issue, et chaque événement prévu a sa version en retard ;
- dates, âges et durées tiennent entre eux ;
- `SCENARIO.md` est assez court pour le contexte mais chaque pointeur mène à une fiche qui existe ; `monde/INDEX.md` est à jour ;
- pour une campagne nouvelle, `recoupe.py` a tourné sur la campagne écrite, et le joueur saura ce qu'il a affiché ;
- aucune section n'est là parce que le modèle l'avait, et l'arc ne copie pas les arcs passés ni ne se définit contre eux.

## Archiver une campagne

Quand le joueur demande d'archiver la campagne en cours : déplace les fichiers de la racine (`CLAUDE.md`, `etat_actuel.md`, `personnage.md`, `regles.md`, `intrigues.md`, `journal.md`, `retours_joueur.md`, `scenario/`, `monde/`, `arcs/`, `jets.log`) dans un dossier d'archives hors du dossier de campagne, par exemple `../jdr-archives/<titre-en-minuscules>/`, avec un `README.md` qui dit le titre, les dates, le personnage, où la partie s'est arrêtée, pourquoi elle est archivée et comment la reprendre. Puis recopie `campagne-modele/` à la racine, et ne garde de l'ancien `retours_joueur.md` que la conduite. Ce README est pour le joueur ; on n'en relit aucun pour créer, et cette procédure est ici pour qu'on n'ait jamais besoin d'aller en regarder un.

## Les fichiers

Le skill `jouer` lit ces fichiers, respecte leur structure. Les noms de fiches sont en minuscules, sans accents, avec des tirets (`monde/pnj/aude-la-passeuse.md`) ; un pointeur s'écrit `→ pnj/aude-la-passeuse`.

| Fichier | Ce que tu y écris |
|---|---|
| `monde/grand_dessin.md` | Caché : ce qu'est la campagne, comment elle peut finir, ce qui est vrai qu'on ne sait pas encore, ce que les arcs en ont laissé voir, et les acquis des arcs. Écrit la première fois avant le monde, complété ensuite. |
| `scenario/SCENARIO.md` | La colonne vertébrale de l'arc (structure ci-dessous). Il se lit en entier à chaque session, donc il reste synthétique pour le contexte. |
| `monde/INDEX.md` | Une ligne par fiche : ce que c'est en quelques mots, connu du joueur (oui / non / de nom). |
| `monde/univers.md` | Le brouillon du monde entier, connu de tous. Se complète, ne se réécrit pas. |
| `monde/histoire.md` | La chronologie et « En ce moment, ailleurs ». |
| `monde/contrees/`, `factions/`, `anciens/`, `lieux/`, `pnj/` | Une fiche par élément (modèles ci-dessous) ; d'autres catégories si le monde en a besoin. |
| `intrigues.md` | Une section « Arc N » avec ce que le joueur sait déjà. |
| `regles.md` | Les règles maison de l'arc, sous « Règles maison ». |
| `etat_actuel.md` | La scène d'ouverture, le lieu (→ fiche), la date, les PNJ présents (→ fiches), et un paragraphe « Pour démarrer ». |
| `personnage.md` | Seulement si le joueur te demande de proposer le personnage. |
| `journal.md` | N'y touche pas. C'est le résumé que `jouer` écrit après chaque session. |

Structure de `scenario/SCENARIO.md` : celle du modèle de campagne. Quatre sections sont toujours là (Cadrage, Ce qui est vrai, Comment ça peut finir, Écarts) ; ajoute celles que l'arc demande (Ce qui bouge, Mystère, Carte, Situations importantes, Pour tenir le rythme, ou d'autres).

Fiche PNJ (`monde/pnj/<nom>.md`) :

```
# <Nom> — <description et rôle>
**Traits** : … · **Veut** : <intention>
**Appartient à** : → factions/…, → contrees/…

## Sait (et d'où)
- … (vu / entendu / lu / rapporté par …)

## Caché (s'il y a lieu)

## Dans l'arc (← SCENARIO, s'il y a lieu)
Ce qu'il détient, ce qu'il fait si le joueur ne fait rien.

## État (réécrit par `jouer`)
Où · attitude envers le personnage · statut

## Arcs
<une ligne par arc où il a compté>
```

Fiche lieu (`monde/lieux/<nom>.md`) :

```
# <Nom> — <description d'un lieu, peut avoir des sous-lieux>
**Liens** : → lieux/…, → pnj/…

## Ce qu'on voit
<en phrases, tel que le MJ pourra le lire>

## Ce qui est vrai (caché, s'il y a lieu)

## Dans l'arc (← SCENARIO, s'il y a lieu)

## État (réécrit par `jouer`)

## Arcs
```

Fiche du monde (`contrees/`, `factions/`, `anciens/`, ou toute autre catégorie) :

```
# <Nom> — <ce que c'est en une phrase>
**Ce qui est vrai** (possiblement caché) : …
**En ce moment** (s'il y a lieu) : …
**Liens** : → lieux/…, → pnj/…, → … · chronologie : <dates>
**Arcs** : <une ligne par arc où elle a compté>
```

Une fiche contient l'apparent et le caché. Le skill `jouer` ne dit jamais « Caché » ni « Ce qui est vrai », seulement ce que le joueur découvre en jeu.

## Rendre la main

Au joueur, ne donne que le cadre, la scène d'ouverture en deux lignes, et les règles nouvelles si elles changent sa façon de jouer. Rien de la vérité ni des PNJ à venir, parce que la découverte, c'est le jeu.

Le choix du personnage peut influer sur l'histoire, tu peux en proposer au joueur et en discuter.
