import socket as factory
import functions
import sys
import json

sys.path.append('../encryption')

import knapsack
import solitaire

clientId = 33302

HOST = 'localhost'
PORT = 30001

knap = knapsack.Knapsack(8)

print('Client started')
# Connecting the client to the server
socket = factory.socket(factory.AF_INET, factory.SOCK_STREAM)
server_address = (HOST, PORT)
socket.connect(server_address)
print('Connected to the keyserver')

functions.login(socket, clientId, knap.publicKey)
print('Logged in to keyserver')
# Creating a new socket by which we can speak to the other client
clientSocket = factory.socket(factory.AF_INET, factory.SOCK_STREAM)
clientSocket.bind((HOST, clientId))

print('Listening for the client that wants to chat')
clientSocket.listen()
# Accept the connection
conn, addr = clientSocket.accept()
print('Accepted connection from peer')

# Getting Hello
peerId = functions.stringToJSON(functions.read_from_socket(conn).decode('utf-8'))['peer']
pubKey = functions.stringToIntList(functions.createCommunication(socket, peerId))

# Sending ACK
functions.send_msg(conn, json.dumps({"ACK" : 1}))

# Defining the phrase which will be used by the Solitaire encryption
print('Select a phrase for encryption:')
phrase = input()

# Sending and reading phrase with which we will use the Solitaire encryptions
formatedPhrase = functions.intListToString(knap.encrypt(phrase, pubKey))
functions.send_msg(conn, formatedPhrase)

# Assembling the secret phrase
phrase = knap.decrypt(functions.stringToIntList(functions.read_from_socket(conn))).decode('utf-8') + phrase
print('Assembled the encrypting phrase with my peer')
print(phrase)

# Creating the Solitaire encryption tool
sol = solitaire.Solitaire()
sol.phraseShuffle(phrase)

print('Waiting for conversation to start')

msg = ''
while msg != 'exit':
    formatedMsg = functions.stringToIntList(functions.read_from_socket(conn).decode('utf-8'))
    if formatedMsg == 'exit':
        break
    print(sol.decrypt(formatedMsg))
    msg = input()
    encMsg = functions.intListToString(sol.encrypt(msg))
    functions.send_msg(conn, encMsg)

functions.send_msg(socket, json.dumps({"close": True}))
