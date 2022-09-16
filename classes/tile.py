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

    def __str__(self):
        if self.is_flag:
            return "F"
        elif self.is_open:
            raise NotImplementedError()
        else:
            return "#"
