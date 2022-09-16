from classes.tile import Tile
from classes.tileMine import TileMine


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
                    current_case_x = x + startX
                    current_case_y = y + startY
                    # si la case n'est pas elle même ont check
                    if x != current_case_x and y != current_case_y:
                        # si la case est une mine on incrémente la property
                        if isinstance(self.grid.get_tile(current_case_x, current_case_y), TileMine):
                            count += 1
            _hint = str(count) if count > 0 else " "
        return _hint

    def __str__(self):
        return self.hint if self.is_open else super().__str__()
