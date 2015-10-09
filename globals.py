__author__ = 'vishnunair'
import csv

def initGlobals():
    peopleFIle = open("people.txt",'r')
    allNames = peopleFIle.readlines()
    global peopleNames
    peopleNames = [name.strip() for name in allNames]
    peopleFIle.close()

    caveFile = open("caves_hideaways.txt",'r')
    allCaves = caveFile.readlines()
    global caveNames
    caveNames = [cave.rstrip('\n') for cave in allCaves]
    caveFile.close()

    provinceFile = open("provinces.txt", 'r')
    allProvinces = provinceFile.readlines()
    global provinceNames
    provinceNames = [province.strip() for province in allProvinces]
    provinceFile.close()

    global potions
    pFile = open("potions.csv",'r')
    potions = csv.reader(pFile)

    global weapons
    wFile = open("weapons.csv",'r')
    weapons = csv.reader(wFile)

initGlobals()
print(peopleNames)
print(caveNames)
print(provinceNames)
for row in potions:
    print(row)
for row in weapons:
    print(row)