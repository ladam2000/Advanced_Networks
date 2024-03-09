import socket
import sys

if len(sys.argv) != 4:
    print("Usage: client.py server_host server_port filename")
    sys.exit(1)

server_host = sys.argv[1]
server_port = int(sys.argv[2])  # Convert port to integer
filename = sys.argv[3]

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

# Build HTTP GET request
request = f"GET /{filename} HTTP/1.0\r\nHost: {server_host}\r\n\r\n"

# Send the request
client_socket.send(request.encode())

# Receive the response
response = b''
while True:
    chunk = client_socket.recv(1024)
    if not chunk:
        break
    response += chunk

# Print the server's response
print(response.decode()) 

client_socket.close()
