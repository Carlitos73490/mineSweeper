from classes.minesweeper import Minesweeper

if __name__ == '__main__':
    m = Minesweeper()

    while True:
        print("Début de la sélection")
        m.action_splits = input("{action} x y : ").split()
        m.actions_listener()
