import Paint
import Values
import math
import pygame


class Player:
    pygame.init()

    x = 0
    y = 0
    x_original = 0
    y_original = 0
    r = 16
    speed = 0.5
    xspeed = 0
    yspeed = 0
    alive = True
    weapon_x = 0
    weapon_y = 0
    weapon_max = 0
    rot_count = 0
    weapon_angle = 0
    collider = [0, 0, 0, 0]
    collider_r = 32
    collider_top = 0
    troop = ''
    player_img = ''
    weapon_img = ''
    bullet_path = ''

    def __init__(self, x, y, troop):
        self.x = x
        self.y = y
        self.x_original = x
        self.y_original = y
        self.troop = troop
        self.player_img = pygame.image.load(troop.head_name)
        self.weapon_img = pygame.image.load(troop.weapon_name)
        self.bullet_path = troop.bullet_name
        self.weapon_max = 26 + self.troop.r
        self.collider_max = self.weapon_max + self.collider_r - 15
        self.collider = [self.x - self.collider_r/2, self.y - self.collider_max, self.collider_r, self.collider_r]

    def mouse_get_weapon(self):
        x_dif = abs(pygame.mouse.get_pos()[0] - self.x)
        y_dif = abs(pygame.mouse.get_pos()[1] - self.y)

        if x_dif == 0 and y_dif != 0:
            self.weapon_y = self.weapon_max
        elif y_dif == 0 and x_dif != 0:
            self.weapon_x = self.weapon_max
        elif x_dif != 0 and y_dif != 0:
            x_mult = abs(pygame.mouse.get_pos()[0] - self.x) / (pygame.mouse.get_pos()[0] - self.x)
            y_mult = abs(pygame.mouse.get_pos()[1] - self.y) / (pygame.mouse.get_pos()[1] - self.y)
            total = x_dif + y_dif
            frac = self.weapon_max / total
            self.weapon_x = frac * x_dif * x_mult
            self.weapon_y = frac * y_dif * y_mult

    def mouse_get_collider(self):
        x_dif = abs(pygame.mouse.get_pos()[0] - self.x)
        y_dif = abs(pygame.mouse.get_pos()[1] - self.y)

        if x_dif == 0 and y_dif != 0:
            self.collider[0] = self.collider_max
        elif y_dif == 0 and x_dif != 0:
            self.collider[1] = self.collider_max
        elif x_dif != 0 and y_dif != 0:
            x_mult = abs(pygame.mouse.get_pos()[0] - self.x) / (pygame.mouse.get_pos()[0] - self.x)
            y_mult = abs(pygame.mouse.get_pos()[1] - self.y) / (pygame.mouse.get_pos()[1] - self.y)
            total = x_dif + y_dif
            frac = self.collider_max / total
            self.collider[0] = frac * x_dif * x_mult + self.x - self.collider_r/2
            self.collider[1] = frac * y_dif * y_mult + self.y - self.collider_r/2

    def weapon_rotate(self):
        x_dif = pygame.mouse.get_pos()[0] - self.x
        y_dif = pygame.mouse.get_pos()[1] - self.y

        if abs(y_dif) > abs(x_dif) and y_dif < 0:
            self.weapon_img = pygame.transform.rotate(self.weapon_img, -self.weapon_angle)
            self.weapon_angle = 0
            self.weapon_img = pygame.transform.rotate(self.weapon_img, self.weapon_angle)
        elif abs(y_dif) > abs(x_dif) and y_dif > 0:
            self.weapon_img = pygame.transform.rotate(self.weapon_img, -self.weapon_angle)
            self.weapon_angle = 180
            self.weapon_img = pygame.transform.rotate(self.weapon_img, self.weapon_angle)
        elif abs(x_dif) > abs(y_dif) and x_dif < 0:
            self.weapon_img = pygame.transform.rotate(self.weapon_img, -self.weapon_angle)
            self.weapon_angle = 90
            self.weapon_img = pygame.transform.rotate(self.weapon_img, self.weapon_angle)
        elif abs(x_dif) > abs(y_dif) and x_dif > 0:
            self.weapon_img = pygame.transform.rotate(self.weapon_img, -self.weapon_angle)
            self.weapon_angle = -90
            self.weapon_img = pygame.transform.rotate(self.weapon_img, self.weapon_angle)

    def reset(self):
        self.x = self.x_original
        self.y = self.y_original
        self.alive = True

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed

        if self.x + self.r > Values.screen_width:
            self.x = Values.screen_width - self.r
        if self.x - self.r < 0:
            self.x = self.r
        if self.y - self.r < 0:
            self.y = self.r
        if self.y + self.r > Values.screen_height:
            self.y = Values.screen_height - self.r

    def move_stage(self):
        if self.xspeed < 0 or self.x < 700:
            self.x += self.xspeed
            Values.move_stage = False
        else:
            Values.move_stage = True

        self.y += self.yspeed

        if self.x + self.r > Values.screen_width:
            self.x = Values.screen_width - self.r
        if self.x - self.r < 0:
            self.x = self.r
        if self.y - self.r < 0:
            self.y = self.r
        if self.y + self.r > Values.screen_height:
            self.y = Values.screen_height - self.r

    def bullet_collide(self, bullets):
        for bullet in bullets:
            if self.y + self.r > bullet.y - bullet.r and self.y - self.r < bullet.y + bullet.r and self.x + self.r > bullet.x - bullet.r and self.x - self.r < bullet.x + bullet.r:
                # self.alive = False
                bullet.delete = True
                return

    def obstacle_collide(self, obstacles, adder):
        for obstacle in obstacles:
            if self.y + self.r > obstacle.y - obstacle.h / 2 - obstacle.offset and self.y - self.r < obstacle.y - obstacle.h / 2 - obstacle.offset and self.x + self.r > obstacle.x + adder - obstacle.w / 2 - obstacle.offset and self.x - self.r < obstacle.x + adder + obstacle.w / 2 + obstacle.offset:
                self.y = obstacle.y - obstacle.h / 2 - self.r - obstacle.offset
            elif self.y - self.r < obstacle.y + obstacle.h / 2 + obstacle.offset and self.y + self.r > obstacle.y + obstacle.h / 2 + obstacle.offset and self.x + self.r > obstacle.x + adder - obstacle.w / 2 - obstacle.offset and self.x - self.r < obstacle.x + adder + obstacle.w / 2 + obstacle.offset:
                self.y = obstacle.y + obstacle.h / 2 + self.r + obstacle.offset
            elif self.x + self.r > obstacle.x + adder - obstacle.w / 2 - obstacle.offset and self.x - self.r < obstacle.x + adder - obstacle.w / 2 - obstacle.offset and self.y + self.r > obstacle.y - obstacle.h / 2 - obstacle.offset and self.y - self.r < obstacle.y + obstacle.h / 2 + obstacle.offset:
                self.x = obstacle.x + adder - obstacle.w / 2 - self.r - obstacle.offset
            elif self.x - self.r < obstacle.x + adder + obstacle.w / 2 + obstacle.offset and self.x + self.r > obstacle.x + adder + obstacle.w / 2 + obstacle.offset and self.y + self.r > obstacle.y - obstacle.h / 2 and - obstacle.offset and self.y - self.r < obstacle.y + obstacle.h / 2 + obstacle.offset:
                self.x = obstacle.x + adder + obstacle.w / 2 + self.r + obstacle.offset

    def paint_player(self):
        Paint.screen.blit(self.player_img, (int(self.x) - self.r, int(self.y) - self.r))
        Paint.screen.blit(self.weapon_img, (int(self.x) + self.weapon_x - self.troop.r, int(self.y) + self.weapon_y - self.troop.r))
        # pygame.draw.rect(Paint.screen, Paint.black, self.collider)
