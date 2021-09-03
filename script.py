import pygame
import math
from queue import PriorityQueue

width = 800
WINDOW = pygame.display.set_mode((width,width))
pygame.display.set_caption("A* PathFinder - by Vishal Tyagi")

colors = {
    'white':(255,255,255),
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
        