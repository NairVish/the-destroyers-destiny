__author__ = 'vishnunair'

import os
import time
import globals
from exit import exit_program

def print_intro():
    """ Print the intro screen. """
    intro_text = (
        "THIS IS SOME INTRO TEXT."
        "I HAVE NO IDEA WHAT I'M GOING TO PUT HERE."
        "SO I'M PUTTING SOME PLACEHOLDER TEXT HERE."
    )
    print(intro_text)
    time.sleep(4)
    globals.clear_screen()

def show_start_menu():  # The startup menu
    """
    Prints the main startup menu and and requests user input of either starting New Game, continuing (if save is found),
    or quitting.
    """
    print('Main Menu')
    print('\t1. Start a New Game.')
    accepted_answers = ['1','q']
    save = find_save()
    if save is not None:
        print('\t2. Continue from existing save.')
        print('\tq. Quit')
        accepted_answers = ['1','2','q']
    answer = input('Choose your desired option. ')
    while answer not in accepted_answers:
        answer = input('You have entered an inavlid option. Please enter a valid option,')
    globals.clear_screen()
    if answer is '1':
        return None
    elif answer is 'q':
        exit_program()
    else:
        return save

def find_file(name, path):
    """
    :param name: Name of file
    :param path: Directory to look in
    Looks for a specific file in a specific directory. Returns path if found; otherwise returns None.
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
    if result == None:
        return None
    else:
        return open('save.data','r')

def load_player():
    """
    Requests save file from user's input at startup menu.
    If there is no save file OR user specifically requests new game, asks for character name and declares new player
    as a global instance.
    If there is a save file AND user requests continuing from save, extract data and inventory (if there are items)
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
            inventory = [line for line in saved_stats[14:(len(saved_stats)-1)]]
        except IndexError:
            inventory = []
        else:
            pass
        print("Loading existing save...")
        print("Loading save data for %s" % saved_stats[0])
        globals.declare_existing_player(saved_stats, inventory)
        save.close()

def startSequence():
    """
    Executes start sequence for start state
    """
    print_intro()
    load_player()