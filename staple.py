import pygame as p

class Staple():
    def __init__(self, x, y, length, height, color):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.color = color

    def draw(self,screen):
         p.draw.rect(screen, self.color, [ self.x, self.y, self.length, self.height])