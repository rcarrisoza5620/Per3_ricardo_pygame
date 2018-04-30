import pygame, sys

pygame.init()
win_width = int(input("Set the width of the window. "))
win_height = int(input("Set the height of the window. "))

screen = pygame.display.set_mode((win_width,win_height))

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		sys.exit()
		
	