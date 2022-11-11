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
        """ Конструктор класса ball Args: x - начальное положение мяча по горизонтали y - начальное положение мяча по вертикали """
        self.screen = screen 
        self.x = x 
        self.y = y 
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.age = 1 

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXED (g == 5)
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
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXED
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2 :
            print("HIT")
            return True 
        return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        # FIXIT DUDE WHAT ARE YOU STUPID OR SOMETHING?
        pygame.draw.rect(self.screen, self.color, (40, 450, 50, 10))
        pygame.draw.line(self.screen, self.color, (65, 440), (65 + 10 * math.cos(self.an), 440 - 50*math.sin(self.an)),         width = 5)
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__ (self, screen):
    # self.points = 0
    # self.live = 1
    # FIXED
        """ Инициализация новой цели. """
        self.screen = screen
        self.points = 0
        self.live = 1
        x = self.x = random.randrange(600, 780)
        y = self.y = random.randrange(300, 550)
        r = self.r = random.randrange(2, 50)
        color = self.color = RED
    def new_target(self):
        print("NEW TARGET")
        self.live = 1
        self.points = 0
        x = self.x = random.randrange(600, 780)
        y = self.y = random.randrange(300, 550)
        r = self.r = random.randrange(2, 50)
        color = self.color = RED
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
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
        if b.hittest(target) and target.live:
            target.live = 0
            target.new_target()
            target.hit()
            target.draw()
        if b.age > 130:
            balls.remove(b)
    gun.power_up()

pygame.quit()
