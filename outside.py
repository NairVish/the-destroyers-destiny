"""
Handles activities related to the outdoor/city mechanic.
"""

__author__ = "Vishnu Nair"

import globals
import shop
import center_square
from weather import string_weather
from date import string_date


def init_outdoors():
    """
    Initializes to memory the weather statements that are printed when the player first goes outside.
    """
    import csv
    with open("outdoor_statements.csv") as f:
        this = csv.reader(f)
        global statements_conditions
        statements_conditions = {}
        for row in this:
            statements_conditions[row[0]] = row[1]


class Outdoors:
    """
    The Outdoors class holds information about the weather outside in the city. It also holds member functions
    related to traversing available areas in the city.
    """
    def __init__(self, init_weather):
        """
        Initializes the outdoor class with the weather and current date.
        :param init_weather: The weather in the form a dictionary with the 'condition' and 'temp' keys.
        """
        self.weather = init_weather
        self.date = globals.this_player.date

    def header(self, loc):
        """
        The header that is displayed at the top of the screen as the player traverses the city.
        :param loc: The player's current location.
        """
        print("Current Location: %s\n"
              "Weather: %s\n"
              "Date: %s\n" % (loc, string_weather(self.weather), string_date(self.date)))

    def traverse(self):
        """
        The main city traversal member function.
        """
        globals.clear_screen()
        self.opening_statement()
        self.initial()

    def opening_statement(self):
        """
        Displays a statement describing the weather outside.
        """
        cond = self.weather['condition']
        self.header("%s's Home" % globals.this_player.name)
        print(statements_conditions[cond] + '\n')
        input("(Press enter to continue...)")
        globals.clear_screen()

    def initial(self):
        """
        Handles the first stage of the city traversal: Outside the player's home.
        """
        def print_menu():
            """
            Prints a list of available options and returns the player's input.
            """
            print("Locations:\n"
                  "\t1. The Market\n"
                  "\t2. Center Square\n"
                  "\t3. Home\n")
            return input("Where do you want to go? ")

        loc = "Outside %s's Home" % globals.this_player.name
        while True:
            self.header(loc)
            inp = print_menu()
            accepted_answers = ['1', '2', '3']
            while inp not in accepted_answers:
                inp = input("You have entered an invalid option. Please try again: ")

            globals.clear_screen()
            if inp is '1':
                self.market()
            elif inp is '2':
                self.center()
            elif inp is '3':
                return

    def market(self):
        """
        Handles the market stage of the city traversal.
        """
        def print_menu():
            """
            Prints a list of available options and returns the player's input.
            """
            print("Locations:\n"
                  "\t1. The Crazy Weapons Specialist\n"
                  "\t2. The Oddly Unique Alchemist\n"
                  "\t3. The Really Rich Guy that Buys Everything\n"
                  "\t4. Go back home.\n")
            return input("Where do you want to go? ")

        loc = "The Market"
        self.header(loc)
        print("You know you've reached the market because you hear vendors practically begging for your business. You "
              "eventually set your sights on three businesses...\n")
        while True:
            inp = print_menu()
            accepted_answers = ['1', '2', '3', '4']
            while inp not in accepted_answers:
                inp = input("You have entered an invalid option. Please try again: ")

            globals.clear_screen()
            if inp is '1':
                shop.weapon_shop()
            elif inp is '2':
                shop.potion_shop()
            elif inp is '3':
                shop.selling()
            elif inp is '4':
                return

            globals.clear_screen()
            self.header(loc)

    def center(self):
        """
        Handles the Center Square stage of the city traversal.
        """
        def print_menu():
            """
            Prints a list of available options and returns the player's input.
            """
            print("Locations:\n"
                  "\t1. The Battle Practice Area\n"
                  "\t2. The Battle Arena\n"
                  "\t3. The Casino\n"
                  "\t4. Go back home.\n")
            return input("Where do you want to go? ")

        loc = "Center Square"
        self.header(loc)
        print("After some walking, you eventually reach Center Square: The heart of %s. Three attractions here "
              "stand out to you.\n" % globals.this_player.home)
        while True:
            inp = print_menu()
            accepted_answers = ['1', '2', '3', '4']
            while inp not in accepted_answers:
                inp = input("You have entered an invalid option. Please try again: ")

            globals.clear_screen()
            if inp is '1':
                self.header("The Battle Practice Area")
                center_square.battle_practice()
            elif inp is '2':
                self.header("The Battle Arena")
                center_square.battle_arena()
            elif inp is '3':
                self.header("The Casino")
                center_square.roulette()
            elif inp is '4':
                return

            globals.clear_screen()
            self.header(loc)

if __name__ == "__main__":
    print("To play this game, run 'launch.py'.\n"
          "For more information about this file, see 'readme.txt'.")