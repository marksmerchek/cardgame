#!/usr/bin/env python3
"""Card command-line game."""

import sys
import optparse

import constant
import exception
from cards.deck import Deck
from cards.player import Player


class CardGame(object):
    """A simple card game"""

    def __init__(self):
        """Constructs CardGame object"""
        self._players = []
        self._parse_command_line()

    def _parse_command_line(self):
        """Function to get command line arguments"""
        self._parser = optparse.OptionParser()

        self._parser.add_option("--players", default=2, help="Number of players for the game. (default 2)")

        (options, args) = self._parser.parse_args(sys.argv)

        # Check players option
        try:
            players = int(options.players)
        except Exception:
            raise exception.InvalidPlayerException(f'players option [{options.players}] is invalid. must be numeric.')

        if players < constant.PLAYERS_MIN or players > constant.PLAYERS_MAX:
            message = f'[{options.players}] is not a valid number of players. ' \
                      f'( Min={constant.PLAYERS_MIN} Max={constant.PLAYERS_MAX} )'
            raise exception.InvalidPlayerException(message)

        self._players = [Player(f'player{i+1}') for i in range(players)]

    def play(self):
        """Function to play the card game"""

        # Initialize & Shuffle Deck
        deck = Deck()
        deck.shuffle()

        # Deal
        for i in range(constant.CARDS_PER_PLAYER):
            for j in range(len(self._players)):
                self._players[j].add_card(deck.deal())
                self._players[j].sort_hand()

        # Sort players by hand rank
        self._players.sort(key=lambda x: x.hand_rank)

        # Display Winner(s)
        winners = [n for n, x in enumerate(self._players) if x.hand_rank == self._players[-1].hand_rank]
        if len(winners) == 1:
            print(f'Winner: {self._players[winners[0]]}')
        else:
            for x in winners:
                print(f'Tie: {self._players[x]}')


if __name__ == '__main__':
    try:
        cg = CardGame()
        cg.play()
    except exception.InvalidPlayerException as e:
        print(e.__str__())
    except Exception as e:
        print(e.__str__())
