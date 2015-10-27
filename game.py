__author__ = 'vishnunair'
import start_state
import exit
import globals
import terminal
import home_screen
import player
import dungeon
from tabulate import tabulate

def game_sequence():
    start_state.startSequence()
    game_loop()
    exit.exit_sequence()

def game_loop():
     alert_day = None

     while True:  # until we hit a return statement

        player_stage = globals.this_player.main_quest_stage
        curr = globals.dialogue_type[player_stage]

        if curr.startswith('c'):
            print(globals.dialogue[player_stage] + '\n')
            globals.this_player.main_quest_stage += 1
        elif curr.startswith('m'):
            if player_stage == 91:
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
                    globals.this_player.main_quest_stage += 1
            elif alert_day is not None:
                if globals.this_player.day == alert_day:
                    globals.this_player.main_quest_stage += 1
                    alert_day = None
                else:
                    print(globals.dialogue[player_stage] + '\n')
                    exit_bool = home_screen.process_home()
                    if exit_bool is True:
                        return
                    else:
                        globals.this_player.sleep()
        elif curr is 'p':
            print(globals.dialogue[player_stage] + '\n')
            input("(Press enter to continue...)")
            globals.clear_screen()
            globals.this_player.main_quest_stage += 1
        elif curr.startswith('sw'):
            print(globals.dialogue[player_stage] + '\n')
            globals.clear_screen()
            sw_tabular = [['0.', globals.weapon_names[0], globals.weapon_powers[0]],
                          ['1.', globals.weapon_names[1],  globals.weapon_powers[1],],
                          ['2.', globals.weapon_names[2],  globals.weapon_powers[2]]]
            print(tabulate(sw_tabular, headers=['No.', 'Weapon Name', 'Damage']) + '\n')
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
            for num in range(0,3):
                globals.this_player.inventory.append(globals.potion_names[0])
            globals.this_player.current_weapon = player.Weapon(globals.weapon_names[inp])
            globals.this_player.main_quest_stage += 1
        elif curr.startswith('rn'): # response needed
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
        elif curr.startswith('d'):
            print(globals.dialogue[player_stage] + '\n')
            input("(Press enter to continue...)")
            game_over_reversion_target = globals.this_player.main_quest_stage
            if globals.dialogue_jump_targets[globals.this_player.main_quest_stage] != 0:
                    globals.this_player.main_quest_stage = globals.dialogue_jump_targets[globals.this_player.main_quest_stage]
            try:
                if player_stage < 15:
                    curr = dungeon.Dungeon(init_name=globals.main_quest_dungeons[0], init_length=10, enemy_type="valstr", main_quest=True)
                    curr.traverse_dungeon()
                    globals.this_player.toggle_sidequest_flag()
                elif curr.endswith('sneak'):
                    globals.this_player.toggle_assistant_flag()
                    curr = dungeon.Dungeon(init_name=globals.main_quest_dungeons[1], init_length=11, enemy_type="valstr", main_quest=True)
                    curr.traverse_dungeon()
                elif curr.endswith('fight'):
                    globals.this_player.toggle_assistant_flag()
                    curr = dungeon.Dungeon(init_name=globals.main_quest_dungeons[1], init_length=7, enemy_type="valstr", main_quest=True)
                    curr.traverse_dungeon()
                elif player_stage > 70 and player_stage < 80:
                    curr = dungeon.Dungeon(init_name=globals.main_quest_dungeons[2], init_length=17, enemy_type="valstr", main_quest=True)
                    curr.traverse_dungeon()
            except globals.GameOver():
                globals.clear_screen()
                print("<Player Note: Your current health has reached zero!>\n")
                print("As the world fades to black, a white light suddenly flashes before you.\n"
                      "In an instant, you find yourself back at your home. You look at the time.\n"
                      "It's right before you went into that fateful encounter.\n")
                input("Press enter to continue...")
                globals.this_player.main_quest_stage = game_over_reversion_target
            else:
                globals.this_player.main_quest_stage += 1
        elif curr is "term":
            terminal.terminal()
            globals.this_player.main_quest_stage += 1