__author__ = 'vishnunair'

import os

class Player():

    def __init__(self, init_name, init_level=1, init_xp=0, init_target_xp=10, init_health=10, init_attack=2,
                 init_defense=3.5, init_speed=3, init_main_quest_stage=0, init_money=10, init_inventory=[]):
        self.name = init_name
        self.level = init_level
        self.xp = init_xp
        self.target_xp = init_target_xp
        self.health = init_health
        self.attack = init_attack
        self.defense = init_defense
        self.speed = init_speed
        self.main_quest_stage = init_main_quest_stage
        self.money = init_money
        self.inventory = init_inventory


    def __repr__(self):
        return self.name

    def level_up(self):
        diff = self.target_xp - self.xp
        self.xp = diff
        self.targetxp += 5

        self.attack += 1
        self.defense += 1
        self.speed += 1
        self.health += 2.5

        self.level += 1

    def print_stats(self):
        print("STATISTICS FOR PLAYER %s" % self.name)
        print("Level: %s" % self.level)
        print("Current XP: %s" % self.xp)
        print("XP Needed for Level Up: " % self.target_xp)
        print("Total Health: " % self.health)
        print("Total Attack: " % self.attack)
        print("Total Defense: " % self.defense)
        print("Total Speed: " % self.speed)
        print("Current Money: " % self.money)
        print("Current inventory: ")
        for item in self.inventory:
            print('\t' + item)
        input("\nPress any key to return to previous screen.")
        os.system('cls' if os.name == 'nt' else 'clear')