"""
Launches the game.
"""

__author__ = 'Vishnu Nair'

import game
import sys

if __name__ == "__main__":
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=28, cols=80))  # resize terminal window if possible
    game.game_sequence()
