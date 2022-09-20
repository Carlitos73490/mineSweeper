from classes.action import Action


class ActionQuit(Action):
    def action(self,minesweeper):
        minesweeper.is_playing = False
        print("Fin de la partie")
