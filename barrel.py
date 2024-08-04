import pygame

img_1 = 'img_1.png'
image1 = pygame.image.load(img_1)
img_1 = pygame.transform.scale(img_1, [image1.get_width() * 3, image1.get_height() * 3])

class Barrel():
