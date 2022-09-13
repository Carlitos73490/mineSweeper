import sys
from classes.minesweeper import Minesweeper

if __name__ == '__main__':
    m = Minesweeper()
    m.new_game(sys.argv[1])
