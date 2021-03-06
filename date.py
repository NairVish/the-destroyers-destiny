"""
Handles the date mechanic.
"""

__author__ = "Vishnu Nair"

from random import randrange

import globals

# Assign initial None type to some variables used globally
months = None
days_of_the_week = None
days_in_each_month = None
day_in_strings = None


def init_dates():
    """
    Initializes to memory all possible choices for all components of the date.
    """
    global months
    months = ["First Depth",
              "Sun's Darkness",
              "Bloom's Beginning",
              "Blossom's Growth",
              "Morning's Rise",
              "Sun's Rise",
              "Midyear",
              "Sun's Crest",
              "Leaves' Fall",
              "Bloom's End",
              "Sun's Fall",
              "Last Depth"]

    global days_of_the_week
    days_of_the_week = ["Sundap",
                        "Mondap",
                        "Tundap",
                        "Wednap",
                        "Turdap",
                        "Fredap",
                        "Saturp"]

    global days_in_each_month
    days_in_each_month = {
        months[0]: 31,
        months[1]: 28,
        months[2]: 31,
        months[3]: 30,
        months[4]: 31,
        months[5]: 30,
        months[6]: 31,
        months[7]: 31,
        months[8]: 30,
        months[9]: 31,
        months[10]: 30,
        months[11]: 31
    }

    global day_in_strings
    day_in_strings = {
        1: '1st',
        2: '2nd',
        3: '3rd',
        4: '4th',
        5: '5th',
        6: '6th',
        7: '7th',
        8: '8th',
        9: '9th',
        10: '10th',
        11: '11th',
        12: '12th',
        13: '13th',
        14: '14th',
        15: '15th',
        16: '16th',
        17: '17th',
        18: '18th',
        19: '19th',
        20: '20th',
        21: '21st',
        22: '22nd',
        23: '23rd',
        24: '24th',
        25: '25th',
        26: '26th',
        27: '27th',
        28: '28th',
        29: '29th',
        30: '30th',
        31: '31st'
    }


def string_date(date_list):
    """
    Converts a date list into a string.
    :param date_list: The input date list.
    """
    day_of_week = date_list[0]
    day = date_list[1]
    month = date_list[2]
    year = date_list[3]

    string_day = day_in_strings[day]

    whole_date_string = "%s, %s of %s, %s" % (day_of_week, string_day, month, year)
    return whole_date_string


def advance_date(standalone=True):
    """
    Advances the date.
    :param standalone: Boolean that indicates whether or not we're advancing independent of globals.this_player.day,
    which is used for main quest stage tracking.
    """
    globals.this_player.date[1] += 1
    globals.this_player.date_num_days += 1

    new_day_index = days_of_the_week.index(globals.this_player.date[0]) + 1
    if new_day_index > 6:
        new_day_index = 0

    globals.this_player.date[0] = days_of_the_week[new_day_index]

    if globals.this_player.date[2] == months[11] and globals.this_player.date[1] > days_in_each_month[
        globals.this_player.date[2]]:
        globals.this_player.date[2] = months[0]
        globals.this_player.date[1] = 1
        globals.this_player.date[3] += 1
    elif globals.this_player.date[1] > days_in_each_month[globals.this_player.date[2]]:
        new_month_index = months.index(globals.this_player.date[2]) + 1
        globals.this_player.date[2] = months[new_month_index]
        globals.this_player.date[1] = 1

    if standalone is True and globals.this_player.assistant is True:
        globals.clear_screen()
        money = randrange(1, 4)
        print("Assistant Alert: Merlona made $%s today.\n" % money)
        globals.this_player.money += money
        input("(Press enter to continue...)")
        globals.clear_screen()


if __name__ == "__main__":
    print("To play this game, run 'launch.py'.\n"
          "For more information about this file, see 'readme.txt'.")
