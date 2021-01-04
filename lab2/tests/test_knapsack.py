import sys
import unittest

sys.path.append('../source/encryption')

import knapsack
import solitaire

class KnapsackTest(unittest.TestCase):
    def setUp(self):
        self.len = 5
        self.knapsack = knapsack.Knapsack(self.len)

    def test_correctness(self):
        message = 'Message test'
        cipherText = self.knapsack.encrypt(message)
        simpleText = self.knapsack.decrypt(cipherText).decode()

        self.assertEqual(message, simpleText)


if __name__ == '__main__':
    unittest.main()