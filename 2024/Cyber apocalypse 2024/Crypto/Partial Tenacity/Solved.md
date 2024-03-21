- Với chall này ta sẽ khôi phục từng số của  p, q. Với p, q được cung cấp sẽ là  p, q gốc nhưng lần lượt bị xóa đi các số ở vị trí chẵn hoặc lẻ.
`leak_p = '1_5_1_4_4_1_4_7_3_3_5_7_1_3_6_1_5_2_9_8_5_2_1_6_9_8_0_3_9_7_5_2_5_5_9_1_3_0_5_8_7_5_0_9_4_2_8_8_7_3_8_8_2_0_6_9_9_0_6_9_2_7_1_6_7_4_0_2_2_1_6_7_9_0_2_6_4_3'`
`leak_q = '_1_5_6_2_4_3_4_2_0_0_5_7_7_4_1_6_6_5_2_5_0_2_4_6_0_8_0_6_7_4_2_6_5_5_7_0_9_3_5_6_7_3_9_2_6_5_2_7_2_3_1_7_5_3_0_1_6_1_5_4_2_2_3_8_4_5_0_8_2_7_4_2_6_9_3_0_5_'`
- Ta sẽ khôi phục với code sau dựa vào 1 trong 2 số ở vị trí tương ứng đã biết trong  p, q.
```Python
from math import sqrt
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
n = 118641897764566817417551054135914458085151243893181692085585606712347004549784923154978949512746946759125187896834583143236980760760749398862405478042140850200893707709475167551056980474794729592748211827841494511437980466936302569013868048998752111754493558258605042130232239629213049847684412075111663446003
ct = bytes.fromhex('7f33a035c6390508cee1d0277f4712bf01a01a46677233f16387fae072d07bdee4f535b0bd66efa4f2475dc8515696cbc4bc2280c20c93726212695d770b0a8295e2bacbd6b59487b329cc36a5516567b948fed368bf02c50a39e6549312dc6badfef84d4e30494e9ef0a47bd97305639c875b16306fcd91146d3d126c1ea476')
p1 = 151441473357136152985216980397525591305875094288738820699069271674022167902643
q1 = 15624342005774166525024608067426557093567392652723175301615422384508274269305
pbit = ''.join(['1' if i % 2 == 0 else '0' for i in range(155)])
qbit = ''.join(['1' if i % 2 == 1 else '0' for i in range(155)])
p= 0
q= 0
p2= p1
q2= q1
for i in range(155):
    if pbit[-(i+1)] == '1':
        x = 10**(i+1)
        p = 10**i * (p2 % 10) + p
        for d in range(10):
            Checkprime = 10**i * d + q
            if n % x == p * Checkprime % x:
                a = Checkprime
                b = p2 // 10
                p= p
                q= a
                p2= b
    else:
        x = 10**(i+1)
        q = 10**i * (q2 % 10) + q
        for d in range(10):
            Checkprime = 10**i * d + p
            if n % x == q * Checkprime % x:
                a = Checkprime
                b = q2 // 10
                q= q
                p= a
                q2= b
e = 0x10001
d = pow(e, -1, (p-1)*(q-1))
key = RSA.construct((n, e, d))
flag = PKCS1_OAEP.new(key).decrypt(ct)
print(flag)
```
- Flag:`b'HTB{v3r1fy1ng_pr1m3s_m0dul0_p0w3rs_0f_10!}'`
