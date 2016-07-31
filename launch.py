"""
Launches the game.
"""

__author__ = 'Vishnu Nair'

import sys

import game

if __name__ == "__main__":
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=28, cols=103))  # resize terminal window if possible
    game.game_sequence()
