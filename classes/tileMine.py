from classes.tile import Tile
class TileMine(Tile):


    def __str__(self):
        return "O" if super().is_open else super().__str__()

