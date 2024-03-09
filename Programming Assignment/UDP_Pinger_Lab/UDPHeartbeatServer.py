from socket import *
import time

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('localhost',12000))
print('Server running...')

last_seq_num = None

while True:
    message, address = server_socket.recvfrom(1024)
    current_time = time.time()

    seq_num, timestamp = message.decode().split()
    rtt = (current_time - float(timestamp)) * 1000

    if last_seq_num is not None and int(seq_num) - int(last_seq_num) > 1:
        lost_packets = int(seq_num) - int(last_seq_num) -1
        print(f'Lost {lost_packets} packet(s)')

    last_seq_num = seq_num

    print(f'Recivied paket {seq_num} (RTT= {rtt:.3f}ms)')

    server_socket.sendto(message,address)
server_socket.close()