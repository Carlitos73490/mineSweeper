import sys
from classes.minesweeper import Minesweeper

if __name__ == '__main__':
    m = Minesweeper(sys.argv[1])
    print(m.grid_dimension)
