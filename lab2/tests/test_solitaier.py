import sys
import unittest

sys.path.append('../source/encryption')

import knapsack
import solitaire

class SolitaireTest(unittest.TestCase):
    def setUp(self):
        self.solitaire = solitaire.Solitaire()

    def test_shuffle(self):
        phrase = 'testphrase'

    def test_encryption(self):
        message = 'This is a message for encryption'

    def test_decryption(self):
        message = 'This is a message for encryption'

    def test_correctness(self):
        message = 'This is a message for encryption'

