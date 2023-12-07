import pygame, sys
from cell import Cell

class Board:
    selected = None #creates empty class attribute to store the x and y coordinates of the where selected on the board

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [] # creates empty list that will store rows as iterated by the next for loop
        for i in range(9):
            self.cells.append([]) #creates row values in self.cells list
            for j in range(9):
                self.cells[i].append(Cell(0, i, j, screen)) #goes into each row variable and puts in list of corresponding cells
        pygame.init()

    def draw(self):# draw functon that draws the entirety of the board
        for row in self.cells: #nested for loop that draws grid for each cell so that each cell has own surface
            for cell in row:
                cell.draw()
        for j in range(0,600,60): #draws the cell grid
            for k in range(0,600,60): #draws horizontal lines
                for i in range(0, 2):
                    pygame.draw.line(
                    self.screen,
                    'gray',
                        (k, j),
                        (k, i * self.screen.get_width()/9 + j)
                    )

                for i in range(0,2): #draws vertical
                    pygame.draw.line(
                        self.screen,
                        'gray',
                        (j, k),
                        (i *self.screen.get_width()/9 + j, k)
                    )

        for i in range(1, 3): #draws horizontal lines for the large box grid
            pygame.draw.line(
            self.screen,
            'black',
                (0, i * self.screen.get_width()/3),
                (self.screen.get_width(), i * self.screen.get_width()/3),
                3
            )

        for i in range(1,3): #draws vertical lnes for the large box grid
            pygame.draw.line(
                self.screen,
                'black',
                (i*self.screen.get_width()/3, 0),
                (i *self.screen.get_width()/3, self.screen.get_width()),
                3
            )
        pass

    def select(self, row, col): #assigns the selected class attribute to the cell coordinates
        self.selected = self.cells[row][col] #assigns selected the cell coordinates which are the row and col index numbers in self.cells


    def click(self, x, y):
        # sets row and col through taking the coordinates of the mouse click and dividing by 60 to return number 1-9
        #referring to how there are 9 columns and rows on the sudoku board
        row = y//60
        col = x//60
        return int(row), int(col)

    def clear(self): #clears board when reset is used
        if self.selected != None: #checks to make sure that a cell is selected
            if self.selected.default == False: #sees if cell is at default value
                self.selected.set_sketch_value(0) #if cell is not at default then sets back to default by setting to 0

    def sketch(self, value): #puts sketh value on the board
        self.value = value
        if self.selected != None: #checks to make sure the cell is empty
            self.selected.set_sketched_value() #if empty sets the value entered by the user


    def place_number(self, value): #confirms the sketch value
        self.value = value
        if self.confirmed != None: #checks to see i empty
            self.selected.set_value() #if empty sets the value

    def is_full(self): #checks to make sure the board is full so can see whether win or lose
        for row in self.cells:
            for cell in row:
                if cell.confimred:
                    continue
                else:
                    return False
        return True

    def check_board(self): #checks to see that every box, row, and column only has one of each number
        #each of these lists coresponds to the rows, columns, and boxes of the board and the numebr values within them
        board =[] #converts each cells into their number values so the board can be properly checked
        rows = []
        col = []
        box = []
        for row in range(len(self.cells)): #creates list
            board.append([])
            for cell in self.cells[row]:
                board[row].append(cell.value)
        for value in board: #takes values within board and puts the value in each cell to its corresponding row
            rows.append(set(value))

        for i in range(len(board)): #does same except for the columns
            col.append(set())
            for row in board:
                col[i].add(row[i])

        coord = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for top in range(len(coord)): #the hardest one to program, uses the list above of the coordinates of the top left of each box
            box.append(set()) #appends to box as sets
            for j in range(3):
                for k in range(3):
                    box[top].add(board[coord[top][0]+j][coord[top][1]+k]) #goes through and adds the cell values to each box in the box list
        for check in [col, rows, box]: #fnally goes through columns, rows, and boxes and checks to make sure has 1-9 without repeats in the same row, column, or boxes
            for sets in check:
                if sets == {1,2,3,4,5,6,7,8,9}:
                    continue
                else:
                    return False #if repeats, returns False

        return True #if no repeats, returns true



        pass


