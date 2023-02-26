from random import randint
import base64

#Criptografia
a = int(input("Valor: "))

x = oct(a)[2:]
#s = range(randint(a, x), randint(x, a))


for x in range(1, 10):

    global b, c, d

    b = oct(10 + randint(1,1000))
    c = hex(10 + randint(1,1000))
    d = bin(10 + randint(1,1000))

    print(b[2:] + c[2:] + d[2:])

#Decriptografia
