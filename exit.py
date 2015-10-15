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
    with open("save,data",'w') as save:
        save.truncate()
        player = globals.this_player
        save.writelines(player.name + '\n')
        save.writelines(player.province + '\n')
        save.writelines(player.level + '\n')
        save.writelines(player.xp + '\n')
        save.writelines(player.target_xp + '\n')
        save.writelines(player.health + '\n')
        save.writelines(player.total_health + '\n')
        save.writelines(player.attack + '\n')
        save.writelines(player.defense + '\n')
        save.writelines(player.speed + '\n')
        save.writelines(player.main_quest_stage + '\n')
        save.writelines(player.money + '\n')
        save.writelines(player.assistant + '\n')
        save.writelines(player.current_weapon + '\n')
        save.writelines(player.day + '\n')
        save.writelines(player.sidequests + '\n')
        for item in player.inventory:
            save.writelines(item + '\n')

def exit_sequence():
    prompt_for_save()
    exit_program()