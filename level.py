import pygame,balk

class Level():
    def __init__(self):
        p= balk.Balk(0, 48)
        self.image_balk = p.beam_building()
        self.list=[]
        self.level_maker()

    def maker(self):
        for l in self.list:
            pygame.display.get_surface().blit(l['image'], l['rect'])
            pygame.draw.rect(pygame.display.get_surface(),'#ffffff',l['rect'],1)
    def level_maker(self):
        for a in range(5):
            v={}
            image_balk=self.image_balk
            angle=2
            if a!=0 and a%2>0:
                image_balk = pygame.transform.rotate(self.image_balk,-angle)
                v['angle']=-(90+angle)
            elif a!=0 and a%2==0:
                image_balk = pygame.transform.rotate(self.image_balk, angle)
                v['angle'] = 90+angle
            else:
                v['angle']=90
            v["image"]=image_balk
            l=pygame.rect.Rect(50,650-(image_balk.get_height()+50)*a,
                               image_balk.get_width(),image_balk.get_height())
            v['rect']=l
            self.list.append(v)






