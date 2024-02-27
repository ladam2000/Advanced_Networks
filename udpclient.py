

from socket import *

serverName = "127.0.0.1"  # Replace with your server's name or IP address
serverPort = 9650  # Ensure matching port with server

while True:
    clientSocket = socket(AF_INET, SOCK_DGRAM)  # Create socket within the loop

    message = input("Input lowercase sentence: ")
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    print("Sent to Make Upper Case Server: ", message)

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    print("Received back from Server: ", modifiedMessage.decode())  # Decode received message
    print()
    clientSocket.close()  # Close socket after each message exchange

