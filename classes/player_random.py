import random
from classes.actionflag import ActionFlag
from classes.actionnewgame import ActionNewGame
from classes.actionopen import ActionOpen
from classes.player import Player


class PlayerRandom(Player):
    def __init__(self, minesweeper):
        super().__init__(minesweeper)

    def get_action(self):

        random_coord_x = random.randint(0, self.minesweeper.dimension - 1)
        random_coord_y = random.randint(0, self.minesweeper.dimension - 1)

        random_action = bool(random.getrandbits(1))

        if not self.minesweeper.is_playing:
            return ActionNewGame()
        elif random_action:
            return ActionFlag( random_coord_x,  random_coord_y)
        elif not random_action:
            return ActionOpen( random_coord_x,  random_coord_y)
