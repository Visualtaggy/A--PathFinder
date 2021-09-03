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
    'yellow':(255,254,106),
    'grey':(47,79,79)
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

def create_grid_lines(window,rows,width):
     node_width = width // rows
     for i in range (rows):
         pygame.draw.line(window,colors['grey'],(0,i * node_width),(width,i * node_width))
         for j in range (rows):
            pygame.draw.line(window,colors['grey'],(j * node_width,0),(j * node_width,width))         

def draw(window,grid,rows,width):
    window.fill(colors['white'])

    for row in grid:
        for node in row:
            node.draw(window)
    create_grid_lines(window,rows,width)
    pygame.display.update()

#Dividing width of the pixel should help locating where the mouse is clicking
def get_mouse_position(pos,rows,width):
    node_width = width // rows
    y,x = pos

    row = y // node_width
    col = x // node_width
    return row,col


def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col



def main(win, width):
	rows = 40
	grid = make_board(rows, width)

	start = None
	end = None

	run = True
	while run:
		draw(win, grid, rows, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, rows, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.create_start()

				elif not end and spot != start:
					end = spot
					end.create_destination()

				elif spot != end and spot != start:
					spot.create_destination()
            
	pygame.quit()

main(WINDOW, width)