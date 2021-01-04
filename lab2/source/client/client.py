import socket as factory
import functions
import sys
import json

sys.path.append('../encryption')

import knapsack
import solitaire

clientId = 33301

HOST = 'localhost'
PORT = 30001

knap = knapsack.Knapsack(8)

print('Client started')
# Connecting the client to the server
socket = factory.socket(factory.AF_INET, factory.SOCK_STREAM)
server_address = (HOST, PORT)
socket.connect(server_address)
print('Connected to the keyserver')

# Logging into the keyserver
functions.login(socket, clientId, knap.publicKey)
print('Logged in to keyserver')

# Selecting which user we want to speak to
print("Tell me which client you want to speak with:")
c2Id = int(input())

# Getting the users publicKey
pubKey = functions.createCommunication(socket, c2Id)

# Checking if we found the client
while pubKey == -1:
    print('There is no such client logged in to the server')
    print("Tell me which client you want to speak with:")
    c2Id = int(input())

    # Getting the users publicKey
    pubKey = functions.createCommunication(socket, c2Id)

pubKey = functions.stringToIntList(pubKey)

# Creating a new socket by which we can speak to the other client
clientSocket = factory.socket(factory.AF_INET, factory.SOCK_STREAM)
server_address = (HOST, c2Id)

# Connecting to the other client
clientSocket.connect(server_address)
print('Connected to the peer we want to speak with')

# Sending hello
print('Sending hello to the other client')
functions.send_msg(clientSocket, json.dumps({"peer" : clientId}))

# Waiting for hello
ack = functions.read_from_socket(clientSocket).decode('utf-8')
print(ack)
print('Select a phrase for encryption:')
phrase = input()

# Sending the phrase that which we will use in Solitaire encryptions
formatedPhrase = functions.intListToString(knap.encrypt(phrase, pubKey))
functions.send_msg(clientSocket, formatedPhrase)

# Assembling the phrase
phrase += knap.decrypt(functions.stringToIntList(functions.read_from_socket(clientSocket))).decode('utf-8')
print('Assembled the encrypting phrase with my peer')
print(phrase)

# Creating the Solitaire encryption tool
sol = solitaire.Solitaire()
sol.phraseShuffle(phrase)

print('Starting conversation')

msg = ''
stop = False
while stop == False:
    msg = input()
    if msg == 'exit':
        stop = True
    encMsg = functions.intListToString(sol.encrypt(msg))
    functions.send_msg(clientSocket, encMsg)
    formatedMsg = functions.stringToIntList(functions.read_from_socket(clientSocket).decode('utf-8'))
    msg = sol.decrypt(formatedMsg).decode('utf-8')
    if msg == 'exit':
        stop = True
    print(msg)

functions.send_msg(socket, json.dumps({"close": True}))
