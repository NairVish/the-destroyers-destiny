__author__ = 'vishnunair'
import globals

class Cell():
    def __init__(self, num_cell):
        self.enemy = ""
        self.loot = ""
        self.property = self.determineProperty()
        self.number = num_cell

    def determineProperty(self):
        pass
        # TODO write the selection function.


class Dungeon():
    def __init__(self, init_name, init_length, main_quest=False):
        self.name = init_name
        self.total_cells = init_length
        self.current_cell_num = 1
        self.cell = Cell(self.current_cell_num)
        self.main_quest_flag = main_quest

    def __repr__(self):
        return self.name

    def advance(self):
        self.current_cell_num += 1

        del self.cell

        if self.current_cell_num == self.total_cells:
            self.cell = Cell(self.current_cell_num)
        else:
            pass

    def wait_for_cell_action(self):
        if self.cell.enemy is not None and self.cell.loot is None:
            pass
            # TODO pass self.cell.enemy to battle mechanic
        elif self.cell.loot is not None and self.cell.enemy is None:
            pass
            # TODO Modified version of standby dungeon screen but also showing loot and option to accept.
            # show loot on screen and add to inventory if selected
        else:
            pass
            # TODO stay on current cell and do nothing, simply showing stats

    def show_status(self):
        print(self)
        print('You are currently on cell %s of %d.' % (self.current_cell_num, self.total_cells))
        print("Current Health: %s of %d" % (globals.this_player.current_health, globals.this_player.total_health))

def traverse_dungeon():
    pass
    # TODO how do we traverse our dungeon?