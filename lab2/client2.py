import socket as factory
import knapsack
import solitaire

clientId = 33302

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
# Creating a new socket by which we can speak to the other client
clientSocket = factory.socket(factory.AF_INET, factory.SOCK_STREAM)
# In the second client
clientSocket.bind((HOST, clientId))
clientSocket.listen()

# Selecting which user we want to speak to
print("Tell me which client you want to speak with:")
c2Id = int(input())
pubKey = [int(i) for i in createCommunication(socket, c2Id).split()]
socket.close()


# Connecting to the other client
# clientSocket.connect(server_address)

# In the other client accept the connection
conn, addr = clientSocket.accept()
# Reading the phrase which will be used by the Solitaire encryption
print('Select a phrase for encryption:')
phrase = input()

# Sending and reading phrase with which we will use the Solitaire encryptions
formatedPhrase = ' '.join([str(i) for i in knap.encrypt(phrase, pubKey)])
send_msg(conn, formatedPhrase)
# In the second client
phrase = knap.decrypt([int(i) for i in read_from_socket(conn).split()]).decode('utf-8') + phrase
# phrase += knap.decrypt(read_from_socket(clientSocket).decode('utf-8'))
print(phrase)

# Creating the Solitaire encryption tool
sol = solitaire.Solitaire()
sol.phraseShuffle(phrase)

msg = ''
while msg != 'exit':
    formatedMsg = [int(i) for i in read_from_socket(conn).decode('utf-8').split()]
    print(sol.decrypt(formatedMsg))
    msg = input()
    encMsg = ' '.join([str(i) for i in sol.encrypt(msg)])
    send_msg(conn, encMsg)


