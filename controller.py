import pygame


def control():
    event = pygame.event.get()
    for e in event.copy():
        if e.type == pygame.QUIT:
            exit()