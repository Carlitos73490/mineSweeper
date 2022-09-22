import sys

from classes.minesweeper import Minesweeper
from classes.player_human import PlayerHuman
from classes.player_random import PlayerRandom


class PlayGame:
    def __init__(self):
        self.minesweeper = Minesweeper(int(sys.argv[1]))
        self.player = PlayerRandom(self.minesweeper)


    def run(self):
        while True:
            try:

                actionObjet = self.player.get_action()
                actionObjet.action(self.minesweeper)
                print(self.minesweeper.grid)
                print(self.player.game_over())
            except Exception as e:
                print(e)


