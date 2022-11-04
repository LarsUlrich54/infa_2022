import pygame
from pygame.draw import *

def new_surface (width, height, color):
    screen = pygame.display.set_mode((400, 400))
    rect (screen, color, (0, 0, width, height))
    return screen

'''
Creates the screen, where you can draw

width (int) - width of the screen
height (int) - height of the screen
color ((int, int, int) or pygame.Color) - color to fill the screen with given either by the tuple of coordinates in RGB basis or pygame.Color variable
returns pygame.Surface - the created screen

'''

def face (surface, color, border_color, center, radius, border_width):
    circle(surface, border_color, center, radius + border_width)        
    circle(surface, color, center, radius)

''' 
Draws an empty face on a given screen with

surface (pygame.Surface) - the screen to draw on
color ((int, int, int) or pygame.Color) - the color of face given either by the tuple of coordinates in RGB basis or pygame.Color variable
border_color ((int, int, int) or pygame.Color) - the color of face's border given either by the tuple of coordinates in RGB basis or pygame.Color variable
center ((int, int)) - the coordinates of the centre of the face
radius (int) - radius of the face
border_width (int) - the width of the face's border
'''
def eye (surface, color, pupil_color, border_color, pupil_border_color, center, radius, pupil_radius, border_width, pupil_border_width):
   circle(surface, border_color, center, radius + border_width)
   circle(surface, color, center, radius)
   circle(surface, pupil_border_color, center, pupil_radius + pupil_border_width)
   circle(surface, pupil_color, center, pupil_radius)
'''
Draws an eye with a pupil on a given surface

surface (pygame.Surface) - the screen to draw on
color ((int, int, int) or pygame.Color) - the color of the eye given either by the tuple of coordinates in RGB basis or pygame.Color variable
pupil_color ((int, int, int) or pygame.Color) - the color of the pupil given either by the tuple of coordinates in RGB basis or pygame.Color variable
border_color ((int, int, int) or pygame.Color) - the color of eye's border given either by the tuple of coordinates in RGB basis or pygame.Color variable
border_color ((int, int, int) or pygame.Color) - the color of face's border given either by the tuple of coordinates in RGB basis or pygame.Color variable
pupil_border_color ((int, int, int) or pygame.Color) - the color of eye pupil's border given either by the tuple of coordinates in RGB basis or pygame.Color variable
center ((int, int)) - the coordinates of the centre of the eye
radius (int) - radius of the eye
pupil_radius (int) - radius of the pupil
border_width (int) - the width of the pupil's border
pupil_border_width (int) - the width of the pupil's border

'''
def mouth (surface, color, border_color, center_x, center_y, width, height, border_width):
    rect(surface, border_color, (center_x - width/2 - border_width, center_y + height/2 + border_width, width + 2*border_width, height + 2*border_width))
    rect(surface, color, (center_x - width/2, center_y + height/2, width, height))
'''
Draws a mouth in a shape of a horizontal rectangle on a given screen

surface (pygame.Surface) - the screen to draw on
color ((int, int, int) or pygame.Color) - the color of the mouth given either by the tuple of coordinates in RGB basis or pygame.Color variable
border_color ((int, int, int) or pygame.Color) - the color of mouth's border given either by the tuple of coordinates in RGB basis or pygame.Color variable
center_x (int) - x coordinate of the mouth.
center_y (int) - y coordinate of the mouth.
width (int) - width of the mouth
height (int) - height of the mouth (how wide it is open)

'''
def eyebrow (surface, color, points):
    polygon(surface, color, points)
'''
Draws an eyebrow in a shape of arbitrary polygon

surface (pygame.Surface) - the screen to draw on
color ((int, int, int) or pygame.Color) - the color of the mouth given either by the tuple of coordinates in RGB basis or pygame.Color variable
points (tuple (int, int)) - the tuple of coordinates of every vertex of the pollygon

'''
pygame.init()

FPS = 30
screen = new_surface(400, 400, (155, 155, 155))
face (screen, (255, 255, 0), (0, 0, 0), (200, 200), 100, 2)
mouth (screen, (0, 0, 0), (0, 0, 0), 200, 200, 100, 20, 0)
eye (screen, (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (150, 150), 20, 10, 2, 0) 
eye (screen, (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (250, 150), 20, 10, 2, 0) 
eyebrow (screen, (0, 0, 0),[(100,400-310), (106,400-316),  (189,400-258), (183, 400-252)])
eyebrow (screen, (0, 0, 0), [(210,400-247), (204,400-256),  (304,400-326), (310, 400-317)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
