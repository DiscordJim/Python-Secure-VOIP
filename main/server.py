import socket
import logging
from threading import Thread
import opcodes
import packets

PORT = 5050
ADDR = (socket.gethostname(), PORT)

HEADER = "VOIP SECURE SERVER"

logging.basicConfig(level=logging.DEBUG, format='[%(name)s] [%(levelname)s] %(message)s')

logging.info(f'Starting VOIP server on port {PORT}')

clientThreadPool = []


# Packet
# Header (1 byte) -> Size (2 bytes) -> Content


def handle_client(client_socket: socket.socket, address):
    logging.info(f'Launched thread to deal with new client from {address}')
    while True:
        message = input("What would you like to send to our client? ")

        client_socket.send(packets.create_packet(opcodes.MESSAGE_PACKET_CODE, message))

        if client_socket.recv(1) == opcodes.MESSAGE_PACKET_CODE:
            packet_size = int.from_bytes(client_socket.recv(2), byteorder='big')
            print(f'Our lovely client says: {client_socket.recv(packet_size).decode()}')



def main():
    # Bind the socket
    server_socket = socket.socket()
    server_socket.bind(ADDR)
    logging.info(f'Bound socket to address {ADDR}')

    server_socket.listen()
    while True:
        c, addr = server_socket.accept()
        clientThreadPool.append(Thread(target=handle_client, args=(c, addr)).start())


# Call our start function
main()
