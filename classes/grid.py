import random

from classes.tilemine import TileMine
from classes.tilehint import TileHint
from exceptions.tile_already_open_exception import TileAlreadyOpenException
from exceptions.tile_dont_exist_exception import TileDontExistException


class Grid:

    def __init__(self, dimension):
        self.first_open = True
        self.dimension = dimension
        self.tiles = []
        self._is_lost = False
        self.remaining = 0
        for x in range(self.dimension):
            for y in range(self.dimension):
                self.tiles.append(TileHint(self, x, y))
                self.remaining += 1


    def open(self, x, y):

        tile_to_open = self.get_tile(x, y)


        if isinstance(tile_to_open, TileMine):
            self._is_lost = True
            # fin de partie ouverture de tout
            for tile in self.tiles:
                tile.is_open = True
        elif tile_to_open is not None:
            tile_to_open.open()
            self.remaining -= 1
            if self.first_open:
                self._mines_coord()
                self.first_open = False
            self._open_full(x, y)
        else:
            raise TileDontExistException(x,y)


    def _open_full(self, x, y):
        start_x = x - 1
        start_y = y - 1
        for i_x in range(3):
            for i_y in range(3):
                current_tile_x = i_x + start_x
                current_tile_y = i_y + start_y
                tile_to_open = self.get_tile(current_tile_x, current_tile_y)
                # la condition sur la mine ne doit pas exister
                if (tile_to_open
                        is not None and isinstance(tile_to_open, TileHint)):
                    if not tile_to_open.is_open:
                        if tile_to_open.open():
                            self.remaining -= 1
                        if tile_to_open.hint == " ":
                            self._open_full(current_tile_x, current_tile_y)

    def toggle_flag(self, x, y):
        tile_to_toggle = self.get_tile(x, y)
        if tile_to_toggle is not None:
            if tile_to_toggle.is_open:
                raise TileAlreadyOpenException()
            else:
                tile_to_toggle.is_flag = not tile_to_toggle.is_flag
        else:
            raise TileDontExistException()

    def _mines_coord(self):
        # selection de tuples au hasard dans la liste
        # filtr?? des tuiles non ouverte (seulement une ouverte)
        filteredtiles = list(filter(lambda tile : tile.is_open is False, self.tiles))
        tiles_to_mine = random.sample(filteredtiles, len(self.tiles) // 10)
        for mine in tiles_to_mine:
            # version optimis??
            tile_to_mine = self.get_tile(mine.x, mine.y)
            if tile_to_mine is not None:
                self.tiles[mine.x * self.dimension + mine.y] = \
                    TileMine(self, mine.x, mine.y)
            # old version
                # R??cup??ration de l'index de l'objet ?? miner
                # dans la liste de tuiles principales
                # index = self.tiles.index(mine)
                # Remplacement dans la liste principales
                # self.tiles[index] = TileMine(self, mine.x, mine.y)
            self.remaining -= 1

    def get_tile(self, x, y):
        if x > self.dimension - 1 or x < 0 or y > self.dimension - 1 or y < 0:
            return None
        else:
            return self.tiles[x * self.dimension + y]

    def is_win(self):
        return self.remaining == 0

    def is_lost(self):
        return self._is_lost

    def __str__(self):
        display_string = ""
        display_line = ""

        # Tiles
        for i in range(len(self.tiles)):
            display_line += " " + str(self.tiles[i])
            if (i + 1) % self.dimension == 0:
                display_string += display_line + "  x :" + \
                                  str(self.tiles[i].x) + "\n"
                display_line = ""

        display_string += "remaining : " + str(self.remaining)
        return display_string
