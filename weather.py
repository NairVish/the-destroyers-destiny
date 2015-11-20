import date
from random import choice

def init_weather():
    global regular_conditions
    regular_conditions = [
        'Sunny',
        'Rainy and Windy',
        'Rainy',
        'Windy',
        'Cloudy',
        'Cloudy and WIndy',
        'Foggy and Cloudy'
    ]

    global seasons
    seasons = {'winter' : [date.months[0], date.months[1], date.months[2]],
               'spring' : [date.months[3], date.months[4], date.months[5]],
               'summer' : [date.months[6], date.months[7], date.months[8]],
               'fall' : [date.months[9], date.months[10], date.months[11]]}

    global season_specific_conditions
    season_specific_conditions = {
        'winter' : ['Blizzard', 'Light Snow'],
        'spring' : ['Breezy'],
        'summer' : ['Breezy', 'Hazy'],
        'fall' : ['Breezy']
    }

    global temp_ranges
    temp_ranges = {
        'winter' : list(range(-20,36)),
        'spring' : list(range(45,69)),
        'summer' : list(range(78,116)),
        'fall' : list(range(54,73))
    }

def determine_weather(date_list): # we need temp, weather cond, and season
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
    return ("%s°F, %s" % (weather['temp'], weather['condition']))