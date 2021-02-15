import Paint
import Values
import pygame


class Trooper_Enemy:
    pygame.init()

    def_col = (100, 0, 0)
    pick_col = (255, 0, 0)
    box_col = def_col
    rect = (0, 0, 0, 0)
    img_head = ''
    img_bullet = ''

    def __init__(self, rect, head_path, bullet_path):
        self.rect = (rect[0] - 2.5, rect[1] - 2.5, rect[2] + 5, rect[3] + 5,)
        self.img_head = head_path
        self.img_bullet = bullet_path

    def paint_helmet(self):
        img = pygame.image.load(self.img_head)
        Paint.screen.blit(img, (self.rect[0] + 4, self.rect[1] + 4))
