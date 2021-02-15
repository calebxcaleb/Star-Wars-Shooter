import Paint
import Values
import pygame


class Planet:
    pygame.init()

    name = ''
    col = (0, 0, 0)
    def_col = (0, 100, 0)
    pick_col = (0, 255, 0)
    box_col = def_col
    rect = (0, 0, 0, 0)
    img_h = ''
    img_v = ''
    img_s1 = ''
    img_s2 = ''

    def __init__(self, pick, name, col, rect, img_h, img_v, img_s1, img_s2):
        if pick:
            self.box_col = self.pick_col
        self.name = name
        self.col = col
        self.rect = rect
        self.img_h = img_h
        self.img_v = img_v
        self.img_s1 = img_s1
        self.img_s2 = img_s2
