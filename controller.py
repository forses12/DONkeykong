import pygame ,model


def control():
    event = pygame.event.get()
    model.b.controller(event)
    for e in event.copy():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYUP and e.key == pygame.K_TAB:
            model.show_racts = not model.show_racts
        if e.type == pygame.KEYUP and e.key == pygame.K_q:
            model.show_images = not model.show_images
