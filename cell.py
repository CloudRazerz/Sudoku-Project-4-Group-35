import pygame, sys
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.confirmed = False
        self.default = None

    def set_cell_value(self, value):
        if self.confirmed == False:
            self.value = value
            self.confirmed = True
        
    def set_sketched_value(self, value):
        if self.confirmed == False:
            self.value = value


    def draw(self):
        for j in range(0,600,60):
            for k in range(0,600,60):
                for i in range(0, 2):
                    pygame.draw.line(
                    self.screen,
                    'gray',
                        (k, j),
                        (k, i * self.screen.get_width()/9 + j)
                    )

                for i in range(0,2):
                    pygame.draw.line(
                        self.screen,
                        'gray',
                        (j, k),
                        (i *self.screen.get_width()/9 + j, k)
                    )
        flont = pygame.font.Font(None, size=30)
        sketch = flont.render(str(self.value), True, 'gray', None)
        self.screen.blit(sketch, (self.col * 60 + 5, self.row * 60))

