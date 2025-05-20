Title: Fangame sur  l'univers de Monsieur Plouf
Date: 2025-05-20 07:20
Category: Talk
Tags: godot, projet, plouf
Slug: fangame-plouf
Author: Jean Gabès
AuthorLogin: naparuba
Summary: J'ai codé un fangame sur l'univers du youtuber Monsieur Plouf.
id: 80
Status: ready

<center><img src='/images/80/article.png'></center>

# J'avais besoin de coder un truc

J'avais fini deux jeux, à savoir Sekiro et [Nine Sols](https://store.steampowered.com/app/1809540/Nine_Sols/?l=french), et je recommande très fortement ce dernier (moins Sekiro, trop focus sur les combats de boss). Ce jeu m'a pris pas loin de 30 heures. Or c'est un peu ma limite pour jouer, après j'ai envie de créer un truc.

Et là j'ai eu pour idée de faire un petit jeu, en [Godot](https://godotengine.org/). Je me suis dit que tant qu'à faire je vais faire un fangame sur l'univers d'un youtuber que j'aime bien : [Monsieur Plouf](https://www.youtube.com/@MonsieurPlouf), qui des chroniques très intéressantes et amusantes.

Et ça tombe bien, son univers est en 2d, et ça me va très bien. J'ai pensé un moment à faire un jeu de baston, genre en réutilisant le moteur [Mugen/Ikemen-go](https://ikemen-engine.github.io/), mais en regardant combien de sprite il fallait pour faire un combatant, et que le découpage de sprites c'est pas mon fort, j'ai cherché autre chose de plus réalisable.

Et là je me suis rapellé un petit jeu auquel j'ai joué et que j'avais bien aimé pour son efficacité: [Reigns](https://store.steampowered.com/app/474750/Reigns/?l=french).

Je me suis donc dit: et pourquoi pas refaire un Reigns, mais mode Monsieur Plouf? 

Etait né "Une semaine en tant que Monsieur Plouf" qui doit arriver à faire sa chronique à temps. Bon alors pour être honnête, Monsieur Plouf sort une vidéo toutes les deux semaines, mais ça sonnait moins bien comme titre :)

Voici a quoi ça ressemble:

<center><img src='/images/80/gameplay.png'></center> 

Le but principal du jeu est de vous faire passer un bon moment, et bien rigoler. Si ça c'est fait, j'ai réussi alors :)

# Gameplay

Le gameplay est assez simple:
 
   * on a une suite de problèmes
   * le joueur a deux réponses possibles
   * chaque réponse influe sur 4 critères qui sont indiqués en haut de l'écran, mais on ne sait pas quel impact précis ça va avoir
   * une réponse peut avoir un effet positif ou négatif sur les critères
   * si un critères tombe à 0 ou est au max, alors la partie est finie
   * il faut atteindre un certains nombres de problèmes pour gagner, dans mon cas j'ai choisi 50

Alors sur ordi on va gérer à la souris et manette (joystick), et sur téléphone ça sera au tactile, rien de bien méchant a priori, Godot aide bien.

Le gameplay est simple, et a priori Reigns est assez connu, donc les joueurs vont s'en sortir, mais à coder ce n'est pas si simple que ça en a l'air.


# Droits d'un fan game

Alors je mets de côté le fait que je ne sais pas dessiner, donc je vais me permettre de prendre des screenshots des chroniques comme base pour mes images. 

Que ce soit bien clair: je n'ai pas le *droit* de le faire, mais j'espère que vu que c'est un fangame open source et gratuit ça sera toléré. Mais dans les faits l'auteur original (Monsieur Plouf) n'aurait qu'à m'envoyer un email et je devrais supprimer toutes les images (et donc tuer le projet). C'est le risque des fangame, et soyons clair, si ça aurait été Nintendo je n'aurais pas pris le risque :) 


# Focus sur des points de gameplay

Alors on va vu que le gameplay est simple, mais pas simpliste non plus. Les problèmes et les choix doivent être assez clairs pour que le joueur arrive à deviner dans quel sens les critères vont évoluer.

## Impact des choix
Un des points importants est de lui faire comprendre qu'il est proche d'une limite. J'ai tenté de faire que les icones en haut de l'écrans soient assez explicite, mais ce n'était pas assez à mon goût, et l'effet restait limité.

<center><img src='/images/80/too-much.png'></center> 

Je me suis dit que si ça pouvait mettre le joueur dans le même état psychologique où doit être Monsieur Plouf ça serait très intéressant et plus immersif. Alors oui, j'écoute beaucoup les podcasts de Plouf et Pseudo et donc je fais un peu plus attention à ce genre de points désormais, et fan game ou pas, ça reste un jeu, donc c'est sérieux :)

On a donc plusieurs critères, et voici les impacts suivant si c'est trop haut ou trop bas:

  * vie de famille:
    * si trop bas, sa famille lui manque, donc la vie est fade: plus de couleurs et plus de son
    * si trop haut, c'est l'invasion: un sprite de sa fille et madame Plouf se balade sur l'écran et gènent le joueur
  * vitesse:
    * si trop bas: alors là c'est chaud, car Plouf n'a plus le temps, donc il doit rusher: le joueur n'a plus que 5s pour lire les réponses, après on cache les réponses! C'est clairement le pire impact :)
    * si trop haut: là Plouf va trop vite. Et je me suis toujours demandé: Flash il vite à 200 à l'heure, donc en fait les autres sont au ralenti, tout le temps? Il doit s'ennuyer sévère non? Là Plouf voit tout au ralenti :)
  * créativité:
    * si trop bas: le monde est brut, donc on voit plus les pixels et les textes sont plus "carrés"
    * si trop haut: là Plouf vit la créativité, et tout est psychédélique et flottant
  * popularité:
    * si trop bas: Youtube a oublié Plouf, dans plus de vidéo, ça se retranscrit dans le jeu par l'écran qui devient tout sombre de temps en temps 
    * si trop haut: là c'est trop populaire, Plouf se fait envahir par les marques, donc invasion de sprite d'éditeurs, avec notaement Konami, éditeur préféré de Monsieur Plouf.

## Cartes à gros impacts
Un autre point que j'ai changé par rapport à Reign original: de base j'ai mis un poids random et pas trop haut, mais j'ai aussi mis des cartes qui ont un gros impact (genre 3 fois plus qu'une carte normale). J'ai fait en sorte que visuellement ça se voit bien, j'espère que c'est le cas :)

<center><img src='/images/80/gros-impact.png'></center>

# Voila pour le gameplay
Si on rajoute le fait que Monsieur Plouf a 10 étapes à réaliser pour avoir une vidéo prête, on a notre progression avec 5 cartes par étapes, soit 50 cartes.

J'ai écrit presque 90 cartes pour que ça ne soit pas toujours les mêmes, mais idéalement il en faudrait encore d'autres. J'ai bien outillé cette partie d'ailleurs, c'est assez facile à rajouter, reste à avoir l'inspiration :)

Je me suis bien amusé à imaginer des trucs un peu loufoques, qui collent bien avec l'univers.

# Technique plus tard
On va vu la partie gameplay, on verra une autre fois la partie technique, avec notamment ce que j'ai appris au cours de ce projet: non pas le découpage propre des sprites, ça ... bon disons que c'est toujours compliqué. Non je parle des shaders, c'est plus simple que ce que je pensais, et on verra ça.

# Ok et le jeu il est dispo où?

Alors pour jouer c'est simple, vous avez plusieurs possibilité:

  * Jouer directement en web: [plouf.gabes.fr](https://plouf.gabes.fr)
  * Version pour [windows](https://plouf.gabes.fr/builds/win/)
  * Version pour [linux](https://plouf.gabes.fr/builds/linux/), je ne l'ai pas testé, mais a priori ça devrait être bon pour le Steam Deck
  * Version pour [Android](https://plouf.gabes.fr/builds/android/), testé et approuvé, ma version favorite :)

# C'est Open Source

Alors si on mets de côté les images, c'est Open Source (licence MIT, open bar quoi). Donc si vous voulez fixer un bug (on sait jamais), ou alors rajouter des cartes rigolotes, faut pas hésiter à venir participer: [https://github.com/naparuba/plouf](https://github.com/naparuba/plouf)

Bon jeu!