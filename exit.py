"""
Handles the game's exit sequence, including saving the game.
"""

__author__ = 'Vishnu Nair'

import sys
import globals
import json

def exit_program():
    """
    Exits the program using sys.exit() and prints a message notifying the user.
    """
    print("The program has ended. Thank you for playing.\n")
    sys.exit()


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
        print("Save data has been written to a file named 'save.json' in the "
              "game's directory. If such a file already existed, it has been "
              "overwritten.\n")
        return
    else:
        globals.clear_screen()
        print("The game was not saved.\n")
        return


def save_game():
    """
    Saves the game by writing the player's attributes to a file called "save.json" in the game directory.
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
    print("To play this game, run 'start_here.py.'.\n"
          "For more information about this file, see 'readme.txt'.")