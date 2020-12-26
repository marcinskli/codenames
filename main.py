import pygame
import screen_func
from functions import create_key_card

screen = screen_func.initialize_screen()
start, agents = create_key_card()
pygame.display.set_caption(start[0].upper())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen_func.update_screen(screen, agents)

pygame.quit()
