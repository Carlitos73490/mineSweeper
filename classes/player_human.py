from classes.actionflag import ActionFlag
from classes.actionnewgame import ActionNewGame
from classes.actionopen import ActionOpen
from classes.actionquit import ActionQuit
from classes.player import Player


class PlayerHuman(Player):


    def get_action(self):

        action_splits = input(" newgame | quit | {F} x y : ").split()

        if action_splits[0] == "newgame":
            return ActionNewGame()
        elif action_splits[0] == "F":
            return ActionFlag(action_splits[1],action_splits[2])
        elif len(action_splits) == 2:
            return ActionOpen(action_splits[0],action_splits[1])
        elif action_splits[0] == "quit":
            return ActionQuit()
        else:
            raise Exception("Unrecognized input")
