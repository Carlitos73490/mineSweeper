class GameNotLaunchedException(Exception) :
    def __init__(self):
        self.message = "lancer d'abord la partie avec la commande newgame"
        super().__init__(self.message)