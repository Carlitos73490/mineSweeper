import sys

from classes.minesweeper import Minesweeper

if __name__ == '__main__':
    m = Minesweeper()
    m.grid_dimension = int(sys.argv[1])

    while True:
        m.actions_listener()
        print(m.grid)
        if not m.is_playing:
            break
        elif m.grid.is_lost():
            print('Gagné')
            break
        elif m.grid.is_win():
            print('Vous êtes nul')
            break