import pygame
import math
from queue import PriorityQueue

width = 800
WINDOW = pygame.display.set_mode((width,width))
pygame.display.set_caption("A* PathFinder - by Vishal Tyagi")


white = (255,255,255)
blue = (64,206,227)
navy = (12,53,71)
purple = (128, 0, 128)
orange = (248,54,0)
yellow = (255,254,106)
grey = (47, 79, 79)




class Node:
    def __init__(self,row,col,width,t_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = white
        self.neighbours = []
        self.width = width
        self.total_rows = t_rows

    def find_position(self):
        return self.row,self.col

    def is_visited(self):
        return self.color == blue
    
    def is_blocked(self):
        return self.color == navy

    def is_start(self):
        return self.color == purple
    
    def is_destination(self):
        return self.color == orange

    def reset_board(self):
        self.color = white
    
    def create_blocker(self):
        self.color = navy

    def create_start(self):
        self.color = purple

    def create_visited(self):
        self.color = blue
    
    def create_destination(self):
        self.color = orange
    
    def create_path(self):
        self.color = yellow

    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.width))
    
    def update_neighbour(self,grid):
        self.neighbours = []
        #Going down to find the neighbour
        if self.row < self.total_rows -1 and not grid[self.row + 1][self.col].is_blocked():
            self.neighbours.append(grid[self.row + 1][self.col])

        #Going up to find the neighbour
        if self.row > 0 and not grid[self.row - 1][self.col].is_blocked():
            self.neighbours.append(grid[self.row - 1][self.col])

         #Going right to find the neighbour  
        if self.col < self.total_rows -1 and not grid[self.row][self.col + 1].is_blocked():
            self.neighbours.append(grid[self.row][self.col + 1])   
        
        #Going left to find the neighbour 
        if self.col > 0 and not grid[self.row][self.col - 1].is_blocked():
            self.neighbours.append(grid[self.row][self.col - 1])         
    
    def __lt__(self, other):
        return False

def a_star_algorithm(draw,grid,start,end):
    counter = 0
    open_set = PriorityQueue()
    open_set.put((0,counter,start))

    #where is the node coming from?
    previous = {}

    global_score = {spot: float('inf') for row in grid for spot in row}
    
    #This is here you begin so it's 0
    global_score [start] = 0 

    f_score = {spot: float('inf') for row in grid for spot in row}
    f_score [start] = heuristic(start.find_position(),end.find_position())

    #Hash to keep a track of all the things in the priority que
    open_set_tracker = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
         # indexing two because we want just the node NOT the counter       
        current = open_set.get()[2]
        open_set_tracker.remove(current)

        if current == end:
            #found the path
            return True
        for neighbour in current.neighbours:
            tmp_global_score = global_score[current] + 1

            if tmp_global_score < global_score[neighbour]:
                previous[neighbour] = current
                global_score[neighbour] = tmp_global_score
                f_score[neighbour] =tmp_global_score + heuristic(neighbour.find_position(),end.find_position())
                if neighbour not in open_set_tracker:
                    counter += 1
                    open_set.put((f_score[neighbour],counter,neighbour))
                    open_set_tracker.add(neighbour)
                    #maybe add color for next available block?
        draw()

        if current != start:
            current.create_visited()
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
         pygame.draw.line(window,grey,(0,i * node_width),(width,i * node_width))
         for j in range (rows):
            pygame.draw.line(window,grey,(j * node_width,0),(j * node_width,width))         

def draw(window,grid,rows,width):
    window.fill(white)

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
	rows = 30
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
				location = grid[row][col]
				if not start and location != end:
					start = location
					start.create_start()

				elif not end and location != start:
					end = location
					end.create_destination()

				elif location != end and location != start:
					location.create_blocker()

			elif pygame.mouse.get_pressed()[2]: 
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, rows, width)
				spot = grid[row][col]
				spot.reset_board()
				if spot == start:
					start = None
				elif spot == end:
					end = None
            
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbour(grid)
					a_star_algorithm(lambda: draw(win, grid, rows, width), grid, start, end)

	pygame.quit()

main(WINDOW, width)
