__author__ = 'vishnunair'

import globals
from tabulate import tabulate

class Player():

    def __init__(self, init_name, init_province, init_level=1, init_xp=0, init_target_xp=10, init_health=20, init_attack=2,
                 init_defense=3.5, init_speed=3, init_main_quest_stage=0, init_money=10, init_assistant=False,
                 init_weapon=None, init_day=0, init_sidequest=False, init_inventory=[]):
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

    def print_stats(self):
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
        input("\nPress any key to return to previous screen.")
        globals.clear_screen()

    def toggle_assistant_flag(self):
        self.assistant = not self.assistant

    def use_potion(self, potion):
        with globals.potion_names.index(potion) as pIndex:
            boost = globals.potion_powers[pIndex]
            type = globals.potion_type[pIndex]
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

    def equip_weapon(self, weapon):
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
        print(tabulate(tabular_weapon_inv, headers=["No." "Name" "Power"], tablefmt="fancy_grid"))

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

        # TODO: Return


class Weapon():

    def __init__(self, weapon_name):
        self.name = weapon_name
        self.power = globals.weapon_powers[globals.weapon_names.index(weapon_name)]

    def __repr__(self):
        return self.name