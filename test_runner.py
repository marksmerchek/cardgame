#!/usr/bin/env python3

import unittest

from tests import test_hand, test_deck, test_player, test_card

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_card.CardTestCase())
    suite.addTest(test_deck.DeckTestCase())
    suite.addTest(test_hand.HandTestCase())
    suite.addTest(test_player.PlayerTestCase())

    unittest.TextTestRunner(verbosity=2).run(suite)
