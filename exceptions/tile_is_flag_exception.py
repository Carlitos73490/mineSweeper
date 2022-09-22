class TileIsFlagException(Exception) :
    def __init__(self):
        self.message = "La thuile est déjà flag"
        super().__init__(self.message)