from enum import Enum


class ActionTitle(Enum):
    OPEN = "Ouvrir la case"
    FLAG = "Flagger la case"


class Minesweeper:
    grid_dimension = None
    action_splits = None
    is_playing = False


    def new_game(self):
        self.is_playing = True
        print("Début de la partie")
        #self.grid_dimension = grid_dimension
    def quit(self):
        self.is_playing = False
        print("Fin de la partie")


    def flag(self):
        print(ActionTitle.FLAG.value, " ", self.action_splits[1], ",", self.action_splits[2])

    def open(self):
        print(ActionTitle.OPEN.value, " ", self.action_splits[0], ",", self.action_splits[1])

    def actions_listener(self):
        if self.action_splits[0] == "newgame":
            self.new_game()
        elif not self.is_playing:
            raise Exception("Lauch game with command newgame")
        elif self.action_splits[0] == "F" :
            self.flag()
        elif self.action_splits[0] == "quit":
            self.quit()
        elif len(self.action_splits) == 2:
            self.open()
        else:
            raise Exception("Unrecognized input")


