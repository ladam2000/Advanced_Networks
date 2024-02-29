import sys
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM) 

# Prepare a server socket
serverPort = 8080  # Choose a port number 
serverSocket.bind(('localhost', serverPort)) 
serverSocket.listen(1) 

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try: 
        message = connectionSocket.recv(1024).decode()  
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() 

        # Send one HTTP header line into socket 
        connectionSocket.send("HTTP/1.0 200 OK\r\n\r\n".encode())
        print('HTTP OK 200')

        # Send the content of the requested file to the client 
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close() 

    except IOError:
        # Send response message for file not found (404)
        connectionSocket.send("HTTP/1.0 404 Not Found\r\n\r\n".encode())
        print('HTTP ERROR 404')

        # Close client socket 
        connectionSocket.close() 

serverSocket.close()
sys.exit()  
