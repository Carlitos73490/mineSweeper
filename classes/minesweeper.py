from enum import Enum


class action_title(Enum):
    OPEN = "Ouvrir la case"
    FLAG = "Flagger la case"


class Minesweeper:
    grid_dimension = None
    action_splits = None
    is_playing = False


    def new_game(self,grid_dimension):
        self.is_playing = True
        self.grid_dimension = grid_dimension
        while self.is_playing:
            print("Début de la sélection")
            self.splits = input("{action} x y : ").split()
            self.actions()
    def quit(self):
        self.is_playing = False
    def actions(self):
        if self.action_split[0] == "F":
            self.flag()
        elif self.action_split[0] == "Q":
            self.quit()
        else:
            self.open()

    def open(self):
        print(action_title.FLAG.value, " ", self.action_split[1], ",", self.action_split[2])

    def flag(self):
        print(action_title.OPEN.value, " ", self.action_split[0], ",", self.action_split[1])
