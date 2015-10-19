__author__ = 'vishnunair'

import globals
import tabulate
import dungeon
from random import randrange, choice

def setup_quest_board():
    global numbers
    global descriptions
    global names

    numbers = range(0,3)
    descriptions = []
    names = []
    home_cities = []

    for num in numbers:
        curr = choice(sidequest.types)
        descriptions.append(sidequest.quest_dict[curr])
        names.append(choice(globals.people_names))
        home_cities.append(choice(globals.province_names))

    global quest_tabulate
    quest_tabulate = []

    for num in numbers:
        tmp = []
        tmp.append(num)
        tmp.append(descriptions[num])
        tmp.append(names[num])
        tmp.append(home_cities[num])
        quest_tabulate.append(tmp)


def quest_board():
    tabulate.tabulate(quest_tabulate, headers=["No." "Description" "Job Giver" "Home City"])
    # TODO: receive input


def purge_quest_board():
    global numbers
    global descriptions
    global names
    global quest_tabulate

    del numbers
    del descriptions
    del names
    del quest_tabulate


class sidequest():
    types = ['delivery', 'kidnap', 'scare', 'gang', 'recovery']
    quest_dict = {'delivery': "Deliver a message for someone.",
                  'kidnap': "Search and rescue mission.",
                  'scare': "An intimidation job.",
                  'gang': "Assault a gang's hideout.",
                  'recovery': "Recover a lost/stolen item."}

    def __init__(self, type, dungeon_name):
        self.type = type
        self.dungeon_name = dungeon_name
        self.dungeon_length = randrange(4, 8)
        self.enemy_type = self.determine_enemy()

    def determine_enemy(self):
        return choice(globals.side_enemy_types)

    def execute_quest(self):
        if self.type is 'delivery':
            self.execute_delivery()
        elif self.type is 'kidnap':
            self.execute_kidnap()
        elif self.type is 'scare':
            self.execute_scare()
        elif self.type is 'gang':
            self.execute_gang()
        elif self.type is 'recovery':
            self.execute_recovery()

    def execute_delivery(self):
        pass

    def execute_kidnap(self):
        pass

    def execute_scare(self):
        pass

    def execute_gang(self):
        pass

    def execute_recovery(self):
        pass