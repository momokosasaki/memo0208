from pwn import *
context(os="linux", arch="amd64")
print asm(shellcraft.linux.sh())

