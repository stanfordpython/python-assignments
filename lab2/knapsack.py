import random

def getPrivateKey(n):
    privateKey = []
    privateKey.append(random.randint(0,35))
    sumSA = privateKey[0]
    for _ in range(1, n):
        nextNum = sumSA + random.randint(0, 15)
        privateKey.append(nextNum)
        sumSA += nextNum
    return privateKey

def getPublicKey(privateKey, m, n):
    publicKey = []
    for i in privateKey:
        publicKey.append((i * n)%m)
    return publicKey

def defineM(privateKey):
    return sum(privateKey) + random.randint(0, 10)

def defineN(m):
    x = 2
    n = 0
    while x != 1:
        n = random.randint(0, m)
        x = n
        y = m

        while(y):
            x,y=y,x%y
    return n

# print(superIncreasingArray(25))

print(defineN(2000000))