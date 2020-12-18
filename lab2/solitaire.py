class Solitaire:
    def __init__(self):
        self.__init_deck__()

    # Jokers are:
    # Joker A - card #52
    # Joker A - card #53
    def __init_deck__(self):
        self.deck = []
        for i in range(54):
            self.deck.append(i)

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

        cut1 = self.deck[0:jokerA]
        cut2 = self.deck[jokerA:jokerB+1]
        cut3 = self.deck[jokerB+1:54]

        self.deck = cut3 + cut2 + cut1

    def __count_cut(self, n):
        self.deck[:-1] = self.deck[n:-1] + self.deck[:n]

    def __getIntValue__(self, num):
        val = ord(num)
        if val >= 97:
            return val - 97
        else:
            return val - 39
    
    def __get_char__(self, num):
        num = num % 54
        if num >= 26:
            return chr(num + 39)
        else:
            return chr(num + 97)

    def __getDefaultValues__(self, msg):
        values = []
        for c in msg:
            val = self.__getIntValue__(c)
            values.append(self.deck[val])
        return values

    def __getKeysTream__(self, n):
        keyStream = []
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
            # encryptedMsg += self.__get_char__(values[i] + keyStream[i])
            encryptedMsg.append(values[i] ^ keyStream[i])

        return encryptedMsg

    def decrypt(self, msg):
        decryptedMsg = ''
        keyStream = self.__getKeysTream__(len(msg))
        
        for i in range(len(msg)):
            # encryptedMsg += self.__get_char__(values[i] + keyStream[i])
            decryptedMsg+=(self.__get_char__(msg[i] ^ keyStream[i]))

        return decryptedMsg

sol = Solitaire()
sol2 = Solitaire()
encmsg = sol.encrypt('iashdjnSHJKsds')
print(sol2.decrypt(encmsg))