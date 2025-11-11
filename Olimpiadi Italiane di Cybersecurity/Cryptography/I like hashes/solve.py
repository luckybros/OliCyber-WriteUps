import hashlib
import string

file_name = "/Users/luketto/Documents/Olicyber/I like hashes/ct.txt"

list_hash = []

with open(file_name, 'r') as file:
    for line in file:
        list_hash.append(line.rstrip())

alphabet = string.ascii_letters + string.digits + string.punctuation

hash_map = {}

for char in alphabet:
    hash_map[hashlib.sha256(char.encode('utf-8')).hexdigest()] = char

result = ""

for i in range(len(list_hash)):
    result = result + hash_map[list_hash[i]]

print(result)
