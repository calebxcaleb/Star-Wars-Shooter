import pygame
import Values
import Functions
import math
import imgpath
import characters
import Planets

pygame.init()

# Colours
light_blue = (68, 227, 245)
white = (255, 255, 255)
gray = (60, 60, 60)  # ground
dark_gray = (60, 60, 60)  # tower 3
light_gray = (128, 128, 128)  # light light
light_mid_gray = (100, 100, 100)  # light light
mid_gray = (90, 90, 90)  # light mid
brown = (160, 82, 45)  # pot
green = (50, 205, 50)  # background
dark_green = (0, 128, 0)  # menu
black = (0, 0, 0)  # text
blue = (0, 191, 255)  # tower 1
dark_blue = (0, 0, 128)  # tower 1 dark
yellow = (255, 255, 0)  # tower 2 / start wave
lime_yellow = (173, 255, 47)  # tower 5
purple = (255, 0, 255)  # tower 3
dark_purple = (75, 0, 130)  # tower 3 dark
dark_yellow = (128, 128, 0)  # start wave / tower 2 dark
red = (220, 20, 60)  # enemy light
dark_red = (128, 0, 0)  # enemy heave

####################
###### Delete ######
####################
pygame.display.set_mode((1280, 420))
display_x1 = 0
display_x2 = 1400
back_img = ''

# Fonts
font1 = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 30)
font3 = pygame.font.Font('freesansbold.ttf', 15)
font4 = pygame.font.Font('freesansbold.ttf', 30)
font_start_big = pygame.font.Font('freesansbold.ttf', 40)
font_pause = pygame.font.Font('freesansbold.ttf', 160)

# Set up the drawing window
screen = pygame.display.set_mode([Values.screen_width, Values.screen_height])
pygame.display.set_caption('Show Text')

# Text - Starting
title_text = font_start_big.render('Star Wars Battlefront 2D', True, white, None)
title_textRect = title_text.get_rect()
title_textRect.center = (Values.screen_width / 2 - 100, 60)
start_button_text = font_start_big.render('Start', True, black, None)
start_button_textRect = start_button_text.get_rect()
start_button_textRect.center = (1000, 60)

# Text - start options
planet_title_text = font2.render('Planet:', True, white, None)
planet_title_textRect = planet_title_text.get_rect()
planet_title_textRect.center = (85, 100)

planet_text = font1.render('', True, white, None)
planet_textRect = planet_text.get_rect()
planet_textRect.center = (150, 150)

def paint_main():
    paint()
    text_paint()

def paint():
    ########################################
    # Delete back_img when this is changed #
    ########################################
    screen.blit(back_img, (display_x1, 0))
    screen.blit(back_img, (display_x2, 0))
    # screen.fill(Planets.planets[Values.planet_num].col)
    # pygame.draw.rect(screen, brown, (0, 700, Values.screen_width, 100))

def text_paint():
    a = 0

def start_paint():
    screen.fill(dark_blue)

    pygame.draw.rect(screen, white, Values.start_button_rect)
    pygame.draw.rect(screen, black, Values.start_button_rect, 10)

    screen.blit(title_text, title_textRect)
    screen.blit(start_button_text, start_button_textRect)

    planet_text()

def planet_text():
    screen.blit(planet_title_text, planet_title_textRect)

    for planet in Planets.planets:
        pygame.draw.rect(screen, planet.col, planet.rect, 0)
        pygame.draw.rect(screen, planet.box_col, planet.rect, 3)

        planet_text = font1.render(planet.name, True, white, None)
        planet_textRect = planet_text.get_rect()
        planet_textRect.topleft = (planet.rect[0] + 60, planet.rect[1] + 10)
        screen.blit(planet_text, planet_textRect)

    for trooper_e in characters.troopers_e:
        pygame.draw.rect(screen, trooper_e.box_col, trooper_e.rect, 5)

    for trooper in characters.troopers:
        pygame.draw.rect(screen, trooper.box_col, trooper.rect, 5)
        pygame.draw.rect(screen, white, trooper.rect, 0)
        trooper.paint_helmet()

def paint_flip():
    pygame.display.flip()
