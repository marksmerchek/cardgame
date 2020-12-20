import random

import constant
import exception
from .card import Card


class Deck(object):
    """A single deck of playing cards"""

    def __init__(self):
        """Constructs deck object"""
        self._deck = [Card(i) for i in range(constant.DECK_SIZE)]

    @property
    def deck(self):
        """returns the deck array of card objects"""
        return self._deck

    @property
    def deck_abbr(self):
        """returns the deck array of abbreviated card strings"""
        return [str(s) for s in self._deck]

    def shuffle(self):
        """Shuffle the deck"""
        random.seed()

        for i in range(random.randint(1, constant.SHUFFLE_TIMES)):
            random.shuffle(self._deck)

    def deal(self):
        """Deal a single card off the top of the deck"""

        if len(self._deck) == 0:
            raise exception.DeckEmptyException(f'No more cards, the deck is empty')

        card = self._deck.pop()

        if not card:
            raise Exception(f'Invalid card object [{card}]')

        return card

    def __str__(self):
        """Return String representation of object"""
        return [str(s) for s in self._deck].__str__()
