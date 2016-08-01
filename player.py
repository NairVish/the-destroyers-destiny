"""
Contains definitions for the Player and Weapon classes.
Handles all functions that deal with the player itself.
"""

__author__ = 'Vishnu Nair'

from random import choice, randrange

import date
import globals
from colorama import Fore, init
from tabulate import tabulate

init(autoreset=True)


class Player:
    """
    The Player class hold all attributes and handles all modification and constant activities for the player.
    """

    def __init__(self, init_name, init_province, init_level=1, init_xp=0, init_target_xp=10, init_health=20,
                 init_attack=2.0, init_defense=3.5, init_main_quest_stage=0, init_money=0, init_assistant=False,
                 init_weapon=None, init_day=1, init_sidequest=False, init_inventory=[], init_date=[],
                 start_date=[], init_date_num_days=0):
        """
        NOTE: Defaults are in parentheses.
        :param init_name: The name of the player.
        :param init_province: The player's home province.
        :param init_level: The player's starting level for the session (1 for a new player).
        :param init_xp: The player's current XP progress toward the next level (0 for a new player).
        :param init_target_xp: The target XP for the player to advance to the next level (10 for a new player).
        :param init_health: The player's maximum health level (20 for a new player).
        :param init_attack: The player's attack stat (2.0 for a new player).
        :param init_defense: The player's defense stat(3.5 for a new player).
        :param init_main_quest_stage: The player's starting main quest stage for the session (0 for a new player).
        :param init_money: The player's available money (0 for a new player).
        :param init_assistant: Whether or not the player has an assistant right now (False for a new player).
        :param init_weapon: The player's current weapon represented by a Weapon object (None type for a new player).
        :param init_day: The player's current day [used solely for main quest stage tracking] (1 for a new player).
        :param init_sidequest: Whether or not the player can access sidequests (False for a new player).
        :param init_inventory: A list that represents the player's current inventory (Empty list for a new player).
        :param init_date: The current date (Randomly picked day of the week, month, and day with year 2215 for new player).
        :param start_date: The player's start date (Whatever the init_date is for a new player).
        :param init_date_num_days: The number of days since the start date (0 for a new player).
        Initializes the attributes of the player.
        """
        self.name = init_name
        self.home = init_province
        self.level = init_level
        self.xp = init_xp
        self.target_xp = init_target_xp
        self.current_health = init_health
        self.total_health = init_health
        self.attack = init_attack
        self.defense = init_defense
        self.main_quest_stage = init_main_quest_stage
        self.money = init_money
        self.assistant = init_assistant
        if init_weapon is None or init_weapon == 'None':
            self.current_weapon = None
        else:
            self.current_weapon = Weapon(init_weapon)
        self.day = init_day
        self.sidequests = init_sidequest
        self.inventory = init_inventory
        if len(init_date) == 0:
            init_day_of_week = choice(date.days_of_the_week)
            init_month = choice(date.months)
            this_init_day = randrange(1, date.days_in_each_month[init_month] + 1)
            init_year = 2215
            self.date = [init_day_of_week, this_init_day, init_month, init_year]
            self.start_date = self.date[:]
        else:
            self.date = init_date
            self.start_date = start_date
        self.date_num_days = init_date_num_days

    def __repr__(self):
        """
        If the Player object itself is printed out, the player's name is printed out.
        """
        return self.name

    def level_up(self):
        """
        Handles the mechanic to level up the player.
        If the current XP is above the target XP, the difference is added toward the next level.
        At level up:
            * Target XP is increased by 5.
            * Attack is increased by 1.
            * Defense is increased by 1.
            * Total health is increased by 5.
            * Level is increased by 1.
        """
        if self.xp > self.target_xp:
            self.xp -= self.target_xp
        else:
            self.xp = 0
        self.target_xp += 5

        self.attack += 1
        self.defense += 1
        self.total_health += 5
        self.current_health = self.total_health

        self.level += 1
        print("LEVEL UP!")
        print("You are now at level %s.\n" % self.level)

    def print_stats(self):
        """
        Prints out the player's stats.
        """
        globals.clear_screen()
        print("STATISTICS FOR %s" % self.name)
        print("Level: %s" % self.level)
        print("Current XP: %.1f" % self.xp)
        print("XP Needed for Level Up: %s" % self.target_xp)
        print("Current Health: %s" % self.current_health)
        print("Total Health: %s" % self.total_health)
        print("Total Attack: %s" % self.attack)
        print("Total Defense: %s" % self.defense)
        print("Current Money: $%.2f" % self.money)
        print("Current Weapon: %s" % self.current_weapon)
        print("Adventure started on: %s" % date.string_date(self.start_date))
        print("Days since adventure start: %s" % self.date_num_days)
        print("Current Inventory: ")
        for item in self.inventory:
            print('\t' + item)
        if len(self.inventory) == 0:
            print('\tNone')
        input("\n(Press enter to return...)")
        globals.clear_screen()

    def toggle_assistant_flag(self):
        """
        Toggles the assistant flag.
        """
        self.assistant = not self.assistant

    def toggle_sidequest_flag(self):
        """
        Toggles the sidequest flag.
        """
        self.sidequests = not self.sidequests

    def use_potion(self, enhancement=False):
        """
        :param enhancement:
            * True if we are in a situation where taking a health potion would be unnecessary (i.e. when we are not in battle).
            * False if we are in a situation where taking a health potion would be beneficial (i.e. when in battle).
        Prints out a table of all potions available to use.
        Also processes input from these tables and handles potion effects.
        """
        tabular_potion_inv = []
        number_of_potions = 0
        potion_dict = {}
        for item in self.inventory:
            tmp = []
            if item not in globals.potion_names:
                continue
            if enhancement is True:
                if globals.potion_type[globals.potion_names.index(item)] == "health":
                    continue
            potion_power = globals.potion_powers[globals.potion_names.index(item)]
            potion_type = globals.potion_type[globals.potion_names.index(item)]
            tmp.append(number_of_potions)
            tmp.append(item)
            tmp.append(potion_type)
            tmp.append(potion_power)
            tabular_potion_inv.append(tmp)
            potion_dict[item] = potion_power
            number_of_potions += 1

        print("USE A POTION\n")

        if number_of_potions is 0:
            print("You have no potions in your inventory that you can use right now.\n")
            input("(Press enter to return...)")
            globals.clear_screen()
            return
        print(tabulate(tabular_potion_inv, headers=["No.", "Potion Name", "Type", "Strength (Points)"]) + '\n')

        items_to_remove = []
        inp = input("Please enter the number of the potion you would like to use. Enter the letter 'q' to leave: ")
        while inp is not 'q':
            try:
                inp = int(inp)
            except ValueError:
                inp = input("You did not enter a number. Please enter a valid option: ")
            else:
                if tabular_potion_inv[inp][0] is "USED!" or inp >= len(globals.this_player.inventory):
                    print(Fore.RED + "You have entered an invalid option.")
                    inp = input("Please try again: ")
                    continue
                globals.clear_screen()
                item_to_remove = self.inventory.index(tabular_potion_inv[inp][1])
                type = tabular_potion_inv[inp][2]
                boost = tabular_potion_inv[inp][3]
                if type == "health":
                    self.current_health += boost
                    if self.current_health > self.total_health:
                        self.current_health = self.total_health
                        print(Fore.GREEN + "Current health increased by %s points!\n" % boost)
                elif type == "attack":
                    self.attack += boost
                    print(Fore.GREEN + "Attack increased by %s points!\n" % boost)
                elif type == "defense":
                    self.defense += boost
                    print(Fore.GREEN + "Defense increased by %s points!\n" % boost)
                items_to_remove.append(item_to_remove)
                for index in range(0, 4):
                    tabular_potion_inv[inp][index] = "USED!"
                print(tabulate(tabular_potion_inv, headers=["No.", "Potion Name", "Type", "Strength (Points)"]) + '\n')
                inp = input(
                    "Please enter the number of another potion you would like to use, else enter the letter 'q' to leave: ")

        for item in items_to_remove:
            del globals.this_player.inventory[item]

        globals.clear_screen()

    def equip_weapon(self):
        """
        Prints out a table that shows all the available weapons that the player can equip.
        Also processes user input here and handles actual weapon change.
        """
        tabular_weapon_inv = []
        number_of_weapons = 0
        for item in self.inventory:
            tmp = []
            if item in globals.weapon_names:
                tmp.append(number_of_weapons)
                tmp.append(item)
                tmp.append(globals.weapon_powers[globals.weapon_names.index(item)])
                number_of_weapons += 1
                tabular_weapon_inv.append(tmp)

        print("WEAPON CHOOSER\n")
        if number_of_weapons is 0:
            print("You have no weapons to equip.\n")
            input("(Press enter to return...)")
            return
        print(tabulate(tabular_weapon_inv, headers=["No.", "Name", "Power"], tablefmt="fancy_grid"))

        inp = input("\nEnter the number of the weapon you wish to equip. Enter 'q' to go back: ")

        input_legal = False
        while input_legal is False:
            try:
                inp = int(inp)
            except ValueError:
                if inp is 'q':
                    break
                print(Fore.RED + "That is an invalid option.")
                inp = input("Please try again: ")
            else:
                if inp >= len(globals.weapon_names):
                    print(Fore.RED + "That is an invalid option.")
                    inp = input("Please try again: ")
                    continue
                input_legal = True

        if inp is not 'q':
            w_name = globals.weapon_names[globals.weapon_names.index(tabular_weapon_inv[inp][1])]
            print(Fore.GREEN + "\nThe %s has been equipped.\n" % w_name)
            self.current_weapon = Weapon(w_name)
            input("(Press enter to return...)")

        globals.clear_screen()

    def see_inventory(self):
        """
        Prints out player's inventory.
        """
        print("YOUR INVENTORY\n")

        if not self.inventory:
            print("You have nothing in your inventory.\n")
        else:
            for item in self.inventory:
                print('* ' + item)
            print('\n')

        input("(Press enter to return...)")

    def sleep(self):
        """
        Handles player sleep option.
        Also awards a random amount of money ($5-$15) as part of the assistant mechanic.
        """
        self.day += 1
        date.advance_date(standalone=False)
        globals.clear_screen()

        if globals.this_player.assistant is True:
            money = randrange(5, 15)
            print(Fore.GREEN + "Assistant Alert: Merlona made $%s today.\n" % money)
            globals.this_player.money += money
            input("(Press enter to continue...)")
            globals.clear_screen()


class Weapon:
    """
    The Weapon class handles the player's weapon.
    """

    def __init__(self, weapon_name):
        """
        :param weapon_name: The name of the weapon.
        Sets current weapon's attributes.
        Sets power by looking for weapon name in globals.weapon_names, grabbing corresponding index, and looking for index in globals.weapon_powers.
        """
        self.name = weapon_name
        self.power = globals.weapon_powers[globals.weapon_names.index(weapon_name)]

    def __repr__(self):
        """
        If Weapon object is printed out, weapon's name is printed out.
        """
        return self.name


if __name__ == "__main__":
    print("To play this game, run 'launch.py'.\n"
          "For more information about this file, see 'readme.txt'.")
