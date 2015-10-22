__author__ = 'vishnunair'
import globals
import battle
from globals import clear_screen
from random import randrange, choice

class Cell():
    def __init__(self, name, num_cell, enemy_type, final=False):
        self.number = num_cell
        self.name = name
        self.enemy_type = enemy_type
        self.final = final
        if final:
            self.enemy_selector()
            self.loot = None
        else:
            self.determineProperty()

    def determineProperty(self):
        result = randrange(0,100)
        if result in range(0,10):
            self.enemy = None
            self.loot = None
        elif result in range(20,40):
            self.enemy = None
            self.loot = self.loot_selector()
        elif result in range(40,100):
            self.enemy = self.enemy_selector()
            self.loot = None

    def loot_selector(self):
        return choice(globals.loot_names)

    def enemy_selector(self):
        if self.final is True and self.enemy_type is "valstr":
            boss_index = globals.main_quest_dungeons.index(self.name)
            return globals.main_quest_bosses[boss_index]
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


class Dungeon():
    def __init__(self, init_name, init_length, enemy_type, main_quest=False):
        globals.clear_screen()
        self.name = init_name
        self.total_cells = init_length
        self.enemy_type = enemy_type
        self.current_cell_num = 1
        self.cell = Cell(self.name, self.current_cell_num, self.enemy_type)
        self.main_quest_flag = main_quest

    def __repr__(self):
        return self.name

    def advance(self):
        self.current_cell_num += 1

        del self.cell

        if self.current_cell_num < self.total_cells:
            return Cell(self.current_cell_num, self.name, self.enemy_type)
        elif self.current_cell_num is self.total_cells:
            return Cell(self.current_cell_num, self.name, self.enemy_type, final=True)
        else:
            return None

    def execute_cell_action(self):
        if self.cell.enemy is not None and self.cell.loot is None:
            if self.cell.final is True:
                this_battle = battle.battle(self.cell.enemy, "boss")
            else:
                this_battle = battle.battle(self.cell.enemy)
            try:
                this_battle.do_battle()
            except globals.GameOver():
                pass # TODO: implement game over
        elif self.cell.loot is not None and self.cell.enemy is None:
            print("You've found the following loot: %s" % self.cell.loot)
            inp = input("Would you like to add it to your inventory?\n"
                        "You can sell it later for some more money. (y/n) ")
            accepted_answers = ['y','n']
            while inp not in accepted_answers:
                inp = input("You have entered an invalid option. Please try again: ")
            if inp is 'y':
                globals.this_player.inventory.append(self.cell.loot)
                print("\n%s added to your inventory!\n" % self.cell.loot)
            else:
                print("\n%s was NOT added to your inventory!\n" % self.cell.loot)

            self.show_menu()
        else:
            print("There's nothing in this cell...\n")
            self.show_menu()

    def show_status(self):
        print(self.__repr__().upper())
        print("You are currently in cell %s of %d.\n" % (self.current_cell_num, self.total_cells))

    def show_menu(self):
        print("\ta. Advance.")
        print("\t1. Show current stats.")
        print("\t2. Use a potion.")
        print("\t3. Switch weapon.")

        inp = input("\nChoose an option: ")

        while inp is not 'a':
            try:
                inp = int(inp)
            except ValueError:
                inp = input("You have entered an invalid option. Please enter a valid option: ")
                continue
            else:
                if inp not in range(1,4):
                    inp = input("You have entered an invalid option. Please enter a valid option: ")
                    continue
                if inp is 1:
                    clear_screen()
                    globals.this_player.print_stats()
                elif inp is 2:
                    clear_screen()
                    globals.this_player.use_potion(enhancement=True)
                elif inp is 3:
                    clear_screen()
                    globals.this_player.equip_weapon()
            inp = input("\nChoose an option: ")

    def traverse_dungeon(self):
        while self.current_cell_num <= self.total_cells:
            if self.cell is None:
                return
            self.show_status()
            self.execute_cell_action()
            self.cell = self.advance()

    def monitor_main_quest(self):
        pass
        # TODO: monitor main quest