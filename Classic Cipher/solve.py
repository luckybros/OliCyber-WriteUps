alphabet = "abcdefghijklmnopqrstuvwxyz"

def decrypt(ciphertext, key):
    plaintext = ""
    for c in ciphertext:
        if 'a' <= c <= 'z':
            i = key.index(c)           
            plaintext += alphabet[i]   
            key = key[-1] + key[:-1]
        else:
            plaintext += c
    return plaintext


ciphertext = "xcqv{gvyavn_zvztv_etvtddlnxcgy}"

for i in range(1,26):
    key = alphabet[i:] + alphabet[:i]
    plain = decrypt(ciphertext, key)
    if "flag" in plain:
        print(plain)
        break
