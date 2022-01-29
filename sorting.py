import pygame as p
from button import Button 
from staple import Staple
import random
import time
import sys


WIDTH = 980
HEIGHT = 980
MAX_FPS = 60
p.init()
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
smallfont = p.font.SysFont('Corbel',35)
quit_text = smallfont.render('quit' , True , WHITE)
bubble_text = smallfont.render("Bubble", True, WHITE)
insertion_text = smallfont.render("Insertion", True, WHITE)
scramble_text = smallfont.render("Scramble", True, WHITE)
number_of_staples = 50

button_list = []
button_map = {}

QUIT_BUTTON = Button( 0, 0, 100, 100, RED, quit_text)
button_list.append(QUIT_BUTTON)
button_map[QUIT_BUTTON] = "quit"

BUBBLESORT_BUTTON = Button( 150, 0, 100, 100, RED, bubble_text)
button_list.append(BUBBLESORT_BUTTON)
button_map[BUBBLESORT_BUTTON] = "Bubblesort"

INSERTIONSORT_BUTTON = Button(300, 0, 100, 100, RED, insertion_text)
button_list.append(INSERTIONSORT_BUTTON)
button_map[INSERTIONSORT_BUTTON] = "Insertionsort"

SCRAMBLE_BUTTON = Button(450, 0, 100,100, RED, scramble_text)
button_list.append(SCRAMBLE_BUTTON)
button_map[SCRAMBLE_BUTTON] = "Scramble"

def create_staples(number_of_staples):
    staple_list = []
    staple_width = WIDTH/number_of_staples
    for i in range(0,number_of_staples):
        staple = Staple(staple_width*i, HEIGHT, staple_width, -random.randint(0, 3*HEIGHT)/4, BLUE)
        staple_list.append(staple)
    return staple_list

def bubblesort(staple_list, screen, clock):

    n = len(staple_list) - 1
    for j in range(n, 0, -1):
        for i in range(j):
            if abs(staple_list[i].height) > abs(staple_list[i+1].height):
                #staple_list[i].color = RED
                #staple_list[i+1].color = RED
                staple_list[i].height, staple_list[i+1].height = staple_list[i+1].height, staple_list[i].height
            n -= 1
            #time.sleep(0.1)
            draw_objects(screen, clock, button_list, staple_list)
            #staple_list[i].color = BLUE
            #staple_list[i+1].color = BLUE
    return staple_list

def insertionsort(staple_list, screen, clock):
    for i in range(1, len(staple_list)):
        key = staple_list[i].height
        j = i - 1
        while j >= 0 and abs(key) < abs(staple_list[j].height):
            staple_list[j+1].height = staple_list[j].height
            draw_objects(screen, clock, button_list, staple_list)
            j -= 1
        staple_list[j+1].height = key
    return staple_list

def draw_objects(screen, clock, button_list, staple_list):
    clock.tick(MAX_FPS)
    screen.fill(p.Color("Black"))
    for button in button_list:
        button.draw(screen)
    for staple in staple_list:
        #print(abs(staple.height))
        staple.draw(screen)
    p.draw.line(screen, WHITE, (0, HEIGHT/4), (WIDTH, HEIGHT/4))
    p.display.flip()


def main():
    screen = p.display.set_mode((WIDTH, HEIGHT)) #create the screen
    clock = p.time.Clock() #create a clock
    staple_list = create_staples(number_of_staples)
    run = True
    while run:
            for event in p.event.get():
                if event.type == p.QUIT:
                    run = False
                elif event.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos() #(x,y) location of mouse
                    x = location[0]
                    y = location[1]
                    for button in button_list:
                        if button.check_if_clicked(x,y):
                            action = button_map[button]
                            if action == "quit":
                                run = False
                            elif action == "Bubblesort":
                                staple_list = bubblesort(staple_list, screen, clock)
                            elif action == "Insertionsort":
                                staple_list = insertionsort(staple_list, screen, clock)
                            elif action == "Scramble":
                                staple_list = create_staples(number_of_staples)
            draw_objects(screen, clock, button_list, staple_list)

if __name__ == "__main__":
    main()