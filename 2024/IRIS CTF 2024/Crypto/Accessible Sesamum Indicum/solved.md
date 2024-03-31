- Challenge yêu cấu ta nhập bộ 4 số để pass qua 16 lần. Tuy nhiên lại có giới hạn về số lần gửi mã đi cũng như giới hạn về thời gian nhận với gửi tới sever.
```Python
from pwn import *
a= ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
m= str()
n= str()
for x in a:
    for y in a:
        for z in a:
            for t in a:
                m= x+ y+ z+ t
                n= n+ m
r = remote("accessible-sesasum-indicum.chal.irisc.tf", 10104)
r.recvuntil()
for i in range(16):
    r.sendline(n)
    r.recvline()
data= r.recvline()
print(data)
```
