// libflag.c
#include <stdio.h>
#include <string.h>

void reveal_flag() {
    // Flag chiffre
    unsigned char encrypted_flag[] = {
        0x13, 0x0e, 0x03, 0x14, 0x06, 0x3b, 0x72, 0x0f, 0x72, 0x74, 0x1f, 0x77, 0x30, 0x34, 0x01, 0x2d, 0x22, 0x73, 0x32, 0x1f, 0x76, 0x34, 0x73, 0x73, 0x2e, 0x14, 0x08, 0x3d
    };

    // clé pour chiffré le flag
    unsigned char key = 64;

    // Taille du flag chiffre
    int len = sizeof(encrypted_flag) / sizeof(encrypted_flag[0]);

    // Afficher le flag chiffre
    printf("encrypted_flag = [");
    for (int i = 0; i < len; i++) {
        printf("0x%x", encrypted_flag[i]);
        if (i < len - 1) {
            printf(", ");
        }
    }
    printf("]\n");

    // Afficher la cle
    printf("Key: %u\n", key);
}

int main() {
    reveal_flag();
    return 0;
}
