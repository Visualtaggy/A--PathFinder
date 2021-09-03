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
    'orange':(248,54,0),
    'yellow':(255,254,106)
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
    
    def create_blocker(self):
        self.color == colors['navy']

    def create_start(self):
        self.color == colors['purple']

    def create_visited(self):
        self.color == colors['blue']
    
    def create_destination(self):
         return self.color == colors['orange']
    
    def make_path(self):
        return self.color == colors['yellow']

    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.width))
    
    def update_neighbour(self,grid):
        pass

    def __lt__(self, other):
        return False

#Making H value value A*(Algo) aka         

def heuristic(point_1,point_2):
    x1,y1 = point_1
    x2,y2 = point_2
    return abs(x1 - x2) +  abs(y1 - y2)

def make_board(rows,width):
    """
    Trying to make a datastructre of this sort inorder to store 
    status of various nodes
    board = [
        [][][][][][][][][][]
        [][][][][][][][][][]
        [][][][][][][][][][]
        [][][][][][][][][][]
        [][][][][][][][][][]
        [][][][][][][][][][]
        [][][][][][][][][][]
        [][][][][][][][][][]
    ]

    """
    board = []
    node_width = width // rows
    for i in range(rows):
        board.append([])
        for j in range(rows):
            node = Node(i,j,node_width,rows)
            board[i].append(node)
    return board

