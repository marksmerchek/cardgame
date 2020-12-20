import unittest

import exception
from cards.player import Player
from cards.card import Card


class PlayerTestCase(unittest.TestCase):
    """Tests the player class"""

    def runTest(self):
        self.test_empty()
        self.test_valid()
        self.test_invalid()

    def test_empty(self):
        self.assertEquals(Player('Player1').name, 'Player1')
        self.assertEquals(Player('Player1').hand_rank, 0)

    def test_valid(self):
        self.assertEquals(Player('Player1').name, 'Player1')

        player_1 = Player('Player1')
        player_1.add_card(Card(1))
        player_1.add_card(Card(24))
        player_1.add_card(Card(44))
        self.assertEquals(str(player_1.hand), "['3s', 'Kd', '7c']")
        self.assertEquals(player_1.hand_rank, 57)
        player_1.sort_hand()
        self.assertEquals(str(player_1.hand), "['3s', 'Kd', '7c']")
        self.assertEquals(str(player_1), "Player1 - 57 - ['3s', 'Kd', '7c']")

        player_2 = Player('Player2')
        player_2.add_card(Card(24))
        player_2.add_card(Card(41))
        player_2.add_card(Card(3))
        self.assertEquals(str(player_2.hand), "['Kd', '4c', '5s']")
        self.assertEquals(player_2.hand_rank, 47)
        player_2.sort_hand()
        self.assertEquals(str(player_2.hand), "['5s', '4c', 'Kd']")

        player_3 = Player('Player3')
        player_3.add_card(Card(21))
        player_3.add_card(Card(42))
        player_3.add_card(Card(5))
        self.assertEquals(str(player_3.hand), "['Td', '5c', '7s']")
        self.assertEquals(player_3.hand_rank, 47)
        player_3.sort_hand()
        self.assertEquals(str(player_3.hand), "['7s', 'Td', '5c']")

        self.assertEquals(player_1 == player_2, False)
        self.assertEquals(player_1 > player_2, True)
        self.assertEquals(player_1 < player_2, False)

        self.assertEquals(player_2 == player_3, True)
        self.assertEquals(player_2 > player_3, False)
        self.assertEquals(player_2 < player_3, False)

    def test_invalid(self):
        player = Player('Player1')
        self.assertRaises(exception.InvalidCardException, lambda: str(player.add_card('')))
