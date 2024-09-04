import pygame, ladder


for f in range(10000000):
    a=ladder.Ladder.math([70,96,460],50,600,50)
    if a>70 and a<96:
        print(a)