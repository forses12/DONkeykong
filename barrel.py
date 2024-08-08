import pygame, math_utils
pygame.init()
img_1 = 'img_1.png'
img_1 = pygame.image.load(img_1)
img_1 = pygame.transform.scale(img_1, [img_1.get_width() * 3, img_1.get_height() * 3])
p = pygame.event.custom_type()

class Barrel():
    def __init__(self,list):
        self.rect=pygame.rect.Rect(500,500,img_1.get_width(),img_1.get_height())
        self.list=list
        y=0
        self.c=None
        for c in list:
            if c['rect'].top>y:
                y=c['rect'].top
                self.c=c
        if self.c['angle']<0:
            self.rect.center=[self.c['rect'].left,c['rect'].top-self.rect.height/2]
        else:
            self.rect.center = [self.c['rect'].right, c['rect'].top - self.rect.height / 2]
        pygame.time.set_timer(p, 10)
        self.center=self.rect.center

    def maker(self):
        pygame.display.get_surface().blit(img_1,self.rect)
        pygame.draw.rect(pygame.display.get_surface(), '#ffffff', self.rect, 1)
    def go(self):

        self.center = math_utils.get_point_by_angle([*self.center], self.c['angle'], 3)
        # self.rect.center=math_utils.get_point_by_angle([*self.rect.center],92,3)
        self.rect.center=self.center

    def controller(self,event):
        for e in event:
            if e.type==p:
                self.go()
    def dpc(self):
        pass
    def fall(self):
        self.center[1]+=3
        self.rect.center = self.center

q

