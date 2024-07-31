import sys

if len(sys.argv) != 2:
    print("Usage: python convertlib.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'rb') as f:
    content = f.read()

print(f"unsigned char libflag_so[] = {{")
for i in range(0, len(content), 16):
    chunk = content[i:i+16]
    print("    " + ", ".join(f"0x{byte:02x}" for byte in chunk) + ",")
print(f"}};")
print(f"unsigned int libflag_so_size = {len(content)};")
