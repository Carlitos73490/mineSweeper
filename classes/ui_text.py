

class UIText:
    def __init__(self,pygame):
        self.pygame = pygame
        pygame.init()
        self.WINDOW_WIDTH = 500
        self.WINDOW_HEIGHT = 500
        self.SCREEN =  pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.SCREEN.fill((255,255,255))

        pygame.display.set_caption('Minesweeper')


    def drawGrid(self,grid):

        self.SCREEN.fill((255,255,255))

        # ajout des Tiles
        blockSize = self.WINDOW_WIDTH / (grid.dimension)  #On set la taille de chaque block par rapport à la taille de la grille et de la windows pygame

        for i in range(len(grid.tiles)):

            rect_object = self.pygame.Rect((grid.tiles[i].x) * blockSize, (grid.tiles[i].y) * blockSize, blockSize, blockSize)
            text_surface_object = self.pygame.font.SysFont('Arial', 15).render(str(grid.tiles[i]), True,(10, 10, 10) )
            text_rect = text_surface_object.get_rect(center=rect_object.center)
            self.SCREEN.blit(text_surface_object, text_rect)






