import pygame, sys

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen =screen
        self.difficulty = difficulty
        pygame.init() #Dont know if this goes here or not but we will see

    def draw(self):
        pass

    def select(self, row, col):
        pass

    def click(self, x, y):
        self.x = x
        self.y = y
        pass

    def clear(self):
        pass

    def sketch(self, value):
        self.value = value
        pass

    def place_number(self, value):
        self.value = value
        pass

    def reset_to_original(self, value):
        self.value = value
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass