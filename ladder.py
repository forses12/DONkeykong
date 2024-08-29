import pygame,img_helper,random


v=img_helper.loader("ladder_top.png",'ladder_middle.png','ladder_bottom.png',folder='DonkeyKong/items/ladder/green/')


class Ladder():
    def __init__(self):
        self.ladder_top, self.ladder_middle, self.ladder_bottom = v
        self.rect=pygame.Rect(0,0,10,10)
    def rects_maker(self):
        pygame.draw.rect(pygame.display.get_surface(), '#ffffff', self.rect, 1)

    def maker(self):

        pass
    def ladder_maker(self,balk,bottom_balk):
        self.rect.left=balk['rect'].left
        self.rect.top=balk['rect'].bottom




