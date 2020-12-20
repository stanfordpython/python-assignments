import random
from bitstring import BitArray

class Knapsack:
    def __init__(self, len):
        self.privateKey = self.__getPrivateKey__(len)
        self.publicKey = self.__getPublicKey__(self.privateKey)
        self.len = len

    def encrypt(self, msg, pubKey=None):
        # We can encrypt messages with other publicKeys
        if pubKey == None:
            pubKey = self.publicKey
        encryptedMsg = []

        # Converting the msg into bit array
        bitMsg = BitArray(str.encode(msg))
        bitSum = 0
        # Variable to loop trough our private key
        j = 0
        for i in range(0, len(bitMsg)):
            if j == len(pubKey):
                encryptedMsg.append(bitSum)
                bitSum = 0
                j = 0
            bitSum += int(bitMsg[i]) * pubKey[j]
            j += 1
        if j != 0:
            encryptedMsg.append(bitSum)
        return encryptedMsg

    def decrypt(self, msg):
        decryptedMsg = ''
        invN = pow(self.n, -1, self.m)
        for i in msg:
            invMul = (invN * i)%self.m
            partMsg = ''
            for j in range(self.len-1, -1, -1):
                if self.privateKey[j] <= invMul:
                    partMsg += '1'
                    invMul -= self.privateKey[j]
                else:
                    partMsg += '0'
            decryptedMsg += partMsg[::-1]
        return self.decode_binary_string(decryptedMsg)

    def __getPrivateKey__(self, n):
        privateKey = []
        privateKey.append(random.randint(0,35))
        sumSA = privateKey[0]
        for _ in range(1, n):
            nextNum = sumSA + random.randint(0, 15)
            privateKey.append(nextNum)
            sumSA += nextNum
        return privateKey

    def __getPublicKey__(self, privateKey):
        self.m = self.__defineM__(privateKey)
        self.n = self.__defineN__(self.m)

        publicKey = []
        for i in privateKey:
            publicKey.append((i * self.n)%self.m)
        return publicKey

    def __defineM__(self, privateKey):
        return sum(privateKey) + random.randint(0, 10)

    def __defineN__(self, m):
        x = 2
        n = 0
        while x != 1:
            n = random.randint(0, m)
            x = n
            y = m

            while(y):
                x,y=y,x%y
        return n

    def decode_binary_string(self, s):
        return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8)).encode('utf-8')
