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