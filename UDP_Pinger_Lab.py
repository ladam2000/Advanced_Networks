import socket
import time

# Server details
serverName = 'localhost'  # Replace with the server's IP if needed
serverPort = 12000

# Create a UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)  # Set 1-second timeout

# Send 10 ping requests
for sequence_number in range(1, 110):
    message = f"Ping {sequence_number} {time.time()}"  # Format the message
    startTime = time.time()  # Record the send time 

    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        data, server = clientSocket.recvfrom(1024)
        rtt = time.time() - startTime
        print(f"Reply from {server}: {data.decode()} RTT: {rtt:.3f} seconds")

    except socket.timeout:
        print("Request timed out")

clientSocket.close()
