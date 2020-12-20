
class InvalidPlayerException(Exception):
    """Exception raised for errors in the player option"""
    pass


class DeckEmptyException(Exception):
    """Exception raised with trying to deal with no more cards"""
    pass


class InvalidCardException(Exception):
    """Exception raised for invalid card object"""
    pass
