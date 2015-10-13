__author__ = 'vishnunair'

import globals
from tabulate import tabulate

# TODO: shop implementation

def weapon_shop():
    # TODO: weapon shop implementation
    print("The Crazy Weapons Specialist\n".upper())
    # TODO: write a welcome message
    print(tabulate(globals.tabular_potions, headers=["No.", "Potion Name", "Potion Type", "Cost ($)"], tablefmt="fancy_grid"))

    pass


def potion_shop():
    # TODO: potion shop implementation
    print("The Oddly Unique Alchemist\n".upper())
    # TODO: write a welcome message
    print(tabulate(globals.tabular_weapons, headers=["No.", "Weapon Name", "Attack Power", "Cost ($)"], tablefmt="fancy_grid"))
    pass


def selling():
    print("The Really Rich Guy that Buys Everything\n".upper())

    if not globals.this_player.inventory:
        print("The Rich Guy: You have nothing to sell me. Why on Nira are you here?\n")
        print("You have nothing in your inventory. Come back when you have something to sell.\n")
        input("Press enter to return home...")
        return



        # TODO: selling implementation