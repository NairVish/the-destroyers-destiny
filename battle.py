"""
Contains definitions for the enemy and battle classes.
Handles all activities related to the battle mechanic.
"""

__author__ = 'Vishnu Nair'

from random import randrange
from colorama import Fore, init
import math
import globals

init(autoreset=True)

class Enemy:
    """
    The Enemy class holds all the data for the enemy in a battle.
    """
    def __init__(self, enemy_name, enemy_type=None):
        """
        :param enemy_name: The enemy's name.
        :param enemy_type: The enemy type (bandit, looter, mobster, valstr).
        Initializes the enemy and its attributes.
        """
        if enemy_name == "An Innocent Dummy":
            self.enemy_name = enemy_name
            self.enemy_type = "dummy"
            self.level = 0
            self.attack = 0
            self.defense = 0
            self.health = math.inf
            self.max_health = math.inf
            return
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
    def __init__(self, enemy_name=None, type="reg", custom_parameters=None):
        """
        :param enemy_name: The name of the enemy (for the enemy's __init__ function).
        :param type: The type of the enemy (for the enemy's __init__ function).
        :param custom_parameters: An array of custom battle parameters.
        Initialized a battle with an enemy. Also, determines possible XP gained from the battle as well
        as the player's max health.
        """
        if custom_parameters is not None:
            if custom_parameters == 'dummy':
                self.enemy = Enemy(enemy_name="An Innocent Dummy")
                self.possible_xp = 0
                self.p_max_health = globals.this_player.total_health
                self.power_attack_used = False
                self.custom_param = custom_parameters
            elif custom_parameters == 'arena':
                pass
            return
        self.enemy = Enemy(enemy_name, type)
        self.possible_xp = int(self.enemy.level) + 3
        # NOTE: player health is globals.this_player.current_health
        self.p_max_health = globals.this_player.total_health
        self.power_attack_used = False
        self.custom_param = None

    def do_battle(self):
        """
        Executes the battle sequence until either the player or the enemy runs out of health. If the player runs
        out of health, the GameOver exception is raised. Else, the battle is ended, and XP is awarded.
        """
        while globals.this_player.current_health > 0 and self.enemy.health > 0:
            self.show_status()
            this = self.execute_move()
            if this == "dummy_exit":
                break
        globals.clear_screen()
        if globals.this_player.current_health <= 0:
            print(Fore.RED + "You have no health remaining! "
                  "You have whited out.")
            raise globals.GameOver()
        else:
            globals.this_player.current_health = globals.this_player.total_health
            if self.custom_param == "dummy":
                print(Fore.GREEN + "Through battle practice, you gained %.1f XP!\n" % self.possible_xp)
            else:
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
        if skip == "dummy_exit":
            return "dummy_exit"
        elif skip is True:
            print(Fore.RED + "You lost your turn because you used a potion!")
        else:
            p_damage = globals.this_player.attack + globals.this_player.current_weapon.power - (self.enemy.defense * 0.5)
            if skip is None:
                self.power_attack_used = True
                p_damage = p_damage * 1.25
                print(Fore.GREEN + "You dealt %.1f damage in a power attack to the enemy!" % p_damage)
            else:
                print(Fore.GREEN + "You dealt %.1f damage to the enemy!" % p_damage)
            self.enemy.health -= p_damage
            if self.custom_param == "dummy":
                self.possible_xp += 0.1

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
        (from their inventory). Returns False in a regular attack. Returns None if doing a power attack.
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
                    if self.power_attack_used is False:
                        return None
                    else:
                        inp = input("You cannot perform another power attack. Choose another option: ")
                        continue
                elif inp is 3:
                    globals.clear_screen()
                    old_length = len(globals.this_player.inventory)
                    globals.this_player.use_potion()
                    new_length = len(globals.this_player.inventory)
                    if old_length != new_length:
                        return True
                elif inp is 4:
                    globals.clear_screen()
                    globals.this_player.equip_weapon()
                elif inp is 5:
                    globals.this_player.print_stats()
                elif inp is 6 and self.custom_param == "dummy":
                    return "dummy_exit"
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
              "\t2. Power Attack! (performs 25% more damage, once per battle)\n"
              "\t3. Use health item (lose turn).\n"
              "\t4. Switch weapon (will not lose turn).\n"
              "\t5. Show your stats (will not lose turn).")
        if self.custom_param == "dummy":
            print("\t6. Leave Battle Practice\n")
        else:
            print("\n")

if __name__ == "__main__":
    print("To play this game, run 'start_here.py.'.\n"
          "For more information about this file, see 'readme.txt'.")