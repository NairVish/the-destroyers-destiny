"""
Handles all minigames/activities in Center Square in the player's home city.
"""

__author__ = "Vishnu Nair"

import globals
import tkinter
import battle
import exit
import random
from time import sleep
from random import choice
from colorama import Fore, init

init(autoreset=True)


def battle_arena():
    """
    Function for an eight-player, single-elimination battle tournament that the player can participate in.
    Each of the player's battles is a boss fight and is fought in real-time. The program randomly chooses the
    winners of the remaining fights. If the player is eliminated, the rest of the tournament is simulated.
    Eliminated participants are removed from the list of tournament participants.
    """

    def opening():
        """
        The intro sequence to the battle arena.
        """
        print("Ahh, the Battle Arena.\n")
        print("That place where the best warriors in all of Nira gather together and try to beat "
              "each other up...\n")
        print("Sometimes to death...\n")
        print("In front of a live audience...\n")
        print("The mere thought of getting beaten up badly in public is enough to send you running out of there, but "
              "you decide otherwise. You're perfectly capable. Why not do this?\n")
        print("So, you go forth and hope for the best.\n")
        input("(Press enter to go forth...)")
        globals.clear_screen()
        inp = input("Are you sure you want to enter the Battle Arena? (y/n) ")
        accepted_answers = ['y', 'n']
        while inp not in accepted_answers:
            inp = input("You have entered an invalid option. Please try again: ")
        globals.clear_screen()
        return inp

    def display_round_matches(participants):
        """
        Displays the matches in each round before the round begins.
        :param participants: A list of participants in the round.
            * In this list, match n-1's participants are in positions 2*n and 2*n+1. So, match 1's participants are
            in positions 0 and 1.
            * If the player is still in the tournament, he/she is always in position 0.
        """
        num_matches = int(len(participants)/2)
        if curr_round == max_round:
            print("FINAL ROUND")
        else:
            print("ROUND %s" % curr_round)

        if num_matches > 1:
            print("The matches for this round are as follows:\n")
        else:
            print("The final match is as follows:\n")

        for num in range(num_matches):
            print("Match %s" % str(num+1))
            print("%s vs. %s\n" % (participants[2*num], participants[2*num+1]))

        if this_player in participants and curr_round == max_round:
            print("You will be battling against %s in the final match.\n" % participants[1])
        elif this_player in participants:
            print("You will be battling against %s in Match 1.\n" % participants[1])
        else:
            print(Fore.RED + "You were eliminated from the tournament and will not be participating in further rounds.\n")

        input("(Press enter to start the round...)")
        globals.clear_screen()

    def battle_intro(player_battle_participants):
        """
        The intro to the player's battle. NOT executed if the player has been eliminated.
        :param player_battle_participants: The participants in the player's battle.
        """
        print("Like always, the announcer goes up to the ring to introduce the challengers.\n")
        input("(Press enter to continue...)")
        globals.clear_screen()
        if curr_round == max_round:
            print("Announcer: And now for the final round!\n")
            input("(Press enter to continue...)")
            globals.clear_screen()
            print("On the left side, an up and coming fighter hailing from your hometown of %s, please welcome %s!\n" %
                (globals.this_player.home, this_player))
        else:
            print("Announcer: On the left side, hailing from your hometown of %s, please welcome %s!\n" %
                (globals.this_player.home, this_player))
        input("(Press enter to continue...)")
        globals.clear_screen()
        print("And, on the right side, please welcome one of the strongest fighters in all of Nira, %s!\n" %
              player_battle_participants[1])
        input("(Press enter to continue...)")
        globals.clear_screen()
        if curr_round == max_round:
            print("Let the final battle begin!\n")
        else:
            print("Let the battle begin!\n")
        input("(Press enter to continue...)")
        globals.clear_screen()

    def execute_round():
        """
        Executes the current round.
        """
        nonlocal tourney_participants

        def yield_matches(num_matches, participants):
            """
            Generator function that yields the matches in each round.
            :param num_matches: The number of matches in each round.
            :param participants: A list of the round's participants.
            """
            for match in range(num_matches):
                yield match+1, participants[2*match], participants[2*match+1]

        def show_round_results():
            """
            Shows the results of the round after the conclusion of each round.
            """
            globals.clear_screen()
            print("ROUND RESULTS\n")
            for match_num, part1, part2 in yield_matches(num_matches, tourney_participants):
                print("Match %s" % match_num)
                if part1 not in eliminated:
                    print("%s defeated %s.\n" % (part1, part2))
                else:
                    print("%s defeated %s.\n" % (part2, part1))
            input("(Press enter to proceed...)")
            globals.clear_screen()

        eliminated = []
        if this_player in tourney_participants:
            curr = battle.Battle(enemy_name=this_battle_participants[1], type="boss")
            try:
                curr.do_battle()
            except globals.GameOver:
                globals.clear_screen()
                eliminated.append(this_player)
                print(Fore.RED + "You have lost the battle and have been eliminated from the tournament!\n")
                input("(Press enter to continue...)")
            else:
                eliminated.append(this_battle_participants[1])
            start = 1
        else:
            start = 0

        num_matches = int(len(tourney_participants) / 2)
        for match in range(start, num_matches):
            curr_match = [tourney_participants[2*match], tourney_participants[2*match+1]]
            winner = random.choice(curr_match)
            for participant in curr_match:
                if participant != winner:
                    eliminated.append(participant)

        show_round_results()
        tourney_participants = [participant for participant in tourney_participants if participant not in eliminated]

    # Give the player a second choice at proceeding
    answer = opening()

    if answer == 'n':
        print("On second thought, you'd rather save your energy for some other endeavor. Accordingly, you run out "
              "of the arena as fast as you can.\n")
        input("(Press enter to return to Center Square...)")
        globals.clear_screen()
        return

    if globals.this_player.current_weapon is None:
        print("However, as you walk toward the registration booth, you're hit with the sudden realization that you don't "
              "own a weapon.\n\nHow are you going to fight without a weapon?\n\n"
              "Accordingly, you sulk out of the arena and back into the city.\n")
        input("(Press enter to return to Center Square...)")
        return

    # Establish tournament participants
    tourney_participants = random.sample(globals.arena_enemy_names, 7)
    random.shuffle(tourney_participants)
    this_player = globals.this_player.name
    tourney_participants.insert(0, this_player)

    # Keep simulating the tournament until we have only one participant left
    curr_round = 0
    max_round = 3
    while len(tourney_participants) > 1:
        curr_round += 1
        display_round_matches(tourney_participants)
        if this_player in tourney_participants:
            this_battle_participants = [tourney_participants[0], tourney_participants[1]]
            battle_intro(this_battle_participants)
        execute_round()

    # Award player $25 for winning, else nothing
    globals.clear_screen()
    if tourney_participants[0] == this_player:
        print("You have won the tournament! Congratulations!\n")
        print("As your prize, you have been awarded $25!\n")
        globals.this_player.money += 25
    else:
        print("%s went on to win the tournament.\n" % tourney_participants[0])
        print("Better luck next time.\n")

    input("(Press enter to return to Center Square...)")

def battle_practice():
    """
    Function to initiate the battle practice mechanic. The mechanic itself is handled by the battle class, which is
    notified of the dummy battle using the "dummy" custom parameter. Player faces off against a dummy with infinite
    health. Each hit on the dummy nets the player 0.1 XP. XP is awarded when the player leaves battle practice.
    """
    print("You decide to go to the Battle Practice Area. You could always get stronger, and practice makes perfect, "
          "right?\n")
    print("Alas, the only way to train here is to whack on a dummy until you get bored. Seriously. These dummys "
          "don't even award a lot of XP. Might as well go and fight a bunch of aliens...\n")
    print("But you're here, so you ultimately decide to fulfill your destiny and whack on a dummy until you get bored.\n")
    input("(Press enter to start whacking...)")
    globals.clear_screen()

    if globals.this_player.current_weapon is None:
        print("Alas, you realize that you don't have a weapon to whack the dummy with.\n\n"
              "Faced with no way around this predicament, you have no choice but to leave the Battle Practice Area and "
              "hope that you get a weapon by some gracious act of war.\n")
        input("(Press enter to return to Center Square...)")
        return

    curr = battle.Battle(custom_parameters="dummy")
    curr.do_battle()


def roulette():
    """
    Function for the roulette minigame.
    """

    class RouletteExit(Exception):
        """
        An empty exception to indicate that the player has elected to leave the minigame.
        """
        pass

    def opening():
        """
        The intro sequence to the roulette minigame.
        """
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
        """
        Returns list representations of the various groups of numbers on the roulette board.
        """
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
        reds = ['1','3','5','7','9','12','14','16','18','21','23','25','27','28','30','32','34','36']
        blacks = ['2','4','6','8','10','11','13','15','17','19','20','22','24','26','29','31','33','35']
        evens = ['2','4','6','8','10','12','14','16','18','20','22','24','26','28','30','32','34','36']
        odds = ['1','3','5','7','9','11','13','15','17','19','21','23','25','27','29','31','33','35']
        first_half = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
        second_half = ['19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']
        first_dozen = ['1','2','3','4','5','6','7','8','9','10','11','12']
        second_dozen = ['13','14','15','16','17','18','19','20','21','22','23','24']
        third_dozen = ['25','26','27','28','29','30','31','32','33','34','35','36']
        return board_rows, board_columns, reds, blacks, evens, odds, first_half, second_half, first_dozen, second_dozen, third_dozen

    def main_header():
        """
        The header shown on the main roulette menu.
        """
        print("ROULETTE")
        print("Game Type: %s" % game_type)
        print("Your money: $%.2f" % float(globals.this_player.money))
        print("Minimum Bet: $%s" % min_bet)
        print("Maximum Bet: $%s\n" % max_bet)

    def choose_bet():
        """
        Prints the list of available bets and returns the player's desired choice.
        """
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
        """
        The header shown on the bet screen.
        :param bet_type: The name of the bet being played.
        :param payoff: The payoff of this bet.
        """
        print("ROULETTE: %s" % bet_type)
        print("Payoff: %s:1" % str(payoff))
        print("Your money: $%.2f" % float(globals.this_player.money))
        print("Minimum Bet: $%s" % min_bet)
        print("Maximum Bet: $%s\n" % max_bet)

    def get_wager():
        """
        Receives and validates the player's wager.
        """
        wager = input("Please enter your wager, enter 'q' if you wish to turn back: $")
        while True:
            try:
                if wager == 'q':
                    return wager
                wager = float(wager)
            except ValueError:
                wager = input("You have entered an invalid amount. Please try again: $")
                continue
            else:
                if wager > globals.this_player.money:
                    wager = input("You do not have enough money. Please enter a new wager: $")
                    continue
                if wager < min_bet or wager > max_bet:
                    wager = input("Your wager must be within the bounds of the house's minimum and maximum bets.\n"
                                  "Please try again: $")
                    continue
                break
        return wager

    def determine_function(choice):
        """
        Determines the bet function to be executed considering the player's choice.
        :param choice: The player's choice.
        """
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
        """
        The main roulette loop. We leave when the RouletteExit or KeyboardInterrupt exception is raised.

        NOTE: Tkinter interferes with the main game loop's handling of the KeyboardInterrupt exception. As a result,
        we have to handle the exception directly in the roulette game loop.
        """
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
            except KeyboardInterrupt:
                globals.clear_screen()
                layout_ref.destroy()
                exit.force_exit_program()
            else:
                try:
                    bet = determine_function(choice)
                    winnings = bet()
                    net_winnings += winnings
                    globals.clear_screen()
                except KeyboardInterrupt:
                    globals.clear_screen()
                    layout_ref.destroy()
                    exit.force_exit_program()

    # Bet functions. All bet functions return the player's net winnings.
    def straight_up():
        """
        Bet where the player bets on exactly one number on the roulette board.
        Payoff - 35:1
        """
        bet_type = "Straight Up"
        payoff = 35
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()

        if wager == 'q':
            return earning

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
        else:
            print("Amazing! How on Nira did you do that?!")
            winnings = wager * payoff
            print("You won $%.2f!\n" % winnings)
            globals.this_player.money += winnings
            earning += winnings
        input("(Press enter to continue...)")
        return earning

    def split_bet():
        """
        Bet where the player bets on two numbers that are adjacent to each other on the roulette board.
        Payoff - 17:1
        """
        bet_type = "Split Bet"
        payoff = 17
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()

        if wager == 'q':
            return earning

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
        else:
            winnings = wager * payoff
            print("Awesome! You won $%.2f!\n" % winnings)
            globals.this_player.money += winnings
            earning += winnings
        input("(Press enter to continue...)")
        return earning

    def street_bet():
        """
        Bet where the player bets on a row of three numbers on the roulette board.
        Payoff - 11:1
        """
        bet_type = "Street Bet"
        payoff = 11
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()

        if wager == 'q':
            return earning

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
        else:
            winnings = wager * payoff
            print("Awesome! You won $%.2f!\n" % winnings)
            globals.this_player.money += winnings
            earning += winnings
        input("(Press enter to continue...)")
        return earning

    def double_street():
        """
        Bet where the player bets on two rows of three numbers, that are adjacent to each other on the roulette board.
        Payoff - 5:1
        """
        bet_type = "Double Street"
        payoff = 5
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()

        if wager == 'q':
            return earning

        globals.this_player.money -= wager
        earning -= wager
        inp = input("Please select the first row of numbers you would like to bet on.\n"
                    "Here, a 'row' is a row of three consecutive numbers on the roulette board.\n"
                    "For example, row 1 would be [1,2,3] and so on.\n\n"
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
        else:
            winnings = wager * payoff
            print("Awesome! You won $%.2f!\n" % winnings)
            globals.this_player.money += winnings
            earning += winnings
        input("(Press enter to continue...)")
        return earning

    def basket():
        """
        Bet where the player bets on the top pocket of numbers on the roulette board:
        [0,1,2,3] (and 00 if playing American Roulette). Commonly considered the worst bet in roulette.
        Payoff - 6:1
        """
        bet_type = "Basket"
        payoff = 6
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()

        if wager == 'q':
            return earning

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
        else:
            winnings = wager * payoff
            print("Awesome! You won $%.2f!\n" % winnings)
            globals.this_player.money += winnings
            earning += winnings
        input("(Press enter to continue...)")
        return earning

    def halves():
        """
        Bet where the player bets on either the first (1-18) or second (19-36) half of numbers on the roulette board.
        Payoff - 1:1
        """
        bet_type = "Halves"
        payoff = 1
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()

        if wager == 'q':
            return earning

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
        else:
            winnings = wager * payoff
            print("Awesome! You won $%.2f!\n" % winnings)
            globals.this_player.money += winnings
            earning += winnings
        input("(Press enter to continue...)")
        return earning

    def bet_color_red():
        """
        Bet where the player bets on all of the numbers that are in red squares on the roulette board.
        Payoff - 1:1
        """
        bet_type = "All Reds"
        payoff = 1
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()

        if wager == 'q':
            return earning

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
        else:
            winnings = wager * payoff
            print("Awesome! You won $%.2f!\n" % winnings)
            globals.this_player.money += winnings
            earning += winnings
        input("(Press enter to continue...)")
        return earning

    def bet_color_black():
        """
        Bet where the player bets on all of the numbers that are in black squares on the roulette board.
        Payoff - 1:1
        """
        bet_type = "All Blacks"
        payoff = 1
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()

        if wager == 'q':
            return earning

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
        else:
            winnings = wager * payoff
            print("Awesome! You won $%.2f!\n" % winnings)
            globals.this_player.money += winnings
            earning += winnings
        input("(Press enter to continue...)")
        return earning

    def bet_odd():
        """
        Bet where the player bets on all of the odd numbers on the roulette board.
        Payoff - 1:1
        """
        bet_type = "All Odds"
        payoff = 1
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()

        if wager == 'q':
            return earning

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
        else:
            winnings = wager * payoff
            print("Awesome! You won $%.2f!\n" % winnings)
            globals.this_player.money += winnings
            earning += winnings
        input("(Press enter to continue...)")
        return earning

    def bet_even():
        """
        Bet where the player bets on all of the even numbers on the roulette board.
        Payoff - 1:1
        """
        bet_type = "All Evens"
        payoff = 1
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()

        if wager == 'q':
            return earning

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
        else:
            winnings = wager * payoff
            print("Awesome! You won $%.2f!\n" % winnings)
            globals.this_player.money += winnings
            earning += winnings
        input("(Press enter to continue...)")
        return earning

    def dozens():
        """
        Bet where the player bets on one of the three dozens of numbers on the roulette board: [1-12, 13-24, 25-36].
        Payoff - 2:1
        """
        bet_type = "Dozens"
        payoff = 2
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()

        if wager == 'q':
            return earning

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
        else:
            winnings = wager * payoff
            print("Awesome! You won $%.2f!\n" % winnings)
            globals.this_player.money += winnings
            earning += winnings
        input("(Press enter to continue...)")
        return earning

    def column():
        """
        Bet where the player bets on one of the three columns of the roulette board.
        Payoff - 2:1
        """
        bet_type = "Columns"
        payoff = 2
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()

        if wager == 'q':
            return earning

        globals.this_player.money -= wager
        earning -= wager
        print("Columns:\n"
              "\t1. First Column\n"
              "\t2. Second Column\n"
              "\t3. Third Column\n")
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
        else:
            winnings = wager * payoff
            print("Awesome! You won $%.2f!\n" % winnings)
            globals.this_player.money += winnings
            earning += winnings
        input("(Press enter to continue...)")
        return earning
    # END bet functions

    # Set house min and max bets to arbitrary numbers.
    min_bet = 3
    max_bet = 15
    net_winnings = 0

    # Receive player's opening choice.
    this_type = opening()

    # Determine if player actually has enough money to participate
    if globals.this_player.money < min_bet:
        print("Unfortunately, the only way to throw away your money is to actually have some money.\n\n"
              "Thus, you have no choice but to leave.\n")
        input("(Press enter to return to Center Square...)")
        return

    # Set game type
    if this_type == '1':
        game_type = "American Roulette"
    else:
        game_type = "European Roulette"

    roulette_choices = [str(x) for x in range(0,37)]
    # American Roulette has an extra number on the board.
    if this_type == '1':
        roulette_choices.append('00')

    # Set up roulette board row and column list representations as well as various groups.
    roulette_board_rows, roulette_board_columns, reds, blacks, evens, odds, first_half, second_half, first_dozen, second_dozen, third_dozen = init_roulette_board()

    # initialize layout reference GUI.
    layout_ref = tkinter.Tk()
    title = "%s: Board Layout" % game_type
    layout_ref.wm_title(title)
    layout_ref.geometry('{}x{}'.format(707, 300))
    image_name = "%s.gif" % game_type
    layout_image = tkinter.PhotoImage(file=image_name)
    new_image = layout_image.subsample(2, 2)
    canvas = tkinter.Canvas()
    canvas.create_image(0, 0, anchor='nw', image=new_image)
    canvas.pack(fill='both', expand='yes')
    layout_ref.after(0, game_loop)
    layout_ref.mainloop()

    # Give player overview of net earnings
    if net_winnings < 0:
        print("Counting all of the rounds you played today, you ended up losing a total of $%.2f.\n" % abs(net_winnings))
    elif net_winnings == 0:
        print("Counting all of the rounds you played, you ended up neither gaining nor losing money!\n")
    else:
        print("Counting all of the rounds you played today, you ended up gaining a total of $%.2f.\n" % abs(net_winnings))
    input("(Press enter to return to Center Square...)")

if __name__ == "__main__":
    print("To play this game, run 'launch.py'.\n"
          "For more information about this file, see 'readme.txt'.")