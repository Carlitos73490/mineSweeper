from classes.tile import Tile
from classes.tilemine import TileMine


class TileHint(Tile):
    _hint = None

    @property
    def hint(self):
        if self._hint is None:
            count = 0
            startX = self.x - 1
            startY = self.y - 1

            for x in range(3):
                for y in range(3):
                    current_tile_x = x + startX
                    current_tile_y = y + startY
                    # On ne check pas la case du milieu qui est elle même
                    if x == 1 and y == 1:
                        pass
                    else:
                        # Si la case est une mine on incrémente la property
                        if isinstance(
                                self.grid.get_tile(current_tile_x,
                                                   current_tile_y),
                                TileMine):
                            count += 1
            self._hint = str(count) if count > 0 else ' '
        return self._hint

    def __str__(self):
        return self.hint if self.is_open else super().__str__()
