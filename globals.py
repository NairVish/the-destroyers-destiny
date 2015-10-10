__author__ = 'vishnunair'
import csv

def init_globals():
    with open("people.txt",'r') as people_fIle:
        all_names = people_fIle.readlines()
        global people_names
        people_names = [name.strip() for name in all_names]

    with open("caves_hideaways.txt",'r') as cave_file:
        all_caves = cave_file.readlines()
        global cave_names
        cave_names = [cave.rstrip('\n') for cave in all_caves]

    with open("provinces.txt", 'r') as province_file:
        all_provinces = province_file.readlines()
        global province_names
        province_names = [province.strip() for province in all_provinces]

    global potions
    potions = csv.reader(open("potions.csv",'r'))

    global weapons
    weapons = csv.reader(open("weapons.csv",'r'))

init_globals()
print(people_names)
print(cave_names)
print(province_names)
for row in potions:
    print(row)
for row in weapons:
    print(row)