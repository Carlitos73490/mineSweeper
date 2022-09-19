from enum import Enum
from classes.grid import Grid


class ActionTitle(Enum):
    OPEN = "Ouvrir la case"
    FLAG = "Flagger la case"


class Minesweeper:

    def __init__(self):
        self.action_splits = None
        self.is_playing = False
        self.grid = None

    def actions_listener(self):
        self.action_splits = input("{action} x y : " if self.is_playing else "Nouvelle partie : ").split()

        if self.action_splits[0] == "newgame":
           self._newgame()
        elif not self.is_playing :
            raise Exception("Game not launched : newgame")
        elif self.action_splits[0] == "F":
            self._flagg()
        elif len(self.action_splits) == 2:
            self._open()
        elif self.action_splits[0] == "quit":
            self._quit()
        else:
            raise Exception("Unrecognized input")

            self.is_playing = not self.is_win and not self.is_lost

    def _open(self):

        if self.grid.is_win() or self.grid.is_lost():
            raise Exception("la partie est terminé relancez en une avec : newgame ")

        print(ActionTitle.OPEN.value,
              " ",
              self.action_splits[0],
              ",",
              self.action_splits[1])
        self.grid.open(int(self.action_splits[0]),
                       int(self.action_splits[1]))

    def _flagg(self):
        print(ActionTitle.FLAG.value,
              " ",
              self.action_splits[1],
              ",",
              self.action_splits[2])
        self.grid.toggle_flag(int(self.action_splits[1]),
                              int(self.action_splits[2]))
    def _newgame(self):
        print("Début de la partie")
        self.is_playing = True
        self.grid = Grid(self.grid_dimension)

    def _quit(self):
        print("Fin de la partie")
        self.is_playing = False