__author__ = 'vishnunair'
import startState
import exit
import globals
import terminal
import home_screen
import player
import dungeon
from tabulate import tabulate

def game_sequence():
    startState.startSequence()
    game_loop()
    exit.exit_sequence()

def game_loop():
     alert_day = None

     while True:  # until we return from the function

        player_stage = globals.this_player.main_quest_stage
        curr = globals.dialogue_type[player_stage]

        if curr.startswith('c'):
            print(globals.dialogue[player_stage] + '\n')
            globals.this_player.main_quest_stage += 1
        elif curr.startswith('m'):
            print(globals.dialogue[player_stage] + '\n')
            if player_stage == 91:
                exit_bool = home_screen.process_home()
                if exit_bool is True:
                    return
                else:
                    globals.this_player.sleep()
            elif alert_day == None:
                alert_day = globals.this_player.day + 2
                exit_bool = home_screen.process_home()
                if exit_bool is True:
                    return
                else:
                    globals.this_player.sleep()
            elif alert_day is not None:
                if globals.this_player.day == alert_day:
                    globals.this_player.main_quest_stage += 1
                    alert_day = None
        elif curr is 'p':
            print(globals.dialogue[player_stage] + '\n')
            input("(Press enter to continue...)")
            globals.clear_screen()
            globals.this_player.main_quest_stage += 1
        elif curr is 'sw':
            globals.clear_screen()
            sw_tabular = [['0.', 'Generic Plasma Blaster', '3.2'], ['1.', 'Generic Electrocuter', '3',],
                          ['2.', 'Generic Fire-Starter', '2.8']]
            print(tabulate(sw_tabular, headers=['No.', 'Weapon Name', 'Damage']))
            inp = input("Enter the number of the weapon you would like to take: ")
            accepted_answers = [0,1,2]
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
            globals.this_player.current_weapon = player.Weapon(globals.weapon_names[inp])
            globals.this_player.main_quest_stage += 1
        elif curr is 'rn': # response needed
            print(globals.dialogue[player_stage] + '\n')
            print("[Enter the number of the response you would like to make:]")
            i = 1
            while globals.dialogue_type[player_stage + i] == 'r':
                print('\t' + i + '. ' + globals.dialogue[player_stage + i] + '\n')
                i += 1
            selection = input("Selection: ")
            while selection > player_stage + i - 1:
                input("You have entered an invalid option. Please try again: ")
            globals.this_player.main_quest_stage += selection
            globals.clear_screen()
            print("You: " + globals.dialogue[player_stage] + '\n')
            globals.this_player.main_quest_stage = globals.dialogue_jump_targets[player_stage]
        elif curr is 'b': # always boss in main quest
            pass # let's do this in the dungeon object itself
        elif curr.startswith('d'):
            if player_stage < 15:
                curr = dungeon.Dungeon(globals.main_quest_dungeons[0], 10, "valstr", main_quest=True)
                curr.traverse_dungeon()
            elif curr.endswith('sneak'):
                curr = dungeon.Dungeon(globals.main_quest_dungeons[1], 7, "valstr", main_quest=True)
                curr.traverse_dungeon()
            elif curr.endswith('fight'):
                curr = dungeon.Dungeon(globals.main_quest_dungeons[1], 11, "valstr", main_quest=True)
                curr.traverse_dungeon()
            elif player_stage > 70 and player_stage < 80:
                curr = dungeon.Dungeon(globals.main_quest_dungeons[2], 17, "valstr", main_quest=True)
                curr.traverse_dungeon()
            globals.this_player.main_quest_stage += 1
        elif curr is "term":
            terminal.terminal()
            globals.this_player.main_quest_stage += 1