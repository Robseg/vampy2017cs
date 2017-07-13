import pygame
import random
import time

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

chance = float(input("How likely are random squares to be alive at first? (eg., 0.75): "))
grid = []
for i in range(48):
	grid.append([])
	for j in range(64):
		if random.uniform(0, 1)< chance:
			grid[i].append(1)
		else:
			grid[i].append(0)
genx = []
for i in range(48):
	genx.append([])
	for j in range(64):
		genx[i].append(0)

print(grid)


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Conway's game!")

while True:
	print(str(grid))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	for i in range(48):
		for j in range(64):
			xpos = j*10
			ypos = i*10
			cell = pygame.Rect(xpos, ypos, 10, 10)
			if grid[i][j] == 1:
				pygame.draw.rect(screen, BLACK, cell)
			else:
				pygame.draw.rect(screen, WHITE, cell)



	for i in range(48):
		for j in range(64):	
			N = 0
			above = (i-1) % 48
			below = (i+1) % 48
			left  = (j-1) % 64
			right = (j+1) % 64
			N += grid[above][j]
			N += grid[below][j]
			N += grid[i][left]
			N += grid[i][right]
			N += grid[above][left]
			N += grid[above][right]
			N += grid[below][left]
			N += grid[below][right]
			if N < 2:
				genx[i][j] = 0
			if N > 3:
				genx[i][j] = 0
			if N == 3:
				genx[i][j] = 1
			else:
				genx[i][j] = grid[i][j]
	pygame.display.flip()
	pygame.display.update()
	time.sleep(.25)

	grid, genx = genx, grid




