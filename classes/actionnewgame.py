from classes.action import Action
from classes.grid import Grid


class ActionNewGame(Action):

    def action(self, minesweeper):
        print("Début de la partie")
        minesweeper.is_playing = True
        minesweeper.grid = Grid(minesweeper.dimension)
