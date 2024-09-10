import math

import pygame, math_utils

pygame.init()
img_1 = 'img_1.png'
img_1 = pygame.image.load(img_1)
img_1 = pygame.transform.scale(img_1, [img_1.get_width() * 3, img_1.get_width() * 3])
p = pygame.event.custom_type()
d = pygame.event.custom_type()


class Barrel():
    def __init__(self, listp):
        self.rect = pygame.rect.Rect(1000, 50, img_1.get_width(), img_1.get_height())
        self.list = listp
        self.dpc_helper()

        if self.c['angle'] < 0:
            self.rect.centerx = self.c['rect'].left
            self.rect.bottom = self.c['rect'].top + 1


        else:
            self.rect.centerx = self.c['rect'].right
            self.rect.bottom = self.c['rect'].top + 1

        pygame.time.set_timer(p, 10)
        pygame.time.set_timer(d, 100)
        self.center = list(self.rect.center)
        self.can_go = True
        self.angle=0
        self.img_1=img_1

    def maker(self):
        pygame.display.get_surface().blit(self.img_1, self.rect)
    def coup(self):
        global img_1
        self.angle+=90
        self.angle=self.angle%360
        self.img_1 = pygame.transform.rotate(img_1, self.angle)

    def rects_maker(self):
        pygame.draw.rect(pygame.display.get_surface(), '#ffffff', self.rect, 1)

    def go(self):

        self.center = math_utils.get_point_by_angle([*self.center], self.c['angle'], 3)
        # self.rect.center=math_utils.get_point_by_angle([*self.rect.center],92,3)
        self.rect.center = self.center

    def move(self):

        if self.can_go:
            self.go()
        else:
            self.fall()
        self.dpc()


    def controller(self, event):
        print(self.rect)
        for e in event:
            if e.type == p: self.move()
            if e.type == d: self.coup()


    def dpc(self):
        if not self.rect.colliderect(self.c['rect']):
            self.dpc_helper()
            self.can_go = False
        else:
            self.rect.bottom = self.dpc_math(self.c)
            self.can_go = True

    def fall(self):
        self.center[1] += 3
        self.rect.center = self.center

    def dpc_helper(self):
        best_balk = []
        for c in self.list:
            if      c['rect'].left <= self.rect.right and \
                    c['rect'].right >= self.rect.left and \
                    c['rect'].top > self.rect.top:
                best_balk.append(c)

        y = 10000
        for c in best_balk:
            if y > c['rect'].top:
                self.c = c
                y = c['rect'].top

    def dpc_math(self, balk):
        # angle = abs(balk['angle']) - 90
        # if balk['angle'] > 0:
        #     x = balk['rect'].right - self.rect.centerx
        #
        # elif balk['angle'] < 0:
        #     x = self.rect.centerx - balk['rect'].left
        #
        # y = balk['rect'].top + math.tan(math.radians(angle)) * x
        y=math_utils.get_y_by_angle_and_x(balk['rect'],balk['angle'],self.rect.centerx)
        return y
