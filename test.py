import base64
from math import ceil
from os import system
from time import sleep, time
import colorsys as a
#import keyword
#import subprocess as sub

#sub.getstatusoutput("ipconfig")

global a
global b
global c

a = input("a: ")
b = input("b: ")
c = input("c: ")

print("{}".format(a + b + c))

def get_(valor, self):
        if(self == "a"):
                a = valor
                v2 = input("próximo (valor): ")
                s2 = input("próximo (self): ")
                if(s2 == "b")

"""
def get_(protocol, self):

        if(self == "a"):
                a = protocol
        elif(self == "b"):
                b = protocol
        elif(self == "c"):
                c = protocol

        return a + b + c

get_(2, a)

def notification_(self):
    sleep(2)
    w = system("msg * {}".format(self))

    return w 

notification_("Ola")

for w in range(1, 5):
    print(w)


def function_time(self):

    for y in range(1, self + 1):
        i = time()
        sleep(self - (self - y))
        f = time()
        z = ceil(i - f)*(-1)
        print(z)

function_time(5)

system("echo ola")
"""
#msg = "ola"

"""
b = msg.encode("utf-8")

#base64 encript
c = (base64.b64encode(b)).decode("utf-8")
#base64 decript
a1 = c.encode("utf-8")
c1 = (base64.b64decode(a1)).decode("utf-8")

#base85 encript
e = (base64.b85encode(b)).decode("utf-8")
#base85 decript
b1 = e.encode("utf-8")
e1 = (base64.b85decode(b1)).decode("utf-8")
"""