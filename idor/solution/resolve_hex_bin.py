with open('exe.txt', 'rb') as f:
    data = f.read().split()

val = [int(hex_data, 16) for hex_data in data]
res = bytes(val)

with open('flag', 'wb') as f:
    f.write(res)