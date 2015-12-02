import globals
import shop
import center_square
from weather import string_weather
from date import string_date


def init_outdoors():
    import csv
    with open("outdoor_statements.csv") as f:
        this = csv.reader(f)
        global statements_conditions
        statements_conditions = {}
        for row in this:
            statements_conditions[row[0]] = row[1]


class Outdoors:
    def __init__(self, init_weather):
        self.weather = init_weather
        self.date = globals.this_player.date

    def header(self, loc):
        print("Current Location: %s\n"
              "Weather: %s\n"
              "Date: %s\n" % (loc, string_weather(self.weather), string_date(self.date)))

    def traverse(self):
        globals.clear_screen()
        self.opening_statement()
        self.initial()

    def opening_statement(self):
        cond = self.weather['condition']
        self.header("%s's Home" % globals.this_player.name)
        print(statements_conditions[cond] + '\n')
        input("(Press enter to continue...)")
        globals.clear_screen()

    def initial(self):
        def print_menu():
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
        def print_menu():
            print("Locations:\n"
                  "\t1. The Crazy Weapons Specialist\n"
                  "\t2. The Oddly Unique Alchemist\n"
                  "\t3. The Really Rich Guy that Buys Everything\n"
                  "\t4. Go back home.\n")
            return input("Where do you want to go? ")

        loc = "The Market"
        self.header(loc)
        print("Just as you reach the market, you hear vendors practically begging for your business. You "
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
        def print_menu():
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