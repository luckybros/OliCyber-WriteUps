from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes
from binascii import unhexlify

process = remote('rsa.challs.olicyber.it', 10300)

result = process.recvrepeat(timeout=0.5).decode().split()

numbers = [int(x) for x in result if x.isdigit()]

print(numbers)
p = numbers[0]
q = numbers[1]
e = numbers[2]

n = p * q
phi_n = (p-1)*(q-1)
d = pow(e, -1, phi_n)

process.sendline(str(n))
process.sendline(str(phi_n))
process.sendline(str(d))

result = process.recvrepeat(timeout=0.5).decode().split()
result = result[-1]
plain = result[:len(result)-1]
plain = plain[1:]
plain = plain[:-1]
print(plain)

plain = int.from_bytes(plain.encode(), byteorder='big')
cipher = pow(plain, e, n)

process.sendline(str(cipher))
result = process.recvrepeat(timeout=0.5).decode().split()

print(result)

iv = result[-5]
enc_key = result[-3]
token = result[-1]

iv = bytes.fromhex(iv)
enc_key = bytes.fromhex(enc_key)
token = bytes.fromhex(token)

enc_key = int.from_bytes(enc_key, byteorder='big')

key = pow(enc_key, d, n)
key = long_to_bytes(key)

cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(token)

print(pt)




