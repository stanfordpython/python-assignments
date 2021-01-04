import socket as factory
import threading
import json

HOST = 'localhost'
PORT = 30001

connections = []


def read_from_socket(socket, id = None):
    # Getting how many bytes we need to read
    n = int.from_bytes(socket.recv(1), 'big')
    length = n
    while n == 255:
        n = int.from_bytes(socket.recv(1), 'big')
        length += n
    
    print(length)

    # Reading those bytes
    msg = socket.recv(length)

    if id != None:
        print('Client: ' + str(id))
    print('Received:')
    print(msg)

    return msg

def send_msg(socket, msg):
    size = len(str(msg))
    while size > 255:
        socket.sendall(bytes([255]))
        size -= 255
    socket.sendall(bytes([size]))
    socket.sendall(msg.encode())


def client_actions(i):
    # Adding the ids to the clients
    conn = connections[i][0]
    close = False
    id = -1
    publicKey = -1
    try:
        while close == False:
            # Receiving a json msg from the client
            text = read_from_socket(conn).decode('utf-8')
            if len(text) < 2:
                connections[i][0].close()
                connections[i] = None
                return
            msg = json.loads(text)

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
                found = False
                for c in connections:
                    if c != None and c[1] == communicationId:
                        found = True
                        # Returning the clients publicKey
                        sentMsg = {
                            "peer" : c[2]
                        }
                        send_msg(conn, json.dumps(sentMsg))
                        break
                if not found:
                    sentMsg = {
                            "peer" : -1
                        }
                    send_msg(conn, json.dumps(sentMsg))
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
    while True:
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




# TODO: Correct steps:
            # 1. Client 1 connects to the keyserver
            # 2. Client 1 sends  message to Client 2
            # 3. Client 2 asks for the key of Client 1
            # 4. Client 2 sends a confirmation msg to Client 1
            # 5. Communication starts

    

