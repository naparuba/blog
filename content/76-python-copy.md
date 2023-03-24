Title: Python: la différence entre copy et deepcopy
Date: 2023-04-14 10:20
Category: Talk
Tags: linux, debug, admin
Slug: python-copy
Author: Jean Gabès
AuthorLogin: naparuba
Summary: En Python, quand on souhaite copier un conteneur, on a le choix entre copy et deepcopy.<br/>Se tromper entre les deux est c'est le bug assuré. Voyons pourquoi.
id: 76
Status: draft

# Les conteneurs en Python
S'il y a bien deux éléments que je trouve structurant dans un language de programmation, c'est autant sa grammaire que ses conteneurs standards. Ces derniers sont importants, car
ils representent le plus gros des troupes de ce que l'on va utiliser au jour le jour. Une absence de liste dynamique par défaut sera très, très handicapante, et on va 
se retrouver à prendre une librairie tierce pour ça.

Sauf que d'autres librairies/projets auront fait un autre choix et pris une autre librairie, avec sa phase d'aprentissage qui va avec (et ses bugs?). Ce n'est pas pour rien que les 
languages de maintenant sont équipés dès le départ de conteneurs standards:

 * liste à taille fixe ou dynamique
 * tableau de hash, dictionnaire, map, appelez ça comme vous voulez
 * struct et/ou objet

Contrairement aux types natifs simples comme les int ou les float, les conteneurs peuvent être modifiés, et ne sont donc pas à utiliser à la légère. Que ce soit lorsqu'on les 
passe à une fonction/méthode, qu'on tente d'y accéder depuis des threads ou même qu'on vive avec au fil de son programme linéairement.

# Parfois, il faut faire une copie
Le piège le plus simple des conteneurs vient de la copie. On peut avoir besoin d'une simple copie pour donner une liste à un autre élément qui va avoir besoin de faire un tri différent, tri 
qui pourrait être "in place", et donc impacter celui qui a gentiement fourni la liste!

Parfois on a pas trop confiance dans cet "autre" élément, comme si c'est un module tiers qui est chargé par l'utilisateur, et qu'on lui donne des données auquel on tient (ordre compris).

Bref, parfois, on souhaite juste copier sa liste/dict. En Python, le module copy est là pour ça. On a deux méthodes qui nous intéresse, et qu'il est primordial de connaitre avant d'en utiliser une ou l'autre:
 
 * copy
 * deepcopy

<center><img src='/images/common/maybe.gif'></center>

# copy et deepcopy
## Le principe de copy
copy.copy est la plus simple, mais pas forcément la moins traitre au jour le jour.

copy() va uniquement copier le conteneur, ``mais pas son contenu``. Ce dernier point est très important. Ceci signifie que si on a:

    a = [3, 2, 1]
    b = copy.copy(a)
    b.sort()
    print('a => %s' % a)
    print('b => %s' % b)

Donne:

    a => [3, 2, 1]
    b => [1, 2, 3]

Par contre attention, ici c'était le cas simple, on a des objets immutables dans nos listes, de simples int. Dans la vie de tous les jours, on
aura une liste de dict ou d'instances par exemple.

<center><img src='/images/common/pointers.jpg'></center>

Et là, attention, car on a vu que copy() ne touche qu'au conteneur, pas au contenant. Donc ici la copie aura des pointeurs vers les mêmes objets.

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
copy.deepcopy() va régler le problème. Mais bien entendu rien n'est gratuit, et en réglant un problème, on en créé un symétrique. Voire deux ``^^'``

deepcopy() va faire une copie en profondeur (merci captain obvious...). Il va donc copier également le contenu, et ce récursivement.

On aura donc deux impacts par rapport à copy():
 
 * ça va coûter autrement plus cher. Si c'est négligeable pour des int, dans la vie de tous les jours on peux avoir un gros volume de données qui sont pointées, et deepcopy() peut être très long
 * il va vraiment tout copier, ceci peux produire des soucis bien complexes à débugger si les objets étaient référencés ailleurs

Au moins nos cas simples sont réglés:

    a = [{'name':'jean'}, {'name':'rené'}, {'name':'claude'}]
    b = copy.deepcopy(a)
    b[0]['name'] = 'paul'
    print('a => %s' % a)
    print('b => %s' % b)
    print(a[1] is b[1])

Donne:

    a => [{'name': 'jean'}, {'name': 'rené'}, {'name': 'claude'}]
    b => [{'name': 'paul'}, {'name': 'rené'}, {'name': 'claude'}]
    False

Par contre, si on prend le cas où on pointait vers de vrais objets, genre des personnes, qui étaient également référencées dans une autre partie du programme, on aura également copié ces instances.

    jean = User('jean', age=40)
    a = [{'contact':jean}, ...]
    b = copy.deepcopy(a)
    [... se passe un peu de temps...]
    jean.celebrate_birthday()
    [... on passe quelques milliers de lignes, on est 5 niveaux d'appels et on a oublié d'où venait b initialement]
    print(b[0])

Donne:
   
    Name=Jean, age=40

<center><img src='/images/common/bug 2.gif'></center>

Ici, nous nous sommes retrouvés avec deux objets 'jean', et une partie du programme est resté avec la première instance, l'autre moitié avec l'autre.

Le pire, c'est qu'au débug, avant de modifier une des instances, bon courage pour détecter que ce sont deux instances différentes, car on aura pendant un long moment le même affichage:

    Name=jean, age=40

C'est une des raisons qui font qu'il m'est souvent arrivé dans ce genre de cas d'afficher dans le print d'un élément son pointeur avec un id(self) par exemple:

   Name=jean, age=40, ptr=140526325860624

Bon faut avouer que ce n'est pas ultra lisible. Mais lors d'un debug ça peut sauver des journées à se demander pourquoi un objet n'a pas la modification qu'on a faite 20s avant. Et oui, ça m'est arrivé, et non je ne donnerai pas le temps que j'ai perdu sur cette connerie mais c'était beaucoup trop ``(／‵Д′)／~ ┻━┻``

<center><img src='/images/76/article.png'></center>

# Attention: le choix n'est pas anodin
Comme on l'a vu, ce n'est pas anodin comme choix. Aucun n'est sans risque. C'est pour ça que si vous venez à devoir faire une copie, ne choississez surtout par au hasard. Demandez-vous combien de temps la copie va vivre, où et par qui elle va être utilisée, etc.

S'il vous manque des infos sur la vie de vos objets, n'allez pas plus loin et aller les chercher.

Votre moi du futur vous remerciera des heures de debug économisées pour ces 5 petites minutes de réflexions.

<center><img src='/images/common/thanks 4.gif'></center>

