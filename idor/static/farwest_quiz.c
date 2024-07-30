#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <dlfcn.h>
#include <errno.h>
#include "libflag_data.h"

// Fonction pour créer un fichier en mémoire, écrire des données dans ce fichier,
// et charger ce fichier comme une bibliothèque partagée.
void hidden_file() {

    // Créer un fichier en mémoire
    int fd = memfd_create("hidden_flag", 0);
    if (fd == -1) {
        perror("memfd_create"); // Afficher une erreur en cas d'échec
        exit(1);
    }

    // Écrire les données dans le fichier en mémoire
    if (write(fd, libflag_so, libflag_so_size) != libflag_so_size) {
        perror("write"); // Afficher une erreur en cas d'échec
        close(fd);
        exit(1);
    }

    // Construire le chemin d'accès au fichier en mémoire pour le chargement
    char s[256];
    sprintf(s, "/proc/self/fd/%d", fd);

    // Charger le fichier en mémoire comme une bibliothèque partagée
    void *handle = dlopen(s, RTLD_NOW);
    if (!handle) {
        fprintf(stderr, "Erreur dlopen: %s\n", dlerror()); // Afficher une erreur en cas d'échec
        close(fd);
        exit(1);
    }

    // Afficher un message indiquant que le fichier a été chargé comme bibliothèque partagée
    printf("Fichier en mémoire créé et chargé comme bibliothèque partagée.\n");

    // Décommenter et compléter ces lignes si vous souhaitez utiliser la fonction `reveal_flag`
    /*
    void (*reveal_flag)();
    *(void **) (&reveal_flag) = dlsym(handle, "reveal_flag");
    if (!reveal_flag) {
        fprintf(stderr, "Erreur dlsym: %s\n", dlerror()); // Afficher une erreur en cas d'échec
        dlclose(handle); // Fermer la bibliothèque chargée avant de quitter
        close(fd);
        exit(1);
    }
    */

    // Fermer la bibliothèque partagée et le fichier
    dlclose(handle);
    close(fd);
}

// Fonction de quiz
void quiz() {
    char answer[11]; // Tableau pour stocker les réponses de l'utilisateur

    // Afficher le message de bienvenue
    printf("Bienvenue au quiz Farwest!\n");

    // Demander la date du conseil secret
    printf("Quel est le jour du conseil secret? (format: AAAA-MM-JJ)\n");
    scanf("%10s", answer); 
    printf("Réponse reçue: %s\n", answer);
    if (strcmp(answer, "2024-07-30") != 0) { 
        printf("Mauvaise réponse! Essayez encore.\n");
        exit(1); // Quitter en cas de mauvaise réponse
    }

    // Demander la capitale de l'Arizona
    printf("Quelle est la capitale de l'Arizona?\n");
    scanf("%10s", answer); 
    printf("Réponse reçue: %s\n", answer);
    if (strcmp(answer, "Phoenix") != 0) { 
        printf("Mauvaise réponse! Essayez encore.\n");
    }

    // Demander qui a tiré sur Jesse James
    printf("Qui a tiré sur Jesse James?\n");
    scanf("%10s", answer); 
    printf("Réponse reçue: %s\n", answer);
    if (strcmp(answer, "Bob Ford") != 0) { 
        printf("Mauvaise réponse! \n");
    }

    // Afficher un message de fin de quiz pour indiquer de faire un reverse
    printf("Pff dommage si seulement tu avais réfléchi à chercher en profondeur :(((()))).\n");
}

// Fonction main
int main() {
    quiz(); // Appeler la fonction quiz
    return 0;
}
