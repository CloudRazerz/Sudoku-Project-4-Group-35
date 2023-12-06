import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):

        ##initialize variables
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = math.sqrt(row_length)
        no_dup_col_count = 0
        rand_num_row = []
        rand_num_col = []
        self.removed_cells_copy = removed_cells

        ##create sudoku number list
        while no_dup_col_count != row_length:
            rand_num_2D_grid = []
            no_dup_col_count = 0
            removal_comp = 0
            i = 0
            j = 0
            reset = False
            # print("rand num col", rand_num_col)

            ##create a random number grid without the rows having duplicate numbers
            for i in range(row_length):
                random.seed()
                rand_num_row = random.sample(range(1, row_length + 1), k=row_length)
                rand_num_2D_grid.append(rand_num_row)
                rand_num_row = []

            ##obtain the grid's columns to check and remove duplicates in all columns
            for j in range(row_length):
                k = 0
                for k in range(row_length):
                    rand_num_col.append(rand_num_2D_grid[k][j])
                    # print(rand_num_2D_grid[k][j])
                # print(set(rand_num_col))
                # print("rand_num_col", rand_num_col)

                ##if a sudoku column has duplicate numbers besides zero, remove them
                rand_num_col_copy = rand_num_col.copy()
                for x in rand_num_col_copy:
                    if x > 0 and rand_num_col_copy.count(x) > 1:
                        rand_num_col_copy.remove(x)

                if len(rand_num_col_copy) != row_length:
                    if removed_cells > 0:

                        ##replace duplicate numbers in columns with zeros
                        seen = set()
                        for l, e in enumerate(rand_num_col):
                            if reset == True:
                                break
                            if e in seen:
                                # print("seen")
                                if removed_cells != 0:
                                    # print("rand_num_col: ", rand_num_col)
                                    rand_num_col[l] = 0
                                    removed_cells -= 1
                                    removal_comp += 1
                                    print("Removed a cell. Only", removed_cells, "cells left!")
                                    # print("removal comp", removal_comp)
                                else:
                                    rand_num_col = []
                                    removed_cells += removal_comp
                                    removal_comp = 0
                                    # print("removal comp else", removal_comp)
                                    # print("rand_num_col else", rand_num_col)
                                    reset = True
                                """    
                                ##reset the 2D grid

                                    i = 0
                                    ##create a random number grid without the rows having duplicate numbers
                                    for i in range(row_length):
                                        random.seed()
                                        rand_num_row = random.sample(range(1,row_length+1), k=row_length)
                                        rand_num_2D_grid.append(rand_num_row)
                                        rand_num_row = []
                                """

                            else:
                                seen.add(e)
                                # print("seen else")
                        # print("2D Grid before:", rand_num_2D_grid)
                        # print("rand_num_col to add", rand_num_col)
                        # print("col to remove", rand_num_2D_grid[j][:])
                        if reset == False:
                            # print("Before 2D Grid # of 0s:", sum(x.count(0) for x in rand_num_2D_grid))
                            print("Changing 2D Grid...")

                            ##replace rand_num_col with the new rand_num_col
                            k = 0
                            if rand_num_col != []:
                                for k in range(row_length):
                                    rand_num_2D_grid[k][j] = rand_num_col[k]
                                    # print("k & j:", k,j)

                            # print("2D Grid after", rand_num_2D_grid)
                            # print("2D Grid # of 0s:", sum(x.count(0) for x in rand_num_2D_grid))
                            # print('changed')
                            no_dup_col_count += 1
                            rand_num_col = []


                    else:
                        ##reset removed cells
                        removed_cells = removal_comp
                        removal_comp = 0
                        rand_num_col = []
                        print("Resetting removed cells...")

                else:
                    no_dup_col_count += 1
                    rand_num_col = []
                    # print("check if working")

                # reset process
                if reset == True:
                    reset = False
                    print("Resetting process...")
                    break

            print(no_dup_col_count, "columns without duplicates!")

        # print(rand_num_2D_grid)
        self.board_for_solver = rand_num_2D_grid

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board_for_solver

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        print(self.board_for_solver)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        i = 0
        j = 0
        for i in range(len(self.board_for_solver)):
            for j in range(len(self.board_for_solver)):
                if self.board_for_solver[row][j] == num:
                    return True
                else:
                    return False

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        i = 0
        j = 0
        for i in range(len(self.board_for_solver)):
            for j in range(len(self.board_for_solver)):
                if self.board_for_solver[col][j] == num:
                    return True
                else:
                    return False

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        i = 0
        j = 0
        for i in range(3):
            for j in range(3):
                if self.board_for_solver[row_start + i][col_start + j] == num:
                    return False
                else:
                    return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        if self.valid_in_box == True and self.valid_in_col == True and self.valid_in_row == True:
            return True
        else:
            return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        pass

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        pass

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
    def generate_sudoku(self, size,  removed):


        # comment print board out when finished changing sudoku_generator.py
        self.print_board()

        self.fill_values()
        board = self.get_board()
        self.remove_cells()
        board = self.get_board()
        return board
    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        ##remove cells
        # print(self.removed_cells)
        for i in range(self.removed_cells_copy - sum(x.count(0) for x in self.board_for_solver)):
            rand_num1 = random.randrange(0, self.row_length)
            rand_num2 = random.randrange(0, self.row_length)

            # only remove cell if it has not already been removed
            while self.board_for_solver[rand_num1][rand_num2] == 0:
                rand_num1 = random.randrange(0, self.row_length)
                rand_num2 = random.randrange(0, self.row_length)
                if self.board_for_solver[rand_num1][rand_num2] != 0:
                    self.board_for_solver[rand_num1][rand_num2] = 0
                    break
            else:
                self.board_for_solver[rand_num1][rand_num2] = 0
                # print("Popped location:", rand_num1, rand_num2)

            self.board_for_user = self.board_for_solver


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)

    # comment print board out when finished changing sudoku_generator.py
    sudoku.print_board()

    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


"test functions"
# SG = SudokuGenerator(2,2)
generate_sudoku(9, 30)
