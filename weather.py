"""
Handles the weather mechanic.
"""

__author__ = "Vishnu Nair"

import date
from random import choice


def init_weather():
    """
    Initializes to memory all possible choices for all components of the weather as well as information needed
    to pick the day's weather.
    """
    global regular_conditions
    regular_conditions = [
        'Sunny',
        'Rainy and Windy',
        'Rainy',
        'Sunny and Windy',
        'Cloudy',
        'Cloudy and Windy',
        'Foggy and Cloudy'
    ]

    global seasons
    seasons = {'winter': [date.months[0], date.months[1], date.months[2]],
               'spring': [date.months[3], date.months[4], date.months[5]],
               'summer': [date.months[6], date.months[7], date.months[8]],
               'fall': [date.months[9], date.months[10], date.months[11]]}

    global season_specific_conditions
    season_specific_conditions = {
        'winter': ['Blizzard', 'Light Snow'],
        'spring': ['Sunny and Breezy'],
        'summer': ['Sunny and Breezy', 'Hazy'],
        'fall': ['Sunny and Breezy']
    }

    global temp_ranges
    temp_ranges = {
        'winter': list(range(-20, 36)),
        'spring': list(range(45, 69)),
        'summer': list(range(78, 116)),
        'fall': list(range(54, 73))
    }


def determine_weather(date_list):
    """
    Returns a dictionary representing the weather.
    The weather is determined according to the date provided, which determines the season.
    :param date_list: The input date list.
    """
    month = date_list[2]
    this_season = None
    weather = {}
    for season in seasons:
        if month in seasons[season]:
            weather['season'] = season
            this_season = season
            break

    this_seasons_conditions = regular_conditions[:]
    for cond in season_specific_conditions[this_season]:
        this_seasons_conditions.append(cond)

    weather['condition'] = choice(this_seasons_conditions)
    weather['temp'] = choice(temp_ranges[this_season])

    return weather


def string_weather(weather):
    """
    Stringifys the weather.
    :param weather: The input weather dictionary.
    """
    return "%s°F, %s" % (weather['temp'], weather['condition'])


if __name__ == "__main__":
    print("To play this game, run 'launch.py'.\n"
          "For more information about this file, see 'readme.txt'.")
