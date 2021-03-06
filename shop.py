"""
Handles the mechanic for the shops.
There are three shops in the game:
    * 'The Crazy Weapons Specialist' (weapons)
    * 'The Oddly Unique Alchemist' (potions)
    * 'The Really Rich Guy that Buys Everything' (selling anything in inventory)
"""

__author__ = 'Vishnu Nair'

import globals
from colorama import Fore, init
from tabulate import tabulate

init(autoreset=True)


def weapon_shop():
    """
    Handles all actions associated with the weapon shop: 'The Crazy Weapons Specialist.'
    Prints out all weapons available and handles actual insertion into inventory as well as deduction of money.
    """
    print("The Crazy Weapons Specialist\n".upper())
    print("Your current money: $%.2f\n" % globals.this_player.money)
    print("Welcome to The Crazy Weapons Specialist. What would you like to buy?\n")
    print(tabulate(globals.tabular_weapons, headers=["No.", "Weapon Name", "Weapon Power", "Cost ($)"],
                   tablefmt="rst"))

    inp = input("\nPlease enter the number of the item you would like to buy. Enter the letter 'q' to leave: ")
    while inp is not 'q':
        try:
            inp = int(inp)
        except ValueError:
            print(Fore.RED + "You have entered an invalid option.")
            inp = input("Please enter a valid option: ")
        else:
            if inp >= len(globals.weapon_names):
                print(Fore.RED + "You have entered an invalid option.")
                inp = input("Please enter a valid option: ")
                continue
            cost = int(globals.weapon_cost[inp])
            if cost > globals.this_player.money:
                print(Fore.RED + "You don't have enough money.")
                inp = input("Try buying something else, else enter the letter 'q' to leave: ")
                continue
            if globals.weapon_names[inp] in globals.this_player.inventory:
                print(Fore.RED + "You already have this weapon in your inventory.")
                inp = input("Please choose another option: ")
                continue
            globals.this_player.inventory.append(globals.weapon_names[inp])
            globals.this_player.money -= cost
            globals.clear_screen()
            print(Fore.GREEN + "<Alert: %s has been added to your inventory. You have $%.2f left.>\n" % (
                globals.weapon_names[inp], globals.this_player.money))
            print(tabulate(globals.tabular_weapons, headers=["No.", "Weapon Name", "Weapon Power", "Cost ($)"],
                           tablefmt="rst") + '\n')
            inp = input(
                "Please enter the number of another item you would like to buy, else enter the letter 'q' to leave: ")


def potion_shop():
    """
    Handles all actions associated with the potion shop: 'The Oddly Unique Alchemist.'
    Prints out all potions available and handles actual insertion into inventory as well as deduction of money.
    """
    print("The Oddly Unique Alchemist\n".upper())
    print("Your current money: $%.2f\n" % globals.this_player.money)
    print("Welcome to The Oddly Unique Alchemist. What would you like to buy?\n")

    print(tabulate(globals.tabular_potions, headers=["No.", "Name", "Strength (Points)", "Type", "Cost ($)"],
                   tablefmt="rst"))

    inp = input("\nPlease enter the number of the item you would like to buy. Enter the letter 'q' to leave: ")
    while inp is not 'q':
        try:
            inp = int(inp)
        except ValueError:
            print(Fore.RED + "You have entered an invalid option.")
            inp = input("Please enter a valid option: ")
        else:
            if inp >= len(globals.potion_names):
                print(Fore.RED + "You have entered an invalid option.")
                inp = input("Please enter a valid option: ")
                continue
            cost = int(globals.potion_cost[inp])
            if cost > globals.this_player.money:
                print(Fore.RED + "You don't have enough money.")
                inp = input("Try buying something else, else enter the letter 'q' to leave: ")
                continue
            globals.this_player.inventory.append(globals.potion_names[inp])
            globals.this_player.money -= cost
            globals.clear_screen()
            print(Fore.GREEN + "<Alert: %s has been added to your inventory. You have $%.2f left.>\n" % (
                globals.potion_names[inp], globals.this_player.money))
            print(tabulate(globals.tabular_potions, headers=["No.", "Name", "Strength (Points)", "Type", "Cost ($)"],
                           tablefmt="rst") + '\n')
            inp = input(
                "Please enter the number of another item you would like to buy, else enter the letter 'q' to leave: ")


def selling():
    """
    Handles all actions associated with selling to 'The Really Rich Guy that Buys Everything.'
    Prints out entire inventory as well as associated prices.
    Also, handles removal from inventory and adding of money.
    This function also prevents the currently equipped weapon from being sold.
    """
    print("The Really Rich Guy that Buys Everything\n".upper())
    print("Your current money: $%.2f\n" % globals.this_player.money)

    if not globals.this_player.inventory:
        print("The Rich Guy: You have nothing to sell me. Why on Nira are you here?\n")
        print(Fore.RED + "<Alert: You have nothing in your inventory. Come back when you have something to sell.>\n")
        input("(Press enter to return to the Market...)")
        return

    print("The Rich Guy: I'm an insanely rich guy that likes to buy stuff. What would you like to sell to me?\n")
    tabular_data = []
    inventory_dict = {}
    items_to_remove = []
    num = 0
    for item in globals.this_player.inventory:
        tmp = [num, item]
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
        num += 1

    print(tabulate(tabular_data, headers=["No.", "Item Name", "Value ($)"]) + '\n')

    inp = input("Please enter the number of the item you would like to sell. Enter the letter 'q' to leave: ")
    while inp is not 'q':
        try:
            inp = int(inp)
        except ValueError:
            print(Fore.RED + "You have entered an invalid option.")
            inp = input("Please enter a valid option: ")
        else:
            if inp >= len(globals.this_player.inventory):
                print(Fore.RED + "You have entered an invalid option.")
                inp = input("Please enter a valid option: ")
                continue
            if tabular_data[inp][0] is "SOLD!":
                print(Fore.RED + "You have entered an invalid option.")
                inp = input("Please enter a valid option: ")
                continue
            if globals.this_player.current_weapon is not None:
                if tabular_data[inp][1] == globals.this_player.current_weapon.name:
                    print(Fore.RED + "You can't sell your currently equipped weapon!")
                    inp = input("Please enter another option: ")
                    continue
            globals.clear_screen()
            item_to_remove = globals.this_player.inventory[inp]
            item_value = inventory_dict[globals.this_player.inventory[inp]]
            globals.clear_screen()
            print("%s sold for $%s!" % (item_to_remove, item_value))
            globals.this_player.money += float(item_value)
            print("You now have $%.2f.\n" % globals.this_player.money)
            items_to_remove.append(item_to_remove)
            tabular_data[inp][0] = "SOLD!"
            tabular_data[inp][1] = "SOLD!"
            tabular_data[inp][2] = "SOLD!"
            print(tabulate(tabular_data, headers=['No.', 'Item Name', 'Value ($)']) + '\n')
            inp = input(
                "Please enter the number of another item you would like to sell, else enter the letter 'q' to leave: ")

    for item in items_to_remove:
        globals.this_player.inventory.remove(item)


if __name__ == "__main__":
    print("To play this game, run 'launch.py'.\n"
          "For more information about this file, see 'readme.txt'.")
