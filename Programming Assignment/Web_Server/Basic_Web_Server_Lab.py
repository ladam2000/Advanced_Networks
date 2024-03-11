#import socket module
from socket import *
import sys
# Prepare a sever socket
serverPort = 8081  # Choose a port number
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))  # Bind to all interfaces on the chosen port
serverSocket.listen(1)  # Listen for incoming connections (max queue of 1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Accept a connection

    try:
        message = connectionSocket.recv(1024)  # Receive request
        print ('-------the message is------- ', message)
        filename = message.split()[1]
        print ('-------the filename is------ ', filename)
        f = open(filename[1:])  # Open the requested file
        outputdata = f.read()  # Read file contents

        # Send HTTP header lines
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())  # Assuming HTML
        connectionSocket.send("\r\n".encode())  # End of headers
        print ('-------length is------ ', len(outputdata))

        # Send the content of the requested file
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())  # Encode each character
        connectionSocket.send("\r\n".encode())  # Encode the final newline as well

        connectionSocket.close()
        print ('File sending success')

    except IOError:
        # Send 404 response
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode()) 
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode()) # Assuming)


        connectionSocket.close() 

serverSocket.close()
sys.exit()
