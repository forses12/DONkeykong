import pygame,balk

class Level():
    def __init__(self):
        p= balk.Balk(25, 48)
        self.balk = p.beam_building()
        self.balk = pygame.transform.rotate(self.balk, -10)
    def sozdavatel(self):
        pygame.display.get_surface().blit(self.balk, [0, 12])
