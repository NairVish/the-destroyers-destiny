"""
Handles the start sequence for the game.
"""

__author__ = 'Vishnu Nair'

import os
import time
import globals
import json
from exit import exit_program

from colorama import Fore, init

init(autoreset=True)

def print_intro():
    """
    Prints the intro screen.
    """
    globals.clear_screen()
    print(
        "THE DESTROYER'S DESTINY\n"
        "\tCSC 11300 Projects 1 & 2\n"
        "\tBy: Vishnu Nair\n\n"
        "(C) 2015 Vishnu Nair. All rights reserved.\n"
    )


def show_start_menu():  # The startup menu
    """
    Prints the main startup menu and requests user input of either starting New Game, continuing (if save is found),
    or quitting.
    """
    print('MAIN MENU')
    print('\t1. Start a new game.')
    accepted_answers = ['1','q']
    save = find_save()
    if save is not None:
        print('\t2. Continue from existing save.')
        accepted_answers = ['1','2','q']
    print('\tq. Quit.\n')
    answer = input('Choose your desired option: ')
    while answer not in accepted_answers:
        answer = input('You have entered an invalid option. Please try again: ')
    globals.clear_screen()
    if answer is '1':
        return None
    elif answer is 'q':
        exit_program()
    else:
        return save


def find_save():
    """
    Looks for a game save file (called 'save.json') in the current working directory.
    If not found, returns None.
    If found, returns opened file.
    """
    if 'save.json' in os.listdir(os.getcwd()):
        return open('save.json','r')
    else:
        return None


def load_player():
    """
    Requests save file as per user's input at startup menu.
    If there is no save file OR user specifically requests a new game, asks for character name and declares new player
    as a global instance.
    If there is a save file AND user requests continuing from save, extracts data and inventory (if there are items)
    from save and declares new global player instance using existing data.
    """
    save = show_start_menu()
    if save is None:
        print("NEW GAME START")
        name = input('Please enter a name for your character: ')
        globals.declare_new_player(name)
    else:
        save_data = json.load(save)
        print("Loading existing save...")
        print("Loading save data for %s..." % save_data['name'])
        globals.declare_existing_player(save_data)
        save.close()
    print(Fore.GREEN + "\nThe game was successfully loaded!")
    input("(Press enter to continue...)")
    globals.clear_screen()


def startSequence():
    """
    Executes start sequence for start state
    """
    print_intro()
    globals.init_globals()
    time.sleep(2.3)
    globals.clear_screen()
    load_player()

if __name__ == "__main__":
    print("To play this game, run 'launch.py'.\n"
          "For more information about this file, see 'readme.txt'.")