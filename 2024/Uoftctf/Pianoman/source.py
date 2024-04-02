# no secrets for you!
flag = ...

# Prime numbers
p = 151974537061323957822386073908385085419559026351164685426097479266890291010147521691623222013307654711435195917538910433499461592808140930995554881397135856676650008657702221890681556382541341154333619026995004346614954741516470916984007797447848200982844325683748644670322174197570545222141895743221967042369
q = 174984645401233071825665708002522121612485226530706132712010887487642973021704769474826989160974464933559818767568944237124745165979610355867977190192654030573049063822083356316183080709550520634370714336131664619311165756257899116089875225537979520325826655873483634761961805768588413832262117172840398661229
n = p * q

# a public exponent hidden away by Windy's musical talents
e = ...

# Converting the message to an integer
m = int.from_bytes(message.encode(), 'big')

# Encrypting the message: c = m^e mod n
inc_m = pow(message_int, e, n)

print(encrypted_message_int)
