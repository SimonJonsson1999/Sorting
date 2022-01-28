import pygame as p

class Button():
    def __init__(self, x, y, length, height, color, text):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.color = color
        self.text = text


    def draw(self, screen):
        p.draw.rect(screen, self.color,[ self.x, self.y, self.length, self.height])
        screen.blit(self.text, (self.x, self.y))


    def check_if_clicked(self, mouse_x, mouse_y):
        if (self.x <= mouse_x <= self.x + self.length) and (self.y <= mouse_y <= self.y + self.height):
            return True
        else:
            return False


