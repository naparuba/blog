Title: Python: pourquoi je ne suis pas un fan des @property
Date: 2023-05-12 10:20
Category: Talk
Tags: python, philosophie, maintenance
Slug: python-property
Author: Jean Gabès
AuthorLogin: naparuba
Summary: Après quasi 15ans de Python, je ne vois toujours d'intérêt légitime au @property. Voici pourquoi.
id: 78
Status: ready

<center><img src='/images/78/article.jpg'></center>

# Les @property: des getter/setter à pas chers
Pour les développeurs, les getter et setters sont bien connus. Quand on a un objet, on protège sépare bien son utilisation de son implémentation.

On doit être capable de changer tout ce que l'on souhaite dans l'implémentation sans changer l'utilisation d'un objet. 

Sans ce principe fondateur, vous pouvez mettre à la poubelle toute idée de maintenance de votre code/librairie.

Python étant également un langage objet, il a évidement respecté ce principe. On peut avoir des getter/setter avec ses classes.

Je passe leur définition, c'est par définition assez trivial.

Par contre, il a également une autre manière de faire en Python (déjà on s'éloigne du `There should be one-- and preferably only one --obvious way to do it.` du [https://peps.python.org/pep-0020/](zen of Python)): l'annotation `@property`

<center><img src='/images/common/reading.gif'></center> 

Son principe est assez simple: on va relier une méthode à un nom de propriété classique. Voici ce que ça donne sur un exemple simple, développé par un premier développeur, `Jean`:

    class Human:
        def __init__(name, birthday):
            self._name = name
            self._age = birthday - now()  # simplifié pour l'exemple

        @property
        def name(self):
            return self._name

       @age.setter
        def name(self, value):
            self._name = value


        @property
        def age(self):
            return self._age

       @age.setter
        def age(self, value):
            self._age = value
       

On accède alors aux propriétés de manière "transparente" (lol, carrément pas) de la manière suivante:

    h = Human('jean', '1982/12/13')
    print('%s is %d' % (h.name, h.age))

Joli? Oui. Trompeur? Oh que oui aussi. Car si on ne regarde que le code d'un point de vue utilisateur, on pense que name et age ne sont que des propriétés simples, sans coût spécial à l'appel, juste une string et un int, gratuit en gros.

Or non, cette impression peut être totalement fausse et donner des résultats qui vont être trompeurs.

<center><img src='/images/common/outch 2.gif'></center> 

# Quand les @property mentent

Les `@property` ne sont que des appels à des méthodes. Juste que la syntaxe nous a caché ça. Rien de plus.

Revenons un peu à notre exemple. Imaginons que nous avons un nouveau développeur, nommé `William`, qui a besoin de faire une moyenne sur beaucoup de personnes, genre 100_000. `William` va procéder ainsi:

    # en supposant qu'il y en a au moins un évidement
    moyenne = sum([human.age for human in lot_of_humans]) / len(lot_of_humans)

D'après son interface, `William` s'attend à ce que le temps du calcul soit très rapide, c'est une bête somme d'entier après tout. Il ne connait pas les détails `internes` de Human, car il l'utilise, on a pas à savoir `comment` il est fait.

<center><img src='/images/common/pasfaux.png'></center> 

## Un autre développeur corrige le bug de Human dans son coin

Mais maintenant un autre développeur, nommée `Amy`, corrige le bug de la classe Human sur son `self._age = birthday - now()` car c'est peut-être vrai au moment de l'instanciation de l'objet
mais il suffit d'attendre un ou deux jours pour avoir des cas où l'anniversaire est passé pour avoir un autre âge. 

<center><img src='/images/common/bug.jpg'></center> 

`Amy` va donc déplacer le calcul à chaque fois qu'on demande l'age:

        # note: simplifié
        @property
        def age(self):
            return self._birthday - now()

       @age.setter
        def age(self, value):
            self._birthday = now() - value

Ok, c'est fixé de manière simple. 

`Amy` aurait pu rajouter un cache, ou avoir un calcul une fois par jour, mais ça demande que le démon ait un ordonnancement et cie, et un cache demande de le vider de temps en temps. Ce fix a le mérite d'être fonctionnel, et elle n'a pas plus de temps à y passer de toute manière.

## Le premier développeur voit ses tests de performances s'éffondrer
Revenons à notre développeur `William` qui devait calculer sa moyenne. 

C'est une grosse équipe, il n'est pas au courant de tous les détails des fix des autres développeurs. 

Par contre, on lui avait demandé de s'engager sur les performances de son calcul de moyenne.
Confiant dans le calcul de `sum()` sur de simples entiers, il avait mis un test de performance avec très peu de marge sur son calcul.

Problème, les calculs de date sont très, **très**, couteux, peu importe le language. 

<center><img src='/images/common/sad (2).gif'></center> 

Python ne fait pas exception. Et ici, là où il pensait naivement avoir affaire à des entiers, il a désormais dans sa boucle N fois un gros calcul de temps. D'où ses problèmes de performances. 

Un accès direct à un entier, c'est peu cher (enfin avec Python, disons que c'est moyennement cher), mais là avec un calcul de date, c'est la mort.

## Qui s'est raté alors?
A qui la faute? 

 * `Amy` a corrigé aussi bien qu'elle a pu dans le temps imparti un bug important
 * `William` a pris un `human.age` affiché comme un entier pour... bah un entier. Je ne vois pas comment lui en vouloir.

Non. Je pense que la faute revient à `Jean`, qui a défini l'interface de Human. 

<center><img src='/images/common/stess (2).jpg'></center> 

Je peux tout à fait pardonner à `William` d'avoir fait la faute sur `human.age`, car j'aurais fait la même.

On ne s'attend pas à avoir un appel de méthode ici, et encore moins un appel couteux.

Par contre, si on avait un appel du genre `human.get_age()` on fait un peu plus attention. La supposition de "on récupère juste un entier quasi gratuitement" ne tient plus, et on est tenté d'aller voir ce qu'il y a dans le get_age(), ou à minima de la sortir de sa boucle, et le timer à part.

## Les @property, un piège
Et c'est bien ça que je reproche au `@property`. C'est pratique sur le papier, mais c'est piégeux.

On va faire de fausses suppositions sur des propriétés alors qu'en fait le calcul peut être bien plus important, voir accéder à un cache avec tous les problèmes que ça demande, les accès concurrents (moins un souci si on fait que du read sur un entier), etc.

Oh, bien sûr, on peut me répondre: "c'est au développeur qui l'utilise de faire attention"

Mais non je ne suis pas d'accord. Il doit déjà faire attention à son propre code, alors réussir à deviner toutes les suppositions du code des autres, ça commence à faire beaucoup si on lui mets des peaux de bananes sous les pieds.


## Le vrai usage des @property : ratraper un cas foireux
Pour moi les `@property` sont un moyen de ratraper le code d'une interface qui a été mauvaise dès le début: on avait donné l'accès à une de ses propriétés internes, et on s'aperçoit qu'il n'aurait pas fallu. 

On tente alors de catcher les appels "à l'arrache" sans avoir à changer son interface d'appels de la part de ses clients.

Mais c'est donc une solution à un problème qui n'aurait pas dû se poser dès le départ. Sauf si tu es une classe "friend" comme en C++, tu n'as pas à accéder à mes propriétés en direct, que j'ai mis un _ au début ou pas (ou alors tu peux planter, ça sera ta faute si je change une ligne `(⌐■_■)–︻╦╤─ – – – (╥﹏╥)` ).

Au moins les getter/setter, tu ne feras pas de suppositions de performance ou accès concurrents. On fait naturellement attention dans ces cas-là.

Les @property c'est l'opposé de ma philosophie de développement. C'est "too much" et ça donne une fausse idée de simplicité. 

Je préfère largement quand la simplicité est véridique `༼ つ ͡◕ Ѿ ͡◕ ༽つ`

<center><img src='/images/common/café.gif'></center> 
