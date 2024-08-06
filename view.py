import pygame,model
screen=pygame.display.set_mode([1400,700])

def view():
    screen.fill([0,0,0])
    model.l.maker()
    model.b.maker()
    pygame.display.flip()