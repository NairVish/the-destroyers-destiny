__author__ = 'vishnunair'
import sys
import os


def exit_program():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("The program has ended. Thank you for playing.")
    print('\n')
    sys.exit()