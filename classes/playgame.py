import sys

from classes.minesweeper import Minesweeper
from classes.player import Player


class PlayGame:
    def __init__(self):
        self.player = Player()
        self.minesweeper = Minesweeper(int(sys.argv[1]))

    def run(self):
        while True:
            action = self.player.get_action()
            action.action(self.minesweeper)
            print(self.minesweeper.grid)


