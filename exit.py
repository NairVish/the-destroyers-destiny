__author__ = 'vishnunair'
import sys
import globals

def exit_program():
    globals.clear_screen()
    print("The program has ended. Thank you for playing.")
    print('\n')
    sys.exit()

def prompt_for_save():
    globals.clear_screen()
    inp = input("Would you like to save the game? (y/n) ")
    if inp is 'y':
        save_game()
    else:
        return

def save_game():
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
    prompt_for_save()
    exit_program()