import socket as factory
import threading

HOST = 'localhost'
PORT = 30001

connections = []


def read_from_socket(socket):
    # Getting how many bytes we need to read
    n = int.from_bytes(socket.recv(1), 'big')

    # Reading those bytes
    msg = socket.recv(n)

    print('Received:')
    print(msg)

    return msg

def send_msg(socket, msg):
    socket.sendall(bytes([len(str(msg))]))
    socket.sendall(bytes(str(msg), 'utf-8'))


def client_actions(i):
    # Adding the ids to the clients
    conn = connections[i][0]
    id = read_from_socket(connections[i][0])
    connections[i].append(id)

    # Receiving the publicKeys
    publicKey = read_from_socket(connections[i][0])
    connections[i].append(publicKey)

    # Get the interested id
    communicationId = read_from_socket(connections[i][0])

    for conn in connections:
        if conn[2] == communicationId:
            # Returning the clients publicKey

            break


with factory.socket(factory.AF_INET, factory.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    threads = []
    i = 0
    while i < 2:
        # Accepting the clients
        conn, addr = server.accept()
        connections.append([conn])

        # Creating a new thread for each client
        t = threading.Thread(target=client_actions, args=(i,))
        t.start()
        threads.append(t)
        
        i = i+1
    
    # Joining all threads
    for t in threads:
        t.join()





    

