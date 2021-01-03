import socket as factory
import threading
import json

HOST = 'localhost'
PORT = 30001

connections = []


def read_from_socket(socket, id = None):
    # Getting how many bytes we need to read
    n = int.from_bytes(socket.recv(1), 'big')

    # Reading those bytes
    msg = socket.recv(n)

    if id != None:
        print('Client: ' + str(id))
    print('Received:')
    print(msg)

    return msg

def send_msg(socket, msg):
    socket.sendall(bytes([len(str(msg))]))
    socket.sendall(bytes(str(msg), 'utf-8'))


def client_actions(i):
    # Adding the ids to the clients
    conn = connections[i][0]
    close = False
    id = -1
    publicKey = -1
    try:
        while close == False:
            # Receiving a json msg from the client
            msg = json.loads(read_from_socket(conn).decode('utf-8'))

            # Saving the id
            if 'id' in msg:
                if id == -1:
                    id = int(msg['id'])
                    connections[i].append(id)
                else:
                    id = int(msg['id'])
                    connections[i][1] = id

            # Saving the publicKeys
            if 'publicKey' in msg:
                if publicKey == -1:
                    publicKey = msg['publicKey']
                    connections[i].append(publicKey)
                else:
                    publicKey = msg['publicKey']
                    connections[i][2] = publicKey

            # Get the interested id
            if 'peer' in msg:
                communicationId = int(msg['peer'])

                for c in connections:
                    if c[1] == communicationId:
                        # Returning the clients publicKey
                        sentMsg = {
                            "peer" : c[2]
                        }
                        send_msg(conn, json.dumps(sentMsg))
                        break
            if 'close' in msg:
                connections[i] = None
                close = True
    except:
        print('There was an error decoding the json')


with factory.socket(factory.AF_INET, factory.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    threads = []
    i = 0
    print('Server started')
    while i < 2:
        # Accepting the clients
        conn, addr = server.accept()
        connections.append([conn])
        print('Accepted connection')
        # Creating a new thread for each client
        t = threading.Thread(target=client_actions, args=(i,))
        t.start()
        threads.append(t)
        
        i = i+1
    
    # Joining all threads
    print('Closing all threads and stopping')
    for t in threads:
        t.join()





    

