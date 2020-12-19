import socket as factory
import knapsack
import json

clientId = 33301

HOST = 'localhost'
PORT = 30001

def send_msg(socket, msg):
    socket.sendall(bytes([len(str(msg))]))
    socket.sendall(bytes(str(msg), 'utf-8'))

def read_from_socket(socket):
    # Getting how many bytes we need to read
    n = int.from_bytes(socket.recv(1), 'big')

    # Reading those bytes
    msg = socket.recv(n)

    print('Received:')
    print(msg)

    return msg

def login(socket, publicKey):
    # Sending our id and publicKey to the server
    send_msg(socket, clientId)

    pkMsg = ' '.join([str(i) for i in publicKey])
    send_msg(socket, pkMsg)


def createCommunication(socket, id):
    # Telling the server which client we want to speak to
    send_msg(socket, id)

    # Receiving it's public key and addr
    publicKey = read_from_socket(socket).decode('utf-8')
    return publicKey

knap = knapsack.Knapsack(8)


# Connecting the client to the server
socket = factory.socket(factory.AF_INET, factory.SOCK_STREAM)
server_address = (HOST, PORT)
socket.connect(server_address)

login(socket, knap.publicKey)

print("Tell me which client you want to speak with:")
c2Id = int(input())
createCommunication(socket, c2Id)

