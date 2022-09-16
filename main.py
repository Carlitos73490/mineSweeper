import sys

from classes.minesweeper import Minesweeper

if __name__ == '__main__':
    m = Minesweeper()
    m.grid_dimension = int(sys.argv[1])


    while True :
        m.actions_listener()
        print(m.grid)
        if not m.is_playing:
            break

    if m.is_win:
        print('Gagné')
    elif m.is_lost:
        print('Vous êtes nul')