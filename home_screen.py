__author__ = 'vishnunair'

import globals
from globals import clear_screen
import shop
import exit
import sidequest

def print_home_screen():
    print("HOME SCREEN\n")

    print("Day %s" % globals.this_player.day)
    print("%s, Level %d" % (globals.this_player, globals.this_player.level))
    print("Home Province: %s\n" % globals.this_player.home)

    print("\t1. Sleep until tomorrow.")
    print("\t2. Go to a shop in the city.")
    print("\t3. Check for side jobs.")
    print("\t4. See detailed statistics.")
    print("\t5. See your inventory.")
    print("\t6. Equip another weapon.")
    print("\t7. Use an enhancement potion.")
    print("\t8. Exit (and Save).\n")

    inp = input("What would you like to do? ")
    accepted_answers = ['1','2','3','4','5','6','7','8']
    while input not in accepted_answers:
        inp = input("You have entered an invalid option. Please try again: ")
    return inp

def process_home():
    sidequest.setup_quest_board()
    while True:
        inp = print_home_screen()
        globals.clear_screen()
        if inp is '1':
            globals.this_player.sleep()
            sidequest.purge_quest_board()
            sidequest.setup_quest_board() # return to main game loop instead and do all this there.
        elif inp is '2':
            shop_input = print_shop_selector()
            globals.clear_screen()
            if shop_input is '1':
                shop.potion_shop()
            elif shop_input is '2':
                shop.weapon_shop()
            elif shop_input is '3':
                shop.selling()
        elif inp is '3':
            try:
                if globals.this_player.sidequests is False:
                    print("You are an Unknown.\n"
                          "Unknowns are not allowed to view or participate in quests on the quest board.\n"
                          "You must return home.\n")
                    input("Press enter to continue...")
                    continue
                sidequest.quest_board()
                sidequest.purge_quest_board()
                sidequest.setup_quest_board()
            except globals.GameOver():
                print("As the world fades to black, a white light suddenly flashes before you.\n"
                      "In an instant, you find yourself back at your home. You look at the time.\n"
                      "It's right before you went into that fateful encounter.\n")
                input("Press enter to continue...")
        elif inp is '4':
            globals.this_player.print_stats()
        elif inp is '5':
            globals.this_player.see_inventory()
        elif inp is '6':
            globals.this_player.equip_weapon()
        elif inp is '7':
            globals.this_player.use_potion(enhancement=True)
        elif inp is '8':
            exit.exit_sequence() # return to main game loop instead and do all this there.
        clear_screen()
        # TODO: maybe return certain values to indicate state transition?

def print_shop_selector():
    print("SHOPS\n")

    print("\t1. The Oddly Unique Alchemist")
    print("\t2. The Crazy Weapons Specialist")
    print("\t3. The Really Rich Guy that Buys Everything")
    print("\t4. Return to Home Screen.\n")

    inp = input("Where would you like to go? ")
    while input not in range(1,5):
        inp = input("You have entered an invalid option. Please try again: ")
    return inp
