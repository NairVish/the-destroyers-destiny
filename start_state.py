"""
Handles the start sequence for the game.
"""

__author__ = 'Vishnu Nair'

import os
import time
import globals
from exit import exit_program

def print_intro():
    """
    Prints the intro screen.
    """
    globals.clear_screen()
    intro_text = (
        "THE DESTROYER'S DESTINY\n"
        "\tCSC 11300 Project 1\n"
        "\tBy: Vishnu Nair\n\n"
        "(C) 2015 Vishnu Nair. All rights reserved.\n"
    )
    print(intro_text)
    time.sleep(2.5)
    globals.clear_screen()

def show_start_menu():  # The startup menu
    """
    Prints the main startup menu and requests user input of either starting New Game, continuing (if save is found),
    or quitting.
    """
    print('Main Menu'.upper())
    print('\t1. Start a new game.')
    accepted_answers = ['1','q']
    save = find_save()
    if save is not None:
        print('\t2. Continue from existing save.')
        accepted_answers = ['1','2','q']
    print('\tq. Quit.')
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

def find_file(name, path):
    """
    :param name: Name of file.
    :param path: Directory to look in.
    Looks for a specific file in a specific directory. Returns path if found; otherwise returns nothing.
    """
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def find_save():
    """
    Looks for a game save file in the current working directory.
    If not found, returns None.
    If found, returns opened file.
    """
    result = find_file('save.data', os.getcwd())
    if result is None:
        return None
    else:
        return open('save.data','r')

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
        saved_stats = [line.rstrip('\n') for line in save.readlines()]
        try:
            inventory = [item for item in saved_stats[14:(len(saved_stats))]]
        except IndexError:
            inventory = []
        else:
            pass
        print("Loading existing save...")
        print("Loading save data for %s..." % saved_stats[0])
        globals.declare_existing_player(saved_stats, inventory)
        save.close()
    print("\nThe game was successfully loaded!")
    input("(Press enter to continue...)")
    globals.clear_screen()

def startSequence():
    """
    Executes start sequence for start state
    """
    globals.init_globals()
    print_intro()
    load_player()

if __name__ == "__main__":
    print("To play this game, run 'start_here.py.'.\n"
          "For more information about this file, see 'readme.txt'.")