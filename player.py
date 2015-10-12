__author__ = 'vishnunair'

import os
import globals

class Player():

    def __init__(self, init_name, init_level=1, init_xp=0, init_target_xp=10, init_health=20, init_attack=2,
                 init_defense=3.5, init_speed=3, init_main_quest_stage=0, init_money=10, init_assistant=False,
                 init_inventory=[]):
        self.name = init_name
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
        print("Current inventory: ")
        for item in self.inventory:
            print('\t' + item)
        input("\nPress any key to return to previous screen.")
        globals.clear_screen()

    def toggle_assistant_flag(self):
        self.assistant = not self.assistant

    def use_potion(self, potion):
        pass # for now