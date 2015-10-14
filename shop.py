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

    tabular_data = []
    for item in globals.this_player.inventory:
        for num in range(len(globals.this_player.inventory)):
            tmp = []
            tmp.append(num)
            tmp.append(item)
            if item in globals.potion_names:
                tmp.append(globals.potion_cost[globals.potion_names.index(item)])
            elif item in globals.weapon_names:
                tmp.append(globals.weapon_cost[globals.weapon_names.index(item)])
            elif item in globals.loot_names:
                tmp.append(globals.loot_values[globals.loot_names.index(item)])
            elif item in globals.rare_loot_names:
                tmp.append(globals.rare_loot_values[globals.rare_loot_names.index(item)])
            tabular_data.append(tmp)

    print(tabulate(tabular_data, headers=["No." "Item Name" "Value ($)"]))

    inp = ""
    while inp is not 'q':
        inp = "Please enter the number of the item you would like to sell. Enter the letter 'q' to leave. "

        if inp is not 'q':
            try:
                inp = int(inp)
            except ValueError:
                print("You did not enter a number. Please try again.")
            else:
                inventory.remove(inventory[inp])

    # TODO: return to home screen