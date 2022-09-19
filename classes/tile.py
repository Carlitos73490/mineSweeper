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
        if self is not None:
            if self.is_flag:
                raise Exception("La thuile est flag")
            elif self.is_open == False:
                self.is_open = True
                opened = True
            else:
                raise Exception("La thuile est déjà ouverte")

        else:
            raise Exception("La thuile n'existe pas")
        return opened

    def __str__(self):
        if self.is_flag:
            return "F"
        else:
            return "#"
