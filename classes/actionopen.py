from classes.action import Action
from enums.actiontitle import  ActionTitle


class ActionOpen(Action):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def action(self,minesweeper):
        super()

        if minesweeper.is_playing:
            print(ActionTitle.OPEN.value,
                  " ",
                  self.x,
                  ",",
                  self.y)
            minesweeper.grid.open(int(self.x),int(self.y))
        else:
         print("Lancez d'abord la partie")
