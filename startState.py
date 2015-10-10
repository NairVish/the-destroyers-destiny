__author__ = 'vishnunair'

import os
import time
import player

def print_intro():  # We're printing out our awesome intro screen here.
    intro_text = (
        "THIS IS SOME INTRO TEXT."
        "I HAVE NO IDEA WHAT I'M GOING TO PUT HERE."
        "SO I'M PUTTING SOME PLACEHOLDER TEXT HERE."
    )
    print(intro_text)
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')

def show_start_menu():  # The main menu
    print('Main Menu')
    print('\t1. Start a New Game.')
    accepted_answers = ['1','1.']
    save = find_save()
    if save is not None:
        print('\t2. Continue from save.')
        accepted_answers = ['1','2','1.','2.']
    answer = input('Choose your desired option.')
    while answer not in accepted_answers:
        answer = input('You have entered an inavlid option. Please enter a valid option,')
    os.system('cls' if os.name == 'nt' else 'clear')
    if answer is '1' or '1.':
        return None
    else:
        return save


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def find_save():
    result = find_file('save.data', os.getcwd())
    if result == None:
        return None

    answer = ''
    print('A save file has been detected in the game directory.')
    answer = input('Would you like to load this save? (Y/N)').lower()
    accepted_answers = ['y','n','yes','no']
    while answer not in accepted_answers:
        answer = input('You have entered an inavlid option. Please enter a valid option,').lower()
    if 'y':
        return open('save.data','r')
    elif 'n':
        return None

def load_player():
    save = show_start_menu()
    global player
    if save is None:
        print("NEW GAME START")
        name = input('Please enter a name for your character: ')
        player = player.Player(name)
    else:
        save_data = [line.rstrip('\n') for line in save.readlines()]
        inventory = [line for line in save_data[10:(len(save_data)-1)]]
        print("Loading existing save...")
        print("Loading save data for %s" % save_data[0])
        player = player.Player(save_data[0],save_data[1],save_data[2],save_data[3],save_data[4],save_data[5],
                               save_data[6],save_data[7],save_data[8],save_data[9], inventory)
