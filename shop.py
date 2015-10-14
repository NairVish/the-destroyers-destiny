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
    inventory_dict = {}
    for item in globals.this_player.inventory:
        for num in range(len(globals.this_player.inventory)):
            tmp = []
            val = 0
            tmp.append(num)
            tmp.append(item)
            if item in globals.potion_names:
                val = globals.potion_cost[globals.potion_names.index(item)]
            elif item in globals.weapon_names:
                val = globals.weapon_cost[globals.weapon_names.index(item)]
            elif item in globals.loot_names:
                val = globals.loot_values[globals.loot_names.index(item)]
            elif item in globals.rare_loot_names:
                val = globals.rare_loot_values[globals.rare_loot_names.index(item)]
            tmp.append(val)
            inventory_dict[item] = val
            tabular_data.append(tmp)

    print(tabulate(tabular_data, headers=["No." "Item Name" "Value ($)"]))

    inp = "Please enter the number of the item you would like to sell. Enter the letter 'q' to leave. "
    while inp is not 'q':
        if inp is not 'q':
            try:
                inp = int(inp)
            except ValueError:
                print("You did not enter a number. Please try again.")
            else:
                globals.this_player.money += inventory_dict[globals.this_player.inventory[inp]]
                globals.this_player.inventory.remove(globals.this_player.inventory[inp])
                inp = input("Please enter the number of another item you would like to sell, else enter the letter 'q' to leave.")

    # TODO: return to home screen