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

        global_ui = UIText(pygame)
        while True:
            try:

                action_objet = self.player.get_action()
                action_objet.action(self.minesweeper)
                print(self.minesweeper.grid)

                global_ui.drawgrid(self.minesweeper.grid)
                pygame.display.update()
                print(self.player.game_over())

            except Exception as exception_output:
                print(exception_output)
