import socket
import sys

porta = int(sys.argv[1])

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.bind(("0.0.0.0" , porta))
s.listen(1)

print("Aguardando conexão em 0.0.0.0:" + str(porta))
s2 , endereco = s.accept()

print("Conectado com: " , endereco)
while True:
    msg = s2.recv(1024).decode()
    print(msg)

    data = input("<<< ") + "\n"
    
    s2.send(data.encode())

    