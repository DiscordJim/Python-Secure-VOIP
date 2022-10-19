import socket
import logging

PORT = 5050
ADDR = ("10.0.0.95", PORT)

HEADER = "VOIP SECURE SERVER"

logging.basicConfig(level=logging.DEBUG, format='[%(name)s] [%(levelname)s] %(message)s')

logging.info(f'Starting VOIP server on port {PORT}')

serverSocket = None

clients = []

def main():
    # Bind the socket
    serverSocket = socket.socket()
    serverSocket.bind(ADDR)
    logging.info(f'Bound socket to address {ADDR}')

    serverSocket.listen()
    while True:
        c, addr = serverSocket.accept()
        logging.info(f'Accepted connection from {addr}')

# Call our start function
main()