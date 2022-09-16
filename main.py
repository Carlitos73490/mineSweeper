import sys

from classes.minesweeper import Minesweeper

if __name__ == '__main__':
    m = Minesweeper()
    m.grid_dimension = int(sys.argv[1])

    while True:
        print("Début de la sélection")
        m.action_splits = input("{action} x y : ").split()
        m.actions_listener()
