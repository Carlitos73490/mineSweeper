class Player:
    def __init__(self,minesweeper):
        self.minesweeper = minesweeper

    def game_over(self):
        if self.minesweeper.grid.is_win():
            self.minesweeper.is_playing = False
            return "Vous avez gagné"
        elif self.minesweeper.grid.is_lost():
            self.minesweeper.is_playing = False
            return f"la mine vous a explosé c'est perdu, {self.minesweeper.grid.remaining} cases restantes"
        else:
            return ""
