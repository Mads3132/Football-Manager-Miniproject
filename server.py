import socket  # Import socket module
import time
import threading
import multiprocessing
#import players #importing all player data



#def player1(arr): # making an array for player 1
    #arr[0] += 1 # 1 is the number that is abitrary, depends on the players array

#def player2(arr): # making an array for player 2
    #arr[0] += 1 # 1 is the number that is abitrary, depends on the players array


#array = multiprocessing.Array("i", [0,1]) # this is the section we declare our array to our multiprocessing

#process1 = multiprocessing.Process(target =player1, args=[array]) # this is where each process will then go in to the players arguments
#process2 = multiprocessing.Process(target =player2, args=[array]) # this is where each process will then go in to the players arguments



#process1.start() # here we create a new process
#process2.start() # here we create another process
#process1.join() # here we join the first process
#process2.join() # here we join the second process



port = 50000  # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()  # Create a socket object
host = ""  # Get local machine name
s.bind(('localhost', port))  # Bind to the port
s.listen(5)  # Now wait for client connection.

print('Server listening....')

x = 0

while True:
    conn, address = s.accept()  # Establish connection with client.

    while True:
        try:
            print('Got connection from', address)
            data = conn.recv(1024)
            print('Server received', data)

            st = 'Thank you for connecting'
            byt = st.encode()
            conn.send(byt)

            x += 1

        except Exception as e:
            print(e)
            #break

#conn.close()