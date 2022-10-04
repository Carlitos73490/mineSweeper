class UIText:
    def __init__(self, pygame):
        self.pygame = pygame
        pygame.init()
        self.window_width = 500
        self.window_height = 500
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.screen.fill((255, 255, 255))

        pygame.display.set_caption('Minesweeper')

    def drawgrid(self, grid):
        self.screen.fill((255, 255, 255))

        # On set la taille de chaque block
        # par rapport à la taille de la grille et de la windows pygame
        block_size = self.window_width / grid.dimension

        for i in range(len(grid.tiles)):
            rect_object = self.pygame.Rect(
                grid.tiles[i].x * block_size,
                grid.tiles[i].y * block_size,
                block_size,
                block_size)
            text_surface_object = self.pygame.font.SysFont('Arial', 15)\
                .render(str(grid.tiles[i]), True, (10, 10, 10))
            text_rect = text_surface_object.get_rect(center=rect_object.center)
            self.screen.blit(text_surface_object, text_rect)
