import socket
import time
from socket import *
import random

client_socket = socket(AF_INET, SOCK_DGRAM)

server_address = ('localhost', 12000)

client_socket.settimeout(1)

rtts = []

lost_packets = 0

for i in range(1, 11):
    timestamp = time.time()  # Capture timestamp before sending
    message = f'{i} {timestamp}'.encode()

    try:
        client_socket.sendto(message, server_address)
        response, address = client_socket.recvfrom(1024)
        rtt = (time.time() - timestamp) * 1000
        print(f'Recivied paket {i} (RTT= {rtt:.3f}ms)')
        rtts.append(rtt)
    except (socket.timeout, ConnectionError):  # Catch both timeout and connection errors
        print(f'Packet {i} timed out')
        lost_packets += 1

packet_lost_rate = (lost_packets / 10) * 100
min_rtt = min(rtts)
max_rtt = max(rtts)
avg_rtt = sum(rtts) / len(rtts)

print(f'\nPacket loss rate: {lost_packets:.1f}%')
print(f'Minimum RTT: {min_rtt}')
print(f'Maximum RTT: {max_rtt}')
print(f'Average RTT: {avg_rtt}')
