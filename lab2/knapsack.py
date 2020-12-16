import random

class Knapsack:
    def __init__(self, n):
        self.privateKey = self.__getPrivateKey__(n)
        self.publicKey = self.__getPublicKey__(self.privateKey)
        self.n = n

    def encrypt(self, msg):
        encryptedMsg = []

        # Converting the msg into bit array
        bitMsg = bin(int.from_bytes(msg.encode(), 'big'))[2:]
        bitSum = 0
        # Variable to loop trough our private key
        j = 0
        for i in range(0, len(bitMsg)):
            if j == self.n:
                encryptedMsg.append(bitSum)
                bitSum = 0
                j = 0
            bitSum += int(bitMsg[i]) * self.privateKey[j]
            j += 1
        if j != 0:
            encryptedMsg.append(bitSum)
        return encryptedMsg

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
        m = self.__defineM__(privateKey)
        n = self.__defineN__(m)

        publicKey = []
        for i in privateKey:
            publicKey.append((i * n)%m)
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

knap = Knapsack(16)
print(knap.privateKey)
print(knap.publicKey)
print(knap.encrypt('hellokaa'))