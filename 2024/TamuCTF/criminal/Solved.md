**Chall:**
- [server.py](https://github.com/Caycon/CTF/blob/main/2024/TamuCTF/criminal/server.py)

**Solved:**
- Với chall này mình sẽ khai thác ở hàm `compress`. Và sau khi tìm hiểu thì ta thấy được hàm này liên quan đến len của chuỗi.
- Ta thử và nhận ra khi ký tự đó đúng với flag thì len sẽ  bé hơn 1 khi mà ký tự sai.
- Ta sẽ brute force flag:

```Python
from pwn import *

context.log_level = "debug"
io = remote("tamuctf.com", 443, ssl=True, sni="criminal")
a = "}{abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789"
flag= 'gigem{'
x= flag+ '$'
io.recvuntil(b'Append whatever you want to the flag: ')
io.sendline(x)
data = io.recvuntil(b'\n',drop=True).decode()
data = base64.b64decode(data)
for j in range (20):
    for i in a:
        print(i)
        x= flag+ i
        io.recvuntil(b'Append whatever you want to the flag: ')
        io.sendline(x.encode())
        data1= io.recvuntil(b'\n',drop=True).decode()
        data1= base64.b64decode(data1)
        if len(data)> len(data1):
            flag= flag+ i
            break
print(flag)
# flag: gigem{foiledagain}
```
