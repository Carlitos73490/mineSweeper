import sys

import pygame

from classes.minesweeper import Minesweeper
from classes.player_human import PlayerHuman
from classes.player_random import PlayerRandom
from classes.ui_text import UIText


class PlayGame:
    def __init__(self):
        self.minesweeper = Minesweeper(int(sys.argv[1]))
        self.player = PlayerHuman(self.minesweeper)

    def run(self):


        ui = UIText(pygame)
        while True:
            try:

                actionObjet = self.player.get_action()
                actionObjet.action(self.minesweeper)
                print(self.minesweeper.grid)

                ui.drawGrid(self.minesweeper.grid)
                pygame.display.update()
                print(self.player.game_over())

            except Exception as e:
                print(e)
