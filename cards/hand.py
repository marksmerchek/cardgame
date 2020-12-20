import exception
from cards.card import Card


class Hand(object):
    """A set of cards"""

    def __init__(self):
        """Constructs hand object"""
        self._hand = []
        self._rank = 0

    @property
    def rank(self):
        """returns to the calculated hand rank"""
        return self.determine_hand_rank()

    def add_card(self, card: Card):
        """adds a card to the hand"""

        if not isinstance(card, Card):
            raise exception.InvalidCardException(f'card [{card}] is a valid Card instance.')

        self._hand.append(card)

    def sort(self):
        """sort hand based on rank"""
        self._hand.sort(key=lambda x: x.rank)

    def determine_hand_rank(self):
        """sum up each card rank to get hand rank"""
        return sum([s.rank for s in self._hand])

    def __str__(self):
        """Return String representation of object"""
        return [str(s) for s in self._hand].__str__()

    def __eq__(self, other):
        """Return True if hand ranks are equal"""
        return self.determine_hand_rank() == other.determine_hand_rank()

    def __lt__(self, other):
        """Return True if first hand is less than other hand"""
        return self.determine_hand_rank() < other.determine_hand_rank()

    def __gt__(self, other):
        """Return True if first hand is greater than other hand"""
        return self.determine_hand_rank() > other.determine_hand_rank()
