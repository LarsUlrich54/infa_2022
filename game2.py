import pygame
from pygame.draw import *
from random import randint
pygame.init()
FPS = 2

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

def player_set():
    '''sets the player name an creates his points'''
    global name, pts
    name = input()
    pts = 0

print ("Please, state your name")
player_set()
FPS = 2
screen = pygame.display.set_mode((1200, 900))

def mouse_hit(event, balls):
    '''checks if a mouse click has hit any balls, removes all the hit balls, and adds points for every ball hit'''
    for ball in balls:
        if (ball[1][0]-event.pos[0])**2 + (ball[1][1]-event.pos[1])**2 <= ball[2]**2:
            pts_update(ball[2])
            balls.remove(ball)
    return balls

def new_ball(balls):
    '''creates a new random ball and appends it to the list of balls'''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    print(x,y,r)
    color = COLORS[randint(0, 5)]
    balls.append([color, (x,y), r])

def draw_balls(balls):
    '''draws all the balls that are on the screen at the moment'''
    screen.fill(BLACK)
    for ball in balls:
        circle(screen, ball[0], ball[1], ball[2])        

def pts_update(r):
    '''updates the player's score. The amount of points depends on the radius of the ball hit'''
    global pts 
    pts = pts + 100/r

def pts_show(pts, name):
    '''shows points that the player has got'''
    print(name, " - ", pts)

def leaderboard_update(player, points):
    ''' updates the leaderboard '''
    board1 = list()
    f = open("leaderboard.txt", "r",  encoding = "utf-8")
    for line in f:
        s = line.split()
        board1.append((s[0], float(s[1])))
    f1 = open("leaderboard.txt", "w")
    board1.append((player, points))
    board1.sort(key = lambda x: -x[1])
    for player in board1:
        f1.write("%s\n" % (player[0] + ' ' + str(player[1])))
#main

balls = list()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Click")
            balls = mouse_hit(event, balls)
    new_ball(balls)
    draw_balls(balls)
    pygame.display.update()
pygame.quit()
leaderboard_update(name, pts)
