- Sau khi tìm hiểu thì tôi nhận thấy rằng Salsa20 khá tương đồng với AES, nên nếu có được state thì ta sẽ decrypt được.
```Python
from pwn import *
from Crypto.Util.number import long_to_bytes
import binascii
def ROTL(a, b):
    return (((a) << (b)) | ((a % 2**32) >> (32 - (b)))) % 2**32
def qr(x, a, b, c, d):
    x[a] += x[b]; x[d] ^= x[a]; x[d] = ROTL(x[d],16)
    x[c] += x[d]; x[b] ^= x[c]; x[b] = ROTL(x[b],12)
    x[a] += x[b]; x[d] ^= x[a]; x[d] = ROTL(x[d], 8)
    x[c] += x[d]; x[b] ^= x[c]; x[b] = ROTL(x[b], 7)
ROUNDS = 20
def chacha_block(inp):
    x = list(inp)
    for i in range(0, ROUNDS, 2):
        qr(x, 0, 4, 8, 12)
        qr(x, 1, 5, 9, 13)
        qr(x, 2, 6, 10, 14)
        qr(x, 3, 7, 11, 15)

        qr(x, 0, 5, 10, 15)
        qr(x, 1, 6, 11, 12)
        qr(x, 2, 7, 8, 13)
        qr(x, 3, 4, 9, 14)

    return [(a+b) % 2**32 for a, b in zip(x, inp)]

r = remote('babycha.chal.irisc.tf', 10100)
r.sendlineafter(b'> ', b'1')
r.sendlineafter(b'? ', b'\x00'*64)
state_hex = r.recvuntil(b'\n')[:-1]
state = [int(state_hex[i:i+8], 16) for i in range(0, len(state_hex), 8)]

state = chacha_block(state)
buffer = b"".join(long_to_bytes(x).rjust(4, b"\x00") for x in state)

r.sendlineafter(b'> ', b'2')
ct = r.recvuntil(b'\n')[:-1]
ct = binascii.unhexlify(ct)

flag = b''
for i in range(len(ct)):
    flag += bytes([ct[i] ^ buffer[i]])
print(flag)
```
