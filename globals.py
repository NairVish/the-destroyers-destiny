__author__ = 'vishnunair'
import csv
import player
import os


def init_globals():
    with open("people.txt", 'r') as people_fIle:
        all_names = people_fIle.readlines()
        global people_names
        people_names = [name.strip() for name in all_names]

    with open("caves_hideaways.txt", 'r') as cave_file:
        all_caves = cave_file.readlines()
        global cave_names
        cave_names = [cave.rstrip('\n') for cave in all_caves]

    with open("provinces.txt", 'r') as province_file:
        all_provinces = province_file.readlines()
        global province_names
        province_names = [province.strip() for province in all_provinces]

    global potion_names
    global potion_powers
    global potion_type
    global potion_cost
    i = 0
    potions = csv.reader(open("potions.csv", 'r'))
    for row in potions:
        potion_names[i] = row[0]
        potion_powers[i] = row[1]
        potion_type[i] = row[2]
        potion_cost[i] = row[3]
        i += 1

    global weapon_names
    global weapon_powers
    global weapon_cost
    i = 0
    weapons = csv.reader(open("weapons.csv", 'r'))
    for row in weapons:
        weapon_names[i] = row[0]
        weapon_powers[i] = row[1]
        weapon_cost[i] = row[2]
        i += 1

def declare_new_player(name):
    global this_player
    this_player = player.Player(name)


def declare_existing_player(saved_stats, inventory):
    global this_player
    this_player = player.Player(saved_stats[0], saved_stats[1], saved_stats[2], saved_stats[3], saved_stats[4],
                                saved_stats[5], saved_stats[6], saved_stats[7], saved_stats[8], saved_stats[9],
                                saved_stats[10], saved_stats[11], inventory)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# init_globals()
# print(people_names)
# print(cave_names)
# print(province_names)
# for row in potions:
#     print(row)
# for row in weapons:
#     print(row)
# clear_screen()
