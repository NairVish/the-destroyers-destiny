"""
Handles and contains all definitions for the terminal sequence of the main quest.
"""

__author__ = 'Vishnu Nair'

import getpass
from time import sleep

import globals


def terminal():
    """
    Executes the terminal sequence.
    """
    stage1()
    stage2()
    stage3()
    text_interlude()
    stage4()


def receive_input():
    """
    Receives and returns input from a shell-style prompt.
    """
    return input("root@MissileLaunch main$ ")


def receive_input_2():
    """
    Receives and returns input from an option prompt.
    """
    return input(">> ")


def stage1():
    """
    Executes stage 1 of the terminal sequence.
    """
    def print_menu():
        globals.clear_screen()
        print("WELCOME TO THE MISSILE COMMAND MENU!\n"
              "Please read all options carefully and select the option you wish to use.\n"
              "Please also remember to use some common sense.\n"
              "\t1. Proceed with missile launch.\n"
              "\t2. Self-destruct missiles (WARNING: Will cause mass destruction on user's home planet!)\n"
              "\t3. View missile status.\n"
              "\t4. Quit.\n")
        return receive_input()

    accepted_answers = ['1', '2', '3', '4']
    inp = print_menu()
    while True:
        while inp not in accepted_answers:
            if inp.startswith(('pwd', 'ls', 'rm', 'mv', 'bash', 'sudo', 'awk', 'sed')):
                print("-launch: %s: Normal shell functions disabled. Operation aborted." % (inp.split(' ', 1)[0]))
                inp = receive_input()
                continue
            print("-launch: %s: command not found" % (inp.split(' ', 1)[0]))
            inp = receive_input()
        if inp is '1':
            return
        elif inp is '2':
            globals.clear_screen()
            print("Loading self-destruction program...\n")
            sleep(3)
            print("Fatal error: Self-destruction program not configured.\n"
                  "Operation aborted.\n")
            input("Press enter to continue...")
            inp = print_menu()
        elif inp is '3':
            globals.clear_screen()
            print("Missile 1 Status\n"
                  "* Overall: OK!\n"
                  "* Guidance systems: Ready!\n"
                  "* Hexonium status: Dormant. Ready for ultimate reactions.\n\n"
                  "Missile 2 Status\n"
                  "* Overall: OK!\n"
                  "* Guidance systems: Ready!\n"
                  "* Hexonium status: Dormant. Ready for ultimate reactions.\n")
            input("Press enter to continue...")
            inp = print_menu()
        elif inp is '4':
            print("-launch: quit: Quitting failed. Once started, missile launch procedure cannot be aborted.")
            inp = receive_input()


def stage2():
    """
    Executes stage 2 of the terminal sequence.
    """
    def print_menu():
        globals.clear_screen()
        print("Select any one of the following already-configured celestial entities:\n"
              "\t1. Valst'r Home Planet (valstr1)\n")
        return receive_input_2()

    inp = print_menu()
    while True:
        if inp is not '1':
            globals.clear_screen()
            print("MissileLaunch: Invalid option.\n")
            input("Press any button to return to previous menu.")
        else:
            return
        inp = print_menu()


def stage3():
    """
    Executes stage 3 of the terminal sequence.
    """
    def print_menu():
        globals.clear_screen()
        print("Please type in the launch password to finalize the procedure.\n"
              "Type in 'hint' for a hint.\n"
              "Note: You will not see your input on the terminal screen.")
        return getpass.getpass()

    word = print_menu()
    while word != "valstrDestroy":
        if word == "hint":
            globals.clear_screen()
            print(
                "Merlona: If I remember correctly, it has the word 'Destroy' in it as the second part of the password. " \
                "I believe the first part of the password is who we're trying to destroy. Lowercase too.\n")
            input("(Press enter to continue...)")
            word = print_menu()
            continue
        else:
            print("You have entered an invalid password. Please try again.")
            word = getpass.getpass()
    globals.clear_screen()
    print("Preparing missile systems...Done!\n"
          "Checking internal sensors...Done!\n"
          "Checking hexonium containers...Done!\n"
          "All systems ready!\n"
          "Starting countdown...")
    sleep(2)
    print("10...")
    sleep(0.5)
    print("9...")
    sleep(0.5)
    print("8...")
    sleep(0.5)
    print("7...")
    sleep(0.5)
    print("6...")
    sleep(0.5)
    print("5...")
    sleep(0.5)
    print("4...")
    sleep(0.5)
    print("3...")
    sleep(0.5)
    print("2...")
    sleep(0.5)
    print("1...")
    sleep(0.5)
    print("Lift-off of both missiles reported!\n")
    input("Press enter to continue...")


def text_interlude():
    """
    Prints the text interlude occurring between stages 3 and 4.
    """
    globals.clear_screen()
    print(
        "You and your assistant look at the other screens in the room that are tracking the missiles. It is five agonizing minutes before the missiles reach the Valst'r's home system. You realize that the Imperial Commander wasn't joking when he was talking about the warp drive.\n")
    print("On the radars, you notice other objects trying to head toward the missiles, but the missiles evade these objects with ease.\n")
    print("The two missiles head toward opposite sides of the Valst'r home planet and stay there for one final second before disappearing from the radars.\n")
    print("You look back at the main screen...\n")
    input("(Press enter to continue...)")


def stage4():
    """
    Executes stage 4 of the terminal sequence.
    """
    globals.clear_screen()
    print("Missiles currently en route to destination...",end="")
    sleep(1)
    print("Done!\n"
          "...\n"
          "...")
    sleep(2)
    print("Detonation of missile 1 of 2 reported!")
    print("Lost contact with missile 1.")
    print("...\n"
          "...")
    sleep(2)
    print("Detonation of missile 2 of 2 reported!")
    print("Lost contact with missile 2.")
    print("...\n"
          "...")
    print("Missile launch program to Valst'r Home Planet is presumed succeeded.\n"
          "EXIT SUCCESS.\n")

    input("Press enter to exit...")
    globals.clear_screen()

if __name__ == "__main__":
    print("To play this game, run 'launch.py.'.\n"
          "For more information about this file, see 'readme.txt'.")