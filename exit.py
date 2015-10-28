"""
Handles the game's exit sequence, including saving the game.
"""


__author__ = 'Vishnu Nair'


import sys
import globals

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
        print("Save data has been written to a file named 'save.data' in the "
              "game's directory. If such a file already existed, it has been "
              "overwritten.\n")
        return
    else:
        globals.clear_screen()
        print("The game was not saved.\n")
        return


def save_game():
    """
    Saves the game by writing the player's attributes to a file called "save.data" in the game directory.
    """
    with open("save.data",'w') as save:
        save.truncate()
        player = globals.this_player
        save.writelines(player.name + '\n') # 0
        save.writelines(player.home + '\n') # 1
        save.writelines(str(player.level) + '\n') # 2
        save.writelines(str(player.xp) + '\n') # 3
        save.writelines(str(player.target_xp) + '\n') # 4
        save.writelines(str(player.total_health) + '\n') # 6
        save.writelines(str(player.attack) + '\n') # 7
        save.writelines(str(player.defense) + '\n') # 8
        save.writelines(str(player.main_quest_stage) + '\n') # 9
        save.writelines(str(player.money) + '\n') # 10
        save.writelines(str(player.assistant) + '\n') # 11
        save.writelines(str(player.current_weapon) + '\n') # 12
        save.writelines(str(player.day) + '\n') # 13
        save.writelines(str(player.sidequests) + '\n') # 14
        for item in player.inventory:
            save.writelines(item + '\n')

def exit_sequence():
    """
    Executes the main exit sequence.
    """
    prompt_for_save()
    exit_program()

if __name__ == "__main__":
    print("To play this game, run 'start_here.py.'.\n"
          "For more information about this file, see 'readme.txt'.")