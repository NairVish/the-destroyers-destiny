"""
Contains definitions for the Cell and Dungeon classes.
Handles all activities related to the dungeon mechanic.
"""

__author__ = 'Vishnu Nair'

from random import randrange, choice

import battle
import globals


class Cell:
    """
    The Cell class holds all the information about the current cell in a dungeon.
    """

    def __init__(self, name, num_cell, enemy_type, final=False):
        """
        :param name: The name of the dungeon (used in some cases to determine the cell's enemy).
        :param num_cell: The cell number (in the dungeon).
        :param enemy_type: The type of the enemy (for enemy selector).
        :param final: Boolean value that says whether or not we are in the dungeon's final cell.
        Initializes the current cell's attributes. If this is the final cell, we go directly to the enemy selector.
        """
        self.number = num_cell
        self.name = name
        self.enemy_type = enemy_type
        self.final = final
        if final:
            self.enemy = self.enemy_selector()
            self.loot = None
        else:
            self.determine_property()

    def determine_property(self):
        """
        Determines whether the player will face an enemy, find loot, or encounter nothing in a cell.
        """
        result = randrange(0, 100)
        if result in range(0, 10):  # 10% chance for nothing.
            self.enemy = None
            self.loot = None
        elif result in range(20, 40):  # 20% chance for loot.
            self.enemy = None
            self.loot = self.loot_selector()
        else:  # 70% chance for enemy.
            self.enemy = self.enemy_selector()
            self.loot = None

    def loot_selector(self):
        """
        Returns a random piece of loot. There is a 5% chance of getting rare loot.
        """
        result = randrange(0, 100)
        if result in range(0, 5):
            return choice(globals.rare_loot_names)
        else:
            return choice(globals.loot_names)

    def enemy_selector(self):
        """
        Returns the name of the enemy. If the enemy type is "valstr" and final is True, matches the index of the
        dungeon's name in 'main_quest dungeons' with a boss name in 'main_quest_bosses.' If final is not True, chooses
        a random enemy from a list of enemies of that type. If final is just True, returns a specific boss name.
        """
        if self.final is True and self.enemy_type is "valstr":
            d_name = self.name[0:10]
            for dungeon in globals.main_quest_dungeons:
                if dungeon.startswith(d_name):
                    boss_index = globals.main_quest_dungeons.index(dungeon)
                    break
            return globals.main_quest_bosses[boss_index]
        elif self.enemy_type is "valstr":
            return choice(globals.main_quest_enemies)
        elif self.final is True:
            if self.enemy_type is "bandit":
                return "Bandit Chief"
            elif self.enemy_type is "looter":
                return "Lead Looter"
            elif self.enemy_type is "mobster":
                return "Master Mobster"
        else:
            if self.enemy_type is "bandit":
                return choice(globals.side_quest_enemies[0])
            elif self.enemy_type is "looter":
                return choice(globals.side_quest_enemies[1])
            elif self.enemy_type is "mobster":
                return choice(globals.side_quest_enemies[2])


class Dungeon:
    """
    The Dungeon class holds all the information about the current dungeon.
    """

    def __init__(self, init_name, init_length, enemy_type, main_quest=False):
        """
        :param init_name: The name of the dungeon.
        :param init_length: The length of the dungeon.
        :param enemy_type: The type of enemies in the dungeon.
        :param main_quest: Whether or not this dungeon is part of the main quest.
        Initializes a new dungron and its attributes. Also initializes the first cell.
        """
        globals.clear_screen()
        self.name = init_name
        self.total_cells = init_length
        self.enemy_type = enemy_type
        self.current_cell_num = 1
        self.cell = Cell(self.name, self.current_cell_num, self.enemy_type)
        self.main_quest_flag = main_quest

    def __repr__(self):
        """
        Printing 'self' or a dungeon object outputs the dungeon's name.
        """
        return self.name

    def advance(self):
        """
        Advances the player through the dungeon and calls the cell class's constructor (also with the final flag if
        final is True). If we are done with the dungeon, the None type is returned.
        """
        self.current_cell_num += 1

        del self.cell

        if self.current_cell_num < self.total_cells:
            return Cell(self.name, self.current_cell_num, self.enemy_type)
        elif self.current_cell_num == self.total_cells:
            return Cell(self.name, self.current_cell_num, self.enemy_type, final=True)
        else:
            return None

    def execute_cell_action(self):
        """
        Executes the appropriate cell action depending on the attributes of the current cell. Then, shows the
        dungeon menu once the action has been taken.
        """
        if self.cell.enemy is not None and self.cell.loot is None:
            if self.cell.final is True:
                this_battle = battle.Battle(self.cell.enemy, "boss")
            else:
                this_battle = battle.Battle(self.cell.enemy)
            try:
                this_battle.do_battle()
            except globals.GameOver:
                raise globals.GameOver()
            self.show_status()
        elif self.cell.loot is not None and self.cell.enemy is None:
            print("You've found the following loot: %s" % self.cell.loot)
            inp = input("Would you like to add it to your inventory?\n"
                        "You can sell it later for some more money. (y/n) ")
            accepted_answers = ['y', 'n']
            while inp not in accepted_answers:
                inp = input("You have entered an invalid option. Please try again: ")
            if inp is 'y':
                globals.this_player.inventory.append(self.cell.loot)
                print("\n%s was added to your inventory!\n" % self.cell.loot)
            else:
                print("\n%s was NOT added to your inventory!\n" % self.cell.loot)
        else:
            print("There's nothing in this cell...\n")

        self.show_menu()

    def show_status(self):
        """
        Prints the dungeon's current status: the name of the dungeon as well as the current cell number.
        """
        print(self.__repr__().upper())
        print("You are currently in cell %s of %d.\n" % (self.current_cell_num, self.total_cells))

    def show_menu(self):
        """
        Accepts and processes input from the dungeon menu.
        """

        def print_menu():
            """
            Prints out the dungeon menu and returns the player's input to the parent function.
            """
            print("\ta. Advance.")
            print("\t1. Show current stats.")
            print("\t2. Use a potion.")
            print("\t3. Switch weapon.\n")
            return input("Choose an option: ")

        inp = print_menu()

        if inp is 'a':
            globals.clear_screen()

        while inp is not 'a':
            try:
                inp = int(inp)
            except ValueError:
                inp = input("You have entered an invalid option. Please enter a valid option: ")
                continue
            else:
                if inp not in range(1, 4):
                    inp = input("You have entered an invalid option. Please enter a valid option: ")
                    continue
                if inp is 'a':
                    globals.clear_screen()
                    break
                if inp is 1:
                    globals.clear_screen()
                    globals.this_player.print_stats()
                elif inp is 2:
                    globals.clear_screen()
                    globals.this_player.use_potion(enhancement=True)
                elif inp is 3:
                    globals.clear_screen()
                    globals.this_player.equip_weapon()
            self.show_status()
            inp = print_menu()
            globals.clear_screen()

    def traverse_dungeon(self):
        """
        The loop that controls the player's progression through a dungeon.
        """
        while self.current_cell_num <= self.total_cells:
            if self.cell is None:
                return
            if self.main_quest_flag is True:
                self.monitor_main_quest()
            globals.clear_screen()
            self.show_status()
            self.execute_cell_action()
            self.cell = self.advance()

    def monitor_main_quest(self):
        """
        Only executed if the main quest flag for the dungeon is True. Controls main quest stage advancement, dialogue
        output, response handling, and response-to-stage jumps inside a dungeon. Works similarly to the main game loop
        in game.py.
        """
        if self.cell.final is True:
            globals.clear_screen()
            while globals.dialogue_type[globals.this_player.main_quest_stage] is not 'b':
                player_stage = globals.this_player.main_quest_stage
                curr = globals.dialogue_type[player_stage]
                if curr.startswith("c"):
                    print(globals.dialogue[player_stage] + '\n')
                    if globals.dialogue_jump_targets[globals.this_player.main_quest_stage] != 0:
                        globals.this_player.main_quest_stage = globals.dialogue_jump_targets[
                            globals.this_player.main_quest_stage]
                    else:
                        globals.this_player.main_quest_stage += 1
                elif curr.startswith("p"):
                    print(globals.dialogue[player_stage] + '\n')
                    input("(Press enter to continue...)")
                    globals.clear_screen()
                    if globals.dialogue_jump_targets[globals.this_player.main_quest_stage] != 0:
                        globals.this_player.main_quest_stage = globals.dialogue_jump_targets[
                            globals.this_player.main_quest_stage]
                    else:
                        globals.this_player.main_quest_stage += 1
                elif curr.startswith("rn"):
                    print(globals.dialogue[player_stage] + '\n')
                    print("[Enter the number of the response you would like to make:]")
                    i = 1
                    while globals.dialogue_type[player_stage + i] == 'r':
                        print('\t' + str(i) + '. ' + globals.dialogue[player_stage + i])
                        i += 1
                    selection = input("Selection: ")
                    while True:
                        try:
                            selection = int(selection)
                        except ValueError:
                            selection = input("You have entered an invalid option. Please try again: ")
                            continue
                        else:
                            if int(selection) > i or int(selection) <= 0:
                                selection = input("You have entered an invalid option. Please try again: ")
                                continue
                            break
                    globals.this_player.main_quest_stage += selection
                    globals.clear_screen()
                    print("You: " + globals.dialogue[globals.this_player.main_quest_stage] + '\n')
                    globals.this_player.main_quest_stage = globals.dialogue_jump_targets[
                        globals.this_player.main_quest_stage]
            print(globals.dialogue[globals.this_player.main_quest_stage] + '\n')
            if globals.dialogue_jump_targets[globals.this_player.main_quest_stage + 1] != 0:
                globals.this_player.main_quest_stage = globals.dialogue_jump_targets[
                                                           globals.this_player.main_quest_stage + 1] - 1
            input("(Press enter to continue...)")


if __name__ == "__main__":
    print("To play this game, run 'launch.py'.\n"
          "For more information about this file, see 'readme.txt'.")
