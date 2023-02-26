from fractions import gcd
from random import randint

#Gerando numeros primos

f = randint(1, 10000000)

for c in range(1, f + 1):
    if (f % c == 0):
        return True

#----------------------------------------

P = 3
Q = 11
n = P * Q

phi_N = (P - 1)(Q - 1)

#Chave publica
E = 7

chave_public = gcd(E, phi_N)

#Chave privada

D = 3
N1 = E * D

chav_private = 1 % (P - 1)(Q - 1) 

if (chav_private == E * D):
    return True
else:
    return "Errado"

#Encriptação

A = 2
E = 7
N2 = 33

encript_ = b % N2

if (encript_ == A ^ E):
    return True
else:
    return "Errado"

#Decriptação

decript_ = A % N2

if (decript_ == B ^ D):
    return True
else:
    return "Errado"