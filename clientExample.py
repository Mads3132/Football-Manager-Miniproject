import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 5555

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)

#This takes user input, will be changed from this
while True:
    Input = input('say something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()

#Convert list of different type items to string using join() in Python
'''mix_list = ["This", 44, 56, "is", "something"]

#Covert list of different type of items to string
full_str = ' '.join([str(elem) for elem in mix_list])

print(full_str)'''