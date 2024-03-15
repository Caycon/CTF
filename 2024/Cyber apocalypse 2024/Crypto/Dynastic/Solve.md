- Chall này chỉ cần ta logic giải ngược mã là có thể thu được flag
```Python
def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

enc= 'DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL'

flag = ''
for i in range(len(enc)):
    ech = enc[i]
    if not ech.isalpha():
        m = ech
    else:
        echi = to_identity_map(ech)
        m = from_identity_map(echi - i)
    flag += m

print(f'HTB{{{flag}}}')
```
- Flag: `HTB{DID_YOU_KNOW_ABOUT_THE_TRITHEMIUS_CIPHER?!_IT_IS_SIMILAR_TO_CAESAR_CIPHER}`
![image](https://github.com/Caycon/CTF/assets/97203151/9e4f45a1-ff10-420b-be24-0583f59217d6)
