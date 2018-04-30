import pygame

pygame.init()
win_width = int(input("Set the width of the window. "))
win_height = int(input("Set the height of the window. "))

screen = pygame.display.set_mode((win_width,win_height))
running = True
while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False
		
	