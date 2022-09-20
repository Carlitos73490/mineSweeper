from classes.action import Action
from enums.actiontitle import  ActionTitle


class ActionFlag(Action):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def action(self,minesweeper):

        super().action()
        if(minesweeper.is_playing):
            print(ActionTitle.FLAG.value,
                    " ",self.x,
                    ",",self.y)
            minesweeper.grid.toggle_flag(int(self.x),int(self.y))
        else:
         print("Lancez d'abord la partie")
