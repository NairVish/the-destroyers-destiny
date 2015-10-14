__author__ = 'vishnunair'

import globals
from tabulate import tabulate


# TODO: shop implementation

def weapon_shop():
    # TODO: weapon shop implementation
    print("The Crazy Weapons Specialist\n".upper())
    print("Welcome to The Craxy Weapons Specialist. What would you like to buy?")
    print(tabulate(globals.tabular_potions, headers=["No.", "Potion Name", "Potion Type", "Cost ($)"],
                   tablefmt="fancy_grid"))

    inp = input("\nPlease enter the number of the item you would like to buy. Enter the letter 'q' to leave: ")
    while inp is not 'q':
        try:
            inp = int(inp)
        except ValueError:
            inp = input("You did not enter a number. Please enter a valid option: ")
        else:
            if inp >= len(globals.weapon_names):
                inp = input("You have entered an invalid option. Please enter a valid option: ")
                continue
            globals.this_player.inventory.append(globals.weapon_names[inp])
            globals.this_player.money -= globals.weapon_cost[inp]
            inp = input(
                "Please enter the number of another item you would like to buy, else enter the letter 'q' to leave: ")

    # TODO: Return to home


def potion_shop():
    # TODO: potion shop implementation
    print("The Oddly Unique Alchemist\n".upper())
    # TODO: write a welcome message
    print(tabulate(globals.tabular_weapons, headers=["No.", "Strength (Points)", "Type", "Cost ($)"],
                   tablefmt="fancy_grid"))

    inp = input("\nPlease enter the number of the item you would like to buy. Enter the letter 'q' to leave: ")
    while inp is not 'q':
        try:
            inp = int(inp)
        except ValueError:
            inp = input("You did not enter a number. Please enter a valid option: ")
        else:
            if inp >= len(globals.potion_names):
                inp = input("You have entered an invalid option. Please enter a valid option: ")
                continue
            globals.this_player.inventory.append(globals.potion_names[inp])
            globals.this_player.money -= globals.potion_cost[inp]
            inp = input(
                "Please enter the number of another item you would like to buy, else enter the letter 'q' to leave: ")
    # TODO: Return to home


def selling():
    print("The Really Rich Guy that Buys Everything\n".upper())

    if not globals.this_player.inventory:
        print("The Rich Guy: You have nothing to sell me. Why on Nira are you here?\n")
        print("You have nothing in your inventory. Come back when you have something to sell.\n")
        input("Press enter to return home...")
        return

    tabular_data = []
    inventory_dict = {}
    items_to_remove = []
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

    inp = input("Please enter the number of the item you would like to sell. Enter the letter 'q' to leave: ")
    while inp is not 'q':
        try:
            inp = int(inp)
        except ValueError:
            inp = input("You did not enter a number. Please enter a valid option: ")
        else:
            if tabular_data[inp][0] is "SOLD!" or inp >= len(globals.this_player.inventory):
                inp = input("You have entered an invalid option. Please enter a valid option: ")
                continue
            if tabular_data[inp][0] is globals.this_player.current_weapon.name:
                inp = input("You can't sell your currently equipped weapon! Please enter another option: ")
            item_to_remove = globals.this_player.inventory[inp]
            item_value = inventory_dict[globals.this_player.inventory[inp]]
            print("%s sold for $%d" % (item_to_remove, item_value))
            globals.this_player.money += item_value
            items_to_remove.append(item_to_remove)
            tabular_data[inp][0] = "SOLD!"
            tabular_data[inp][1] = "SOLD!"
            print(tabulate(tabular_data, headers=['No.' 'Item Name' 'Value ($)']))
            inp = input(
                "Please enter the number of another item you would like to sell, else enter the letter 'q' to leave: ")

    for item in items_to_remove:
        globals.this_player.inventory.remove(item)

        # TODO: return to home screen
