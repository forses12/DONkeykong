import pygame ,model


def control():
    event = pygame.event.get()
    model.b.controller(event)
    for e in event.copy():
        if e.type == pygame.QUIT:
            exit()