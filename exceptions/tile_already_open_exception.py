class TileAlreadyOpenException(Exception) :
    def __init__(self):
       self.message = "La thuile est déjà ouverte"
       super().__init__(self.message)

