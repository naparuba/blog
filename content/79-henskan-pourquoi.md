Title: Henskan: pourquoi un (nouveau) projet pour liseuse
Date: 2024-09-05 10:20
Category: Talk
Tags: python, projet
Slug: henskan-pourquoi
Author: Jean Gabès
AuthorLogin: naparuba
Summary: Après plus de 10ans d'usage du logiciel Mangle, j'ai forké le projet. Voici pourquoi.
id: 79
Status: ready

<center><img src='/images/79/article.jpg'></center>

# J'aime ma liseuse

Je suis un gros consommateur de livres, et tout particulièrement de mangas. J'ai une liseuse depuis des années, et c'est surement un des objets que j'utilise le plus dans ma vie de tous les jours.

J'ai toujours eu des liseuses Kobo, et j'ai toujours été satisfait de leur produit. Mais il y a un point qui m'a toujours dérangé: avoir des bandes blanches sur les côtés de mes mangas. Les liseuses ne sont pas gigantestes, et perdre de l'espace de lecture c'est quand même dommage.

C'est pour ça que j'avais commencé à m'intéresser aux logiciels qui permet de transformer des images en fichiers CBZ, un format de fichier qui permet de lire des mangas sur une liseuse. Ces logiciels permettent d'optimiser les images pour qu'elles soient bien affichées sur une liseuse, et de les mettre dans un fichier zip pour que la liseuse puisse les lire.

J'avais testé deux logiciels : [Mangle](https://github.com/FooSoft/mangle) et [KCC](https://github.com/ciromattia/kcc). J'avais préféré Mangle, car il était bien plus simple à utiliser. J'avais donc commencé à l'utiliser pour transformer mes mangas en fichiers CBZ.

Je l'avais modifié pour rajouter deux options :
    
    * La possibilité de choisir l'ordre de découpage des images (de gauche à droite ou de droite à gauche je ne sais plus, mais une seule était disponible)
    * La possibilité de découper l'image pour enlever au maximum les bandes blanches, et même les numéros de pages afin de gagner en espace de lecture.

Ces modifications étaient assez simples, le code était en Python2 et Qt3, encore d'actualités à l'époque. Je les avais proposées au développeur de Mangle. Il les avait acceptées, et j'avais continué à utiliser Mangle.

<center><img src='/images/79/mangle_screenshot.png'></center> 

Et jusque-là, tout allait bien. 


# Nouvelle liseuse, nouveau problème, nouveau projet

J'utilisais une version compilée de Mangle, et je n'avais pas eu besoin de faire de modifications depuis des années. Mais récemment, j'ai changé de liseuse pour une `Kobo Elipsa 2e`, avec une nouvelle résolution. Et là, j'ai eu un problème : rajouter la nouvelle liseuse était trivial, mais le logiciel était en `Python 2` et `Qt3`. Autant dire que réussir à lancer la version de dev était désormais un exploit en soi en 2024.

Je reviendrai dans un prochain article sur les problèmes de migrations de Python 2 et Qt3.

Je m'aperçois alors que le projet Mangle est archivé, et que le développeur n'a pas l'intention de le mettre à jour. J'ai donc décidé de le forker pour le mettre à jour.

Tant qu'à faire, j'ai décidé de l'adapter à mon propre besoin. Depuis 10 ans, je faisais tout le temps les mêmes paramétrages dans l'outil à chaque lancement. Ce n'était pas assez embétant pour justifier un fix, surtout si je devais justifier les choix auprès du développeur principal.

Mais là, tant qu'à reprendre les rennes, autant adapter à mon usage.

Je me suis donc posé un peu, et j'ai listé ce que je voulais enlever, changer ou rajouter.

Vient alors un moment que je redoute : le moment où je dois choisir un nom pour mon projet `(ง︡’-‘︠)ง`.

Je cherche un nom japonisant, et je tombe sur `Henkan`, qui signifie "conversion" en japonais. C'est parfait, c'est exactement ce que je veux faire : convertir des images en fichiers CBZ (ou PDF pour les Kindle, merci Amazon).

Je présente le nom à mes enfants, et mon petit dernier se trompe et l'appelle `Henskan`. Ça sonne encore mieux, et ça rappelle les "scan" de manga. C'est parfait, je garde ce nom. `(っ∩_∩)っ`

`Henskan` était né, et c'est parti pour son développement qui va m'occuper pendant les quelques semaines de vacances que j'ai eu entre mon départ de Pony et mon arrivée chez Contentsquare.

<center><img src='/images/common/coder.gif'></center> 

Voici ce que ça donne au final, et qu'on va analyser dans le futur :

<center><img src='/images/79/henskan_screenshot.png'></center>