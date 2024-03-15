- Chall này đơn giản chỉ là thay đổi vị trí của các ký tự trong flag.
```Python
cipher = r'!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB'
new_flag = ''
for i in range(0, len(cipher), 3):
    new_flag += cipher[i+2]
    new_flag += cipher[i]
    new_flag += cipher[i+1]
flag = new_flag[::-1]
print(flag)
```
- Flag:`HTB{4_b3tTeR_w3apOn_i5_n3edeD!?!}`
![image](https://github.com/Caycon/CTF/assets/97203151/9ef13179-e996-4520-b6bd-082cd8802e46)
