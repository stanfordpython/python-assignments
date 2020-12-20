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

def intListToString(l):
    return ' '.join([str(i) for i in l])

def stringToIntList(string):
    return [int(i) for i in string.split()]

knap = knapsack.Knapsack(8)

print('Client started')
# Connecting the client to the server
socket = factory.socket(factory.AF_INET, factory.SOCK_STREAM)
server_address = (HOST, PORT)
socket.connect(server_address)
print('Connected to the keyserver')

login(socket, knap.publicKey)
print('Logged in to keyserver')
# Creating a new socket by which we can speak to the other client
clientSocket = factory.socket(factory.AF_INET, factory.SOCK_STREAM)
# In the second client
clientSocket.bind((HOST, clientId))
clientSocket.listen()
print('Listening for the client that wants to chat')
# Selecting which user we want to speak to
print("Tell me which client you want to speak with:")
c2Id = int(input())
pubKey = stringToIntList(createCommunication(socket, c2Id))
socket.close()
print('Closed communication with the keyserver')

# Connecting to the other client
# clientSocket.connect(server_address)

# In the other client accept the connection
conn, addr = clientSocket.accept()
print('Accepted connection from peer')
# Reading the phrase which will be used by the Solitaire encryption
print('Select a phrase for encryption:')
phrase = input()

# Sending and reading phrase with which we will use the Solitaire encryptions
formatedPhrase = intListToString(knap.encrypt(phrase, pubKey))
send_msg(conn, formatedPhrase)
# In the second client
phrase = knap.decrypt(stringToIntList(read_from_socket(conn))).decode('utf-8') + phrase
# phrase += knap.decrypt(read_from_socket(clientSocket).decode('utf-8'))
print('Assembled the encrypting phrase with my peer')
print(phrase)

# Creating the Solitaire encryption tool
sol = solitaire.Solitaire()
sol.phraseShuffle(phrase)

print('Waiting for conversation to start')

msg = ''
while msg != 'exit':
    formatedMsg = stringToIntList(read_from_socket(conn).decode('utf-8'))
    if formatedMsg == 'exit':
        break
    print(sol.decrypt(formatedMsg))
    msg = input()
    encMsg = intListToString(sol.encrypt(msg))
    send_msg(conn, encMsg)


