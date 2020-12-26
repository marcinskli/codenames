import pygame
import settings
import functions

def initialize_screen():
    pygame.init()
    screen = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption(settings.caption)
    screen.fill(settings.colors["grey"])
    return screen

def update_screen(screen, agents):
    functions.create_rectangle_agents(screen, agents)
    pygame.display.update()
