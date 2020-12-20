import unittest

import constant
import exception
from cards.deck import Deck


class DeckTestCase(unittest.TestCase):
    """Tests the deck class"""

    def runTest(self):
        self.test_valid()
        self.test_invalid()

    def test_valid(self):
        initial_deck = ['2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks', 'As', '2d', '3d', '4d',
                        '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad', '2h', '3h', '4h', '5h', '6h', '7h',
                        '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc',
                        'Jc', 'Qc', 'Kc', 'Ac']

        self.assertEquals(Deck().deck_abbr, initial_deck)

    def test_invalid(self):
        deck = Deck()
        for i in range(constant.DECK_SIZE):
            deck.deal()

        self.assertRaises(exception.DeckEmptyException, lambda: deck.deal())
