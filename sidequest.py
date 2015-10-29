"""
Handles the sidequest mechanic of the game.
There are five types of sidequests in the game:
    * delivery: Delivering a message for someone.
    * kidnap: A search and rescue mission.
    * scare: Intimidating a group of bandits.
    * gang: Destroy a gang in their hideout.
    * recovery: Recover an item that was stolen by bandits.
"""

__author__ = 'Vishnu Nair'

import globals
import tabulate
import dungeon
from random import randrange, choice
from time import sleep

def setup_quest_board():
    """
    Sets up quest board by randomly selecting three types of quests (may be the same)
    and adding their descriptions, quest giver, and giver's city to nested lists
    that will eventually be passed to tabulate.
    """
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
    """
    Prints out the quest board itself and handles all input from the quest screen.
    Also, initiates and executes the sidequest.
    """
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
    curr = Sidequest(curr_types[inp], choice(globals.cave_names), names[inp],
                     globals.people_genders[globals.people_names.index(names[inp])], home_cities[inp])
    curr.execute_quest()


class Sidequest():
    """
    The Sidequest class handles all information about and executes the desired sidequest.
    """
    types = ['delivery', 'kidnap', 'scare', 'gang', 'recovery']
    quest_dict = {'delivery': "Deliver a message for someone.",
                  'kidnap': "Search and rescue mission.",
                  'scare': "An intimidation job.",
                  'gang': "Assault a gang's hideout.",
                  'recovery': "Recover a lost/stolen item."}

    def __init__(self, type, dungeon_name, giver, giver_gender, origin_city):
        """
        :param type: The type of sidequest.
        :param dungeon_name: The name of the dungeon associated with the sidequest.
        :param giver: The name of the quest giver.
        :param giver_gender: The gender of the quest giver.
        :param origin_city: The name of the quest giver's city.
        Initializes the sidequest.
        """
        self.type = type
        self.dungeon_name = dungeon_name
        self.quest_giver = giver
        self.giver_gender = giver_gender
        self.giver_city = origin_city
        self.dungeon_length = randrange(4, 8)
        self.determine_pronouns()

    def determine_pronouns(self):
        """
        Determines the pronouns that will be used in the sidequest intro and outro text.
        """
        if self.giver_gender is 'm':
            self.subject_pronoun = "He"
            self.object_pronoun = "him"
            self.possessive_pronoun = "his"
        else:
            self.subject_pronoun = "She"
            self.object_pronoun = "her"
            self.possessive_pronoun = "her"

    def execute_quest(self):
        """
        Initiates execution of the sidequest depending on the quest type.
        """
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
        """
        Executes the delivery sidequest.
        """
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
        """
        Executes the search and rescue sidequest.
        """
        print("%s, a citizen of %s, has been kidnapped by bandits!\n\n"
              "It is up to you to break into the bandits' hideout and save %s!\n" % (self.quest_giver, self.giver_city, self.object_pronoun))
        input("Press enter to continue...")

        curr = dungeon.Dungeon(self.dungeon_name, self.dungeon_length, "bandit")
        curr.traverse_dungeon()

        reward = randrange(15,26)
        globals.this_player.money += reward
        print("%s's family is extremely thankful to you for saving %s.\n"
              "You have been given $%s for your efforts.\n" % (self.quest_giver, self.object_pronoun, str(reward)))

        input("Press enter to return home...")


    def execute_scare(self):
        """
        Executes the intimidation sidequest.
        """
        print("%s hired a group of bandits to sabotage %s competitors in the business.\n"
              "However, the bandits have stepped out of line and have stopped listening to %s.\n"
              "It is up to you to intimidate the bandit leader into always following %s's orders.\n"
              % (self.quest_giver, self.object_pronoun, self.object_pronoun, self.quest_giver))
        input("Press enter to continue...")

        curr = dungeon.Dungeon(self.dungeon_name, self.dungeon_length, "bandit")
        curr.traverse_dungeon()

        reward = randrange(15,26)
        globals.this_player.money += reward
        print("The bandits will cause no more trouble for %s after your rampage.\n"
              "You have been given $%s for your efforts.\n" % (self.quest_giver, str(reward)))

        input("Press enter to return home...")

    def execute_gang(self):
        """
        Executes the gang assault sidequest.
        """
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
        """
        Executes the item recovery sidequest.
        """
        print("%s, from %s, has asked you to recover a precious heirloom that some bandits stole.\n\n"
              "Your job is simple. You break into the bandits' hideout, destroy the bandits,\n"
              "and retrieve the stolen item.\n" % (self.quest_giver, self.giver_city))
        input("Press enter to continue...")

        curr = dungeon.Dungeon(self.dungeon_name, self.dungeon_length, "bandit")
        curr.traverse_dungeon()

        reward = randrange(20,30)
        globals.this_player.money += reward
        print("%s will be forever thankful to you for retrieving %s family's heirloom.\n"
              "You have been given $%s for your efforts.\n" % (self.quest_giver, self.possessive_pronoun, str(reward)))

        input("Press enter to return home...")

if __name__ == "__main__":
    print("To play this game, run 'start_here.py.'.\n"
          "For more information about this file, see 'readme.txt'.")