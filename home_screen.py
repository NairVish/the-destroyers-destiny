"""
Handles all activities related to the home screen.
"""

__author__ = 'Vishnu Nair'

import globals
import sidequest
import date
import exit
import weather
import outside

from colorama import Fore, init

init(autoreset=True)


class Home:
    """
    The main home screen class.
    """

    def __init__(self):
        """
        Initializes the home screen by selecting the day's weather.
        """
        self.weather = weather.determine_weather(globals.this_player.date)
        self.weather_string = weather.string_weather(self.weather)

    def print_home_screen(self):
        """
        Prints home screen and accepts and returns player input.
        """
        print("HOME SCREEN\n")

        print("Day %s" % str(globals.this_player.date_num_days + 1))
        print("%s, Level %d" % (globals.this_player, globals.this_player.level))
        print("Home Province: %s" % globals.this_player.home)
        print("Date: %s" % date.string_date(globals.this_player.date))
        print("Current Weather: %s\n" % self.weather_string)

        print("\t1. Do nothing and sleep until tomorrow.")
        print("\t2. Go outside.")
        print("\t3. Check for side jobs.")
        print("\t4. See detailed statistics.")
        print("\t5. See your inventory.")
        print("\t6. Equip another weapon.")
        print("\t7. Use an enhancement potion.")
        print("\t8. Exit (and Save).\n")

        inp = input("What would you like to do? ")
        accepted_answers = ['1', '2', '3', '4', '5', '6', '7', '8']
        while inp not in accepted_answers:
            inp = input("You have entered an invalid option. Please try again: ")
        return inp

    def process_home(self):
        """
        Processes home screen input. Returns True if player decides to exit, False if player just decides to sleep
        until the next day.
        """
        sidequest.setup_quest_board()
        while True:
            inp = self.print_home_screen()
            globals.clear_screen()
            if inp is '1':
                return False
            elif inp is '2':
                out = outside.Outdoors(self.weather)
                out.traverse()
            elif inp is '3':
                date_advanced = False
                try:
                    if globals.this_player.sidequests is False:
                        print(Fore.RED + "You are an Unknown.\n"
                                         "Unknowns are not allowed to view or participate in quests on the quest board.\n"
                                         "You must return home.\n")
                        input("(Press enter to continue...)")
                        globals.clear_screen()
                        continue
                    date_advanced = sidequest.quest_board()
                    sidequest.setup_quest_board()
                except KeyboardInterrupt:
                    exit.force_exit_program()
                except:
                    globals.clear_screen()
                    print(Fore.RED + "<Alert: Your current health has reached zero!>\n")
                    print("As the world fades to black, a white light suddenly flashes before you.\n"
                          "In an instant, you find yourself back at your home. You look at the time.\n"
                          "It's right before you went into that fateful encounter.\n")
                    print("<Note: All loot collected and XP gained will carry over. However, you have\n"
                          "lost the reward for this sidequest.>\n")
                    input("(Press enter to continue...)")
                if date_advanced is True:
                    self.weather = weather.determine_weather(globals.this_player.date)
                    self.weather_string = weather.string_weather(self.weather)
            elif inp is '4':
                globals.this_player.print_stats()
            elif inp is '5':
                globals.this_player.see_inventory()
            elif inp is '6':
                globals.this_player.equip_weapon()
            elif inp is '7':
                globals.this_player.use_potion(enhancement=True)
            elif inp is '8':
                return True
            globals.clear_screen()

    def print_shop_selector(self):
        """
        Prints shop selection screen and returns user input.
        """
        print("SHOPS\n")

        print("\t1. The Oddly Unique Alchemist")
        print("\t2. The Crazy Weapons Specialist")
        print("\t3. The Really Rich Guy that Buys Everything")
        print("\t4. Return to Home Screen.\n")

        inp = input("Where would you like to go? ")
        accepted_answers = ['1', '2', '3', '4', '5']
        while inp not in accepted_answers:
            inp = input("You have entered an invalid option. Please try again: ")

        return inp


if __name__ == "__main__":
    print("To play this game, run 'launch.py'.\n"
          "For more information about this file, see 'readme.txt'.")
