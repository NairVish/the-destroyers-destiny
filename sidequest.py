__author__ = 'vishnunair'

import globals
import tabulate
import dungeon
from random import randrange, choice
from time import sleep

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
        curr = choice(Sidequest.types)
        curr_types.append(curr)
        descriptions.append(Sidequest.quest_dict[curr])
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
    print("QUEST BOARD")
    print("Welcome to the quest board!\n")
    print(tabulate.tabulate(quest_tabulate, headers=["No.", "Type", "Description", "Job Giver", "Home City"]))
    accepted_answers = ['0','1','2','q']
    inp = input("\nWhat job would you like to take? To go back, enter the letter 'q': ")
    while inp not in accepted_answers:
        inp = input("You have entered an invalid option. Please try again: ")

    if inp is 'q':
        return

    inp = int(inp)
    curr = Sidequest(curr_types[inp], choice(globals.cave_names), names[inp], home_cities[inp])
    curr.execute_quest()


class Sidequest():
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
        globals.clear_screen()
        sleep(0.1)
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
        print("%s from %s needs you to deliver a package to someone.\n"
              "Do this simple quest, and you'll get a modest reward.\n"
              "Sounds simple enough, right?\n" % (self.quest_giver, self.giver_city))
        print("However, you have to remember that the roads between the\n"
              "provinces are dangerous, and that you'll encounter loads of enemies...\n")
        input("Press enter to continue...")

        curr = dungeon.Dungeon("A Random Road", self.dungeon_length, "looter")
        curr.traverse_dungeon()

        reward = randrange(15,26)
        globals.this_player.money += reward
        print("%s is extremely thankful for delivering the message.\n"
              "You have been given $%s for your efforts.\n" % (self.quest_giver, str(reward)))

        input("Press enter to return home...")

    def execute_kidnap(self):
        print("%s, a citizen of %s, has been kidnapped by bandits!\n\n"
              "It is up to you to break into the bandits' hideout and save %s!\n" % (self.quest_giver, self.giver_city, self.quest_giver))
        input("Press enter to continue...")

        curr = dungeon.Dungeon(self.dungeon_name, self.dungeon_length, "bandit")
        curr.traverse_dungeon()

        reward = randrange(15,26)
        globals.this_player.money += reward
        print("%s's family is extremely thankful to you for saving %s.\n"
              "You have been given $%s for your efforts.\n" % (self.quest_giver, self.quest_giver, str(reward)))

        input("Press enter to return home...")


    def execute_scare(self):
        print("%s hired a group of bandits to sabotage his competitors in the business.\n"
              "However, the bandits have stepped out of line and have stopped listening to %s.\n"
              "It is up to you to intimidate the bandit leader into always following %s's orders.\n"
              % (self.quest_giver, self.quest_giver, self.quest_giver))
        input("Press enter to continue...")

        curr = dungeon.Dungeon(self.dungeon_name, self.dungeon_length, "bandit")
        curr.traverse_dungeon()

        reward = randrange(15,26)
        globals.this_player.money += reward
        print("The bandits will cause no more trouble for %s after your rampage.\n"
              "You have been given $%s for your efforts.\n" % (self.quest_giver, str(reward)))

        input("Press enter to return home...")

    def execute_gang(self):
        print("The imperial police have asked for your help in assualting a gang's hideout.\n\n"
              "The gang is notorious for unimaginable crimes, and it is up to you to stop\n"
              "their evil ways.\n")
        input("Press enter to continue...")

        curr = dungeon.Dungeon(self.dungeon_name, self.dungeon_length, "mobster")
        curr.traverse_dungeon()

        reward = randrange(15,26)
        globals.this_player.money += reward
        print("The gang won't terrorize any one else now that you've destroyed them.\n"
              "You have been given $%s for your efforts.\n" % (str(reward)))

        input("Press enter to return home...")

    def execute_recovery(self):
        print("%s, from %s, has asked you to recover a precious heirloom that some bandits stole.\n\n"
              "Your job is simple. You break into the bandits' hideout, destroy the bandits,\n"
              "and retrieve the stolen item.\n" % (self.quest_giver, self.giver_city))
        input("Press enter to continue...")

        curr = dungeon.Dungeon(self.dungeon_name, self.dungeon_length, "bandit")
        curr.traverse_dungeon()

        reward = randrange(20,30)
        globals.this_player.money += reward
        print("%s will be forever thankful to you for retrieving their family's heirloom.\n"
              "You have been given $%s for your efforts.\n" % (self.quest_giver, str(reward)))

        input("Press enter to return home...")

# globals.init_globals()
# setup_quest_board()
# quest_board()


# globals.init_globals()
# curr = sidequest("scare", "The Ratway", "Vishnu", "Whiterun")
# curr.execute_quest()