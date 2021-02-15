import Paint
import Values
import pygame


class Trooper_Player:
    pygame.init()

    def_col = (0, 100, 0)
    pick_col = (0, 255, 0)
    box_col = def_col
    rect = (0, 0, 0, 0)
    spacer = 0
    r = 0
    hero = False
    head_name = ''
    weapon_name = ''
    bullet_name = ''

    def __init__(self, rect, r, hero, paths):
        self.rect = rect
        self.r = r
        self.hero = hero
        self.head_name = paths[0]
        self.weapon_name = paths[1]
        self.bullet_name = paths[2]
        # self.bullet_name = img_bullet

    def paint_helmet(self):
        img = pygame.image.load(self.head_name)
        Paint.screen.blit(img, (self.rect[0] + 4, self.rect[1] + 4))
