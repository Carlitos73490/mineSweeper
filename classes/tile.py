from exceptions.tile_already_open_exception import TileAlreadyOpenException
from exceptions.tile_dont_exist_exception import TileDontExistException
from exceptions.tile_is_flag_exception import TileIsFlagException


class Tile:
    grid = None
    x = None
    y = None
    is_flag = False
    is_open = False

    def __init__(self, grid, x, y):
        self.grid = grid
        self.x = x
        self.y = y

    def open(self):
        opened = False
        if self.is_flag:
            raise TileIsFlagException()
        elif self.is_open is False:
            self.is_open = True
            opened = True
        else:
            raise TileAlreadyOpenException()

        return opened

    def __str__(self):
        if self.is_flag:
            return "F"
        else:
            return "#"
