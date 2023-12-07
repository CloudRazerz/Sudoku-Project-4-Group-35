import pygame, sys
class Cell:
    def __init__(self, value, row, col, screen): #initializes the parameters of the Cell class
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.confirmed = False #Boolean variable to check if there is a value in the cell
        self.default = None #Boolean to see if the cell started empty or is one of the filled cells

    def set_cell_value(self, value): #sets the value for the cell
        if self.confirmed == False: #first checks if confirm false (if so cell empty
            self.value = value #then sets the value in that cell
            self.confirmed = True #changes confirmed from fale to true so the value cant be changed
        
    def set_sketched_value(self, value): #repeat of the function above except doesn't confirms the value
        if self.confirmed == False: #if cell empty...
            self.value = value #then set place holder value in the cell
            #does not confirm value as the answer


    def draw(self):
        for j in range(0,600,60): # nested for loops here work to draw the cell grid for pygame
            for k in range(0,600,60):
                for i in range(0, 2): #draws the horizontal lines
                    pygame.draw.line(
                    self.screen,
                    'gray',
                        (k, j),
                        (k, i * self.screen.get_width()/9 + j)
                    )

                for i in range(0,2): #draws the vertical lines
                    pygame.draw.line(
                        self.screen,
                        'gray',
                        (j, k),
                        (i *self.screen.get_width()/9 + j, k)
                    )
        #Sets the font for the numbers to be entered in the cells
        flont = pygame.font.Font(None, size=30)
        sketch = flont.render(str(self.value), True, 'gray', None)
        self.screen.blit(sketch, (self.col * 60 + 5, self.row * 60))

