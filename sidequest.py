__author__ = 'vishnunair'

import globals
from globals import clear_screen
import tabulate
import dungeon
from random import randrange, choice

def setup_quest_board():
    global numbers
    global curr_types
    global descriptions
    global names
    global home_cities

    numbers = range(0,3)
    curr_types = []
    descriptions = []
    names = []
    home_cities = []

    for num in numbers:
        curr = choice(sidequest.types)
        curr_types.append(curr)
        descriptions.append(sidequest.quest_dict[curr])
        names.append(choice(globals.people_names))
        home_cities.append(choice(globals.province_names))

    global quest_tabulate
    quest_tabulate = []

    for num in numbers:
        tmp = []
        tmp.append(num)
        tmp.append(curr_types[num])
        tmp.append(descriptions[num])
        tmp.append(names[num])
        tmp.append(home_cities[num])
        quest_tabulate.append(tmp)


def quest_board():
    tabulate.tabulate(quest_tabulate, headers=["No." "Type" "Description" "Job Giver" "Home City"])
    accepted_answers = ['0','1','2','q']
    inp = input("\nWhat job would you like to take? To go back, enter the letter 'q': ")
    while inp not in accepted_answers:
        inp = input("You have entered an invalid option. Please try again: ")

    if input is 'q':
        return

    inp = int(inp)
    curr = sidequest(curr_types[inp], choice(globals.cave_names), names[inp], home_cities[inp])
    curr.execute_quest()
    purge_quest_board()


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

    def __init__(self, type, dungeon_name, giver, origin_city):
        self.type = type
        self.dungeon_name = dungeon_name
        self.quest_giver = giver
        self.giver_city = origin_city
        self.dungeon_length = randrange(4, 8)
        self.enemy_type = self.determine_enemy()

    def determine_enemy(self):
        return choice(globals.side_enemy_types)

    def execute_quest(self):
        clear_screen()
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
        print("%s from %d needs you to deliver a package to someone.\n"
              "Do this simple quest, and you'll get a modest reward.\n"
              "Sounds simple enough, right?\n" % (self.quest_giver, self.giver_city))
        print("However, you have to remember that the roads between the provinces are dangerous,\n"
              "and that you'll encounter loads of enemies...\n")
        input("Press enter to continue...")

        curr = dungeon.Dungeon("A Random Road", self.dungeon_length, "looter")
        curr.traverse_dungeon()

        reward = randrange(15,26)
        globals.this_player.money += reward
        print("%s is extremely thankful for delivering the message.\n"
              "You have been given %d for your efforts.\n" % (self.quest_giver, str(reward)))

        input("Press enter to return home...")

    def execute_kidnap(self):
        pass

    def execute_scare(self):
        pass

    def execute_gang(self):
        pass

    def execute_recovery(self):
        pass