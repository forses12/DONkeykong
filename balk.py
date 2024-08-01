import pygame

beam1 = 'beam1.png'

image1 = pygame.image.load(beam1)

beam1= pygame.transform.flip(image1, 0, 1)

beam1 = pygame.transform.scale(beam1, [image1.get_width() * 3, image1.get_height() * 3])



class Balk():
    def __init__(self,x,how_many):
        self.x=x
        self.how_many=how_many

        self.list=[]
        self.image=beam1
    def maker(self):
        balk=pygame.surface.Surface([self.how_many*beam1.get_width(),beam1.get_height()],pygame.SRCALPHA)
        for beam in self.list:
            balk.blit(self.image,[beam.x,0])
        return balk
    def beam_building(self):
        for beam in range(self.how_many):
            xy=[self.x+beam1.get_width()*beam,0]
            rect=pygame.Rect(xy,beam1.get_size())
            self.list.append(rect)

            print(xy)
        return self.maker()

