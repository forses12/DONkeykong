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
        y=list[0]['rect'].top
        for c in list:
            if y>c['rect'].top:
                y=c['rect'].top
                self.c=c

        if self.c['angle']<0:
            self.rect.center=[self.c['rect'].left,self.c['rect'].top-self.rect.height/2]

        else:
            self.rect.center = [self.c['rect'].right, self.c['rect'].top - self.rect.height / 2]

        pygame.time.set_timer(p, 10)
        self.center=self.rect.center
        self.can_go=True

    def maker(self):
        pygame.display.get_surface().blit(img_1,self.rect)

    def rects_maker(self):
        pygame.draw.rect(pygame.display.get_surface(), '#ffffff', self.rect, 1)

    def go(self):

        self.center = math_utils.get_point_by_angle([*self.center], self.c['angle'], 3)
        # self.rect.center=math_utils.get_point_by_angle([*self.rect.center],92,3)
        self.rect.center=self.center

    def controller(self,event):
        self.dpc()
        for e in event:
            if e.type==p and self.can_go:
                self.go()
            elif e.type==p:
                self.fall()
    def dpc(self):
        if (self.c['angle']>0 and self.c['rect'].left>=self.rect.right and self.can_go) or \
            (self.c['angle']<0 and self.c['rect'].right<=self.rect.left and self.can_go):
            self.can_go=False
        elif not self.can_go:
            for c in self.list:
                if c['rect'].left<=self.rect.right and c['rect'].right>=self.rect.left:
                    self.list.remove(self.c)
                    self.c=c
                    if self.rect.bottom>=c['rect'].top:
                        self.can_go = True


    def fall(self):
        self.center[1]+=3
        self.rect.center = self.center



