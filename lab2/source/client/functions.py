import json

def send_msg(socket, msg):
    size = len(str(msg))
    while size > 255:
        socket.sendall(bytes([255]))
        size -= 255
    socket.sendall(bytes([size]))
    socket.sendall(msg.encode())

def read_from_socket(socket):
    # Getting how many bytes we need to read
    n = int.from_bytes(socket.recv(1), 'big')
    length = n
    while n == 255:
        n = int.from_bytes(socket.recv(1), 'big')
        length += n

    # Reading those bytes
    msg = socket.recv(length)

    print('Received:')
    print(msg)

    return msg

def login(socket, clientId, publicKey):
    pkMsg = intListToString(publicKey)
    msg = {
        "id" : clientId,
        "publicKey" : pkMsg
    }
    # Sending our id and publicKey to the server
    send_msg(socket, json.dumps(msg))


def createCommunication(socket, id):
    # Telling the server which client we want to speak to
    msg = {
        "peer" : id
    }
    send_msg(socket, json.dumps(msg))

    # Receiving it's public key and addr
    publicKey = json.loads(read_from_socket(socket).decode('utf-8'))['peer']
    return publicKey

def intListToString(l):
    return ' '.join([str(i) for i in l])

def stringToIntList(string):
    return [int(i) for i in string.split()]

def stringToJSON(string):
    try:
        return json.loads(string)
    except:
        print('JSON parse error')
        return -1