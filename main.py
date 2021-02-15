# Star Wars Game

import pygame
import Values
import Paint
import Functions

pygame.init()

# Main game loop
running = True

Functions.setup()

while running:

    while Values.starting:
        Paint.start_paint()
        Paint.paint_flip()
        Functions.mouse_check_start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Values.starting = False
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT or Values.end:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            Values.can_click = True
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            Values.can_restart = True
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            Values.press[0] = False
        if event.type == pygame.KEYUP and event.key == pygame.K_s:
            Values.press[1] = False
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            Values.press[2] = False
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            Values.press[3] = False

    Paint.paint_main()
    Functions.mouse_check()
    Functions.Bullet_player_main()
    Functions.Bullet_enemy_main()
    Functions.Enemy_main()
    Functions.Obstacle_main()
    Functions.move_stage()
    Functions.Player_main()

    Paint.paint_flip()

pygame.quit()
