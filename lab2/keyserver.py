import socket as factory

HOST = 'localhost'
PORT = 30001

connections = []




with factory.socket(factory.AF_INET, factory.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    # Accepting the first client
    conn, addr = server.accept()
    connections.append([conn, addr])

    # Accepting the second client
    conn, addr = server.accept()
    connections.append([conn, addr])

    id1 = connections[0][0].recv(8)
    id2 = connections[0][0].recv(8)

    # Adding the ids to the clients
    connections[0].append(id1)
    connections[1].append(id2)

    

