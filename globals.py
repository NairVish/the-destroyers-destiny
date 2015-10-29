"""
Contains all variables and functions that will be referenced by almost every other module in the game.
"""

__author__ = 'Vishnu Nair'

import csv
import player
import os
import random


def init_globals():
    """
    Initializes all necessary global variables.
    """
    with open("people.txt", 'r') as people_fIle:    # people names for quest board
        all_names = people_fIle.readlines()
        global people_names
        people_names = [name.strip() for name in all_names]

    with open("caves_hideaways.txt", 'r') as cave_file: # dungeon names for side quests
        all_caves = cave_file.readlines()
        global cave_names
        cave_names = [cave.rstrip('\n') for cave in all_caves]

    with open("provinces.txt", 'r') as province_file:   # province names
        all_provinces = province_file.readlines()
        global province_names
        province_names = [province.strip() for province in all_provinces]

    global potion_names     # all potion data
    potion_names = []
    global potion_powers
    potion_powers = []
    global potion_type
    potion_type = []
    global potion_cost
    potion_cost = []
    global tabular_potions  # potion data for 'tabulate' function
    tabular_potions = []
    # amount_of_potions = 6
    potions = csv.reader(open("potions.csv", 'r'))
    num = 0
    for row in potions:
        potion_names.append(row[0])
        potion_powers.append(float(row[1]))
        potion_type.append(row[2])
        potion_cost.append(float(row[3]))
        tmp = []
        tmp.append(num)
        tmp.append(row[0])
        tmp.append(float(row[1]))
        tmp.append(row[2])
        tmp.append(float(row[3]))
        tabular_potions.append(tmp)
        num += 1

    global weapon_names     # all weapon data
    weapon_names = []
    global weapon_powers
    weapon_powers = []
    global weapon_cost
    weapon_cost = []
    global tabular_weapons
    tabular_weapons = []
    # amount_of_weapons = 12
    weapons = csv.reader(open("weapons.csv", 'r'))
    num = 0
    for row in weapons:
        weapon_names.append(row[0])
        weapon_powers.append(float(row[1]))
        weapon_cost.append(float(row[2]))
        tmp = []
        tmp.append(num)
        tmp.append(row[0])
        tmp.append(float(row[1]))
        tmp.append(float(row[2]))
        tabular_weapons.append(tmp)
        num += 1

    global loot_names   # all loot data
    loot_names = []
    global rare_loot_names
    rare_loot_names = []
    global loot_values
    loot_values = []
    global rare_loot_values
    rare_loot_values = []
    # amount_of_loot = 11
    # amount_of_rare_loot = 7
    loot = csv.reader(open("loot.csv", 'r'))
    rare_loot = csv.reader(open("rare_loot.csv", 'r'))
    for row in loot:
        loot_names.append(row[0])
        loot_values.append(row[1])
    for row in rare_loot:
        rare_loot_names.append(row[0])
        rare_loot_values.append(row[1])

    global main_quest_enemies   # all necessary main quest data
    global main_quest_bosses
    global main_quest_dungeons
    main_quest_bosses = ["Valst'r Lieutenant General", "Valst'r General", "Valst'r Commander-in-Chief"]
    main_quest_dungeons = ["The Battle for Home", "Valst'r Base Camp", "The Road to the Imperial Launch SIte"]
    with open("main_enemies.txt", 'r') as main_enemy_fIle:
        all_enemies = main_enemy_fIle.readlines()
        main_quest_enemies = [enemy.rstrip('\n') for enemy in all_enemies]

    global side_enemy_types     # all necessary side quest data
    global side_quest_enemies
    side_enemy_types = ["bandit", "looter", "mobster"]
    side_quest_enemies = []
    with open("side_enemies.txt", 'r') as side_enemy_fIle:
        all_enemies = side_enemy_fIle.readlines()
        for group in all_enemies:
            group = group.rstrip('\n')
            group = group.split(', ')
            side_quest_enemies.append(group)

    global dialogue             # all dialogue data
    global dialogue_type
    global dialogue_jump_targets
    dialogue = []
    dialogue_type = []
    dialogue_jump_targets = []
    all_dialogue = csv.reader(open("dialogue.csv",'r'))
    for row in all_dialogue:
        dialogue.append(row[0])
        dialogue_type.append(row[1])
        dialogue_jump_targets.append(int(row[2]))


def select_province():
    """
    Selects and returns a random province from the list of provinces.
    """
    return random.choice(province_names)


def declare_new_player(name):
    """
    :param name: The player's name.
    Initializes and declares a new player (if there is no save data or the user chooses not to load save data) using
    only the two pieces of data required by the player's __init__ function. The player is declared as a global
    variable.
    """
    global this_player
    province = select_province()
    this_player = player.Player(name, province)


def declare_existing_player(saved_stats, inventory):
    """
    :param saved_stats: All save data from the 'save.data' file, converted into a list.
    :param inventory: All inventory data from the last part of the 'save.data' file, converted into a list.
    Initializes and declares a player using existing save data. The player is declared as a global variable.
    """
    global this_player
    if saved_stats[11] == "None":
        weapon = None
    else:
        weapon = saved_stats[11]
    this_player = player.Player(saved_stats[0], saved_stats[1], int(saved_stats[2]), int(saved_stats[3]),
                                int(saved_stats[4]), int(saved_stats[5]), float(saved_stats[6]), float(saved_stats[7]),
                                int(saved_stats[8]), float(saved_stats[9]),(saved_stats[10] == "True"), weapon,
                                int(saved_stats[12]), (saved_stats[13] == "True"), inventory)


def clear_screen():
    """
    Clears the screen using the shell's clear command. If on Windows, 'cls' is passed to the shell, else 'clear'
    is passed.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


class GameOver(Exception):
    """
    An empty game over exception.
    """
    pass

if __name__ == "__main__":
    print("To play this game, run 'start_here.py.'.\n"
          "For more information about this file, see 'readme.txt'.")