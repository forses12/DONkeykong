import pygame, ladder

class Garage():
    def __init__(self,balk,bottom_balk):
        self.top_balk=balk
        self.bottom_balk=bottom_balk
        self.lader=ladder.Ladder(self.top_balk,self.bottom_balk)

