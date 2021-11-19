import socket
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 5555
ThreadCount = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for incoming connection(s)...')
ServerSocket.listen(3)

def threaded_client(connection):
    connection.send(str.encode('Welcome to the server'))
    while True:
        data = connection.recv(1024)
        reply = 'This is your starting lineup: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount +=1
    print('Thread number: ' + str(ThreadCount))
ServerSocket.close()