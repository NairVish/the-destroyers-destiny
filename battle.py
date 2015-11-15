"""
Contains definitions for the enemy and battle classes.
Handles all activities related to the battle mechanic.
"""

__author__ = 'Vishnu Nair'

from random import randrange
from colorama import Fore, init

import globals

init(autoreset=True)

class Enemy:
    """
    The Enemy class holds all the data for the enemy in a battle.
    """
    def __init__(self, enemy_name, enemy_type):
        """
        :param enemy_name: The enemy's name.
        :param enemy_type: The enemy type (bandit, looter, mobster, valstr).
        Initializes the enemy and its attributes.
        """
        self.enemy_name = enemy_name
        self.enemy_type = enemy_type
        self.level = self.determine_enemy_level()
        self.attack = self.level
        self.defense = self.attack+1
        self.health = self.determine_health()
        self.max_health = self.health

    def determine_enemy_level(self):
        """
        Determines and returns the enemy's level. Regular enemies are half a level below the player, while boss levels
        equal that of the player.
        """
        if self.enemy_type is "reg":
            return globals.this_player.level-0.5
        elif self.enemy_type is "boss":
            return globals.this_player.level

    def determine_health(self):
        """
        Determines and returns the enemy's health. Regular enemies have half the player's health; bosses
        have 95% of the player's health.
        """
        if self.enemy_type is "reg":
            return int(globals.this_player.total_health*0.5)
        else:
            return int(globals.this_player.total_health*0.95)


class Battle:
    """
    The Battle class holds all data for and executes the battle mechanic.
    """
    def __init__(self, enemy_name, type="reg"):
        """
        :param enemy_name: The name of the enemy (for the enemy's __init__ function).
        :param type: The type of the enemy ((for the enemy's __init__ function).
        Initialized a battle with an enemy. Also, determines possible XP gained from the battle as well
        as the player's max health.
        """
        self.enemy = Enemy(enemy_name, type)
        self.possible_xp = int(self.enemy.level) + 3
        # NOTE: player health is globals.this_player.current_health
        self.p_max_health = globals.this_player.total_health

    def do_battle(self):
        """
        Executes the battle sequence until either the player or the enemy runs out of health. If the player runs
        out of health, the GameOver exception is raised. Else, the battle is ended, and XP is awarded.
        """
        while globals.this_player.current_health > 0 and self.enemy.health > 0:
            self.show_status()
            self.execute_move()
        globals.clear_screen()
        if globals.this_player.current_health <= 0:
            print(Fore.RED + "You have no health remaining! "
                  "You have whited out.")
            raise globals.GameOver()
        else:
            globals.this_player.current_health = globals.this_player.total_health
            print(Fore.GREEN + "You have defeated your enemy and have gained %s XP!" % self.possible_xp)
            globals.this_player.xp += self.possible_xp
            if globals.this_player.xp > globals.this_player.target_xp:
                globals.this_player.level_up()
            input("(Press enter to continue...)")
            globals.clear_screen()
            return

    def show_status(self):
        """
        Prints the battle's current status.
        """
        print("BATTLE WITH %s" % self.enemy.enemy_name.upper())
        print("Your health: %.1f/%s" % (globals.this_player.current_health, self.p_max_health))
        print("Enemy health: %.1f/%s" % (self.enemy.health, self.enemy.max_health))

    def execute_move(self):
        """
        Determines damage cast by the player to the enemy using a (frankly overly complex) formula and deducts from
        the enemy's health and vice versa. If the the player's assistant flag is set to True, there is a small (10%)
        chance that the assistant will attack too. If the skip flag is True, the player's turn is skipped.
        """
        skip = self.show_menu()
        globals.clear_screen()
        if skip is True:
            print(Fore.RED + "You lost your turn because you used a potion!")
        else:
            p_damage = globals.this_player.attack + globals.this_player.current_weapon.power - (self.enemy.defense * 0.5)
            print(Fore.GREEN + "You dealt %.1f damage to the enemy!" % p_damage)
            self.enemy.health -= p_damage

        if globals.this_player.assistant is True:
            prob = randrange(0,100)
            if prob in range(0,10):
                a_damage = (globals.this_player.attack + globals.this_player.current_weapon.power - (self.enemy.defense * 0.5))/4
                self.enemy.health -= a_damage
                print(Fore.GREEN + "Merlona dealt %.1f damage to the enemy!" % a_damage)
        if self.enemy.health <= 0:
            return

        e_damage = self.enemy.attack
        print(Fore.RED + "The enemy dealt %.1f damage to you!\n" % e_damage)
        globals.this_player.current_health -= e_damage


    def show_menu(self):
        """
        Accepts and executes the player's desired action on the main battle screen. Returns True if the player uses a potion
        (from their inventory). Returns False in all other situations.
        """
        self.show_options()
        inp = input("Choose an option: ")

        while inp != '1':
            try:
                inp = int(inp)
            except ValueError:
                inp = input("You have entered an invalid option. Please enter a valid option: ")
                continue
            else:
                if inp is 2:
                    globals.clear_screen()
                    old_length = len(globals.this_player.inventory)
                    globals.this_player.use_potion()
                    new_length = len(globals.this_player.inventory)
                    if old_length != new_length:
                        return True
                elif inp is 3:
                    globals.clear_screen()
                    globals.this_player.equip_weapon()
                elif inp is 4:
                    globals.this_player.print_stats()
                else:
                    inp = input("You have entered an invalid option. Please enter a valid option: ")
                    continue
                self.show_status()
                self.show_options()
                inp = input("Choose an option: ")
        return False

    def show_options(self):
        """
        Prints the battle screen menu.
        """
        print("Battle Menu:\n"
              "\t1. Attack!\n"
              "\t2. Use health item (lose turn).\n"
              "\t3. Switch weapon (will not lose turn).\n"
              "\t4. Show your stats (will not lose turn).\n")

if __name__ == "__main__":
    print("To play this game, run 'start_here.py.'.\n"
          "For more information about this file, see 'readme.txt'.")