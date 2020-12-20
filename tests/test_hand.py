import unittest

import exception
from cards.hand import Hand
from cards.card import Card


class HandTestCase(unittest.TestCase):
    """Tests the hand class"""

    def runTest(self):
        self.test_empty()
        self.test_valid()
        self.test_invalid()

    def test_empty(self):
        self.assertEquals(str(Hand()), "[]")
        self.assertEquals(Hand().rank, 0)

    def build_hand(self, val1: int, val2: int, val3: int):
        hand = Hand()
        hand.add_card(Card(val1))
        hand.add_card(Card(val2))
        hand.add_card(Card(val3))
        return hand

    def test_valid(self):
        hand_1 = self.build_hand(33, 0, 22)
        hand_2 = self.build_hand(31, 5, 19)
        hand_3 = self.build_hand(31, 12, 19)

        self.assertEquals(str(hand_1), "['9h', '2s', 'Jd']")
        self.assertEquals(hand_1.rank, 51)
        hand_1.sort()
        self.assertEquals(str(hand_1), "['2s', 'Jd', '9h']")

        self.assertEquals(str(hand_2), "['7h', '7s', '8d']")
        self.assertEquals(hand_2.rank, 44)

        self.assertEquals(str(hand_3), "['7h', 'As', '8d']")
        self.assertEquals(hand_3.rank, 51)
        hand_3.sort()
        self.assertEquals(str(hand_3), "['As', '8d', '7h']")

        self.assertEquals(hand_1 == hand_2, False)
        self.assertEquals(hand_1 > hand_2, True)
        self.assertEquals(hand_1 < hand_2, False)
        self.assertEquals(hand_1 == hand_3, True)
        self.assertEquals(hand_1 < hand_3, False)
        self.assertEquals(hand_1 > hand_3, False)

    def test_invalid(self):
        hand = Hand()
        self.assertRaises(exception.InvalidCardException, lambda: str(hand.add_card('')))
