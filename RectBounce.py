import pygame
import time

#helper constants for later
SIZE = (640*2, 300*2)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

#start game engine, open window, set window title
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Helllo World")

#a square and a direction speed
square = pygame.Rect(640/2 - 100/2, 480/2 - 100/2, 100, 100)
directionx = 1
directiony = 1

# main loop
while True:

	# handle all events pygame has collected since the last loop
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			directionx = 10
			#square = square.move(10, 0)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			directionx = -10
			#square = square.move(-10, 0)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			directiony = -10
			#square = square.move(0, -10)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			directiony = 10
			#square = square.move(0, 10)
		elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
			directionx = 0
			#square = square.move(10, 0)
		elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
			directionx = 0
			#square = square.move(-10, 0)
		elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
			directiony = 0
			#square = square.move(0, -10)
		elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
			directiony = 0
			#square = square.move(0, 10)
	# erase the board, draw a box, and flip to the new drawing
	screen.fill(GREEN)
	pygame.draw.rect(screen, BLUE, square)
	pygame.display.flip()

	#shoot for about 30 fps
	time.sleep(1/300)

	#    motion logic before looping again
	square = square.move(directionx, directiony)
	if square.x + square.w >= SIZE[0]:
		#directionx = -abs(directionx)
		square = square.move(-10, 0)
	elif square.x <= 0:
		#directionx = abs(directionx)
		square = square.move(10, 0)
	if square.y + square.w >= SIZE[1]:
		#directiony = -abs(directiony)
		square = square.move(0, -10)
	elif square.y <= 0:
		#directiony = abs(directiony)
		square = square.move(0, 10)
