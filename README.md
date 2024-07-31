# Challenge

## SALOON (VOIE)

### Lore :

Il y a toujours des infos qui tournent dans un saloon, ça serait intéressant d’y faire un tour.
*Il y a un routeur wifi pour que tout le monde se connecte*

### Technique :
 
Trouve le mot de passe de la wifi (un truc facile à casser) pour se connecter et analyser le réseau et trouver le numéro de la voie du train

Mot de passe de la wifi : KAcA1234
ce sera du wep (indice 1) 




## GARE SNCTF (UID, permet de vérifier les informations)

### Lore : 
La gare vient tout juste de mettre en place un nouveau système pour héberger des informations relativement précises sur les trains. Mais il y a des trains cacher et avec l’injection on peut les voirs


### Technique : 
SQL injection pour avoir tout la bdd est trouver le bon train avec les informations que tu as récupéré avant.
Front avec un tableau des trains
API web pour avoir les trains, ya une catégorie train secret qu on peut accéder avec une vuln
Une chier de données, ils doivent trouver le bon train avec les infos avant, date heure voie.


## Prison/sheriff (wagon)
### Lore : 
Malgré sa passion pour les enfants, un prisonnier s’est fait choper pour avoir tenté le braquage du siècle. Il pourrait connaître l’emplacement de la cargaison.

Un mec était sur le coup mais il s’est fait chopper avant par le shérif, il est en prison ducoup. Mais il a peut-être une info sur le train. Mais il faut aussi trouver le prisonnier.

### Technique : 
Tu te co en visiteur dans la prison, et il faut s’augmenter les privilèges de 2 façons différentes avant d’avoir les droits pour accéder à la cellule du prisonnier concerné

1er Escalation : OTP Key reuse, mdp de gardien est un des strings à retrouver
2ème Escalation : Exploitation mauvaise config des droits sudo pour pouvoir exécuter des commandes en root.
 

## Banque (Heure)

### Lore: 
Ils ont développé leur propre algorithme de chiffrement pour sécuriser leurs données. 
Site vitrine avec “Pour nous contacter envoyer le mail ici : adresse email”
Boite mail, envoie avec pj et un bot qui l’ouvre 
Après dans les mails ya l’heure chiffré, on a accès à l’algo de chiffrement custom claqué et ya une bd avec la clé

### Technique : 
Ouverture auto du bot pour exec la png (RCE)
Accès au mail. Et il y a le mail chiffré avec l’info de l’heure. 
La clé de l’algo est dans la bdd. Et l’algo est dans un git sur le serveur. 





## Mairie (Date)

### Lore : 
Le site de la mairie et il est pété


### Technique : 
Une idor sur les événements listé par la mairie, ya une partie publique et une partie privé pour plusieurs event. Dans la bonne partie privée il y’a un fichier binaire, il faut le reverse pour avoir le flag.



# Projet-Annuel-ESGI4
