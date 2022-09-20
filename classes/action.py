class Action:
    def __init__(self):
        pass

    def action(self,minesweeper):
        if minesweeper.grid.is_win():
            raise Exception("la partie est gagné "
                            "relancez en une avec : newgame ")
        elif minesweeper.grid.is_lost():

            raise Exception("la partie est perdu "
                            "relancez en une avec : newgame ")
