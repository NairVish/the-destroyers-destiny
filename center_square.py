import globals
import tkinter
from time import sleep
from random import choice

def battle_arena():
    pass


def battle_practice():
    pass


def roulette():
    globals.clear_screen()

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
        inp = input("What type of game would you like to play? ")
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
              "\t2. Split Bet (bet on two adjoining numbers, 17:1)\n"
              "\t3. Street Bet (bet on one of the 12 rows, 11:1)\n"
              "\t4. Double Street (bet on two adjoining rows, 5:1)\n"
              "\t5. Basket (bet on one of 2 (or 3) special combos, 6:1)\n"
              "\t6. Top Line (bet on 0, 1, 2, and 3 (and 00 if American), 8:1)\n"
              "\t7. Halves (bet on 1-18 or 18-36, 1:1)\n"
              "\t8. All Reds (bet on all reds, 1:1)\n"
              "\t9. All Blacks (bet on all blacks, 1:1)\n"
              "\t10. All Odds (bet on all odds, 1:1)\n"
              "\t11. All Evens (bet on all evens, 1:1)\n"
              "\t12. Dozens Bet (bet on consecutive dozen, 2:1)\n"
              "\t13. Columns Bet (bet on one of the three vertical columns, 2:1)\n")
        inp = input("Enter the number of the bet you would like to make, else enter 'q' to leave: ")
        accepted_answers = [str(x) for x in range(0,14)]
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
        wager = input("Please enter your wager: ")
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
            return top_line
        elif choice == '7':
            return halves
        elif choice == '8':
            return bet_color_red
        elif choice == '9':
            return bet_color_black
        elif choice == '10':
            return bet_odd
        elif choice == '11':
            return bet_even
        elif choice == '12':
            return dozens
        elif choice == '13':
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
        pass

    def street_bet():
        bet_type = "Street Bet"
        payoff = 11
        pass

    def double_street():
        bet_type = "Double Street"
        payoff = 5
        pass

    def basket():
        bet_type = "Basket"
        payoff = 6
        pass

    def top_line():
        bet_type = "Top Line"
        payoff = 8
        pass

    def halves():
        bet_type = "Halves"
        payoff = 1
        pass

    def bet_color_red():
        bet_type = "All Reds"
        payoff = 1
        pass

    def bet_color_black():
        bet_type = "All Blacks"
        payoff = 1
        pass

    def bet_odd():
        bet_type = "All Odds"
        payoff = 1
        earning = 0
        bet_header(bet_type, payoff)
        wager = get_wager()
        globals.this_player.money -= wager
        earning -= wager
        your_choice = ['1','3','5','7','9','11','13','15','17','19','21','23','25','27','29','31','33','35']
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
        your_choice = ['2','4','6','8','10','12','14','16','18','20','22','24','26','28','30','32','34','36']
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
        pass

    def column():
        bet_type = "Columns"
        payoff = 2
        pass

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

    roulette_board_rows, roulette_board_columns = init_roulette_board()
    reds = ['1','3','5','7','9','12','14','16','18','21','23','25','27','28','30','32','34','36']
    blacks = ['2','4','6','8','10','11','13','15','17','19','20','22','24','26','29','31','33','35']

    # initialize layout reference GUI
    layout_ref = tkinter.Tk()
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