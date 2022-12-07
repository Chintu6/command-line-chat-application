# command-line-chat-application
#server
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
#client
from socket import *

client=socket()
client.connect(('localhost',12000))
print('Connected to server')
while True:
    recData=client.recv(1024).decode()
    print('Server: ',recData)
    data=input("Client:")
    client.send(bytes(data,'utf-8'))
    print("Data Sent")


client.close()
