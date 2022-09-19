from enum import Enum
from classes.grid import Grid


class ActionTitle(Enum):
    OPEN = "Ouvrir la case"
    FLAG = "Flagger la case"


class Minesweeper:
    def __init__(self):
        pass

    grid = None
    is_playing = False
    is_lost = False
    is_win = False

    def actions_listener(self):
        self.action_splits = input("{action} x y : ").split()

        if not self.is_playing:
            if self.action_splits[0] == "newgame":
                # New Game
                print("Début de la partie")
                self.is_playing = True
                self.grid = Grid(self.grid_dimension)
            else:
                raise Exception("Launch game with command newgame")
        elif self.is_playing:

            if self.action_splits[0] == "F":
                # Flag
                print(ActionTitle.FLAG.value,
                      " ",
                      self.action_splits[1],
                      ",",
                      self.action_splits[2])
                self.grid.toggle_flag(int(self.action_splits[1]),
                                      int(self.action_splits[2]))
            elif len(self.action_splits) == 2:
                # Open
                print(ActionTitle.OPEN.value,
                      " ",
                      self.action_splits[0],
                      ",",
                      self.action_splits[1])
                self.grid.open(int(self.action_splits[0]),
                               int(self.action_splits[1]))
            elif self.action_splits[0] == "quit":
                # Quit
                print("Fin de la partie")
                self.is_playing = False
            else:
                raise Exception("Unrecognized input")
            self.is_win = self.grid.is_win
            self.is_lost = self.grid.is_lost
            self.is_playing = not self.is_win and not self.is_lost
