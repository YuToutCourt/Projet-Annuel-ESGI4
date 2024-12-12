# Write Up

## Crack le réseau WEP

Rien de plus compliqué, c'est un crackage de mot de passe WEP qui a de plus simple.
m
Un cours tutoriel pour crack le ot de passe WEP d'un réseau wifi avec john the ripper.

```bash
$ john --wordlist=<wordlist> --stdout --session=upc1 | aircrack-ng -w - -b <target_mac> <fichier.cap>
```

Il vous faudra juste identifier les bonnes adresses MAC


## Trouver le flag

Bien, maintenant qu'on a cracké le mot de passe wifi, on peut naviguer dans les trames pour trouver notre flag. 
On va se servir de l'outil TSHARK fourni avec Wireshark.

```bash
tshark -r capture.pcap -Y 'data.text == "FLAG"'
```

Si tout est OK, vous allez trouver le flag en un rien de temps.

Bonne chance pour la suite !