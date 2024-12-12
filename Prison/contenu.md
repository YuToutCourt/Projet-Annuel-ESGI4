password root : zoulette
password cowboy: cowboy

# 1er étape : 

Le user se connecte à la box en tant que le user visiteur en ssh. (User Cowboy)

Ce user accède alors à la prison, plusieurs dossiers : salle_d_attente, salle_de_visite, cellules

Il a accès a la salle_de_visite et la salle_d_attente, pas d'accès aux cellules.

Dans salle_d_attente, un dialogue avec le sherrif donnera une info importante. 
Comme quoi il utilise OTP avec une clé pour tout les mots de passe

Il y a aussi un `wanted` qui nous doit
```
J'ai entendu le shérif parler avec l'un des gardiens.
Il a prononcé le mot : )&.)(&>(
Je n'ai rien compris, mais je crois que c'est le code pour rentrer dans le vestiaire des gardiens...
```

Jamie qui parle de `Crib Dragging!`

Dans salle_de_visite avec un `ls -la` on peut voir un dossier `.table` qui contient ce fichier 
cle.txt

```txt
Vous regardez sous la petite table et vous trouvez une clé : A?I??I?F

Mais elle semble un peu cassée, sûrement une ancienne clé oubliée.
Il est sûrement possible de la réparer ?
```

Vuln : OTP password avec réutilisation de clé (Crib Dragging!)

la clé correcte: AOIAFIQF

Pour trouver la clé 

`)&.)(&>(` == `highnoon`

Connexion en tant que gardien avec le mdp trouvé

`su gardien`

# 2 eme étape :
Pour accéder aux cellules, le user doit se connecter en tant que garde pour pourvoir avoir accès à /cellules.

Pour cela il doit obtenir les droits root, pour cela, il peut faire sudo -l et voir qu'il peut utiliser sudo

Exploit : `sudo sudo cat cellules/billy/billy.txt`
SNCTF{w4g0n_C4_boum}



## Image Docker

https://hub.docker.com/layers/gizm0o/ctf/prison/images/sha256-61f2c5b50d59a535e04be4790cef6b0d95545e02e1e21a48f321b93ded64b7eb?context=repo

docker pull gizm0o/ctf:prison



apt install -y openssh-server
service ssh status
service ssh start
passwd cowboy
cowboy
cowboy
chsh -s /bin/bash cowboy
chsh -s /bin/bash gardien
vi /etc/ssh/sshd_config                                 # Modifier la ligne #Banner pour mettre Banner /etc/mybanner
vi /etc/mybanner                                         # Lien de la banner: https://www.asciiart.eu/comics/lucky-luke
service ssh restart
cd /home/prison/salle_d_attente
rm luke.txt
vi wanted.txt
```
J'ai entendu le shérif parler avec l'un des gardiens.
Il a prononcé le mot : )&.)(&>(
Je n'ai rien compris, mais je crois que c'est le code pour rentrer dans le vestiaire des gardiens...
```
vi jamie.txt
```
Vive le Crib Dragging!
```
cd ../salle_de_visite
rm -rf abh billy dalton samuel
mkdir .table
vi .table/cle.txt
```
Vous regardez sous la petite table et vous trouvez une clé : A?I??I?F

Mais elle semble un peu cassée, sûrement une ancienne clé oubliée.
Il est sûrement possible de la réparer ?
```
cd ../cellules/billy/
vi billy.txt                     # Rajouter le flag : SNCTF{w4g0n_C4_boum} 



# OLD VERSION

password root : zoulette
password cowboy: cowboy

# 1er étape : 

Le user se connecte à la box en tant que le user visiteur en ssh.

Ce user accède alors à la prison, plusieurs dossiers : salle_d_attente, salle_de_visite, cellules

Il a accès a la salle_de_visite et la salle_d_attente, pas d'accès aux cellules.

Dans salle_d_attente il y a rien d'intéressant, juste quelques dialogues/blagounettes. Un dialogue avec le sherrif donnera une info importante.

Vuln : OTP password avec réutilisation de clé

la clé : AOIAFIQF

mdp: highnoon : )&.)(&>(
string : password : 1.:21&#"

Connexion en tant que gardien avec le mdp trouvé


# 2 eme étape :
Pour accéder aux cellules, le user doit se connecter en tant que garde pour pourvoir avoir accès à /cellules.

Pour cela il doit obtenir les droits route, pour cela, il peut faire sudo -l et voir qu'il peut utiliser sudo

Exploit : sudo sudo cat cellules/flag.txt