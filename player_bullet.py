import Paint
import Values
import pygame


class player_bullet:
    pygame.init()

    x = 0
    y = 0
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    speed = 1.5
    xspeed = 0
    yspeed = 0
    r = 8
    delete = False
    player_bullet_img = ''

    def __init__(self, x1, y1, x2, y2, bullet_path):
        self.x = x1
        self.y = y1
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.player_bullet_img = pygame.image.load(bullet_path)
        self.calculate_target()

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed

    def bullet_collide(self, obstacles, adder):
        for obstacle in obstacles:
            if self.y + self.r > obstacle.y - obstacle.h / 2 and self.y - self.r < obstacle.y + obstacle.h / 2 and self.x + self.r > obstacle.x + adder - obstacle.w / 2 and self.x - self.r < obstacle.x + adder + obstacle.w / 2:
                self.delete = True

    def calculate_target(self):
        x_dif = abs(self.x2 - self.x1)
        y_dif = abs(self.y2 - self.y1)

        if x_dif == 0 and y_dif != 0:
            self.yspeed = self.speed
        elif y_dif == 0 and x_dif != 0:
            self.xspeed = self.speed
        else:
            x_mult = abs(self.x2 - self.x1) / (self.x2 - self.x1)
            y_mult = abs(self.y2 - self.y1) / (self.y2 - self.y1)
            total = x_dif + y_dif
            speed_frac = self.speed / total
            self.xspeed = speed_frac * x_dif * x_mult
            self.yspeed = speed_frac * y_dif * y_mult


    def check_delete(self):
        if (self.x - self.r > Values.screen_width) or (self.x + self.r < 0) or (self.y + self.r < 0) or (
                self.y - self.r > Values.screen_height):
            self.delete = True

    def paint_bullet(self):
        Paint.screen.blit(self.player_bullet_img, (int(self.x) - self.r, int(self.y) - self.r))
        # pygame.draw.circle(Paint.screen, Paint.red, (int(self.x), int(self.y)), self.r)
