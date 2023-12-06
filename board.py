import pygame, sys
from cell import Cell

class Board:
    selected = None

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = []
        for i in range(9):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(Cell(0, i, j, screen))
        pygame.init() #Dont know if this goes here or not but we will see

    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()
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

        for i in range(1, 3):
            pygame.draw.line(
            self.screen,
            'black',
                (0, i * self.screen.get_width()/3),
                (self.screen.get_width(), i * self.screen.get_width()/3),
                3
            )

        for i in range(1,3):
            pygame.draw.line(
                self.screen,
                'black',
                (i*self.screen.get_width()/3, 0),
                (i *self.screen.get_width()/3, self.screen.get_width()),
                3
            )
        pass

    def select(self, row, col):
        self.selected = self.cells[row][col]


    def click(self, x, y):
        row = y//60
        col = x//60
        return int(row), int(col)

    def clear(self):
        if self.selected != None:
            if self.selected.default == False:
                self.selected.set_sketch_value(0)

    def sketch(self, value):
        self.value = value
        if self.selected != None:
            self.selected.set_sketched_value()


    def place_number(self, value):
        self.value = value
        if self.confirmed != None:
            self.selected.set_value()

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.confimred:
                    continue
                else:
                    return False
        return True

    def check_board(self):
        board =[]
        rows = []
        col = []
        box = []
        for row in range(len(self.cells)):
            board.append([])
            for cell in self.cells[row]:
                board[row].append(cell.value)
        for value in board:
            rows.append(set(value))

        for i in range(len(board)):
            col.append(set())
            for row in board:
                col[i].add(row[i])

        coord = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for top in range(len(coord)):
            box.append(set())
            for j in range(3):
                for k in range(3):
                    box[top].add(board[coord[top][0]+j][coord[top][1]+k])
        for check in [col, rows, box]:
            for sets in check:
                if sets == {1,2,3,4,5,6,7,8,9}:
                    continue
                else:
                    return False

        return True



        pass


