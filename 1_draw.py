import pygame
from pygame.draw import *

def new_surface (width, height, color):
    screen = pygame.display.set_mode((400, 400))
    rect (screen, color, (0, 0, width, height))
    return screen
'''
'''
def face (surface, color, border_color, center, radius, border_width):
    circle(surface, border_color, center, radius + border_width)        
    circle(surface, color, center, radius)
'''
fuck this shit
'''
def eye (surface, color, pupil_color, border_color, pupil_border_color, center, radius, pupil_radius, border_width, pupil_border_width):
   circle(surface, border_color, center, radius + border_width)
   circle(surface, color, center, radius)
   circle(surface, pupil_border_color, center, pupil_radius + pupil_border_width)
   circle(surface, pupil_color, center, pupil_radius)
'''
'''
def mouth (surface, color, border_color, center_x, center_y, width, height, border_width):
    rect(surface, border_color, (center_x - width/2 - border_width, center_y + height/2 + border_width, width + 2*border_width, height + 2*border_width))
    rect(surface, color, (center_x - width/2, center_y + height/2, width, height))
'''
'''
def eyebrow (surface, color, points):
    polygon(surface, color, points)
'''
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
