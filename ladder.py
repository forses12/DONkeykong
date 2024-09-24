import pygame,img_helper,random ,math_utils,math


v=img_helper.loader("ladder_top.png",'ladder_middle.png','ladder_bottom.png',folder='DonkeyKong/items/ladder/green/')


class Ladder():
    def __init__(self,top_balk,bottom_balk,level):
        self.ladder_top, self.ladder_middle, self.ladder_bottom = v
        self.rect=pygame.Rect(0,0,10,10)
        self.topbalk=top_balk
        self.bottombalk=bottom_balk
        self.images={}
        self.level=level
        self.ladder_maker()

    def ladder_maker(self):
        left=self.side('left')
        right=self.side('right')
        f=[]
        for  a in self.topbalk['bottom_ladder']:
            f.append(a.rect.centerx)
        self.rect.centerx=self.math(f,left,right,100)
        self.rect.top=self.level.get_balk_y_by_x(self.rect.centerx,self.topbalk,'bottom')
        self.rect.height=self.level.get_balk_y_by_x(self.rect.centerx,self.bottombalk,'top')-self.rect.top
        self.rect.width=self.ladder_bottom.get_width()
        self.calculation_stairs()

    def calculation_stairs(self):
        a=self.rect.height//self.ladder_middle.get_height()
        b=self.rect.height%self.ladder_middle.get_height()
        x=[]
        y=[]
        x.append(pygame.transform.scale(self.ladder_top,[self.rect.width,b]))
        y.append([self.rect.x, self.rect.y])
        for l in range(a):
            x.append(self.ladder_middle)
            y.append([self.rect.x,self.rect.y+self.ladder_middle.get_height()*l+b])
        self.images['image']=x
        self.images['xy']=y

    def side(self,side):
        if side=='left':
            if self.topbalk['rect'].left<self.bottombalk['rect'].left:
                x=self.bottombalk['rect'].left+50
            else :
                x=self.topbalk['rect'].left+50
        else:
            if self.topbalk['rect'].right > self.bottombalk['rect'].right:
                x = self.bottombalk['rect'].right - 50
            else:
                x = self.topbalk['rect'].right - 50
        return x
    @staticmethod
    def garage(balk,bottom_balk,level):
        lader=Ladder(balk,bottom_balk,level)
        return lader

    @staticmethod
    def math(list,start,stop,minimaldis):
        while True:
            x = random.randint(start, stop)
            for a in list:
                left=a-minimaldis
                right=a+minimaldis
                if x<left or x>right:
                    continue
                else:
                    x = 0
                    break
            if x !=0:
                return x









        # while True:
        #     x = random.randint(left, right)
        #     for k in self.topbalk['bottom_ladder']:
        #         if x + 100 < k.rect.left or x - 100 > k.rect.right:
        #             continue
        #         else:
        #             x = 0
        #             break
        #     if x != 0:
        #         self.rect.centerx = x
        #         break





