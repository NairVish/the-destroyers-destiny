__author__ = 'vishnunair'
import csv
import player
import os
import random


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
    potion_names = []
    global potion_powers
    potion_powers = []
    global potion_type
    potion_type = []
    global potion_cost
    potion_cost = []
    global tabular_potions
    tabular_potions = []
    amount_of_potions = 6
    potions = csv.reader(open("potions.csv", 'r'))
    for row in potions:
        for num in range(amount_of_potions):
            potion_names.append(row[0])
            potion_powers.append(float(row[1]))
            potion_type.append(row[2])
            potion_cost.append(float(row[3]))
            tmp = []
            tmp.append(num)
            tmp.append(potion_names[num])
            tmp.append(potion_powers[num])
            tmp.append(potion_type[num])
            tmp.append(potion_cost[num])
            tabular_potions.append(tmp)

    global weapon_names
    weapon_names = []
    global weapon_powers
    weapon_powers = []
    global weapon_cost
    weapon_cost = []
    global tabular_weapons
    tabular_weapons = []
    amount_of_weapons = 12
    weapons = csv.reader(open("weapons.csv", 'r'))
    for row in weapons:
        for num in range(amount_of_weapons):
            weapon_names.append(row[0])
            weapon_powers.append(float(row[1]))
            weapon_cost.append(float(row[2]))
            tmp = []
            tmp.append(num)
            tmp.append(weapon_names[num])
            tmp.append(weapon_powers[num])
            tmp.append(weapon_cost[num])
            tabular_weapons.append(tmp)

    global loot_names
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

    global main_quest_enemies
    global main_quest_bosses
    global main_quest_dungeons
    with open("main_enemies.txt", 'r') as main_enemy_fIle:
        all_enemies = main_enemy_fIle.readlines()
        main_quest_enemies = [enemy.rstrip('\n') for enemy in all_enemies]
    with open("main_bosses.txt", 'r') as main_boss_fIle:
        all_bosses = main_boss_fIle.readlines()
        main_quest_bosses = [boss.rstrip('\n') for boss in all_bosses]
    with open("main_dungeons.txt", 'r') as main_dungeon_fIle:
        all_dungeons = main_dungeon_fIle.readlines()
        main_quest_dungeons = [dungeon.rstrip('\n') for dungeon in all_dungeons]

    global side_enemy_types
    global side_quest_enemies
    side_enemy_types = ["bandit", "looter", "mobster"]
    side_quest_enemies = []
    with open("side_enemies.txt", 'r') as side_enemy_fIle:
        all_enemies = side_enemy_fIle.readlines()
        for group in all_enemies:
            group = group.rstrip('\n')
            group = group.split(', ')
            side_quest_enemies.append(group)

    global dialogue
    global dialogue_types
    global dialogue_jump_targets
    dialogue = []
    dialogue_types = []
    dialogue_jump_targets = []
    all_dialogue = csv.reader(open("dialogue.csv",'r'))
    for row in all_dialogue:
        dialogue.append(row[0])
        dialogue_types.append(row[1])
        dialogue_jump_targets.append(int(row[2]))

def select_province():
    return random.choice(province_names)


def declare_new_player(name):
    global this_player
    province = select_province()
    this_player = player.Player(name, province)


def declare_existing_player(saved_stats, inventory):
    global this_player
    this_player = player.Player(saved_stats[0], saved_stats[1], int(saved_stats[2]), int(saved_stats[3]),
                                int(saved_stats[4]), int(saved_stats[5]), int(saved_stats[6]), int(saved_stats[7]),
                                int(saved_stats[8]), int(saved_stats[9]), int(saved_stats[10]),
                                (saved_stats[11] == "True"), saved_stats[12], int(saved_stats[13]),
                                (saved_stats[14] == "True"), inventory)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class GameOver(Exception):
    pass

init_globals()
print(dialogue)
print(dialogue_types)
print(dialogue_jump_targets)