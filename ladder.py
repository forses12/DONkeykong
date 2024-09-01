import pygame,img_helper,random


v=img_helper.loader("ladder_top.png",'ladder_middle.png','ladder_bottom.png',folder='DonkeyKong/items/ladder/green/')


class Ladder():
    def __init__(self,top_balk,bottom_balk):
        self.ladder_top, self.ladder_middle, self.ladder_bottom = v
        self.rect=pygame.Rect(0,0,10,10)
        self.topbalk=top_balk
        self.bottombalk=bottom_balk
        self.ladder_maker()

    def rects_maker(self):
        pygame.draw.rect(pygame.display.get_surface(), '#ffffff', self.rect, 1)

    def maker(self):

        pass
    def ladder_maker(self):
        left=self.side('left')
        right=self.side('right')
        x=random.randint(left,right)

    def side(self,side):
        if side=='left':
            if self.topbalk['rect'].left<self.bottombalk['rect'].left:
                x=self.bottombalk['rect'].left+50
            else :
                x=self.topbalk['rect'].left+50
        else:
            if self.topbalk['rect'].right < self.bottombalk['rect'].right:
                x = self.bottombalk['rect'].right + 50
            else:
                x = self.topbalk['rect'].right + 50
        return x




