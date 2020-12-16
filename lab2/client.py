import socket as factory

clientId = 33301

HOST = 'localhost'
PORT = 30001

def loginId(socket):
    # Sending our id to the server
    socket.sendall(clientId)

    # Getting our Merkle-Hellman Knapsack key
    socket.recv(2500)

# Connecting the client to the server
socket = factory.socket(factory.AF_INET, factory.SOCK_STREAM)
server_address = (HOST, PORT)
socket.connect(server_address)

