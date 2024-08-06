import pygame, math_utils

img_1 = 'img_1.png'
img_1 = pygame.image.load(img_1)
img_1 = pygame.transform.scale(img_1, [img_1.get_width() * 3, img_1.get_height() * 3])

class Barrel():
    def __init__(self):
        self.rect=pygame.rect.Rect(500,500,img_1.get_width(),img_1.get_height())
    def maker(self):
        pygame.display.get_surface().blit(img_1,self.rect)
        pygame.draw.rect(pygame.display.get_surface(), '#ffffff', self.rect, 1)
    def go(self,list):

        self.rect.center=[list['rect'].right,list['rect'].top-15]
        self.rect.center=math_utils.get_point_by_angle([*self.rect.center],92,1000)


