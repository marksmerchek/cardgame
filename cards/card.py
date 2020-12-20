import constant
import exception


class Card(object):
    """A playing card"""

    def __init__(self, val: int):
        """val is a value in [0,51] where
           [0,12] represents the 2-A ranks in constant.SUIT_ABBR[0]
           [13,25] represents the 2-A ranks in constant.SUIT_ABBR[1]
           [26-38] represents the 2-A ranks in constant.SUIT_ABBR[2]
           [39,51] represents the 2-A ranks in constant.SUIT_ABBR[3]
        """
        try:
            card_val = int(val)
        except Exception:
            raise exception.InvalidCardException(f'card value [{val}] is invalid. Must be numeric.')

        if card_val < 0 or card_val > 51:
            raise exception.InvalidCardException(f'card value [{val}] is invalid. Outside range [0..52].')

        self._suit = int(val / 13)
        self._face = val % 13
        self._rank = (self._suit + 1) * (self._face + 2)

    @property
    def suit(self):
        return self._suit

    @property
    def face(self):
        return self._face

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        """Return string representation of player object"""
        return constant.FACE_ABBR[self._face] + constant.SUIT_ABBR[self._suit]
