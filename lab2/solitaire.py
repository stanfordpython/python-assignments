class Solitaire:
    def __init__(self):
        self.__init_deck__()

    # Jokers are:
    # Joker A - card #52
    # Joker A - card #53
    def __init_deck__(self):
        self.deck = []
        self.streamCount = 0
        for i in range(54):
            self.deck.append(i)

    def phraseShuffle(self, phrase):
        for c in phrase:
            self.__move_jokers__()
            self.__triple_cut__()
            self.__count_cut(self.deck[-1])

            self.__count_cut(ord(c)%54)


    def __move_jokers__(self):
        jokerA = self.deck.index(52)
        jokerB = self.deck.index(53)

        # Moving jokerA
        self.deck[jokerA], self.deck[(jokerA+1)%54] = self.deck[(jokerA+1)%54], self.deck[jokerA]

        # Moving jokerB
        self.deck[jokerB], self.deck[(jokerB+1)%54], self.deck[(jokerB+2)%54] = self.deck[(jokerB+1)%54], self.deck[(jokerB+2)%54], self.deck[jokerB]

    def __triple_cut__(self):
        jokerA = self.deck.index(52)
        jokerB = self.deck.index(53)

        if jokerA > jokerB:
            jokerA, jokerB = jokerB, jokerA
        cut1 = self.deck[0:jokerA]
        cut2 = self.deck[jokerA:jokerB+1]
        cut3 = self.deck[jokerB+1:54]

        self.deck = cut3 + cut2 + cut1

    def __count_cut(self, n):
        self.deck[:-1] = self.deck[n:-1] + self.deck[:n]

    def __getDefaultValues__(self, msg):
        values = []
        for c in msg:
            values.append(ord(c))
        return values

    def __getKeysTream__(self, n):
        keyStream = []
        self.streamCount += n
        for _ in range(n):
            self.__move_jokers__()
            self.__triple_cut__()
            self.__count_cut(self.deck[-1])
            keyStream.append(self.deck[self.deck[0]])
        return keyStream

    def encrypt(self, msg):
        encryptedMsg = []
        values = self.__getDefaultValues__(msg)
        keyStream = self.__getKeysTream__(len(msg))
        
        for i in range(len(values)):
            encryptedMsg.append(values[i] ^ keyStream[i])

        return encryptedMsg

    def decrypt(self, msg):
        decryptedMsg = ''
        keyStream = self.__getKeysTream__(len(msg))
        
        for i in range(len(msg)):
            decryptedMsg+=(chr(msg[i] ^ keyStream[i]))

        return decryptedMsg