import pygame
def loader(*args,folder):
    a=[]
    for c in args:
        f=pygame.image.load(folder+c)
        f = pygame.transform.scale(f, [f.get_width() * 3, f.get_height() * 3])

        a.append(f)
    return a