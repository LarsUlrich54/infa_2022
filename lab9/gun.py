import math
from random import choice
import pygame
import random

FPS = 60

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=65, y=440):
        """ the class that represents the projectile 
        attributes: screen (pygame.surface) - the surface where the game goes on.
                    x, y, r, vx, vy (float) - coordinates, size and velocities of the projectile.
                    color (pygame.color) - the color of the projectile. Is set randomly from GAME_COLORS.
                    self.age (int) - the number of frames that the projectile is existent for. The projectile is 
                    removed when it gets "too old". 
        """
        self.screen = screen 
        self.x = x 
        self.y = y 
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.age = 1 

    def move(self):
        """Moving the ball and updates its state every quant of time.
           
           Updates the coordinates of the projectile and its velocity (using the laws of kinematic fall with g = 5, 
           the bounce is not perfect - the body loses 5% of energy).
        """
        if self.x - self.r <= 0 and self.vx < 0:
            self.vx = -self.vx 
        if self.y - self.r <= 0 and self.vy < 0:
            self.vy = -self.vy * 0.95 + 2
            self.x += self.vx
            return
        if self.x + self.r >= WIDTH and self.vx > 0:
            self.vx = -self.vx
        if self.y + self.r >= HEIGHT and self.vy > 0:
            self.vy = -self.vy * 0.95 + 2
            self.x += self.vx
            return
        self.x += self.vx
        self.y += self.vy
        self.vy += 2
        self.age += 1
    def draw(self):
        ''' draws the projectile in a shape of a circle '''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """ Checks if the projectile has hit the target.
            The condition of hit is the distance between the projectile and the object being less than the 
            sum of radiuses.

        Args:
            obj (Class.Target) - the target.
        Returns:
            True if there is a hit.
            False else.
        """
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2 :
            print("HIT")
            return True 
        return False


class Gun:
    def __init__(self, screen):
        ''' The class that represents the guns.
        Attributes: screen (pygame.surface) - the surface where stuff goes on
                    f2_power (int) - the power of the shot (represents the length of the barrel and
                                     initial velovity of the projectile.
                    f2_on (int) - atribute that represents the begining of the shot. 
                    an (float) - atribute that represents the begining of the shot. 
                    color (pygame.color) - gun's color.
        '''
        self.screen = screen 
        self.f2_power = 10  
        self.f2_on = 0 
        self.an = 1
        self.color = GREY 

    def fire2_start(self, event):
        ''' when the mouse is pushed'''
        self.f2_on = 1

    def fire2_end(self, event):
        """Starts the shot
        Called when the mouse id relesaed.
        Creates a new ball and appends it to the list of balls.
        event (pygame.event) - event from pygame used for interaction with user.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = -math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Targetting. Depends on mouse position.
            event (pygame.event) - module for interaction with user's actions. event.pos[0], event.pos[1] are mouse's
            coordinates. 
            Sets up the angle that the gun is pointing at (and which is going to determine projectile's initial
            speed).
            If the gun is active, its color is RED. If its inactive, its GREY"""
        if event and not event.pos[1] - 450 == 0 and not event.pos[0] == 20:
            self.an = -math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        '''Draws the Gun in a shape of a rectange with a linear barrel, that is pointing where user is aiming.'''
        pygame.draw.rect(self.screen, self.color, (40, 450, 50, 10))
        pygame.draw.line(self.screen, self.color, (65, 450), (65 + self.f2_power * math.cos(self.an), 450 - self.f2_power*math.sin(self.an)),         width = 5)
    def power_up(self):
        '''Increases the attribute self.f2_power which represents the module of initial velocity that the projectile is          going to get''' 
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__ (self, screen):
        """ The class that represents the targets. 
            Attributes:
                        screen (pygame.surface) - surface where the game is going on 
                        points (int) - ????
                        live (int) - attribute to determine if the target is alive (or hit) 
                        x, y, r (float) - The following are atributes of target (it's position and radius) 
                        color (pygame.color) - target's color
        """
        self.screen = screen 
        self.points = 0
        self.live = 1 
        x = self.x = random.randrange(600, 780) 
        y = self.y = random.randrange(300, 550)
        r = self.r = random.randrange(2, 50)
        vy = self.vy = random.randrange (1, 5) 
        color = self.color = RED
    def draw(self):
        ''' Draws the target in a shape of a circle '''
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
    def hit(self, points=1):
        ''' Called if the target is hit '''
        self.points += points
    def move(self):
        ''' Moves the target with a certain speed '''
        if self.y - self.r <= 0 and self.vy < 0:
            self.vy = -self.vy 
            return
        if self.y + self.r >= HEIGHT and self.vy > 0:
            self.vy = -self.vy 
            return
        
        self.y += self.vy 
def targets_draw(targets):
    ''' Draws every target in targets()
    Args:
        targets (list) - list of all available targets
    '''
    for t in targets:
        t.draw()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = list()

clock = pygame.time.Clock()
gun = Gun(screen)
targets.append(Target(screen))
targets.append(Target(screen))
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    targets_draw(targets)
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        for target in targets:
            if b.hittest(target) and target.live:
                target.live = 0
                target.hit()
                targets.remove(target)
                targets.append(Target(screen))
        if b.age > 130:
            balls.remove(b)
    for target in targets:
        target.move()
    gun.power_up()

pygame.quit()
