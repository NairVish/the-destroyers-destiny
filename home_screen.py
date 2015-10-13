__author__ = 'vishnunair'

import globals

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
    print("\t5. Exit (and Save).\n")

    return input("What would you like to do? ")

def print_shop_selector():
    print("SHOPS\n")

    print("\t1. The Oddly Unique Alchemist")
    print("\t2. The Crazy Weapons Specialist")
    print("\t3. The Really Rich Guy that Buys Everything")
    print("\t4. Return to Home Screen.\n")

    return input("Where would you like to go? ")

def grab_home_input():
    # TODO: handle home screen input
    pass