import binascii

# Encodez une image en hexadécimal
def encode_image_to_hex(input_image_path, output_hex_path):
    with open(input_image_path, 'rb') as image_file:
        image_data = image_file.read()
        hex_data = binascii.hexlify(image_data)
        with open(output_hex_path, 'w') as hex_file:
            hex_file.write(hex_data.decode('utf-8'))

# Décodez une image à partir de l'hexadécimal
def decode_image_from_hex(input_hex_path, output_image_path):
    with open(input_hex_path, 'r') as hex_file:
        hex_data = hex_file.read()
        image_data = binascii.unhexlify(hex_data)
        with open(output_image_path, 'wb') as image_file:
            image_file.write(image_data)

# Exemple d'utilisation
input_image_path = 'Capture.PNG'
output_hex_path = 'image_hex.txt'
output_image_path = 'output_image.png'

encode_image_to_hex(input_image_path, output_hex_path)
decode_image_from_hex(output_hex_path, output_image_path)