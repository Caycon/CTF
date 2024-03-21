- Chall sử dụng 1 chút kiến thức về Diffie–Hellman. Ta sẽ sử dụng discrete_log để giải quyết chall này.
```Python
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
from Crypto.Util.Padding import unpad
from hashlib import sha256
p = 0xdd6cc28d
F = GF(p)
g = F(0x83e21c05)
A = F(0xcfabb6dd)
B = F(0xc4a21ba9)
ciphertext = b'\x94\x99\x01\xd1\xad\x95\xe0\x13\xb3\xacZj{\x97|z\x1a(&\xe8\x01\xe4Y\x08\xc4\xbeN\xcd\xb2*\xe6{'
a = discrete_log(A, g)
C = B^a
hash = sha256()
hash.update(long_to_bytes(int(C)))
key = hash.digest()[:16]
iv = b'\xc1V2\xe7\xed\xc7@8\xf9\\\xef\x80\xd7\x80L*'
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(ciphertext)
flag = unpad(decrypted, 16)
print(flag)
```
![image](https://github.com/Caycon/CTF/assets/97203151/60fbfac5-2b8b-4b83-ab3f-a5bc8f1747d7)
