import pygame,model
screen=pygame.display.set_mode([1800,1300])

def view():
    screen.fill([0,0,0])
    if model.show_racts:
        model.l.rects_maker()
        model.b.rects_maker()
    if model.show_images:
        model.l.maker()
        model.b.maker()

    pygame.display.flip()