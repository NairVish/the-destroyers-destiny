import globals
import tkinter
import battle
from time import sleep
from random import choice
from colorama import Fore


def battle_arena():
    pass


def battle_practice():
    print("You decide to go to the Battle Practice Area. You could always get stronger, and practice makes perfect, "
          "right?\n")
    print("Alas, the only way to train here is to whack on a dummy until you get bored. Seriously. These dummys "
          "don't even award a lot of XP. Might as well go and fight a bunch of aliens...\n")
    print("But you're here, so you ultimately decide to fulfill your destiny and "
          "whack on a dummy until you get bored.\n")
    input("(Press enter to start whacking...)")
    globals.clear_screen()
    curr = battle.Battle(custom_parameters="dummy")
    curr.do_battle()

def roulette():

    class RouletteExit(Exception):
        pass

    def opening():
        print("You enter the bustling casino. It seems that, no matter what happens, people will continue throwing "
              "their money away on these games. Might as well throw your money away too.\n")
        print("You're particularly fond of roulette. So, you head over to the roulette table and hope that you "
              "don't lose all of your money.\n")
        input("(Press enter to start playing...)")
        globals.clear_screen()
        print("Game Types:\n"
              "\t1. American Roulette\n"
              "\t2. European Roulette\n")
        print("What type of game would you like to play?\n")
        print(Fore.GREEN + "<NOTE: For your reference, a window containing the layout of the respective "
                           "roulette board will open once you make your selection.>\n")
        inp = input("Board selection: ")
        accepted_answers = ['1','2']
        while inp not in accepted_answers:
            inp = input("You have entered an invalid option. Please try again: ")
        globals.clear_screen()
        return inp

    def init_roulette_board():
        board_rows = []
        board_columns = []
        if game_type == "American Roulette":
            board_rows.append(['0', '00'])
        else:
            board_rows.append(['0'])
        board_rows.append(['1','2','3'])
        board_rows.append(['4','5','6'])
        board_rows.append(['7','8','9'])
        board_rows.append(['10','11','12'])
        board_rows.append(['13','14','15'])
        board_rows.append(['16','17','18'])
        board_rows.append(['19','20','21'])
        board_rows.append(['22','23','24'])
        board_rows.append(['25','26','27'])
        board_rows.append(['28','29','30'])
        board_rows.append(['31','32','33'])
        board_rows.append(['34','35','36'])
        board_columns.append(['1','4','7','10','13','16','19','22','25','28','31','34'])
        board_columns.append(['2','5','8','11','14','17','20','23','26','29','32','35'])
        board_columns.append(['3','6','9','12','15','18','21','24','27','30','33','36'])
        return board_rows, board_columns

    def main_header():
        print("ROULETTE")
        print("Game Type: %s" % game_type)
        print("Your money: $%s" % globals.this_player.money)
        print("Minimum Bet: $%s" % min_bet)
        print("Maximum Bet: $%s\n" % max_bet)

    def choose_bet():
        print("Bet Types:\n"
              "\t1. Straight Up (bet on a single number, 35:1)\n"
              "\t2. Split Bet (bet on two adjacent numbers, 17:1)\n"
              "\t3. Street Bet (bet on one of the 12 rows, 11:1)\n"
              "\t4. Double Street (bet on two adjacent rows, 5:1)\n"
              "\t5. Basket (bet on the top pocket of the board, 6:1)\n"
              "\t6. Halves (bet on 1-18 or 18-36, 1:1)\n"
              "\t7. All Reds (bet on all reds, 1:1)\n"
              "\t8. All Blacks (bet on all blacks, 1:1)\n"
              "\t9. All Odds (bet on all odds, 1:1)\n"
              "\t10. All Evens (bet on all evens, 1:1)\n"
              "\t11. Dozens Bet (bet on a consecutive dozen, 2:1)\n"
              "\t12. Columns Bet (bet on one of the three vertical columns, 2:1)\n")
        inp = input("Enter the number of the bet you would like to make, else enter 'q' to leave: ")
        accepted_answers = [str(x) for x in range(0,13)]
        accepted_answers.append('q')
        while inp not in accepted_answers:
            inp = input("You have entered an invalid option. Please try again: ")
        globals.clear_screen()
        if inp == 'q':
            raise RouletteExit
        else:
            return inp

    def bet_header(bet_type, payoff):
        print("ROULETTE: %s" % bet_type)
        print("Payoff: %s:1" % str(payoff))
        print("Your money: $%s" % globals.this_player.money)
        print("Minimum Bet: $%s" % min_bet)
        print("Maximum Bet: $%s\n" % max_bet)

    def get_wager():
        wager = input("Please enter your wager: $")
        while True:
            try:
                wager = int(wager)
            except ValueError:
                wager = input("You have entered an invalid amount. Please try again: ")
                continue
            else:
                if wager > globals.this_player.money:
                    wager = input("You do not have enough money. Please enter a new wager: ")
                    continue
                if wager < min_bet or wager > max_bet:
                    wager = input("Your wager must be within the bounds of the house's minimum and maximum bets.\n"
                                  "Please try again: ")
                    continue
                break
        return wager

    def determine_function(choice):
        if choice == '1':
            return straight_up
        elif choice == '2':
            return split_bet
        elif choice == '3':
            return street_bet
        elif choice == '4':
            return double_street
        elif choice == '5':
            return basket
        elif choice == '6':
            return halves
        elif choice == '7':
            return bet_color_red
        elif choice == '8':
            return bet_color_black
        elif choice == '9':
            return bet_odd
        elif choice == '10':
            return bet_even
        elif choice == '11':
            return dozens
        elif choice == '12':
            return column

    def game_loop():
        nonlocal net_winnings

        while True:
            main_header()

            try:
                choice = choose_bet()
                globals.clear_screen()
            except RouletteExit:
                globals.clear_screen()
                layout_ref.destroy()
                return
            else:
                bet = determine_function(choice)
                winnings = bet()
                net_winnings += winnings
                globals.clear_screen()

    # Bet functions
    def straight_up():
        bet_type = "Straight Up"
        payoff = 35
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        your_choice = input("What number will you bet on? ")
        while your_choice not in roulette_choices:
            your_choice = input("Please enter a valid choice: ")
        print("\nThe dealer releases the ball into the spinning roulette wheel.\n"
              "The ball eventually stops and lands on...\n")
        sleep(1.5)
        result = choice(roulette_choices)
        print(result + '!\n')
        if your_choice != result:
            print("Sorry, you lost this round.\n")
            input("Press enter to continue...")
            return earning
        else:
            print("Amazing! You won! How on Nira did you do that?!")
            winnings = wager * payoff
            print("You won $%s!" % str(winnings))
            globals.this_player.money += winnings
            earning += winnings
            input("Press enter to continue...")
            return earning

    def split_bet():
        bet_type = "Split Bet"
        payoff = 17
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        inp = input("Please select the ROW of the first number you would like to bet on.\n"
                    "Here, a 'row' is a row of three consecutive numbers on the roulette board.\n"
                    "For example, row 0 would be [0] (or [0,00] if American) and so on.\n"
                    "Row number: ")
        accepted_answers = [str(x) for x in range (0,13)]
        while inp not in accepted_answers:
            inp = input("Please enter a valid option: ")
        inp = int(inp)
        chosen_row = roulette_board_rows[inp]
        your_choice = []

        print("Possible Numbers: ")
        accepted_answers = []
        for num in chosen_row:
            print("\t" + num)
            accepted_answers.append(num)
        inp2 = input("What number do you pick? ")
        while inp2 not in accepted_answers:
            inp2 = input("Please choose a valid option: ")
        if inp2 != '00':
            inp2 = int(inp2)
        your_choice.append(str(inp2))

        accepted_answers_2 = []
        print("Next possible numbers: ")
        if inp == 0:
            if inp2 == '00':
                for num in ['2','3']:
                    print('\t' + num)
                    accepted_answers_2.append(num)
            elif inp2 == 0 and game_type == "American Roulette":
                for num in ['1','2']:
                    print('\t' + num)
                    accepted_answers_2.append(num)
            else:
                for num in ['1','2','3']:
                    print('\t' + num)
                    accepted_answers_2.append(num)
        elif inp == 1:
            if inp2 == 1:
                for num in ['0','2','4']:
                    print('\t' + num)
                    accepted_answers_2.append(num)
            elif inp2 == 2:
                if game_type == "American Roulette":
                    for num in ['0','00','1','3','5']:
                        print('\t' + num)
                        accepted_answers_2.append(num)
                else:
                    for num in ['0','1','3','5']:
                        print('\t' + num)
                        accepted_answers_2.append(num)
            else:
                if game_type == "American Roulette":
                    for num in ['00','2','6']:
                        print('\t' + num)
                        accepted_answers_2.append(num)
                else:
                    for num in ['0','2','6']:
                        print('\t' + num)
                        accepted_answers_2.append(num)
        elif inp == 12:
            if inp2 == 34:
                for num in ['31','35']:
                    print('\t' + num)
                    accepted_answers_2.append(num)
            elif inp2 == 35:
                for num in ['34','36','32']:
                    print('\t' + num)
                    accepted_answers_2.append(num)
            else:
                for num in ['33','35']:
                    print('\t' + num)
                    accepted_answers_2.append(num)
        else:
            if chosen_row.index(str(inp2)) == 0:
                print("\t" + roulette_board_rows[inp-1][0])
                print("\t" + chosen_row[1])
                print("\t" + roulette_board_rows[inp+1][0])
                accepted_answers_2.append(roulette_board_rows[inp-1][0])
                accepted_answers_2.append(chosen_row[1])
                accepted_answers_2.append(roulette_board_rows[inp-1][0])
            elif chosen_row.index(str(inp2)) == 1:
                print("\t" + roulette_board_rows[inp-1][1])
                print("\t" + chosen_row[0])
                print("\t" + chosen_row[2])
                print("\t" + roulette_board_rows[inp+1][1])
                accepted_answers_2.append(roulette_board_rows[inp-1][1])
                accepted_answers_2.append(chosen_row[0])
                accepted_answers_2.append(chosen_row[2])
                accepted_answers_2.append(roulette_board_rows[inp+1][1])
            elif chosen_row.index(str(inp2)) == 2:
                print("\t" + roulette_board_rows[inp-1][2])
                print("\t" + chosen_row[1])
                print("\t" + roulette_board_rows[inp+1][2])
                accepted_answers_2.append(roulette_board_rows[inp-1][2])
                accepted_answers_2.append(chosen_row[1])
                accepted_answers_2.append(roulette_board_rows[inp+1][2])
        inp3 = input("What number will you pick? ")
        while inp3 not in accepted_answers_2:
            inp3 = input("Please enter a valid option: ")
        your_choice.append(inp3)
        print("\nThe dealer releases the ball into the spinning roulette wheel.\n"
              "The ball eventually stops and lands on...\n")
        sleep(2.5)
        result = choice(roulette_choices)
        print(result + '!\n')
        if result not in your_choice:
            print("Sorry, you lost this round.\n")
            input("Press enter to continue...")
            return earning
        else:
            print("Awesome! You won!")
            winnings = wager * payoff
            print("You won $%s!" % str(winnings))
            globals.this_player.money += winnings
            earning += winnings
            input("Press enter to continue...")
            return earning

    def street_bet():
        bet_type = "Street Bet"
        payoff = 11
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        inp = input("Please select the row of numbers you would like to bet on.\n"
                    "Here, a 'row' is a row of three consecutive numbers on the roulette board.\n"
                    "For example, row 1 would be [1,2,3] and so on.\n"
                    "You CANNOT pick the row containing 0 (and 00 if American).\n\n"
                    "Row number: ")
        accepted_answers = [str(x) for x in range (1,13)]
        while inp not in accepted_answers:
            inp = input("Please enter a valid option: ")
        inp = int(inp)
        your_choice = roulette_board_rows[inp]
        print("\nThe dealer releases the ball into the spinning roulette wheel.\n"
              "The ball eventually stops and lands on...\n")
        sleep(2.5)
        result = choice(roulette_choices)
        print(result + '!\n')
        if result not in your_choice:
            print("Sorry, you lost this round.\n")
            input("Press enter to continue...")
            return earning
        else:
            print("Awesome! You won!")
            winnings = wager * payoff
            print("You won $%s!" % str(winnings))
            globals.this_player.money += winnings
            earning += winnings
            input("Press enter to continue...")
            return earning

    def double_street():
        bet_type = "Double Street"
        payoff = 5
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        inp = input("Please select the first row of numbers you would like to bet on.\n"
                    "Here, a 'row' is a row of three consecutive numbers on the roulette board.\n"
                    "For example, row 1 would be [1,2,3] and so on.\n"
                    "Row number: ")
        accepted_answers = [str(x) for x in range (1,13)]
        while inp not in accepted_answers:
            inp = input("Please enter a valid option: ")
        inp = int(inp)
        your_choice = roulette_board_rows[inp][:]
        if inp != 1 and inp != 12:
            print("Next possible choices:\n"
                  "\tRow %s: %s\n"
                  "\tRow %s: %s\n" % (str(inp-1), roulette_board_rows[inp-1],
                                      str(inp+1), roulette_board_rows[inp+1]))
            accepted_answers = [str(inp-1), str(inp+1)]
            inp2 = input("Please enter your second option: ")
            while inp2 not in accepted_answers:
                inp2 = input("Please enter a valid option: ")
            inp2 = int(inp2)
            for num in roulette_board_rows[inp2]:
                your_choice.append(num)
        elif inp == 1:
            print("Your second choice will be row 2, with numbers ['4','5','6'].")
            your_choice.append('4')
            your_choice.append('5')
            your_choice.append('6')
        else:
            print("Your second choice will be row 11, with numbers ['31','32','33'].")
            your_choice.append('31')
            your_choice.append('32')
            your_choice.append('33')
        print("\nThe dealer releases the ball into the spinning roulette wheel.\n"
              "The ball eventually stops and lands on...\n")
        sleep(2.5)
        result = choice(roulette_choices)
        print(result + '!\n')
        if result not in your_choice:
            print("Sorry, you lost this round.\n")
            input("Press enter to continue...")
            return earning
        else:
            print("Awesome! You won!")
            winnings = wager * payoff
            print("You won $%s!" % str(winnings))
            globals.this_player.money += winnings
            earning += winnings
            input("Press enter to continue...")
            return earning

    def basket():
        bet_type = "Basket"
        payoff = 6
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        your_choice = ['0','1','2','3']
        if game_type == 'American Roulette':
            your_choice.append('00')
        print("You are betting on the top pocket of numbers on the board:\n"
              "[0,1,2,3] (as well as 00 if American).\n")
        print("\nThe dealer releases the ball into the spinning roulette wheel.\n"
              "The ball eventually stops and lands on...\n")
        sleep(2.5)
        result = choice(roulette_choices)
        print(result + '!\n')
        if result not in your_choice:
            print("Sorry, you lost this round.\n")
            input("Press enter to continue...")
            return earning
        else:
            print("Awesome! You won!")
            winnings = wager * payoff
            print("You won $%s!" % str(winnings))
            globals.this_player.money += winnings
            earning += winnings
            input("Press enter to continue...")
            return earning

    def halves():
        bet_type = "Halves"
        payoff = 1
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        print("Halves\n"
              "\t1. 1-18\n"
              "\t2. 19-36\n")
        inp = input("Which half will you pick? ")
        accepted_answers = ['1','2']
        while inp not in accepted_answers:
            inp = input("Please enter a valid option: ")
        if inp == '1':
            your_choice = first_half
        else:
            your_choice = second_half
        print("\nThe dealer releases the ball into the spinning roulette wheel.\n"
              "The ball eventually stops and lands on...\n")
        sleep(2.5)
        result = choice(roulette_choices)
        print(result + '!\n')
        if result not in your_choice:
            print("Sorry, you lost this round.\n")
            input("Press enter to continue...")
            return earning
        else:
            print("Awesome! You won!")
            winnings = wager * payoff
            print("You won $%s!" % str(winnings))
            globals.this_player.money += winnings
            earning += winnings
            input("Press enter to continue...")
            return earning


    def bet_color_red():
        bet_type = "All Reds"
        payoff = 1
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        your_choice = reds
        print("\nThe dealer releases the ball into the spinning roulette wheel.\n"
              "The ball eventually stops and lands on...\n")
        sleep(2.5)
        result = choice(roulette_choices)
        print(result + '!\n')
        if result not in your_choice:
            print("Sorry, you lost this round.\n")
            input("Press enter to continue...")
            return earning
        else:
            print("Awesome! You won!")
            winnings = wager * payoff
            print("You won $%s!" % str(winnings))
            globals.this_player.money += winnings
            earning += winnings
            input("Press enter to continue...")
            return earning

    def bet_color_black():
        bet_type = "All Blacks"
        payoff = 1
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        your_choice = blacks
        print("\nThe dealer releases the ball into the spinning roulette wheel.\n"
              "The ball eventually stops and lands on...\n")
        sleep(2.5)
        result = choice(roulette_choices)
        print(result + '!\n')
        if result not in your_choice:
            print("Sorry, you lost this round.\n")
            input("Press enter to continue...")
            return earning
        else:
            print("Awesome! You won!")
            winnings = wager * payoff
            print("You won $%s!" % str(winnings))
            globals.this_player.money += winnings
            earning += winnings
            input("Press enter to continue...")
            return earning


    def bet_odd():
        bet_type = "All Odds"
        payoff = 1
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        your_choice = odds
        print("\nThe dealer releases the ball into the spinning roulette wheel.\n"
              "The ball eventually stops and lands on...\n")
        sleep(2.5)
        result = choice(roulette_choices)
        print(result + '!\n')
        if result not in your_choice:
            print("Sorry, you lost this round.\n")
            input("Press enter to continue...")
            return earning
        else:
            print("Awesome! You won!")
            winnings = wager * payoff
            print("You won $%s!" % str(winnings))
            globals.this_player.money += winnings
            earning += winnings
            input("Press enter to continue...")
            return earning

    def bet_even():
        bet_type = "All Evens"
        payoff = 1
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        your_choice = evens
        print("\nThe dealer releases the ball into the spinning roulette wheel.\n"
              "The ball eventually stops and lands on...\n")
        sleep(2.5)
        result = choice(roulette_choices)
        print(result + '!\n')
        if result not in your_choice:
            print("Sorry, you lost this round.\n")
            input("Press enter to continue...")
            return earning
        else:
            print("Awesome! You won!")
            winnings = wager * payoff
            print("You won $%s!" % str(winnings))
            globals.this_player.money += winnings
            earning += winnings
            input("Press enter to continue...")
            return earning

    def dozens():
        bet_type = "Dozens"
        payoff = 2
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        print("Dozens\n"
              "\t1. 1-12\n"
              "\t2. 13-24\n"
              "\t3. 25-36\n")
        inp = input("Which dozen will you pick? ")
        accepted_answers = ['1','2','3']
        while inp not in accepted_answers:
            inp = input("Please enter a valid option: ")
        if inp == '1':
            your_choice = first_dozen
        elif inp == '2':
            your_choice = second_dozen
        else:
            your_choice = third_dozen
        print("\nThe dealer releases the ball into the spinning roulette wheel.\n"
              "The ball eventually stops and lands on...\n")
        sleep(2.5)
        result = choice(roulette_choices)
        print(result + '!\n')
        if result not in your_choice:
            print("Sorry, you lost this round.\n")
            input("Press enter to continue...")
            return earning
        else:
            print("Awesome! You won!")
            winnings = wager * payoff
            print("You won $%s!" % str(winnings))
            globals.this_player.money += winnings
            earning += winnings
            input("Press enter to continue...")
            return earning

    def column():
        bet_type = "Columns"
        payoff = 2
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        print("Columns:\n"
              "\t1. First Column\n"
              "\t2. Second Column\n"
              "\t3. Third Column")
        print("Here, a 'column' is one of three large columns on the roulette board that comprise of 12 numbers each.\n"
              "For example, the first column comprises of the following: ['1','4','7','10','13','16','19','22','25','28','31','34'] "
              "and so on.\n"
              "None of the columns you can pick will have 0 (and 00 if American).\n")
        inp = input("Which column will you pick? ")
        accepted_answers = ['1','2','3']
        while inp not in accepted_answers:
            inp = input("Please enter a valid option: ")
        if inp == '1':
            your_choice = roulette_board_columns[0]
        elif inp == '2':
            your_choice = roulette_board_columns[1]
        else:
            your_choice = roulette_board_columns[2]
        print("\nThe dealer releases the ball into the spinning roulette wheel.\n"
              "The ball eventually stops and lands on...\n")
        sleep(2.5)
        result = choice(roulette_choices)
        print(result + '!\n')
        if result not in your_choice:
            print("Sorry, you lost this round.\n")
            input("Press enter to continue...")
            return earning
        else:
            print("Awesome! You won!")
            winnings = wager * payoff
            print("You won $%s!" % str(winnings))
            globals.this_player.money += winnings
            earning += winnings
            input("Press enter to continue...")
            return earning
    # END bet functions

    type = opening()
    if type == '1':
        game_type = "American Roulette"
    else:
        game_type = "European Roulette"

    # Set min and max bets
    min_bet = 3
    max_bet = 15
    net_winnings = 0

    roulette_choices = [str(x) for x in range(0,37)]
    # American Roulette has an extra number.
    if type == '1':
        roulette_choices.append('00')

    # Set up roulette board row and column list representations as well as various groups.
    roulette_board_rows, roulette_board_columns = init_roulette_board()
    reds = ['1','3','5','7','9','12','14','16','18','21','23','25','27','28','30','32','34','36']
    blacks = ['2','4','6','8','10','11','13','15','17','19','20','22','24','26','29','31','33','35']
    evens = ['2','4','6','8','10','12','14','16','18','20','22','24','26','28','30','32','34','36']
    odds = ['1','3','5','7','9','11','13','15','17','19','21','23','25','27','29','31','33','35']
    first_half = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
    second_half = ['19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']
    first_dozen = ['1','2','3','4','5','6','7','8','9','10','11','12']
    second_dozen = ['13','14','15','16','17','18','19','20','21','22','23','24']
    third_dozen = ['25','26','27','28','29','30','31','32','33','34','35','36']

    # initialize layout reference GUI
    layout_ref = tkinter.Tk()
    title = "%s: Board Layout" % game_type
    layout_ref.wm_title(title)
    layout_ref.geometry('{}x{}'.format(707, 300))
    image_name = "%s.gif" % game_type
    layout_image = tkinter.PhotoImage(file=image_name)
    new_image = layout_image.subsample(2, 2)
    canvas = tkinter.Canvas()
    canvas.create_image(0, 0, anchor='nw', image=new_image)
    canvas.pack(fill='both',expand='yes')
    layout_ref.after(0, game_loop)
    layout_ref.mainloop()

    if net_winnings < 0:
        print("Counting all of the rounds you played today, you ended up losing a total of $%s.\n" % abs(net_winnings))
    elif net_winnings == 0:
        print("Counting all of the rounds you played, you ended up neither gaining nor losing!\n")
    else:
        print("Counting all of the rounds you played today, you ended up gaining a total of $%s.\n" % abs(net_winnings))
    input("(Press enter to return to Center Square...)")