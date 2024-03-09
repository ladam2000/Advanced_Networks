import socket
import time

# Server details
serverName = 'localhost'  # Replace with the server's IP if needed
serverPort = 12000

# Create a UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)  # Set 1-second timeout

# Variables to track statistics
rtts = []
packets_sent = 0
packets_received = 0

# Send 10 ping requests
for sequence_number in range(1, 11):  # 10 pings is common 
    message = f"Ping {sequence_number} {time.time()}"  
    startTime = time.time()  

    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        data, server = clientSocket.recvfrom(1024)
        rtt = time.time() - startTime
        rtts.append(rtt)  # Store RTT for statistics
        packets_received += 1
        print(f"Reply from {server}: {data.decode()} RTT: {rtt:.3f} seconds")

    except socket.timeout:
        print("Request timed out")

    packets_sent += 1

clientSocket.close()

# Calculate and print statistics
if packets_received > 0:
    print("\n--- Ping Statistics ---")
    print(f"{packets_sent} packets transmitted, {packets_received} received, {100 - (packets_received / packets_sent * 100):.0f}% packet loss")
    print(f"round-trip min/avg/max = {min(rtts):.3f}/{sum(rtts) / len(rtts):.3f}/{max(rtts):.3f} ms")
else:
    print("\nNo packets received.")
