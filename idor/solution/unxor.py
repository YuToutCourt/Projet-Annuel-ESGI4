# Flag chiffré
encrypted_flag = [0x13, 0x0e, 0x03, 0x14, 0x06, 0x3b, 0x72, 0x0f, 0x72, 0x74, 0x1f, 0x77, 0x30, 0x34, 0x01, 0x2d, 0x22, 0x73, 0x32, 0x1f, 0x76, 0x34, 0x73, 0x73, 0x2e, 0x14, 0x08, 0x3d]

# Clé de déchiffrement
key = 64  # Valeur de la clé en décimal

# Fonction pour déchiffrer le flag en utilisant XOR avec la clé
def xor_decrypt(encrypted_flag, key):
    decrypted_flag = ""
    for byte in encrypted_flag:
        decrypted_flag += chr(byte ^ key)  # XOR entre chaque byte du flag chiffré et la clé
    return decrypted_flag

# Déchiffrer le flag
decrypted_flag = xor_decrypt(encrypted_flag, key)

# Afficher le flag déchiffré
print("Le flag déchiffré est :", decrypted_flag)
