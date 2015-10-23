__author__ = 'vishnunair'

import globals
from tabulate import tabulate
from random import randrange


class Player():
    def __init__(self, init_name, init_province, init_level=1, init_xp=0, init_target_xp=10, init_health=20,
                 init_attack=2,init_defense=3.5, init_speed=3, init_main_quest_stage=0, init_money=10,
                 init_assistant=False, init_weapon=None, init_day=1, init_sidequest=False, init_inventory=[]):
        self.name = init_name
        self.home = init_province
        self.level = init_level
        self.xp = init_xp
        self.target_xp = init_target_xp
        self.current_health = init_health
        self.total_health = init_health
        self.attack = init_attack
        self.defense = init_defense
        self.speed = init_speed
        self.main_quest_stage = init_main_quest_stage
        self.money = init_money
        self.assistant = init_assistant
        self.current_weapon = Weapon(init_weapon)
        self.day = init_day
        self.sidequests = init_sidequest
        self.inventory = init_inventory

    def __repr__(self):
        return self.name

    def level_up(self):
        diff = self.target_xp - self.xp
        self.xp = diff
        self.target_xp += 5

        self.attack += 1
        self.defense += 1
        self.speed += 1
        self.total_health += 5
        self.current_health = self.total_health

        self.level += 1
        print("\nLEVEL UP!")
        print("You are now at level %s.\n" % self.level)

        input("Press enter to continue...")

    def print_stats(self):
        globals.clear_screen()
        print("STATISTICS FOR PLAYER %s" % self.name)
        print("Level: %s" % self.level)
        print("Current XP: %s" % self.xp)
        print("XP Needed for Level Up: " % self.target_xp)
        print("Current Health: %s" % self.current_health)
        print("Total Health: " % self.total_health)
        print("Total Attack: " % self.attack)
        print("Total Defense: " % self.defense)
        print("Total Speed: " % self.speed)
        print("Current Money: " % self.money)
        print("Current Weapon: " % self.current_weapon)
        print("Current inventory: ")
        for item in self.inventory:
            print('\t' + item)
        input("\nPress any key to return to previous screen...")
        globals.clear_screen()

    def toggle_assistant_flag(self):
        self.assistant = not self.assistant

    def use_potion(self, enhancement=False):
        tabular_potion_inv = []
        number_of_potions = 0
        potion_dict = {}
        for item in self.inventory:
            tmp = []
            if item not in globals.potion_names:
                continue
            if enhancement is True:
                if globals.potion_type[globals.potion_names.index(item)] is "health":
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
        print(tabulate(tabular_potion_inv, headers=["No.", "Potion Name", "Type", "Strength (Points)"]))

        items_to_remove = []
        inp = input("Please enter the number of the potion you would like to use. Enter the letter 'q' to leave: ")
        while inp is not 'q':
            try:
                inp = int(inp)
            except ValueError:
                inp = input("You did not enter a number. Please enter a valid option: ")
            else:
                if tabular_potion_inv[inp][0] is "USED!" or inp >= len(globals.this_player.inventory):
                    inp = input("You have entered an invalid option. Please enter a valid option: ")
                    continue
                item_to_remove = self.inventory.index(tabular_potion_inv[inp][1])
                boost = tabular_potion_inv[inp][3]
                type = tabular_potion_inv[inp][2]
                if type is "health":
                    self.current_health += boost
                    if self.current_health > self.total_health:
                        self.current_health = self.total_health
                        print("Current health increased by %s points!" % boost)
                elif type is "attack":
                    self.attack += boost
                    print("Attack increased by %s points!" % boost)
                elif type is "defense":
                    self.defense += boost
                    print("Defense increased by %s points!" % boost)
                elif type is "speed":
                    self.speed += boost
                    print("Speed increased by %s points!" % boost)
                items_to_remove.append(item_to_remove)
                for index in range(0, 4):
                    tabular_potion_inv[inp][index] = "USED!"
                print(tabulate(tabular_potion_inv, headers=["No.", "Potion Name", "Type", "Strength (Points)"]))
                inp = input(
                    "Please enter the number of another potion you would like to use, else enter the letter 'q' to leave: ")

        for item in items_to_remove:
            globals.this_player.inventory.remove(item)

        globals.clear_screen()


    def equip_weapon(self):
        tabular_weapon_inv = []
        number_of_weapons = 0
        for item in self.inventory:
            tmp = []
            if item in globals.weapon_names:
                tmp.append(number_of_weapons)
                tmp.append(item)
                tmp.append(globals.weapon_powers[globals.weapon_names.index(weapon_name)])
                number_of_weapons += 1
            if tmp is False:
                continue
            else:
                tabular_weapon_inv.append(tmp)

        if tabular_weapon_inv is False:
            print("You have no weapons to equip.")
            input("Press enter to continue...")
            return
        print("WEAPON CHOOSER\n")
        print(tabulate(tabular_weapon_inv, headers=["No.", "Name", "Power"], tablefmt="fancy_grid"))

        inp = input("\nEnter the number of the weapon you wish to equip: ")

        input_legal = False
        while input_legal is False:
            try:
                inp = int(inp)
            except ValueError:
                inp = input("That is an invalid option. Please try again: ")
            else:
                if input >= len(globals.weapon_names):
                    inp = input("That is an invalid option. Please try again: ")
                    continue
                input_legal = True

        print("The %s has been equipped." % globals.weapon_names[inp])
        self.current_weapon = Weapon(globals.weapon_names[inp])

        input("Press enter to return home...")
        globals.clear_screen()


    def see_inventory(self):
        print("YOUR INVENTORY\n")

        if self.inventory is False:
            print("You have nothing in your inventory\n")
        else:
            for item in self.inventory:
                print(item)
            print('\n')

        input("Press enter to return home...")

    def sleep(self):
        self.day += 1

        if globals.this_player.assistant is True:
            money = randrange(5,15)
            print("Assistant Alert: Merlona made $%s today." % money)
            globals.this_player.money += money
            input("Press enter to continue...")


        # TODO: if main quest stage is less than some amount
        # then we're going to have a function monitor our player's status,
        # using progression of dialogue and maybe even day.


class Weapon():
    def __init__(self, weapon_name):
        self.name = weapon_name
        self.power = globals.weapon_powers[globals.weapon_names.index(weapon_name)]

    def __repr__(self):
        return self.name
