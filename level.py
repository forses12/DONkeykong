import pygame,balk

class Level():
    def __init__(self):
        p= balk.Balk(0, 48)
        self.image_balk = p.beam_building()
        self.list=[]
        self.level_maker()

    def sozdavatel(self):
        for l in self.list:
            pygame.display.get_surface().blit(self.image_balk, [l.left, l.top])
            pygame.draw.rect(pygame.display.get_surface(),'#ffffff',l,1)
    def level_maker(self):
        for a in range(3):
            l=pygame.rect.Rect(50,650-(self.image_balk.get_height()+50)*a,
                               self.image_balk.get_width(),self.image_balk.get_height())
            self.list.append(l)
            print(l)





