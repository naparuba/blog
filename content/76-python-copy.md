Title: Python: la différence entre copy et deepcopy
Date: 2023-04-14 10:20
Category: Talk
Tags: linux, debug, admin
Slug: python-copy
Author: Jean Gabès
AuthorLogin: naparuba
Summary: En Python, quand on souhaite copier un conteneur, on a le choix entre copy et deepcopy.<br/>Se tromper entre les deux est c'est le bug assuré. Voyons pourquoi.
id: 76
Status: ready

<center><img src='/images/76/article.png'></center>

# Les conteneurs en Python
S'il y a bien deux éléments que je trouve structurant dans un langage de programmation, ce sont autant sa grammaire que ses conteneurs standards.

Ces derniers sont importants, car ils représentent le plus gros des troupes de ce que l'on va utiliser au jour le jour. Une absence de liste dynamique par défaut sera très, très handicapante, et on va se retrouver à prendre une bibliothèque tierce pour ça.

Sauf que d'autres bibliothèques/projets auront fait un autre choix et pris une autre bibliothèque, avec sa phase d'apprentissage qui va avec (et ses bugs ?). Ce n'est pas pour rien que les langages de maintenant sont équipés dès le départ de conteneurs standards :

 * liste à taille fixe ou dynamique
 * tableau de hash, dictionnaire, map, appelez ça comme vous voulez
 * struct et/ou objet

Contrairement aux types natifs simples comme les int ou les float, les conteneurs peuvent être modifiés, et ne sont donc pas à utiliser à la légère. Que ce soit lorsqu'on les passe à une fonction/méthode, qu'on tente d'y accéder depuis des threads ou même qu'on vive avec au fil de son programme linéairement.

# Parfois, il faut faire une copie
Le piège le plus simple des conteneurs vient de la copie. On peut avoir besoin d'une simple copie pour donner une liste à un autre élément qui va avoir besoin de faire un tri différent, tri qui pourrait être "in place", et donc impacter celui qui a gentiment fourni la liste!

Parfois on n'a pas trop confiance dans cet "autre" élément, comme si c'est un module tiers qui est chargé par l'utilisateur, et qu'on lui donne des données auxquelles on tient (ordre compris).

Bref, parfois, on souhaite juste copier sa liste/dict. En Python, le module copy est là pour ça. On a deux méthodes qui nous intéressent, et qu'il est primordial de connaître avant d'en utiliser une ou l'autre :

 * copy
 * deepcopy

<center><img src='/images/common/maybe.gif'></center>

# copy et deepcopy
## Le principe de copy
``copy.copy`` est la plus simple, mais pas forcément la moins traitre au jour le jour.

``copy()`` va uniquement copier le conteneur, ``mais pas son contenu``. Ce dernier point est très important. Ceci signifie que si on a:

    a = [3, 2, 1]
    b = copy.copy(a)
    b.sort()
    print('a => %s' % a)
    print('b => %s' % b)

Donne:

    a => [3, 2, 1]
    b => [1, 2, 3]

Par contre, attention, ici c'était le cas simple, on a des objets immuables dans nos listes, de simples int.
Dans la vie de tous les jours, on aura une liste de dict ou d'instances par exemple.

<center><img src='/images/common/pointers.jpg'></center>

Et là, attention, car on a vu que `copy()` ne touche qu'au conteneur, pas au contenant. Donc ici la copie aura des pointeurs vers les mêmes objets.

    a = [{'name':'jean'}, {'name':'rené'}, {'name':'claude'}]
    b = copy.copy(a)
    b[0]['name'] = 'paul'
    print('a => %s' % a)
    print('b => %s' % b)

Donne:

    a => [{'name': 'paul'}, {'name': 'rené'}, {'name': 'claude'}]
    b => [{'name': 'paul'}, {'name': 'rené'}, {'name': 'claude'}]

<center><img src='/images/common/oops.gif'></center>

On aurait pu vérifier en demandant directement si on avait les mêmes pointeurs:

    print(a[0] is b[0])
    True

L'accès qu'on pouvait penser anodin à ``b`` a bien impacté ``a``.


## Le principe de deepcopy
``copy.deepcopy()`` va régler le problème. Mais bien entendu rien n'est gratuit, et en réglant un problème, on en créé un symétrique. Voire deux ``^^'``

``deepcopy()`` crée une copie en profondeur (merci captain obvious...). Cela signifie qu'elle copie également le contenu de manière récursive.

Nous avons donc deux impacts par rapport à la fonction copy():
 
 * ``deepcopy()`` est beaucoup plus coûteuse en termes de performance. Si la copie de simples entiers n'a pas d'impact significatif sur les performances, pour des données plus volumineuses, ``deepcopy()`` peut être très lent. De plus, votre consommation de RAM va augmenter en conséquence.
 * ``deepcopy()`` copie vraiment tout, ce qui peut entraîner des problèmes complexes et difficiles à déboguer si les objets étaient référencés ailleurs.

Au moins nos cas simples sont résolus:

    a = [{'name':'jean'}, {'name':'rené'}, {'name':'claude'}]
    b = copy.deepcopy(a)
    b[0]['name'] = 'paul'
    print('a => %s' % a)
    print('b => %s' % b)
    print(a[1] is b[1])

Ce qui donne :

    a => [{'name': 'jean'}, {'name': 'rené'}, {'name': 'claude'}]
    b => [{'name': 'paul'}, {'name': 'rené'}, {'name': 'claude'}]
    False

Cependant, si nous prenons le cas où nous pointons vers de vrais objets, tels que des personnes, qui sont également référencées
dans une autre partie du programme, nous aurons copié ces instances.

    jean = User('jean', age=40)
    a = [{'contact':jean}, ...]
    b = copy.deepcopy(a)
    [... se passe un peu de temps...]
    jean.celebrate_birthday()
    [... on passe quelques milliers de lignes, on est 5 niveaux d'appels et on a oublié d'où venait b initialement]
    print(b[0])

Ce qui donne :
   
    Name=Jean, age=40

<center><img src='/images/common/bug 2.gif'></center>

Dans ce cas, nous nous sommes retrouvés avec deux objets "jean", une partie du programme ayant la première instance et l'autre moitié ayant l'autre.

Le pire, c'est qu'il peut être difficile de détecter que ce sont deux instances différentes, car on aura pendant un long moment le même affichage :

    Name=jean, age=40

C'est une des raisons qui font qu'il m'est souvent arrivé dans ce genre de cas d'afficher dans le print d'un élément son pointeur avec un id(self) par exemple:

    Name=jean, age=40, ptr=140526325860624

Il est vrai que ce n'est pas très lisible, mais cela peut vous faire gagner des heures de débogage en cas de problème.
En effet, cela m'est arrivé, et je ne donnerai pas le temps que j'ai perdu à cause de cela, mais c'était beaucoup trop ``(／‵Д′)／~ ┻━┻``



# Attention: le choix n'est pas anodin
Comme nous l'avons vu, ce choix n'est pas anodin. Aucune des options n'est sans risque.
C'est pourquoi, si vous avez besoin de faire une copie, ne choisissez pas au hasard.
Demandez-vous combien de temps la copie va être utilisée, où elle sera utilisée et par qui.

Si vous manquez d'informations sur la vie de vos objets, ne cherchez pas plus loin et allez les chercher.

Votre moi du futur vous remerciera pour les heures de débogage économisées en prenant ces 5 petites minutes de réflexion.


<center><img src='/images/common/thanks 4.gif'></center>

