import pygame,balk

class Level():
    def __init__(self):
        p= balk.Balk(0, 48)
        self.image_balk = p.beam_building()
        self.list=[]
        self.list_image=[]
        self.level_maker()

    def sozdavatel(self):
        for l in range(len(self.list)):
            pygame.display.get_surface().blit(self.list_image[l], [self.list[l].left, self.list[l].top])
            pygame.draw.rect(pygame.display.get_surface(),'#ffffff',self.list[l],1)
    def level_maker(self):
        for a in range(5):
            image_balk=self.image_balk
            if a!=0 and a%2>0:
                image_balk = pygame.transform.rotate(self.image_balk,-2)
            elif a!=0 and a%2==0:
                image_balk = pygame.transform.rotate(self.image_balk, 2)

            l=pygame.rect.Rect(50,650-(image_balk.get_height()+50)*a,
                               image_balk.get_width(),image_balk.get_height())
            self.list.append(l)
            self.list_image.append(image_balk)






