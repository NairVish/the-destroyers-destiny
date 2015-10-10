__author__ = 'vishnunair'
from enum import Enum

def game_loop():
    states = Enum('states', 'start home_screen main_quest radiant exit')
    state = states.start

    while state != states.exit:
        if state == states.start:
            pass # for now
