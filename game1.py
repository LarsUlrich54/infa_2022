import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]
def mouse_hit(event, x ,y, r):
    '''checks if a mouse click has hit the ball'''
    if (x-event.pos[0])**2 + (y-event.pos[1])**2 <= r**2:
        print("NICE!")
        return True
    return False

def pts_update(r):
    '''adds the points to the player's score. The amount of points depends on the radius of the ball hit'''
    global pts 
    pts = pts + 100/r
def pts_show(pts, name):
    ''' shows points that the player has got'''
    print(name, " - ", pts)

def new_ball():
    '''рисует новый шарик'''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    print(x,y,r)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
def mouse_action(event):
    ''' function that is called when MOUSEBUTTONDOWN happens. '''
    print("CLICK")
    if mouse_hit (event, x, y, r) == True: 
        pts_update(r)

def player_set():
    '''sets the player name an creates his points'''
    global name, pts
    name = input()
    pts = 0

pygame.display.update()
clock = pygame.time.Clock()
finished = False
player_set()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_action(event)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
pts_show(pts, name)
