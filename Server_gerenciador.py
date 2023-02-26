import socket
import random

rand = random.randint(1, 9999)

ip = 
port = rand

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen() #Número de sistemas que vão passar por transferência de dados com um a mais como ponto de acesso

s.accept()

