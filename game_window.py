import pygame, sys, pygame.color

pygame.init()
win_width = int(input("Set the width of the window. "))
win_height = int(input("Set the height of the window. "))
bg_color = pygame.color.Color("#D7E894")
screen = pygame.display.set_mode((win_width,win_height))

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		sys.exit()
	screen.fill(bg_color)
	pygame.display.flip()
	
	