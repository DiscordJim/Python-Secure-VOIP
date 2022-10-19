import socket
import opcodes
import packets

clientSocket = socket.socket()
HOST = socket.gethostname()
PORT = 5050


clientSocket.connect((HOST, PORT))

while True:
    if clientSocket.recv(1) == opcodes.MESSAGE_PACKET_CODE:
        packet_size = int().from_bytes(clientSocket.recv(2), byteorder='big')
        print(f'Recieved a message code, size of {packet_size}')
        contents = clientSocket.recv(packet_size).decode()
        print(f'Packet reads: "{contents}"')

        reply = input("What will your reply be: ")
        packet = packets.create_packet(opcodes.MESSAGE_PACKET_CODE, reply)
        clientSocket.send(packet)



