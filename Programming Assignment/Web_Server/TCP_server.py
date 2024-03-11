from socket import *
import sys
import threading 

def handle_client(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024) 
        print ('-------the message is------- ', message)
        filename = message.split()[1]
        print ('-------the filename is------ ', filename)
        f = open(filename[1:]) 
        outputdata = f.read() 

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode()) 
        connectionSocket.send("\r\n".encode())  
        print ('-------length is------ ', len(outputdata))

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode()) 

        connectionSocket.close()
        print ('File sending success')

    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())  
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode()) 
        connectionSocket.close() 

# Prepare a server socket
serverPort = 8081  
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))  
serverSocket.listen(1)  

print('The server is ready to serve...')

while True: 
    connectionSocket, addr = serverSocket.accept()
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr)) 
    client_thread.start()  # Start the thread to handle the client

serverSocket.close() 
sys.exit()  
