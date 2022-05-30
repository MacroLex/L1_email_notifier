# L1_email_notifier

# Description

  Nous trouvions qu’il était parfois facile de passer à côté de certaines infos à la fac (mails importants, partiels ou encore lorsque l'on reçoit beaucoup de mails d'un coup). En tant que jeunes, les mails ne sont pas notre moyen de communication privilégié. Nous cherchions donc un moyen de ne pas rater les mails importants, d'une façon la plus autonome possible.

Nous avons donc choisi de faire un petit gadget qui tiendrait sur le bureau, et ferait du son et de la lumière pour attirer notre attention lorsque l'on reçoit un mail et sans forcément avoir besoin de regarder l'écran.

Pour ceci nous avions fais un schéma au préalable :
![image](https://user-images.githubusercontent.com/101505188/170944775-60062ae5-500c-4622-94ba-5d61598b222e.png)


# Librairies 

  Pour élaborer notre projet nous avons utilisés :
  - Atome Feed
  - Feedparser
  - Pygame
  - Moteur ESpeakNG (Voix synthétique)

# Quelles sont les fonctionnalités de L'Email Notifier ? 

Un affichage sur écran HMDI (xpt   ).
Une lecture à haute voix grâce au moteur ESpeakNG qui pourra lire l'expéditeur du mail ainsi que son objet.
3 leds qui vont s'allumés lors de la réception d'un mail (Led qui clignoteront 7 fois)

# Quel Matériel utilisé pour notre projet ?

- Une RaspberryPi
- Un écran HDMI de 5 pouces
- Deux enceintes (récupérées d'un ancien projet)
- Des Câbles de branchements pour le circuit
- 3 LEDS
- Coque en bois

# Comment s'est organisé la conception ?
![image](https://user-images.githubusercontent.com/101505188/170942970-88e5cc3c-d247-4b3f-b236-1c92f01ca5fa.png)

# Projet toujours améliorable...

  Nous avons eu plusieurs idées plus techniques pour améliorer l'Email Notifier comme par exemple :
  - Pouvoir ajouter des animations sur l'écran afin d'améliorer l'ésthetique de celui-ci
  - Améliorer la voix synthétique afin d'avoir une voix de plus en plus fluide et "humaine"
  - Pouvoir le connecter sur téléphone et aussi pouvoir intéragir sur le boîtier depuis celui-ci
  - Personaliser le fonctionnement des LEDS en fonction de l'importance d'un mail (Un mail dont le mot "Partiel" (ou autre) apparaît, ou un mail venant d'un professeur tout simplement).

# Projet fini


