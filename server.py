from socket import *
from time import *
server=socket(AF_INET,SOCK_STREAM)
server.bind(('localhost',12000))
server.listen()
print('Server listening at 12000')
connection,address=server.accept()
print('Connected to client')
while True:
    data=input("Server:")
    connection.send(bytes( data + ctime(),'utf-8'))
    print('data sent')
    recData=connection.recv(1024).decode()
    print("Client :",recData)


connection.close()