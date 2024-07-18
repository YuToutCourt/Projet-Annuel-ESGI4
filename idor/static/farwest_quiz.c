#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <dlfcn.h>
#include <errno.h>
#include "libflag_data.h"


void hidden_file() {
    int fd = memfd_create("hidden_flag", 0);
    if (fd == -1) {
        perror("memfd_create");
        exit(1);
    }

    if (write(fd, libflag_so, libflag_so_size) != libflag_so_size) {
        perror("write");
        close(fd);
        exit(1);
    }

    char s[256];
    sprintf(s, "/proc/self/fd/%d", fd);

    void *handle = dlopen(s, RTLD_NOW);
    if (!handle) {
        fprintf(stderr, "Erreur dlopen: %s\n", dlerror());
        close(fd);
        exit(1);
    }

    printf("Fichier en mémoire créé et chargé comme bibliothèque partagée.\n");

/*    void (*reveal_flag)();
    *(void **) (&reveal_flag) = dlsym(handle, "reveal_flag");
    if (!reveal_flag) {
        fprintf(stderr, "Erreur dlsym: %s\n", dlerror());
        dlclose(handle);
        close(fd);
        exit(1);
    }*/

    dlclose(handle);
    close(fd);
}

void quiz() {
    char answer[11];
    printf("Bienvenue au quiz Farwest!\n");

    printf("Quel est le jour du conseil secret? (format: AAAA-MM-JJ)\n");
    scanf("%10s", answer);
    printf("Réponse reçue: %s\n", answer);
    if (strcmp(answer, "2024-07-30") != 0) {
        printf("Mauvaise réponse! Essayez encore.\n");
        exit(1);
    }

    printf("Quelle est la capitale de l'Arizona?\n");
    scanf("%10s", answer);
    printf("Réponse reçue: %s\n", answer);
    if (strcmp(answer, "Phoenix") != 0) {
        printf("Mauvaise réponse! Essayez encore.\n");
    }

    printf("Qui a tiré sur Jesse James?\n");
    scanf("%10s", answer);
    printf("Réponse reçue: %s\n", answer);
    if (strcmp(answer, "Bob Ford") != 0) {
        printf("Mauvaise réponse! \n");
    }

    printf("Pff dommage si seulement tu avais réfléchi à chercher en profondeur :(((()))).\n");
}

int main() {
    quiz();
    return 0;
}
