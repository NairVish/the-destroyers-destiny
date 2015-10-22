__author__ = 'vishnunair'
import globals
from random import randrange

class enemy():
    def __init__(self, enemy_name, enemy_type):
        self.enemy_name = enemy_name
        self.enemy_type = enemy_type
        self.level = self.determine_enemy_level()
        self.attack = self.level+0.5
        self.defense = self.attack+1
        self.health = self.determine_health()
        self.max_health = self.health

    def determine_enemy_level(self):
        if self.enemy_type is "reg":
            return globals.this_player.level*0.5
        elif self.enemy_type is "boss":
            return globals.this_player.level*0.95

    def determine_health(self):
        if self.enemy_type is "reg":
            return int(globals.this_player.health*0.5)
        else:
            return int(globals.this_player.health*0.95)

class battle():
    def __init__(self, enemy_name, type="reg"):   # regular ("reg") or boss ("boss") enemy
        self.enemy = enemy(enemy_name, type)
        self.possible_xp = int(self.enemy.level)
        self.p_health = globals.this_player.health
        self.p_max_health = self.p_health

    def do_battle(self):
        while self.p_health > 0 and self.enemy.health > 0:
            self.show_status()
            self.execute_move()
        globals.clear_screen()
        if self.p_health <= 0:
            print("You have no health remaining!"
                  "You have whited out.")
            raise globals.GameOver()
        else:
            print("You have defeated your enemy and have gained %s XP!" % self.possible_xp)
            globals.this_player.xp += self.possible_xp
            if globals.this_player.xp > globals.this_player.target_xp:
                globals.this_player.level_up()
            return

    def show_status(self):
        print("BATTLE WITH %s" % self.enemy.enemy_name.upper())
        print("Your health: %s/%s" % (self.p_health, self.p_max_health))
        print("Enemy health: %s/%s" % (self.enemy.health, self.enemy.max_health))

    def execute_move(self):
        skip = self.show_menu()
        if skip is True:
            print("You lost your turn because you used a potion!")
        else:
            p_damage = globals.this_player.attack + globals.this_player.current_weapon.power - (self.enemy.defense * 0.5)
            print("You dealt %s of damage to the enemy!" % str(p_damage))
            self.enemy.health -= p_damage

        if globals.this_player.assistant is True:
            prob = randrange(0,100)
            if prob in range(0,10):
                a_damage = (globals.this_player.attack + globals.this_player.current_weapon.power - (self.enemy.defense * 0.5))/4
                self.enemy.health -= a_damage
                print("Merlona dealt %s damage to the enemy!" & a_damage)

        e_damage = self.enemy.attack
        print("The enemy dealt %s of damage to you!" % e_damage)
        self.p_health -= e_damage


    def show_menu(self):
        self.show_options()

        inp = input("Choose an option: ")

        while inp is not '1':
            try:
                inp = int(inp)
            except ValueError:
                inp = input("You have entered an invalid option. Please enter a valid option: ")
                continue
            else:
                if inp is 2:
                    globals.this_player.use_potion()
                    inp = '1'
                    return True
                elif inp is 3:
                    globals.this_player.equip_weapon()
                    self.show_options()
                elif inp is '4':
                    globals.this_player.print_stats()
                inp = input("Choose an option: ")
        return False

    def show_options(self):
        print("Battle Menu:\n"
              "\t1. Attack!\n"
              "\t2. Use health item (lose turn).\n"
              "\t3. Switch weapon (will not lose turn).\n"
              "\t4. Show your stats (will not lose turn).")