
import exception
from .hand import Hand
from .card import Card


class Player(object):
    """A Card Player"""

    def __init__(self, name):
        """Constructs player object"""
        self._name = name
        self._hand = Hand()

    @property
    def name(self):
        return self._name

    @property
    def hand(self):
        return self._hand

    @property
    def hand_rank(self):
        """returns to the calculated hand rank"""
        return self._hand.rank

    def add_card(self, card: Card):
        """adds a card to players hand"""
        if not isinstance(card, Card):
            raise exception.InvalidCardException(f'card [{card}] is a valid Card instance.')

        self._hand.add_card(card)

    def sort_hand(self):
        """sort players hand"""
        self._hand.sort()

    def __str__(self):
        """Return string representation of player object"""
        return f'{self._name} - {self.hand_rank} - {str(self._hand)}'

    def __eq__(self, other):
        """Return True if player hand ranks are equal"""
        return self.hand_rank == other.hand_rank

    def __lt__(self, other):
        """Return True if first player hand is less than other player hand"""
        return self.hand_rank < other.hand_rank

    def __gt__(self, other):
        """Return True if first player hand is greater than other player hand"""
        return self.hand_rank > other.hand_rank
