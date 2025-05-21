Title: Fangame sur  l'univers de Monsieur Plouf
Date: 2025-05-25 07:20
Category: Talk
Tags: godot, projet, plouf
Slug: fangame-plouf-shaders
Author: Jean Gabès
AuthorLogin: naparuba
Summary: Entrons dans le monde merveilleux des Shaders de sprite
id: 81
Status: ready

<center><img src='/images/81/article.jpg'></center>

# Les shaders: ce que j'avais toujours évités soigneusement

J'ai a mon actif quelques petits développements avec [Godot](https://godotengine.org/), principalement en 2d. Alors bidouiller des sprites avec Gimp ça va a peu près, mais il y a un sujet que j'ai toujours soigneusement évité: les [shaders](https://fr.wikipedia.org/wiki/Shader).

J'ai déjà eu besoin de shaders, genre surligner le contour d'un sprite, mais j'avais fait comme tout bon dev: un bon gros copier coller sans trop chercher à comprendre, et hop fini ᕦ(ò_óˇ)ᕤ

Après je connais le principe des shaders: ce sont des opérations codés dans un simili-C (déjà là ça motive pas des masses) qui peuvent jouer sur les pixels, et appelé un à un avec un très fort parallélisme.

Mais là où ça devient rigolo c'est qu'on a une vision totalement locale, point de structure globale à portée, car le but est de faire du parallélisme sur GPU, et une structure globale en GPU c'est la mort des performances.

# Bon on y arrive: j'ai vraiment besoins des shaders, on mélange deux sprites

Arrive le projet de [fangame Monsieur Plouf](https://github.com/naparuba/plouf). Après quelques tests pour faire bouger de droite à gauche un sprite suivant le mouvement de la souris ou doigt, et j'avais des images avec les personnages.

Mais j'ai voulu les mettre dans des décors, et là ça devient plus complexe, car synchroniser les deux sprites et gérer les inputs des souris c'était faisable, mais galère à coder.

J'ai donc rajouté des images de background, et le tout en png, car j'aime bien la transparence.

Maintenant il fallait mélanger les deux.

Et en fait c'est assez simple. De base on a la texture du personnage, avec des pixels de couleurs pour le perso, et des pixels en alpha transparent ... bah là où c'est transparent.

On va fournir aux sprite du personnage un second sprite, celui du background:

  * si on a un pixel du personnage qui est non transparent: on le garde
  * si c'est un transparent, on met à la place le pixel issu de la même position du background

Voila, ce n'est pas plus compliqué que ça.

# Show me the code

Voici ce que donne le code en question:

    shader_type canvas_item;
    
    uniform sampler2D backTexture;

    vec4 back_rgb = texture(backTexture, UV);
	if (COLOR.a == 0.0){
		COLOR = back_rgb;
	}

Et oui, c'est tout.

Alors voyons ça:

    shader_type canvas_item;

Pour avoir un shader dans Godot, si j'ai bien compris il y a plusieurs dialectes de shaders, ici je ne parlerai que de ceux de Godot 4.

    uniform sampler2D backTexture;

Pour charger la texture du back. Tout le parsing du PNG et cie est géré par Godot, on a juste à lui filer le .png chargé et hop, réglé. Merci Godot.

    vec4 back_rgb = texture(backTexture, UV);

Ici on va récupérer le pixel (``vector 4, RGB + alpha``) dans la backTexture, et à la position ``UV`` (c'est une constante que donne le shader quand il s'exécute).

    if (COLOR.a == 0.0){
		COLOR = back_rgb;
	}

On regarde alors l'alpha (``.a``) et s'il est transparent (``0.0``) dans ``COLOR`` qui est le pixel qu'on est en train de gérer, donc celui de la texture du personnage, alors on y colle le pixel du fond.

Voila, ce n'est pas plus compliqué que ça.

Il faut dire que le plus gros du travail, à savoir le parsing du PNG et tout ce genre de trucs, pas passionnant pour un sous, est fait par le moteur.

On arrive donc à avoir à partir de ce sprite:
<center><img src='/images/81/PLOUF_HESITE.png'></center> 

avec comme paramètre de shader ce sprite ci:
<center><img src='/images/81/BACK_BUREAU.png'></center> 

On arrive à notre résultat:
<center><img src='/images/81/melange.png'></center> 
  

# Un autre usage?

Une carte n'est pas a bord carré, ça ne serait pas très joli. J'aimerai avoir des bords ronds.

Ok, donc prends Gimp, tu modifies tous les PNG des fonds et hop.

Alors oui, mais non:

  * déjà c'est long,
  * je ne sais pas faire ça avec gimp,
  * et si j'ai un perso un peu large il dépasserait. 

Bref, ce n'est pas une bonne solution.

Et là on va ressortir notre petit copain shader: on va faire des coins arondis, tout simplement en mettant l'alpha des pixels dans les coins à ``0.0``.

Ok facile, voila fini.

Bon alors non, ce n'est pas si simple. On a DEJA un shader sur notre texture, et dans Godot on ne peut pas en appliquer deux à la suite, ou en tout cas pas facilement (il y a une histoire de viewports, mais ça a l'air d'être un tel bordel que j'ai abandonné ce truc qui ressemble à une bombe atomique pour écraser une mouche).

Donc il va falloir rajouter notre calcul à notre shader déjà existant:
   * On regarde si on est dans un pixel de coin et on mets l'alpha
   * sinon on applique le mélange entre la texture du personnage et la texture du fond


# Code de l'arrondi de 10 pixels dans chaque coins
Voici le bout du code pour savoir si on est dans un coin arrondi :

    uniform float corner_radius : hint_range(0.0, 20.0) = 10.0;
    uniform vec2 texture_size = vec2(300.0, 300.0);
    
    vec2 pixel_pos = UV * texture_size;
    
    bool in_bottom_left = pixel_pos.x < corner_radius && pixel_pos.y > (texture_size.y - corner_radius);
	bool in_bottom_right = pixel_pos.x > (texture_size.x - corner_radius) && pixel_pos.y > (texture_size.y - corner_radius);
	bool in_top_left = pixel_pos.x < corner_radius && pixel_pos.y < corner_radius;
	bool in_top_right = pixel_pos.x > (texture_size.x - corner_radius) && pixel_pos.y < corner_radius;

    // Calcul de la distance au coin
	float corner_dist = 0.0;
	if (in_bottom_left) {
		corner_dist = length(pixel_pos - vec2(corner_radius, texture_size.y - corner_radius));
	} else if (in_bottom_right) {
		corner_dist = length(pixel_pos - vec2(texture_size.x - corner_radius, texture_size.y - corner_radius));
	} else if (in_top_left) {
		corner_dist = length(pixel_pos - vec2(corner_radius, corner_radius));
	} else if (in_top_right) {
		corner_dist = length(pixel_pos - vec2(texture_size.x - corner_radius, corner_radius));
	}

    bool is_outside_corner = (in_bottom_left || in_bottom_right || in_top_left || in_top_right) && (corner_dist > corner_radius);
	if (is_outside_corner) {
		COLOR.a = 0.0;
		discard;
	}
    
C'est ma méthode, et j'imagine que c'est loin d'être la méthode la plus optimale. De mon côté je regarde si on est dans un carré de 10 par 10 dans un des 4 coins.

À savoir qu'ici je regarde une valeur absolue en nombres de pixels, et ``UV`` est en fait un couple de float entre ``0.0`` et ``1.0`` sur où est-ce qu'on est dans la texture.

Puis je regarde à quelle distance on est du coin en question. Si on est à une distance plus grande que 10, alors on mets en alpha. Ainsi, on a un joli arrondi de 10pixels. C'est comme utiliser un compas dans un carré, si on prend la taille du carré et qu'on se place à un coin, alors hop, arrondi.

C'est plus lourds à calculer qu'un mélange de pixels, mais en fait vu qu'on ne le fait que sur une seule texture à la fois, les performances ne sont vraiment pas notre problème, ça m'arrange :)

Voici le résultat:
<center><img src='/images/81/carte.png'></center> 

Le code est disponible sur le [répo](https://github.com/naparuba/plouf/blob/db12a7f45a670f2fad1e875139a4d4e854abdf14/shaders/dissolve.gdshader). Attention, il fait d'autres actions que juste mélanger les sprite et arrondir les angles.

Voila, c'est tout pour aujourd'hui pour nos shaders.

Alors dans les faits j'en ais d'autres en stocks, mais il me semble que ces deux là sont les plus parlant et utiles pour commencer.

Désormais vous n'avez plus d'excuses pour éviter les shaders, au final ce n'est pas si complexe qu'on pourrait le croire ``(⌐■_■)``