import random

import pygame,balk, garage

class Level():
    def __init__(self):
        p= balk.Balk(0, 48)
        self.image_balk = p.beam_building()
        self.list=[]
        self.level_maker()


    def maker(self):
        for l in self.list:
            pygame.display.get_surface().blit(l['image'], l['rect'])

    def rects_maker(self):
        for l in self.list:
            pygame.draw.rect(pygame.display.get_surface(), '#ffffff', l['rect'], 1)
    def level_maker(self):
        for a in range(5):
            v={}
            image_balk=self.image_balk
            angle=2
            if a!=0 and a%2>0:
                image_balk = pygame.transform.rotate(self.image_balk,-angle)
                v['angle']=-(90+angle)
                h=[]

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
        self.list[-1]['rect'].left+=50
        self.list[-3]['rect'].left+=50
        self.list[-5]['rect'].left+=50
    def add_ladder(self):
        for a in range(1,len(self.list)-1):
            h=[]
            self.garage=garage.Garage(self.list[a], self.list[a - 1])
            for l in range(random.randint(1, 3)):
                h.append(garage.ladder)
            self.list[a]['bottom_ladder']=h
            self.list[a-1]['top_ladder']=h
            print(self.list[a]['bottom_ladder'])





