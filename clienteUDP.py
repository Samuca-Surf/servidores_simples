

import socket
import sys

host = sys.argv[1]
porta = int(sys.argv[2])

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.connect((host , porta))

print("Conectado com o host: " , host)
while True:
    msg = input(">>> " ) + "\n"
    s.send(msg.encode())

    resposta = s.recv(1024).decode()

    print("<<<" ,resposta)