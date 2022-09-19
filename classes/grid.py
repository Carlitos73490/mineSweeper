import random

from classes.tileMine import TileMine
from classes.tileHint import TileHint


class Grid:

    def __init__(self, dimension):
        self.is_lost = False
        self.dimension = dimension
        self.tiles = []
        self.remaining = 0
        for x in range(self.dimension):
            for y in range(self.dimension):
                self.tiles.append(TileHint(self, x, y))
                self.remaining += 1
        self._mines_coord()

    def open(self, x, y):
        tile_to_open = self.get_tile(x, y)
        tile_to_open.open()
        self.remaining -= 1

        if isinstance(tile_to_open, TileMine):
            self.is_lost = True

            #fin de partie ouverture de tout
            for tile in self.tiles:
                tile.is_open = True
        else:
            self._open_full(x, y)

    def _open_full(self,x,y):
            startX = x - 1
            startY = y - 1
            for ix in range(3):
                for iy in range(3):
                    current_tile_x = ix + startX
                    current_tile_y = iy + startY
                    tile_to_open = self.get_tile(current_tile_x, current_tile_y)
                    # la condition sur la mine ne doit pas exister
                    if(tile_to_open is not None and isinstance(tile_to_open, TileHint) ):
                        if not tile_to_open.is_open:
                            if tile_to_open.open():
                                self.remaining -= 1
                            if tile_to_open.hint == " ":
                                self._open_full(current_tile_x, current_tile_y)

    def toggle_flag(self, x, y):
        tile_to_toggle = self.get_tile(x, y)
        if tile_to_toggle is not None:
            if tile_to_toggle.is_open:
                raise Exception("La thuile est déjà ouverte")
            else:
                tile_to_toggle.is_flag = not tile_to_toggle.is_flag
        else:
            raise Exception("La thuile n'existe pas")

    def _mines_coord(self):
        # selection de tuples au hasard dans la liste
        tiles_to_mine = random.sample(self.tiles, len(self.tiles) // 10)
        for mine in tiles_to_mine:
            # Récupération de l'index de l'objet à miner
            # dans la liste de tuiles principales
            index = self.tiles.index(mine)
            # Remplacement dans la liste principales
            self.tiles[index] = TileMine(self, mine.x, mine.y)
            self.remaining -= 1

    def get_tile(self, x, y):
        for tile in self.tiles:
            if tile.x == x and tile.y == y:
                return tile

    @property
    def is_win(self):
        return self.remaining == 0

    def __str__(self):
        display_string = ""
        display_line = ""
        # Tiles
        for i in range(len(self.tiles)):
            display_line += "|" + str(self.tiles[i])
            if (i + 1) % self.dimension == 0:
                display_string += display_line + "|\n"
                display_line = ""

        display_string += "remaining : " + str(self.remaining)
        return display_string
