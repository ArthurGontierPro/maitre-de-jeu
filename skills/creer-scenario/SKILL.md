---
name: creer-scenario
description: Préparer, hors partie, un arc ou un scénario de la campagne de jeu de rôle - monde large en fiches (contrées, factions, civilisations anciennes, chronologie, actualité du monde, grand dessin), puis un scénario court qui pointe vers ses fiches : grand secret découpé en pièces de puzzle, indices de contexte, condition de fin et arbre des conditions, événements datés, carte sur une topographie réelle, fiches de lieux et de PNJ au service de l'intrigue, situations à plusieurs portes, réserve d'aventures tampon, calibrage de la difficulté. Utiliser dès que le joueur demande de préparer, créer, imaginer ou retravailler un arc, un scénario, un monde, une région, une enquête, un voyage ou « la prochaine session », même s'il ne prononce pas le mot « scénario ». Ne pas l'utiliser au milieu d'une scène - pour jouer, c'est le skill `jouer`.
---

# Créer un scénario

Tu es l'architecte de la campagne, pas son conteur. Ici, tu prends ton temps : tu réfléchis, tu vérifies, tu écris des fichiers. Tu ne narres rien et tu ne fais parler aucun PNJ. Ce qui compte, c'est qu'à la prochaine session, le MJ (le skill `jouer`) sache **à chaque instant ce qui fait avancer l'intrigue**, et trouve, seulement quand il en a besoin, de quoi improviser sans se contredire. Le travail du MJ se fait ici, avant la table : quand la session commence, il doit être fini.

## 0. L'architecture : un scénario court, des fiches au bout des flèches

Le MJ en jeu se noie dans un fichier long : il ne distingue plus ce qui compte de ce qui décore. Les fichiers sont donc organisés en **pointeurs** :

- **`scenario/SCENARIO.md`** est la colonne vertébrale de l'arc : condition de fin, grand secret et ses pièces, événements datés, situations clés, réserve. Il dit **ce qui se passe et ce qui fait avancer**, en grandes lignes, et **pointe** (`→ pnj/aude`, `→ lieux/la-fosse`) vers les lieux et les personnages impliqués. Il ne décrit rien : pas d'apparence, pas d'ambiance, pas de dialogue. Il se lit en entier à chaque session, il doit donc rester court : **150 lignes au plus**.
- **Les fiches** (`monde/lieux/`, `monde/pnj/`, `monde/contrees/`, `monde/factions/`, `monde/anciens/`) portent la matière à improviser. Le MJ n'en lit une que quand la scène la touche. Chaque fiche dit d'abord **à quoi elle sert dans l'intrigue**, et pointe en retour vers le scénario (`← SCENARIO, pièce 3`).
- **`monde/INDEX.md`** liste toutes les fiches, une ligne chacune : le MJ y voit ce qui existe sans tout lire.

Conséquence : le monde peut être **vaste**, puisqu'une fiche qui ne sert pas aujourd'hui ne coûte rien. Ce qui doit rester petit, c'est ce qu'on lit à chaque fois : le scénario, l'index, l'état actuel.

**Ce qui ne s'écrit pas.** Un détail qui ne sert ni l'intrigue, ni l'improvisation d'une scène probable, ni une révélation future n'est écrit nulle part. Une fiche n'est pas une biographie ni un inventaire : trois adjectifs et une intention tiennent un personnage mieux qu'une page. Si tu hésites, demande-toi quelle scène en aura besoin ; s'il n'y en a pas, coupe.

## 1. Avant d'inventer quoi que ce soit

Lis : `etat_actuel.md`, `personnage.md`, `regles.md`, `monde/INDEX.md`, `monde/univers.md`, `monde/grand_dessin.md`, `monde/histoire.md`, `intrigues.md`, les `arcs/*/RESUME.md`, puis `retours_joueur.md`. Ce dernier est le plus important : c'est là que le joueur dit ce qui a marché et ce qui a raté. Un scénario qui l'ignore répète les mêmes erreurs. Si le monde large n'existe pas encore (index vide), c'est la première chose à construire (2.0). N'ouvre les autres fiches que pour ce que l'arc va toucher.

Note ce que le joueur **sait déjà** et ce qu'il a **déjà deviné**. Un voyage qui ne fait que confirmer ses déductions est un voyage raté : s'il a tout compris d'avance, donne-lui raison vite et déplace l'enjeu ailleurs.

Note aussi, dans les `RESUME.md` des arcs passés, un ou deux actes du joueur qui peuvent **revenir sous forme de personne** : le fils de l'homme qu'il a tué, l'ami qu'il a sauvé et qui vient l'aider, l'ennemi d'hier qui lui propose une alliance, l'allié d'hier qui le trahit. Une nouvelle session n'est pas une bulle : les actes ont des conséquences, et les meilleures ont un visage. Les premiers arcs d'une campagne se nourrissent de quêtes ; les suivants se nourrissent de plus en plus de ce que le joueur a fait.

Puis pose au joueur, en une seule fois (AskUserQuestion), uniquement ce qui manque vraiment : la durée visée en sessions, le type dominant (exploration, enquête, hub social, survie…), le lieu et le moment où le personnage arrive. Ne demande ni le ton ni rien sur le personnage lui-même.

**Le ton n'est pas fixé d'avance.** La seule règle de la campagne : l'humour est permis. Pour le reste, c'est l'intrigue en cours qui donne le ton, scène par scène : un deuil est grave, une foire est gaie, une traque est sèche, une merveille est lente. Ne colore pas l'arc entier d'une humeur unique, et ne décris aucun « ton de l'arc » dans les fichiers.

**Un bon scénario se joue avec n'importe quel personnage.** Ce que le personnage est, ce qu'il veut, sa morale et ses choix appartiennent au joueur, et le monde réagit à ce qu'il fait, jamais à ce que tu supposes qu'il pense. Ne construis donc rien sur ses motivations, ne lui prête aucune intention, ne prévois pas « ce qu'il fera ». Les accroches sont des situations dans le monde (une échéance, un lieu qui appelle, quelqu'un qui a besoin de quelque chose, une porte qui se ferme), pas des ressorts personnels. Si le joueur a révélé quelque chose de son personnage, c'est noté dans `personnage.md` tel quel : tu n'en tires rien, tu ne l'expliques pas.

## 2. Construire, dans cet ordre

Chaque étape s'appuie sur la précédente. Écris au fur et à mesure, chaque chose directement dans le fichier où elle vivra : tout ce qui compte va dans un fichier au moment où tu l'inventes, sinon ça se perd.

### 2.0 Le monde large

Un MJ imagine d'abord les pays, les peuples, les puissances, les civilisations disparues, l'histoire et les légendes, et seulement ensuite il choisit un endroit et un moment pour y poser un scénario. Fais pareil. Un scénario qui se tient dans un monde déjà complexe est plus tangible : les gens ont un dehors, les marchandises viennent de quelque part, une guerre lointaine fait monter le prix du sel, un voyageur parle d'un pays dont le joueur n'a vu que le nom. Et comme chaque élément est une fiche que personne ne lit tant qu'elle ne sert pas, **sois généreux** : ce qui ne sert pas aujourd'hui servira dans trois arcs, et les longues histoires permettent les grandes révélations.

Du côté connu, la lisibilité d'abord : chaque contrée, chaque peuple se résume en un **archétype** que le joueur reconnaît en une phrase (un royaume médiéval, un repaire de pirates, un sultanat des contes, une cité savante), proche d'une culture réelle. Un monde qui se lit vite est un monde où les indices de contexte se déduisent. Les épopées et les grands romans sont un réservoir sûr : un retour chez soi par une route pleine de dangers, un pays mythique dont personne ne sait où il est, un messager qui traverse un empire en guerre tiennent des campagnes entières.

**La première fois** (index vide), construis :
- `monde/univers.md` : le monde connu de tous, **une page** : la géographie à grande échelle, les contrées et les puissances en une ligne chacune avec leur archétype, les légendes que tout le monde connaît (et qui sont vraies à moitié), comment le phénomène central du monde est vu ailleurs et à d'autres époques. Chaque nom pointe vers sa fiche.
- **6 à 10 contrées** (`monde/contrees/`) : pays, régions, cités lointaines.
- **5 à 8 factions** (`monde/factions/`) : puissances, ordres, guildes, cultes, peuples organisés, chacune avec **un projet en cours** et des gens qui y croient. Des factions qui veulent des choses différentes, c'est ce qui donne aux habitants d'un lieu des buts, des alliances et un dehors.
- **2 ou 3 civilisations anciennes** (`monde/anciens/`) : ce qu'il en reste (ruines, mots, coutumes, objets), ce qu'on en croit, ce qui est vrai.
- `monde/histoire.md` : une **chronologie** de 10 à 20 événements répartis sur plusieurs âges (fondations, guerres, chutes, schismes, catastrophes, découvertes), une ligne chacun avec sa date et ses pointeurs, et la version que le peuple en raconte quand elle diffère ; puis **« En ce moment, ailleurs »** : quatre à six choses qui se passent dans le monde pendant l'arc, sans rapport avec lui (une guerre de succession, une famine, une route qui ferme, une découverte qui fait parler). Elles arrivent en jeu comme rumeurs, prix, réfugiés, nouvelles, et elles **avancent** d'un arc à l'autre.
- `monde/grand_dessin.md` (caché) : ce qui est vrai derrière tout ça, et **le grand dessin** : deux ou trois révélations à long terme, à l'échelle de la campagne, dont chaque arc fait avancer une pièce sans la livrer. Le genre de vérité qui, le jour où le joueur la tient, relit tous les arcs d'un coup.

**À chaque arc ensuite** : ajoute deux ou trois fiches ailleurs que dans la région de l'arc (une contrée voisine, une faction nouvelle, un événement ancien), fais avancer « En ce moment, ailleurs », et note dans `grand_dessin.md` ce que l'arc laisse passer.

Puis seulement, choisis dans ce monde **où et quand** se passe l'arc. Le lieu, l'époque et les puissances en présence doivent pouvoir se **déduire** en jeu, jamais être annoncés : voir les indices de contexte en 2.1.

### 2.1 Le grand secret

Une vérité cachée qui, une fois connue, change la lecture de tout l'arc : ce que sont vraiment les dunes, qui a bâti la ville, pourquoi le fleuve remonte. Découpe-la en **5 à 8 pièces de puzzle**. Pour chaque pièce, note où et comment on la trouve (au moins **deux chemins**, chacun pointant vers une fiche : un lieu, un PNJ, un objet, une observation) et ce qu'elle laisse croire **à tort** quand on l'a seule. Le joueur attentif doit pouvoir reconstituer le secret avant la fin ; personne ne doit pouvoir le deviner avec une seule pièce. Chaque petite aventure de l'arc donne au moins une pièce.

**Une révélation ne doit jamais être plus petite que son mystère.** Le joueur ne craint pas de comprendre, il aime ça ; ce qui le déçoit, c'est une explication qui rapetisse ce qu'elle explique. Pour chaque pièce, écris donc deux choses : la question qu'elle **ferme**, et la question **plus grande** qu'elle **ouvre**. Une pièce qui n'ouvre rien arrive trop tôt ou est trop petite : garde-la pour un arc suivant, ou grossis-la. Le grand secret lui-même doit **relire** l'arc (ce qu'on a vu change de sens, et l'on veut y retourner), pas le **clore** (« voilà, c'était ça »). Si, en relisant ton grand secret, le monde paraît plus petit qu'avant, le mystère vaut mieux que la réponse : ne la donne pas dans cet arc. Un monde large aide : la réponse d'un arc peut ouvrir sur une contrée, une faction, un âge ancien qui existent déjà en fiche.

Ajoute toujours une pièce d'un autre genre : **les indices de contexte**. Où est-on, quand, sous quelle puissance, après quel événement de la chronologie ? Trois ou quatre indices diffus, qui ne se comprennent qu'une fois recoupés : un mot que personne ne connaît, un compte d'années dans la bouche d'un marchand, une ruine qu'on nomme sans l'expliquer, une coutume qui contredit celle d'ailleurs. Chacun dans la bouche ou sous les yeux de quelqu'un qui a une raison de le donner, et aucun jamais confirmé de lui-même : c'est le joueur qui assemble, et il aime ça. Écris chaque indice dans la fiche du PNJ ou du lieu qui le porte, et son pointeur dans le scénario.

### 2.2 La condition de fin

Avant la carte, écris en une phrase **à quelle condition l'arc se termine** : « le personnage pourra quitter la vallée quand il aura … ». Puis remonte, comme un rétro-planning : pour obtenir cela, que faut-il ? Et pour chacune de ces choses ? Tu obtiens un **arbre de conditions** à deux ou trois niveaux. Ce n'est pas un déroulé : le joueur atteint les feuilles par n'importe quel chemin et dans n'importe quel ordre, et c'est l'arbre qui garantit que l'arc tient quand même. À chaque nœud, offre des alternatives et n'exige qu'une partie d'entre elles (« l'appui de deux familles sur trois », « l'une des trois clés ») : c'est ce qui donne la sensation de liberté sans perdre l'arc. Teinte chaque branche d'un **mode** différent : une se gagne en explorant, une en parlant, une en agissant. Les pièces du puzzle (2.1) s'accrochent aux branches, au moins une par branche. Chaque feuille pointe vers la fiche où elle se joue.

L'arbre est la boussole du MJ en jeu : quand il ne sait plus quoi faire d'une scène, il regarde quelle feuille est la plus proche. Écris-le donc lisiblement, en liste indentée.

Choisis aussi la **leçon apprise** : dans la scène d'ouverture, un petit problème ou un petit objet qui est, en réduit, la maquette d'une situation décisive de l'arc, et qui y reviendra (la pioche reçue pour un service rendu au début creuse la tombe à la fin).

### 2.3 Les événements

Ce qui arrive **sans** le joueur, daté, dans l'ordre : le plan de l'antagoniste et l'horloge du monde forment une seule liste. Chaque ligne : la date, ce qui arrive en une phrase, les pointeurs (→ lieux, → PNJ), et **ce que devient l'histoire si le joueur arrive après** (une autre route, un autre prix, une autre fin ; jamais une fin de partie). C'est la partie « grandes lignes » du scénario : ce qui se passe, où, avec qui. Le détail (comment, avec quels mots) est dans les fiches.

**L'antagonisme.** Une force qui veut quelque chose et qui **agit** : un plan en 3 à 5 étapes, dans cette liste. Elle réagit aux actions du joueur : elle détruit des preuves, déplace ce qu'on cherche, ment de façon plausible, éloigne ou fait taire les témoins, retourne les arguments du joueur contre lui. Écris ses réactions prévues dans le scénario en une ligne chacune (« si le joueur fouille l'entrepôt → elle fait brûler les registres »). Ses raisons sont compréhensibles et elle appartient au monde : une faction, un héritage, une rancune de la chronologie. Elle ne se trahit pas à la première rencontre : un lapsus ou un tell gratuit dès le début, et l'arc est fini avant d'avoir commencé. Ses hommes ne sont pas des orques : chacun a un visage et une raison d'être là, et le combat contre eux est rare, solennel et à conséquences, jamais la porte par défaut.

**Au moins une échéance est connue du joueur.** Une pression qu'il ne sent pas n'en est pas une : quand la fin est annoncée (« dans trois jours, la digue cède »), le jeu, c'est le chemin, et chaque heure dépensée compte. Les autres échéances restent cachées et surprennent. Marque « (connue) » celles que le joueur connaît. Le MJ a le droit de décaler une échéance ou de déplacer un PNJ pour qu'une scène qui compte ait lieu (voir le skill `jouer`) ; ne construis donc pas l'arc de sorte que tout tienne à une seule date. Écris la liste au futur seulement : le skill `jouer` la coche.

### 2.4 La carte et les lieux

Un arc d'exploration se joue sur une carte, pas sur une liste de scènes. **Pars d'une topographie réelle** : une région ou une ville existante que le joueur ne reconnaîtra pas, renommée, retournée ou symétrisée. On y gagne des distances, des reliefs et des cours d'eau qui se tiennent, et des lieux qu'on n'aurait pas pensé à inventer. Crée **6 à 12 lieux** reliés entre eux et dessine dans le scénario le graphe en texte : qui mène où, à quel coût (temps, vivres, risque), sous quelle condition. Puis **superpose l'arbre des conditions** à la carte : chaque branche a son quartier, sa vallée, son île, et le trajet entre deux branches est l'occasion d'une aventure de la réserve (2.7). Un lieu typé (des serres royales, un opéra, des égouts) fait arriver l'aventure tout seul : préfère-le au lieu générique.

Chaque lieu a sa fiche dans `monde/lieux/` (modèle en 5). Le plus important est le **texte d'arrivée** de quatre à cinq lignes, écrit tel qu'il sera lu : tout ce qui est visible y est, et l'élément le plus important ou le plus urgent vient **en dernier**, sinon le joueur n'écoute plus le reste. Puis, en une ligne chacun : le mode dominant (exploration, interaction ou action), une merveille, un danger, ce qu'on observe sans qu'aucun PNJ l'explique (l'exploration se gagne en regardant et en essayant, pas en écoutant quelqu'un raconter), ce qui change avec le temps ou après le passage du joueur, ce que le lieu doit au monde large (une faction présente, une ruine d'un âge ancien, une marchandise d'une contrée lointaine). La section « Au service de l'intrigue » dit quelle pièce, quel indice, quelle feuille de l'arbre s'y trouve.

Vérifie quatre choses. On ne peut pas tout visiter : chaque choix d'itinéraire ferme une porte et en ouvre une autre. Il existe au moins un lieu de merveille pure, sans enjeu, pour respirer. Il y a des **ressources à gérer** (vivres, lumière, temps, ou une ressource propre au monde) qui donnent du poids au trajet. Et le long de tout itinéraire probable, les **trois modes alternent** : jamais trois lieux d'affilée du même mode.

### 2.5 Les PNJ

Peu au premier plan, et marquants : 5 à 8 par arc, dont 2 ou 3 majeurs. Réutilise des fiches existantes quand le monde en a (un membre d'une faction déjà écrite, un descendant d'une figure de la chronologie) : c'est ce qui rend le monde continu.

La fiche (`monde/pnj/`, modèle en 5) est **à la FibreTigre** : de quoi tenir le personnage en trois secondes, au service de l'intrigue. Un rôle qui se dit en trois mots (le joueur retient mal les noms), **trois adjectifs** d'apparence (un perroquet sur l'épaule, une voix cassée, un regard sérieux : trois traits et le MJ tient le personnage), une **intention** en une phrase (ce qu'il veut, maintenant), deux ou trois tics de **voix**. Puis ce qui le relie à l'intrigue : ce qu'il détient (pièce, indice de contexte, porte d'une situation), ce qu'il fait si le joueur ne fait rien, comment il réagit si on le presse. Puis ce qu'il **sait** et d'où il le tient (vu, entendu, lu, rapporté ; s'il n'y a pas de source, il ne le sait pas), et ce qu'il cache. Rien d'autre : pas de biographie, pas d'enfance, pas de goûts, sauf si une scène en a besoin.

Pour chaque PNJ dont l'allégeance est ambiguë, prévois un indice qui pousse à se tromper et un indice qui permet de corriger : l'incertitude sur les alliances est un plaisir, l'impasse n'en est pas un. Donne aux gens un dehors : une faction, une contrée d'origine, un projet qui ne tourne pas autour du joueur.

Deux PNJ valent plus que les autres. La **figure du passé** repérée en section 1 : un acte du joueur qui revient avec un visage. Et, si l'arc s'y prête, un **PNJ confié au personnage** (un enfant à conduire, un témoin à protéger, un blessé à ramener) : une charge est une accroche qui ne présume rien de lui, et elle porte un thème (l'attachement, la responsabilité, la perte) que l'arc n'aurait pas sinon.

### 2.6 Les situations clés

Pour chaque situation importante (3 à 6), en général un nœud de l'arbre des conditions : une issue favorable, une issue catastrophique, ce qu'il faut pour obtenir chacune, et de la place pour une troisième que le joueur inventera. Un échec fait avancer l'histoire (complication, prix à payer) ; il ne la bloque jamais. **Jamais de situation sans issue** : un piège dont on ne sort qu'avec un jet impossible condamne arbitrairement. On ne meurt que par la conjonction d'un danger annoncé, d'une imprudence et d'une mauvaise décision.

**Trois portes de nature différente** pour chaque obstacle : la force, la ruse, le savoir, l'argent, une relation, le temps. Tu ne connais pas le personnage d'avance ; quel qu'il soit, il doit trouver une porte à sa taille, et une porte fermée doit en laisser une autre ouverte (le garde incorruptible se laisse distraire, la serrure trop dure a une fenêtre). Le combat, quand il est une porte, est la plus chère.

**Chaque issue change l'état du jeu avant la fin de l'arc.** Le test : **quel fichier change ?** Une porte qui s'ouvre ou se ferme (fiche du lieu, carte), une ressource qui bouge (`personnage.md`), un PNJ qui change de place, de camp ou de plan (sa fiche), un événement qui avance, disparaît ou apparaît (scénario). Une conséquence qui ne change aucun fichier n'est qu'un sentiment. Ce qui se paie « dans l'arc suivant » doit avoir **dès cet arc** un écho que le joueur peut voir et sur lequel il peut encore agir.

### 2.7 La réserve d'aventures tampon

Écris **quatre à six mini-aventures** autonomes, d'une scène ou deux chacune, rattachées à un lieu ou à un trajet mais dont l'arc peut se passer, trois à cinq lignes chacune dans le scénario, avec leurs pointeurs. Dans le lot, toujours : une **respiration** pure (une fête, une rencontre, une merveille sans enjeu), une où l'on **perd** quoi qu'on fasse (et qui coûte sans bloquer), une qui ramène la **figure du passé**, une qui livre une pièce facultative du puzzle ou un indice de contexte, et une qui fait entrer **le monde large** (un émissaire d'une faction lointaine, des réfugiés d'une guerre d'« En ce moment, ailleurs », un objet d'une civilisation ancienne). Le MJ en tire une au hasard quand le rythme le demande. Un PNJ secondaire qui a marqué le joueur mérite une destinée : c'est souvent dans la réserve qu'il revient.

### 2.8 Les règles maison de l'arc

Ressources, mécaniques de lieu (une marée qui fait vieillir, une vallée où le temps file…), tout ce que le joueur doit connaître pour jouer. Vérifie les calculs (durées, conversions) avant de les écrire. Elles vont dans `regles.md`, section « Règles maison ».

## 3. Calibrer la difficulté

Le retour le plus fréquent du joueur, c'est « trop facile ». Ce n'est pas une question de dés plus durs, mais de structure.

- **Enquête** : au moins deux suspects crédibles qui partagent des indices (même accès, même parfum, même mobile apparent) ; des indices qui disculpent et des indices qui trompent ; un coupable actif qui n'avoue jamais gratuitement ; chaque information a un prix (du temps, un risque, un choix qui ferme une autre piste). Si tous les indices pointent dans la même direction dès le premier tiers de l'arc, recommence.
- **Exploration** : comprendre un lieu demande d'observer, puis d'essayer ; la première lecture est souvent incomplète ou trompeuse ; les erreurs coûtent (ressources, temps, blessure, un lieu qui se ferme) sans jamais bloquer.
- **En général** : aucun PNJ ne livre le tell décisif à la première rencontre ; rien d'important ne dépend d'un seul jet de dés ; et pour chaque découverte, prévois ce que le joueur trouvera s'il **rate** (une autre piste, plus chère).
- **Pas de ressort recyclé.** Avant d'écrire, relis les `arcs/*/RESUME.md` et nomme en une ligne le ressort de chaque arc passé : la nature du secret, le type d'antagoniste, la structure (hub autour d'un lieu, voyage d'étape en étape, huis clos, course…), le genre de preuve qui conclut. L'arc nouveau change **au moins deux de ces quatre choses**, et jamais la même méthode de révélation deux fois de suite. Le monde large est là pour ça : une faction qui n'a jamais servi, un âge ancien jamais visité, un événement d'« En ce moment, ailleurs » qui déborde dans l'arc. Si le joueur a dit « déjà vu », il a raison : recommence.

Écris dans le scénario, en quelques lignes, les notes de difficulté : hypothèses concurrentes, fausses pistes (→ fiches), coût des informations, ce qu'on trouve si on rate.

## 4. Liste de contrôle

Avant de rendre la main, vérifie point par point :

- `SCENARIO.md` tient en 150 lignes et ne décrit rien : chaque lieu, chaque PNJ y est un pointeur, et chaque pointeur mène à une fiche qui existe ;
- chaque fiche dit à quoi elle sert dans l'intrigue et pointe en retour vers le scénario ; aucune fiche ne contient de détail qu'aucune scène n'utilisera ;
- `monde/INDEX.md` a une ligne par fiche, avec « connu du joueur » à jour ;
- dates, âges, distances et durées sont cohérents entre eux, avec la chronologie et avec les arcs passés ;
- pour chaque information importante, on sait **qui** la connaît et **comment** il l'a apprise ;
- chaque pièce du puzzle a au moins deux chemins, ferme une question et en ouvre une plus grande ; le grand secret relit l'arc, il ne le clôt pas ;
- au moins deux hypothèses crédibles restent ouvertes jusqu'au milieu de l'arc ;
- la condition de fin tient en une phrase, et chaque nœud de l'arbre offre des alternatives dont une partie seulement est exigée ;
- les événements contiennent le plan de l'antagoniste avec ses réactions, au moins une échéance connue, et chacun sa version « en retard » ;
- chaque situation clé a ses deux issues et ses trois portes de nature différente ; aucune n'est sans issue ; chaque issue change un fichier avant la fin de l'arc ;
- la carte tient sur une topographie réelle, les trois modes alternent le long de tout itinéraire probable, et chaque lieu a son texte d'arrivée (le plus important en dernier) ;
- la réserve contient quatre à six aventures, dont une respiration, une perte, et une qui fait entrer le monde large ;
- une figure du passé revient, ou l'on sait pourquoi pas ; la leçon apprise de l'ouverture a son écho dans une situation clé ;
- l'arc puise **visiblement** dans le monde large (une faction qui agit, un événement de la chronologie qui pèse, une nouvelle d'ailleurs), fait avancer d'un cran au moins une révélation du grand dessin, et ajoute au monde deux ou trois fiches hors de sa région ;
- les gens des lieux habités ont des projets, des appartenances, un dehors ; les puissants ne sont pas tous un conseil à convaincre ;
- les indices de contexte (lieu, époque, puissances) sont au nombre de trois ou quatre, diffus, sourcés, et jamais confirmés par le MJ ;
- le ressort de l'arc (secret, antagoniste, structure, preuve) diffère des arcs passés sur au moins deux points ;
- le joueur peut tout rater sans que l'histoire se bloque ;
- le scénario ne présume rien du personnage et ne fixe aucun ton ;
- chaque retour de `retours_joueur.md` a une réponse concrète dans le scénario.

## 5. Les fichiers

Le skill `jouer` lit ces fichiers et rien d'autre : respecte leur structure pour qu'il retrouve tout. Les noms de fiches sont en minuscules, sans accents, avec des tirets (`monde/pnj/aude-la-passeuse.md`) ; un pointeur s'écrit `→ pnj/aude-la-passeuse` (chemin relatif à `monde/`).

| Fichier | Ce que tu y écris |
|---|---|
| `scenario/SCENARIO.md` | La colonne vertébrale de l'arc (structure ci-dessous). Réécrit à chaque arc. |
| `monde/INDEX.md` | Une ligne par fiche : chemin, nom, ce que c'est en quelques mots, connu du joueur (oui / non / de nom). |
| `monde/univers.md` | Le monde connu de tous, une page, avec pointeurs. Se complète, ne se réécrit pas. |
| `monde/histoire.md` | La chronologie et « En ce moment, ailleurs ». |
| `monde/grand_dessin.md` | Caché : vérités du monde, révélations à long terme, ce que chaque arc en a laissé passer, acquis des arcs passés. |
| `monde/contrees/`, `factions/`, `anciens/`, `lieux/`, `pnj/` | Une fiche par élément (modèles ci-dessous). |
| `intrigues.md` | Une section « Arc N » avec la question centrale et ce que le joueur sait déjà. Rien de plus. |
| `regles.md` | Les règles maison de l'arc, sous « Règles maison (connues du joueur) ». |
| `etat_actuel.md` | La scène d'ouverture (avec la leçon apprise), le lieu (→ fiche), la date, les PNJ présents (→ fiches), et un paragraphe « Pour démarrer ». |
| `journal.md` | N'y touche pas : c'est le skill `jouer` qui l'écrit. |

Structure de `scenario/SCENARIO.md` (150 lignes au plus) :

```
# Arc N : <titre>
_Caché. Ne décrit rien : pointe vers les fiches de `monde/`._

## Cadrage
Type · durée visée · point d'entrée (→ lieu, date) · ce que le joueur sait déjà · topographie source

## Condition de fin et arbre
L'arc se termine quand : <une phrase>
- <nœud> (2 sur 3) [mode]
  - <feuille> → lieux/x, → pnj/y  (pièce 2)
Leçon apprise : <objet ou problème d'ouverture> → revient dans <situation>

## Grand secret
<la vérité en trois lignes>
| # | Pièce | Chemins (→ fiches) | Fausse lecture, seule | Ferme / ouvre |
Indices de contexte : | Indice | → fiche | Ce qu'on en déduit, recoupé |
Grand dessin : ce que l'arc en laisse passer (→ grand_dessin)

## Événements (au futur ; « (connue) » ; cocher quand passés)
- [ ] J3 — <ce qui arrive> → lieux/x, → pnj/y. En retard : <autre route / autre prix>
Réactions de l'antagoniste : si <action du joueur> → <réaction>

## Carte
A → B (coût, condition) ; une ligne par lien, chaque lieu → sa fiche

## Situations clés
### <nom> (nœud de l'arbre) → lieux/x, → pnj/y
Portes : <force / ruse / savoir…> · Favorable : … · Catastrophique : … · Fichier qui change : …

## Réserve d'aventures tampon
- [ ] 1. <titre> (respiration) → … : <trois lignes>

## Difficulté
Hypothèses concurrentes, fausses pistes (→ fiches), coût des informations, si le joueur rate.

## Écarts (rempli par `jouer`)
Événements déplacés, faits improvisés qui touchent l'intrigue, une ligne chacun.
```

Modèle de fiche PNJ (`monde/pnj/<nom>.md`, 25 lignes au plus) :

```
# <Nom> — <rôle en trois mots>
**Trois adjectifs** : … · **Veut** : <intention, une phrase> · **Voix** : <deux ou trois tics>
**Appartient à** : → factions/…, → contrees/…

## Au service de l'intrigue (← SCENARIO, <pièce / situation / événement>)
- Détient : <pièce, indice de contexte, porte>
- Si le joueur ne fait rien : …
- Si on le presse : …
- Indice qui trompe / indice qui corrige (si allégeance ambiguë)

## Sait (et d'où)
- … (vu / entendu / lu / rapporté par …)

## Caché
…

## État (réécrit par `jouer`)
Où · attitude envers le personnage · statut

## Arcs
<une ligne par arc où il a compté>
```

Modèle de fiche lieu (`monde/lieux/<nom>.md`, 30 lignes au plus) :

```
# <Nom> — <ce que c'est en quelques mots>
**Mode** : … · **Liens** : → lieux/…, → pnj/…

## Texte d'arrivée
<quatre à cinq lignes, telles qu'elles seront lues ; le plus important en dernier>

## Au service de l'intrigue (← SCENARIO, …)
<pièce, indice, feuille de l'arbre, situation qui s'y joue>

Merveille : … · Danger : … · On observe : … · Change : … · Doit au monde : → …

## Caché
…

## État (réécrit par `jouer`)

## Arcs
```

Modèle de fiche du monde (`contrees/`, `factions/`, `anciens/`, 15 lignes au plus) :

```
# <Nom> — <archétype en une phrase>
**Ce que tout le monde en sait** : <deux ou trois lignes>
**Ce qui est vrai** (caché) : <deux ou trois lignes>
**Projet en cours** (factions) / **ce qu'il en reste** (anciens) : …
**Ce qui en affleure** : mots, coutumes, objets, rumeurs, marchandises, pour improviser
**Liens** : → …, chronologie : <dates>
**Arcs** : <une ligne par arc où elle a compté>
```

Une fiche contient à la fois l'apparent et le caché : le skill `jouer` sait qu'il ne dit jamais la section « Caché » ni « Ce qui est vrai », sauf ce que le joueur découvre en jeu.

## 6. Rendre la main

Au joueur, ne donne que le cadre, les nouvelles règles maison et la scène d'ouverture en deux lignes. Rien du secret, de la carte cachée ni des PNJ à venir : la découverte, c'est le jeu. Propose ensuite de jouer avec le skill `jouer`.

---

Cette méthode doit beaucoup à FibreTigre (condition de fin et arbre des conditions, texte d'arrivée et unités de lieu, PNJ en trois adjectifs et une intention, aventures tampon, leçon apprise, figure du passé, trois modes) et à Julien Dutel (archétypes proches de cultures réelles). Les sources sont dans `REMERCIEMENTS.md`, à la racine du dépôt `mj`.
