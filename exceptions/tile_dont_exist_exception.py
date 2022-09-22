class TileDontExistException(Exception):
    def __init__(self,x,y):
        self.message = f"La thuile ({x},{y}) n'existe pas"
        super().__init__(self.message)
