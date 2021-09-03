import pygame
import math
from queue import PriorityQueue

width = 800
WINDOW = pygame.display.set_mode((width,width))
pygame.display.set_caption("A* PathFinder - by Vishal Tyagi")

colors = {
    'white':(255,255,255),
    'blue':(64,206,227),
    'navy':(12,53,71),
    'purple':(466,8,99),
    'orange':(248,54,0)
    }


class Node:
    def __init__(self,row,col,width,t_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = colors['white']
        self.neighbours = []
        self.width = width
        self.total_rows = t_rows
        
    def find_position(self):
        return self.row,self.col

    def is_visited(self):
        return self.color == colors['blue']
    
    def is_blocked(self):
        return self.color == colors['navy']

    def is_start(self):
        return self.color == colors['purple']
    
    def is_destination(self):
        return self.color == colors['orange']

    def reset_board(self):
        self.color == colors['white']
    