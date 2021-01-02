import pygame
import random
import settings


class Agent:
    def __init__(self, color, position):
        self.color = color  # blue, red, beige, black
        self.position = position

    def create_rectangle(self, screen):
        pygame.draw.rect(screen, self.color, (self.position))


def create_positions():
    # (x, y, width, height)
    positions = []
    for i in range(5):
        for j in range(5):
            positions.append((j * 100 + 10, i * 100 + 10, 80, 80))
    return positions


def create_rectangle_agents(screen, agents):
    agents_in_game = []
    positions = create_positions()
    for i, agent in enumerate(agents):
        agents_in_game.append(Agent(settings.colors[agent], positions[i]).create_rectangle(screen))
    return agents_in_game


def choose_starting_team():
    start = ["red", "blue"]
    random.shuffle(start)
    return start


def create_new_key(start):
    agents = [start[0] for _ in range(9)]
    agents += [start[1] for _ in range(8)]
    agents += ["beige" for _ in range(7)]
    agents += ["black"]
    random.shuffle(agents)
    return agents


def show_key(start, agents):
    print(f'Starting team: {start[0]}\n')
    for i in range(5):
        print(agents[5 * i:5 * (i + 1)])


def create_key_card():
    start = choose_starting_team()
    agents = create_new_key(start)
    show_key(start, agents)
    return start, agents

