import socket
import sys

porta = int(sys.argv[1])

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

s.bind(("0.0.0.0" , porta))

while True:
    data, endereco = s.recvfrom(1024)
    print(data.decode())

    data = input("<<< ") + "\n"
    
    s.sendto(data.encode(), endereco)