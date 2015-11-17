"""
The game's main file.
Executes the game sequence and the main game loop.
"""

__author__ = 'Vishnu Nair'

import start_state
import exit
import globals
import terminal
import home_screen
import player
import dungeon
from tabulate import tabulate
from colorama import Fore, init

init(autoreset=True)

def game_sequence():
    """
    Executes the game sequence from start to finish.
    """
    try:
        start_state.startSequence()
        game_loop()
        exit.exit_sequence()
    except KeyboardInterrupt:
        exit.force_exit_program()


def game_loop():
    """
    The main game loop. Handles all main quest stage advancement (outside of main dungeons). Also handles all dialogue
    output, responses, main quest dungeons, initial weapon selection, and terminal sequence initiation. Loops using
    data from dialogue.csv until we return from the home screen. We return when True is returned from the home screen.
    """
    alert_day = None
    game_over_reversion_target = None

    while True:  # until we hit a return statement

        player_stage = globals.this_player.main_quest_stage
        curr = globals.dialogue_type[player_stage]

        if curr.startswith('c'):    # 'c': immediately continue with dialogue
            print(globals.dialogue[player_stage] + '\n')
            globals.this_player.main_quest_stage += 1
        elif curr.startswith('m'):  # 'm': show home screen
            if player_stage == 91:
                print(globals.dialogue[player_stage] + '\n')
                exit_bool = home_screen.process_home()
                if exit_bool is True:
                    return
                else:
                    globals.this_player.sleep()
            elif alert_day is None:
                print(globals.dialogue[player_stage] + '\n')
                alert_day = globals.this_player.day + 2
                exit_bool = home_screen.process_home()
                if exit_bool is True:
                    return
                else:
                    globals.this_player.sleep()
                    game_over_reversion_target = globals.this_player.main_quest_stage
                    globals.this_player.main_quest_stage += 1
            elif alert_day is not None:
                if globals.this_player.day == alert_day:
                    game_over_reversion_target = globals.this_player.main_quest_stage
                    globals.this_player.main_quest_stage += 1
                    alert_day = None
                else:
                    print(globals.dialogue[player_stage] + '\n')
                    exit_bool = home_screen.process_home()
                    if exit_bool is True:
                        return
                    else:
                        globals.this_player.sleep()
        elif curr is 'p':   # 'p': pause until user presses 'enter' key
            print(globals.dialogue[player_stage] + '\n')
            input("(Press enter to continue...)")
            globals.clear_screen()
            globals.this_player.main_quest_stage += 1
        elif curr.startswith('sw'):     # 'sw': initiate first weapon selection just before first main quest dungeon
            print(globals.dialogue[player_stage] + '\n')
            globals.clear_screen()
            sw_tabular = [['0.', globals.weapon_names[0], globals.weapon_powers[0]],
                          ['1.', globals.weapon_names[1], globals.weapon_powers[1], ],
                          ['2.', globals.weapon_names[2], globals.weapon_powers[2]]]
            print(tabulate(sw_tabular, headers=['No.', 'Weapon Name', 'Damage']) + '\n')
            inp = input("Enter the number of the weapon you would like to take: ")
            accepted_answers = [0, 1, 2]
            input_legal = False
            while input_legal is False:
                try:
                    inp = int(inp)
                except ValueError:
                    inp = input("You have entered an invalid option. Please try again: ")
                    continue
                else:
                    if inp in accepted_answers:
                        input_legal = True
                    else:
                        inp = input("You have entered an invalid option. Please try again: ")
            globals.this_player.inventory.append(globals.weapon_names[inp])
            for num in range(0, 3):
                globals.this_player.inventory.append(globals.potion_names[0])
            globals.this_player.current_weapon = player.Weapon(globals.weapon_names[inp])
            globals.this_player.main_quest_stage += 1
        elif curr.startswith('rn'):  # 'rn': response needed, output responses and process user-desired response
            print(globals.dialogue[player_stage] + '\n')
            print("[Enter the number of the response you would like to make:]")
            i = 1
            while globals.dialogue_type[player_stage + i] == 'r':
                print('\t' + str(i) + '. ' + globals.dialogue[player_stage + i])
                i += 1
            selection = input("Selection: ")
            while True:
                try:
                    selection = int(selection)
                except ValueError:
                    selection = input("You have entered an invalid option. Please try again: ")
                    continue
                else:
                    if int(selection) > i or int(selection) <= 0:
                        selection = input("You have entered an invalid option. Please try again: ")
                        continue
                    break
            globals.this_player.main_quest_stage += selection
            globals.clear_screen()
            print("You: " + globals.dialogue[globals.this_player.main_quest_stage] + '\n')
            globals.this_player.main_quest_stage = globals.dialogue_jump_targets[globals.this_player.main_quest_stage]
        elif curr.startswith('d'):  # 'd': initiate main quest dungeon; NOTE: sidequest dungeons are handled by the home screen
            print(globals.dialogue[player_stage] + '\n')
            input("(Press enter to continue...)")
            # game_over_reversion_target = globals.this_player.main_quest_stage
            if globals.dialogue_jump_targets[globals.this_player.main_quest_stage] != 0:
                globals.this_player.main_quest_stage = globals.dialogue_jump_targets[
                    globals.this_player.main_quest_stage]
            try:
                if player_stage < 15:
                    curr = dungeon.Dungeon(init_name=globals.main_quest_dungeons[0] % globals.this_player.home,
                                           init_length=10, enemy_type="valstr", main_quest=True)
                    curr.traverse_dungeon()
                    globals.this_player.toggle_sidequest_flag()
                elif curr.endswith('sneak'):
                    globals.this_player.toggle_assistant_flag()
                    curr = dungeon.Dungeon(init_name=globals.main_quest_dungeons[1], init_length=11,
                                           enemy_type="valstr", main_quest=True)
                    curr.traverse_dungeon()
                elif curr.endswith('fight'):
                    globals.this_player.toggle_assistant_flag()
                    curr = dungeon.Dungeon(init_name=globals.main_quest_dungeons[1], init_length=7, enemy_type="valstr",
                                           main_quest=True)
                    curr.traverse_dungeon()
                elif player_stage > 70 and player_stage < 80:
                    curr = dungeon.Dungeon(init_name=globals.main_quest_dungeons[2], init_length=17, enemy_type="valstr",
                                           main_quest=True)
                    curr.traverse_dungeon()
            except KeyboardInterrupt:
                exit.force_exit_program()
            except:
                print(Fore.RED + "<Alert: Your current health has reached zero!>\n")
                print("As the world fades to black, a white light suddenly flashes before you.\n"
                      "In an instant, you find yourself back at your home. You look at the time.\n"
                      "It's right before you went into that fateful encounter.\n")
                print("<Note: Your game's state has been reverted. Any loot collected and XP gained\n"
                      "will carry over. However, you must go through the respective story sequence and"
                      "dungeon again. Upgrade your weapon, buy some more potions, or gain some more"
                      "XP through sidequests before doing so.>\n")
                input("Press enter to continue...")
                globals.clear_screen()
                globals.this_player.main_quest_stage = game_over_reversion_target
            else:
                globals.this_player.main_quest_stage += 1
        elif curr.startswith("term"):   # 'term': initiate terminal sequence
            print(globals.dialogue[player_stage] + '\n')
            input("(Press enter to proceed...)")
            terminal.terminal()
            globals.this_player.main_quest_stage += 1

if __name__ == "__main__":
    print("To play this game, run 'start_here.py.'.\n"
          "For more information about this file, see 'readme.txt'.")
