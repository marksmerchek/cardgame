import unittest

import exception
from cards.card import Card


class CardTestCase(unittest.TestCase):
    """Tests the card class"""

    def runTest(self):
        self.test_valid()
        self.test_invalid()

    def test_valid(self):
        self.assertEquals(str(Card(0)), '2s')
        self.assertEquals(str(Card(22)), 'Jd')
        self.assertEquals(str(Card(51)), 'Ac')
        self.assertEquals(Card(1).rank, 3)
        self.assertEquals(Card(51).rank, 56)

    def test_invalid(self):
        self.assertRaises(exception.InvalidCardException, lambda: str(Card('')))
        self.assertRaises(exception.InvalidCardException, lambda: str(Card(-1)))
        self.assertRaises(exception.InvalidCardException, lambda: str(Card(52)))
