import Paint
import Values
import pygame


class Obstacle:
    pygame.init()

    x = 0
    y = 0
    w = 0
    h = 0
    offset = 10
    alive = True
    obstacle_hori_img = ''
    obstacle_vert_img = ''

    def __init__(self, x, y, w, h, planet):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.obstacle_hori_img = pygame.image.load(planet.img_h)
        self.obstacle_vert_img = pygame.image.load(planet.img_v)

    def move(self):
        # None yet
        a = 0

    def new_planet(self, planet):
        self.obstacle_hori_img = pygame.image.load(planet.img_h)
        self.obstacle_vert_img = pygame.image.load(planet.img_v)

    def paint_obstacle(self, adder):
        if self.w == 380:
            Paint.screen.blit(self.obstacle_hori_img, (int(self.x - self.w / 2 - self.offset) + adder, int(self.y - self.h / 2 - self.offset)))
        elif self.h == 180:
            Paint.screen.blit(self.obstacle_vert_img, (int(self.x - self.w / 2 - self.offset) + adder, int(self.y - self.h / 2 - self.offset)))
        else:
            pygame.draw.rect(Paint.screen, Paint.brown, (int(self.x - self.w/2) + adder, int(self.y - self.h/2), int(self.w), int(self.h)))
