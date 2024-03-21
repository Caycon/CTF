- Cơ bản thì đây là AES mode CBC. Nên ta chỉ cần decrypt ngược lại là thu được flag.
```Python
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from Crypto.Util.Padding import unpad

DELTA = 0x9e3779b9

def decrypt_block(key, ct):
    m0 = b2l(ct[:4])
    m1 = b2l(ct[4:])
    msk = (1 << 32) - 1

    s = 0xc6ef3720

    for i in range(32):
        m1 -= ((m0 << 4) + key[2]) ^ (m0 + s) ^ ((m0 >> 5) + key[3])
        m1 &= msk
        m0 -= ((m1 << 4) + key[0]) ^ (m1 + s) ^ ((m1 >> 5) + key[1])
        m0 &= msk
        s -= DELTA

    m = ((m0 << 32) + m1) & ((1 << 64) - 1)

    return l2b(m)
def decrypt(key, enc_flag):
    key = [b2l(key[i:i+4]) for i in range(0, len(key), 4)]
    blocks = [enc_flag[i:i+8] for i in range(0, len(enc_flag), 8)]
    flag = b''

    for ct in blocks:
        flag += decrypt_block(key, ct)
    
    return flag

def pwn():
    key= bytes.fromhex('850c1413787c389e0b34437a6828a1b2')
    enc_flag= bytes.fromhex('b36c62d96d9daaa90634242e1e6c76556d020de35f7a3b248ed71351cc3f3da97d4d8fd0ebc5c06a655eb57f2b250dcb2b39c8b2000297f635ce4a44110ec66596c50624d6ab582b2fd92228a21ad9eece4729e589aba644393f57736a0b870308ff00d778214f238056b8cf5721a843')
    flag = decrypt(key, enc_flag)
    print(flag)
if __name__ == '__main__':
    pwn()
```
- Flag: `HTB{th1s_1s_th3_t1ny_3ncryp710n_4lg0r1thm_____y0u_m1ght_h4v3_4lr34dy_s7umbl3d_up0n_1t_1f_y0u_d0_r3v3rs1ng}`
