import Paint
import Values
import random
import pygame


class Enemy:
    pygame.init()

    x = 0
    y = 0
    r = 12
    shoot_count = 0
    shoot_count_max = 1125
    shoot_count_max_min = 750
    shoot_count_max_max = 1500
    can_shoot = False
    alive = True
    enemy_img = ''
    bullet_path = ''

    def __init__(self, x, y, img_name, bullet_path):
        self.x = x
        self.y = y
        self.enemy_img = pygame.image.load(img_name)
        self.bullet_path = bullet_path

    def move(self):
        if self.shoot_count >= self.shoot_count_max:
            self.shoot_count = 0
            self.shoot_count_max = random.randint(self.shoot_count_max_min, self.shoot_count_max_max)
            self.can_shoot = True
        else:
            self.shoot_count += 1

    def change_img(self, img_name):
        self.enemy_img = pygame.image.load(img_name)

    def player_bullet_collide(self, bullets):
        for bullet in bullets:
            if self.y + self.r > bullet.y - bullet.r and self.y - self.r < bullet.y + bullet.r and self.x + self.r > bullet.x - bullet.r and self.x - self.r < bullet.x + bullet.r:
                self.alive = False
                bullet.delete = True
                return

    def enemy_bullet_collide(self, bullets):
        for bullet in bullets:
            if self.y + self.r > bullet.y - bullet.r and self.y - self.r < bullet.y + bullet.r and self.x + self.r > bullet.x - bullet.r and self.x - self.r < bullet.x + bullet.r:
                if bullet.is_player:
                    self.alive = False
                    bullet.delete = True
                return

    def weapon_collide(self, collider):
        if self.y + self.r > collider[1] - collider[3] and self.y - self.r < collider[1] + collider[
            3] and self.x + self.r > collider[0] - collider[2] and self.x - self.r < collider[0] + collider[2]:
            self.alive = False

    def paint_enemy(self):
        Paint.screen.blit(self.enemy_img, (int(self.x) - self.r, int(self.y) - self.r))
        # pygame.draw.circle(Paint.screen, Paint.dark_red, (int(self.x), int(self.y)), self.r)
