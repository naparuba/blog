Title: Développer son outil en Open Source et en tant qu’éditeur, deux salles, deux ambiances
Date: 2023-03-17 10:20
Category: Talk
Tags: entreprenariat, open-source
Slug: depuis-open-source-vers-editeur
Author: Jean Gabès
AuthorLogin: naparuba
Summary: Quand on passe d'un hobby de dev sur un outil open source à un éditeur d'une solution payante, on change de monde et également de type de motivation.<br/> Dans cet article, je vais partager comment je l'ai véçu, ce que ça a changé par rapport à ma relation avec le code et le projet dans son ensemble.
id: 74
Status: published

Ce post fait suite aux réflexions que j'ai eu lors de mon entretient avec [Imrane Dessaï](https://fr.linkedin.com/in/imranedessai) que vous pouvez retrouver sur [Youtube](https://www.youtube.com/watch?v=kM42WE0Sa4c)


# De simple consommateur Open Source à contributeur
Petit retour rapide sur l'histoire dont on va parler ici: Shinken était parti comme un simple POC sans nom pour rajouter le côté 
distribué à Nagios. Suite au refus de Nagios d'incorporer les amélorations dans le projet "mère" (car utilisant un nouveau
langage, le Python), [Shinken](http://www.shinken-monitoring.org/) était né.

J'avais toujours vu l'open source depuis mon point de vue de "simple consommateur, un peu contributeur"
à quelques projets. J'avais déjà participé au projet Nagios avec quelques patchs/améliorations par exemple,
ou le projet [Mangos](https://www.getmangos.eu/) (serveur WoW). 

Mais c'était du classique: j'avais un problème,
et hop un peu de C après et quelques recompilations, le problème était réglé. Passé mes patchs, je retournais
dans mon côté consommateur, sans participer plus que ça aux projets, m'inpliquer et régler des problèmes que
je n'avais pas par exemple.

# Lancer son propre projet
Shinken a changé cela. J'avais mon propre projet. Vu que j'avais déjà écrit des articles sur Nagios dans [LinuxMag](https://connect.ed-diamond.com/auteur/gabes-jean)
à l'époque, c'était l'occasion de faire connaitre mon projet à d'autres afin d'avoir des utilisateurs. Et ils sont
venus, avec des questions et (beaucoup) de demandes. Donc l'article avait rammené des consommateurs, logiques et
je n'étais pas plus surpris de ça.

Par contre, j'ai également eu des quelques contributions, petites au début, puis de plus en plus nombreuses au fur
et à mesure. Arrivé à un moment, je pense qu'on pouvait considérer qu'on était deux à quasi-égalité sur le projet,
avec [Gerhard](https://github.com/lausser) (que je remercie chaleureusement!). Vu qu'il était allemand, ça m'a forcé à mettre tout le projet en
anglais par défaut, pas un mal.

Et là, de proche en proche, j'étais en train de gérer un projet communautaire sans trop l'avoir recherché au départ,
mais pourquoi pas :)


<center><img src='/images/common/allow.gif'></center>



## Le projet s'organise tranquillement
Au début, on avait la mailinglist, mais qui n'était pas pratique du tout je trouve (je n'aime pas les emails,
question de goût). Github et ses tickets ont pris le relais rapidement.

L'organisation restait cependant très centralisée. J'ai toujours gardé la main sur le projet, sans avoir à demander
à d'autres avant de faire les choses. Ce qui me plaisait dans le projet, c'était de rajouter de nouvelles fonctionalités,
et corriger des bugs en faisant en sorte qu'ils ne reviennent pas. C'était très satisfaisant de se dire qu'on avançait
vers une version "sans bugs". Et je n'allais pas demander d'autorisation pour améliorer mon propre projet ```┌(▀Ĺ̯ ▀-͠ )┐```

Ce controle absolu est une force pour un petit projet, mais il se révèlera un problème quand il grandira par la suite.

# Quand les demandes de support se font de plus en plus présentes
Vers mi-2012, une grande étape arrive: on écrit à plusieurs un [linuxmag hors série](https://connect.ed-diamond.com/GNU-Linux-Magazine/glmfhs-062). C'était vraiment sympa, car on s'était
bien réparti les tâches. Le hors série est un carton, et attire beaucoup de monde. Et beaucoup de demandes. De plus en
plus de grosses sociétés me demandent en off si une version supportée/boostées est prévue. Par boostée, il faut
comprendre avec une interface de configuration (le moteur n'est pas la problématique de ce type d'utilisateurs, sauf
si leur propre production est bloquée).

Je me rapproche de structures sur Bordeaux pour savoir comment on fait pour monter un éditeur. (Futur article plus
tard sur le sujet). Mi-2013, c'est parti: je trouve un associé orienté commercial, et l'éditeur [Shinken Solutions](https://www.shinken-enterprise.com)
prends vie.


<center><img src='/images/common/hello (2).gif'></center>

# Le début de l'éditeur
Je mets de côté la partie recherche de fonds et le remplissage de nombreux dossiers. Le code lui a avancé comme
lors de la phase Open Source: très vite. Bien trop vite d'ailleurs, car avec bien les 3/4 du temps pris sur les
dossiers, j'ai dû prendre des racourcis sur le dev de la partie configuration (je n'avais pas assez d'exéprience
à l'époque pour estimer si le racourci était trop court ou pas). Des clients sont séduits, plus par le potentiel
que par les premières interfaces il faut bien le dire. On embauche, et l'équipe s'étoffe.

## Les choses à revoir
Et là arrive le retour à la réalité: toute la phase d'installation et d'exploitation était à revoir.

Quand on prend un moteur Open Source (comprendre dans 99% du temps: gratuit), on est concients qu'on prend
un simple moteur qu'il va falloir intégrer soit même dans le SI, le configurer, l'adaptant si besoin. Bref,
payer avec son propre temps.

Mais quand on achète une solution chez un éditeur les attentes ne sont pas du tout les mêmes. Déjà il faut voir
que le public n'est pas le même non plus. Shinken était adapté pour les spécialistes qui n'avaient pas peur se relever
les manches, d'installer les dépendances, et faire l'automatisation de leurs fichiers de configuration.

Mais ceux qui choississent une solution payante veulent que toute cette partie-là soit déjà faite, nouvelle société éditrice
ou pas. De plus, là on a pas forcément affaire à ceux qui sont au courant, qui cherchent la nouveauté, mais justement
l'autre partie du spectre, ceux qui cherchent la stabilité et surtout la facilité.

Bon "facile" n'était pas ce qui catactérisait Shinken à l'époque il faut être honnête. Quand on savait quoi faire,
l'installation était l'histoire d'une bonne heure, configuration de la partie architecture incluse. Mais dans les mains
d'un débutant dans le domaine qui n'allait pas lire la documentation (de toute manière l'outil ne lui donnait pas le lien
où aller chercher) et s'attendait à avoir à lancer une seule commande, c'était l'enfer.

Les premiers retours sur cette partie était calamiteuse. Beaucoup de POC se sont arrétés à cette étape. Il fallait donc
remédier à ça.

<center><img src='/images/common/challenge.gif'></center>

## Création d'un installeur
La création d'un installeur a été salutaire. Il fallait arriver avec bons nombres de dépendances, dont [Mongo](https://www.mongodb.com) et [Graphite](graphite.readthedocs.io/).

Là où il était simple de gérer pleins de distributions différentes pour le moteur Open Source, quand on doit livrer un tut cohérent aux clients (qui
sont dans des réseaux isolés), on a du faire le choix de choisir une distribution à gérer. A l'époque (2013), c'était Centos/Redhat6,
 car elle rassurait. Générer les rpm n'a pas été trop rude, même si la gestion des fichiers de configuration via rpm est un vrai
calvaire au final.

    Astuce: ne donnez pas vos fichiers de configurations à rpm, faites le à la main de suite, car de toute manière vous devez le faire à terme


## Les clients et les cycles de mises à jour
Autre point qui a posé problème était le rythme pour mettre à jour chez nos clients. Vu que c'étaient de grands comptes,
on parle de cycles très longs de validation/tests. Entre livrer une version et la voir installer, c'étaient des semaines
voir des mois. Dans un cas bien spécifique d'un projet où on était à l'année.

Et c'est quelque chose que là encore on ne peut pas bouger. C'est le process interne des clients, et il faut faire avec,
pas le choix.

On a donc dû gérer plusieurs versions en parallèles, ce qui a un coût non négligeable en termes de gestion.


<center><img src='/images/common/killself.gif'></center>

## ok mais là ça fait un moment qu'on a pas évoqué le code non?
Voilà, en fait, c'est toute la problématique d'un éditeur qui s'adresse pour les grandes sociétés (Shinken
n'était pas adapté pour les petites structures): c'est tout sauf un problème de code. 

Il faut faire avec des habitudes et des process internes. Le code n'est que le dernier des soucis, c'est facile à régler par rapport aux
premiers points.

Par exemple, on a dû parfois faire des algorithmes moins efficaces techniquement, mais bien plus faciles et
comprehensibles par les utilisateurs. Un algorithme trop complexe va juste créer des problèmes à l'éditeur, sans
que ses clients y voient un intérêt.

Bref, je gérais au jour à jour des problèmes qui n'étaient pas le code. La différence avec ce qui se passait du
côté Open Source était très forte, dans mon esprit c'était devenu deux "projets" différents.

Techniquement, c'était de plus en plus le cas, vu qu'au début on était trop limites en temps pour maintenir les
modifications dans la version open source (et les tester, adapter, etc, c'est bien plus que juste backporter le code).

# Quand tu découvres qu'il y a deux types de motivations
Pour ceux qui ont lu le livre [The Gamer's Brain de Celia Hodent]( https://www.amazon.fr/Gamers-Brain-Neuroscience-Impact-Design/dp/1498775500 )
savent qu'il y a (au moins) deux types de motivations:
 * intrinsèque : la récompense est de faire l'activité en elle-même  (en résumé: c'est fun en soi)
 * extrinsèque : la récompense t'es donnée car tu as fait l'activité (en résumé: pas marrant, mais tu es payé pour)

Le problème c'est que je n'ai lu ce livre que vers 2020, pas 2013 ^^'

Et donc assez rapidement est arrivé un changement: développer pour Shinken était une activité que je faisais
car c'était marrant, donc une motivation *intrinsèque*. 

Mais après avoir lancé la société, ma paie et surtout
celle de mes salariés en dépendait literralement. J'étais donc passé sur une motivation *extrinsèque*, avec des
contraintes de l'éditeur comme on a vu avant.

Et ce passage de motivation intrinsèque à motivation extrinsèque
est un cas connu: c'est un chemin en sens unique, car une fois que le cervau a identifié une tâche comme une
récompense extrinsèque, il ne revient pas en arrière. Il est même moins sensible que ceux qui n'ont connu que
la récompense extrinsèque!

Et entre ça et le fait que le code du framework avait tellement divergé que je relisais du "vieux" code que
j'avais fixé il y a quelque temps au "travail", le soir c'était tout sauf "fun" à faire.

    J'avais tué mon hobby. Litérallement.


<center><img src='/images/common/cassé 3.gif'></center>

## Gérer seul son projet Open Source
Et c'est là que le fait que je gère seul le projet a été une erreur je pense. Si je devais recommancer,
je pense que dès qu'on lance un éditeur, il faut passer la main sur le projet open source à quelqu'un qui
n'est pas lié économiquement à l'éditeur, ou à défaut le faire avec un groupe neutre. Même pas pour des raisons
de "concurrences" ou autre, mais bien pour être sûr qu'il y ait une bonne motivation à sa tête.

Hereusement, [Christophe Simon](https://github.com/geektophe) de Dailymotion a grandement palié le problème et a géré dans l'ombre le projet
Open Source. Je le remercie chaleureusement pour ça ```(/.__.)/ \(.__.\)```


<center><img src='/images/common/thanks.gif'></center>

## La vitesse d'un éditeur versus celle d'un mec sur son canapé

Autre point qui peu être très désagréable, est que suite à tous ces soucis de gestion des process des
clients, j'ai eu l'impression d'aller beaucoup, _beaucoup_ moins vite en termes de développement que lorsque
j'étais seul dans mon canapé à coder le soir.

En fait, c'est à la fois vrai et faux.


<center><img src='/images/common/maybe.gif'></center>

Le fait de travailler en équipe demande beaucoup de "surcharge" en interne pour que ça avance correctement (bonne
gestion des tickets, communication interne, gestion de la documentation, etc), surtout quand on a de gros clients.

Donc si je me prends en tant qu'individuel, ma vitesse pure dans une telle organisation était bien plus faible que
celle que j'avais avant de monter un éditeur. Et c'est totalement normal. C'était la vitesse de l'équipe qui comptait,
pas la mienne.

Mais c'est dur à accepter, surtout quand on allait très vite avant.
Mes collègues ont moins ce problème, car pour
eux c'est une vitesse "normale", et je me retrouvais à être en décalage par rapport à eux dans mon ressenti.

La vitesse de réflexion et d'exécution ayant toujours été un de mes points forts, c'était quelque chose que j'ai
très, très mal véçu au fil du temps:
  * plus de process
  * moins de vitesse individuelle
  * mais meilleure vitesse d'équipe à la fin


## Deux salles, deux ambiances
Bons nombres de développeurs connaissent déjà tout cela. Car c'est leur métier et ils ont conscience de ces problèmes
de motivation ou de vitesse perçue. 

Mais je n'étais pas un développeur profesionnel à l'époque, j'étais administrateur système ````\̅_̅/̷̚ʾ(•◡•)````


Je pense qu'un développeur professionnel aurait eu moins de soucis, ou en tout cas aurait pu les identifier plus vite. 

## Des solutions
Est-ce qu'il y a des solutions? 

Déjà splitter au plus tôt le travail et le hobby en laissant ce dernier dans les mains
d'autres, ou en tout cas avoir un groupe pour le gérer et non pas une seule personne.

Des conseils pour se lancer dans un éditeur qui s'adresse à de grosses sociétés et à leur process? Pas vraiment.
Prennez votre vélocité "normale" que vous imaginez, et divisez là par un bon gros 3. Vous aurez une bonne estimation quand ça
s'adresse à ce genre de clients. Il faut que votre business plan soit en phase avec ça.

<center><img src='/images/common/tropcher.gif'></center>

Si mon éxpérience vous est utile, ou si vous en avez une similaire (ou contraire), n'hésitez pas à le mettre
en commentaires, c'est le genre de sujet que je n'ai pas trop vu/lu dans le passé et qui m'aurait été pratique
il y a 10 ans ```(づ｡◕‿‿◕｡)づ ```


<center><img src='/images/74/74-open-source-editeur.png'></center>
ps: oui, je n'ai pas menti sur mes dons de design hein? ^^'