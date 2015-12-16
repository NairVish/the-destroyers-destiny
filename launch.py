"""
Launches the game.
"""

__author__ = 'Vishnu Nair'

import game
import sys

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=28, cols=80))
game.game_sequence()