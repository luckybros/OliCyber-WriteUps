import string

def xor(a, b):
    return bytes([ x ^ y for x,y in zip(a,b) ])

file_name = "/Users/luketto/Documents/Olicyber/Cryptography/1337_XOR/output.txt"

with open(file_name, 'r') as file:
    line = file.readline().strip()

ciphertext = line.split()[1]

ciphertext = bytes.fromhex(ciphertext)

plaintext = b"flag{1"

key = bytearray()

for i in range(6):
    key_char = ciphertext[i] ^ plaintext[i]
    key.append(key_char)

print("Plaintext:", xor(ciphertext, key * (len(ciphertext)//len(key) + 1)))
