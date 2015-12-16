"""
Handles the game's exit sequence, including saving the game.
"""

__author__ = 'Vishnu Nair'

import sys
import globals
import json
import os
from colorama import Fore, init

init(autoreset=True)


def exit_program():
    """
    Exits the program using sys.exit() and prints a message notifying the user.
    """
    print("The program has ended. Thank you for playing.\n")
    sys.exit()


def force_exit_program():
    """
    Force exits the program when the KeyboardInterrupt exception is raised (i.e. when Ctrl-C is pressed).

    Note: In many cases where a KeyboardInterrupt occurs, sys.exit() does not work because it simply raises a
    SystemExit exception in the thread/module where it is called. Since we are usually several modules deep during
    program execution, sys.exit() often does not work as intended. In these cases, it is more appropriate to call
    os._exit() because it provides a more sledgehammer-like approach to leaving the program. (The parameter '0' in
    os._exit() represents the normal exit code.)
    """
    globals.clear_screen()
    print(Fore.RED + "You have left the program. Thank you for playing.\n")
    os._exit(0)


def prompt_for_save():
    """
    Prompts for save when the user decides to exit the game. Prints message echoing user's decision.
    """
    globals.clear_screen()
    inp = input("Would you like to save the game? (y/n) ")
    accepted_answers = ['y','n']
    while inp not in accepted_answers:
        inp = input("You have entered an invalid option. Please try again:")
    if inp is 'y':
        save_game()
        globals.clear_screen()
        print(Fore.GREEN + "Save data has been written to a file named 'save.json' in the "
              "game's directory. If such a file already existed, it has been "
              "overwritten.\n")
        return
    else:
        globals.clear_screen()
        print(Fore.RED + "The game was not saved.\n")
        return


def save_game():
    """
    Saves the game by writing the player's attributes to a JSON file called "save.json" in the game directory.
    """
    player = globals.this_player
    save_data = {}
    save_data['name'] = player.name
    save_data['home'] = player.home
    save_data['level'] = player.level
    save_data['xp'] = player.xp
    save_data['target_xp'] = player.target_xp
    save_data['health'] = player.current_health
    save_data['attack'] = player.attack
    save_data['defense'] = player.defense
    save_data['main_quest_stage'] = player.main_quest_stage
    save_data['money'] = player.money
    save_data['assistant'] = player.assistant
    save_data['weapon'] = str(player.current_weapon)
    save_data['day'] = player.day
    save_data['sidequests'] = player.sidequests
    save_data['inventory'] = player.inventory
    save_data['date'] = player.date
    save_data['start_date'] = player.start_date
    save_data['date_num_days'] = player.date_num_days

    with open("save.json",'w') as save:
        save.truncate()
        json.dump(save_data, save)

def exit_sequence():
    """
    Executes the main exit sequence.
    """
    prompt_for_save()
    exit_program()

if __name__ == "__main__":
    print("To play this game, run 'launch.py'.\n"
          "For more information about this file, see 'readme.txt'.")