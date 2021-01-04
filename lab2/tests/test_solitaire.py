import sys
import unittest

sys.path.append('../source/encryption')

import knapsack
import solitaire

class SolitaireTest(unittest.TestCase):
    def setUp(self):
        self.solitaire1 = solitaire.Solitaire()
        self.solitaire2 = solitaire.Solitaire()

    def test_shuffle(self):
        phrase = 'testphrase'

        self.solitaire1.phraseShuffle(phrase)
        self.solitaire2.phraseShuffle(phrase)

        self.assertEquals(self.solitaire1.deck, self.solitaire2.deck)

    def test_encryption(self):
        message = 'This is a message for encryption'
        phrase = 'testphrase'

        self.solitaire1.phraseShuffle(phrase)
        self.solitaire2.phraseShuffle(phrase)

        cipherText1 = self.solitaire1.encrypt(message)
        cipherText2 = self.solitaire2.encrypt(message)

        self.assertEquals(cipherText1, cipherText2)

    
    def test_correctness(self):
        message = 'This is a message for encryption'
        phrase = 'testphrase'

        self.solitaire1.phraseShuffle(phrase)
        self.solitaire2.phraseShuffle(phrase)

        cipherText = self.solitaire1.encrypt(message)

        simpleText = self.solitaire2.decrypt(cipherText)

        self.assertEquals(message, simpleText)