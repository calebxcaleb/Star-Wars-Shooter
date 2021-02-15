import pygame
import Values
import random
import math
import Paint
import imgpath
import characters
import Planets
from Player import Player
from Enemy import Enemy
from Obstacle import Obstacle
from player_bullet import player_bullet
from enemy_bullet import enemy_bullet
from Planet import Planet
from Trooper_Player import Trooper_Player
from Trooper_Enemy import Trooper_Enemy

pygame.init()

player = Player(135, 400, Trooper_Player((0, 0, 0, 0), 16, False, imgpath.normal_p_troops1[0]))

enemy1 = Enemy(200, 100, imgpath.normal_p_troops1[0][0], imgpath.normal_p_troops1[0][2])
enemy2 = Enemy(400, 100, imgpath.normal_p_troops1[0][0], imgpath.normal_p_troops1[0][2])
enemy3 = Enemy(1000, 100, imgpath.normal_p_troops1[0][0], imgpath.normal_p_troops1[0][2])
enemy4 = Enemy(1200, 100, imgpath.normal_p_troops1[0][0], imgpath.normal_p_troops1[0][2])
enemy5 = Enemy(200, 700, imgpath.normal_p_troops1[0][0], imgpath.normal_p_troops1[0][2])
enemy6 = Enemy(400, 700, imgpath.normal_p_troops1[0][0], imgpath.normal_p_troops1[0][2])
enemy7 = Enemy(1000, 700, imgpath.normal_p_troops1[0][0], imgpath.normal_p_troops1[0][2])
enemy8 = Enemy(1200, 700, imgpath.normal_p_troops1[0][0], imgpath.normal_p_troops1[0][2])

enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8]
actual_enemies = []

# now obstacles #
obstacle1 = Obstacle(300, 215, 380, 40, Planets.planets[Values.planet_num])
obstacle2 = Obstacle(1100, 215, 380, 40, Planets.planets[Values.planet_num])
obstacle3 = Obstacle(300, 585, 380, 40, Planets.planets[Values.planet_num])
obstacle4 = Obstacle(1100, 585, 380, 40, Planets.planets[Values.planet_num])
obstacles_hori = [obstacle1, obstacle2, obstacle3, obstacle4]
actual_obstacles_hori = []

obstacle5 = Obstacle(700, 100, 40, 180, Planets.planets[Values.planet_num])
obstacle6 = Obstacle(700, 700, 40, 180, Planets.planets[Values.planet_num])
obstacles_vert = [obstacle5, obstacle6]
actual_obstacles_vert = []

obstacle7 = Obstacle(200, 400, 30, 175, Planets.planets[Values.planet_num])
obstacle8 = Obstacle(135, 327.5, 100, 30, Planets.planets[Values.planet_num])
obstacle9 = Obstacle(135, 472.5, 100, 30, Planets.planets[Values.planet_num])
obstacle10 = Obstacle(1200, 400, 30, 175, Planets.planets[Values.planet_num])
obstacle11 = Obstacle(1265, 327.5, 100, 30, Planets.planets[Values.planet_num])
obstacle12 = Obstacle(1265, 472.5, 100, 30, Planets.planets[Values.planet_num])
starter_obstacles = [obstacle7, obstacle8, obstacle9, obstacle10, obstacle11, obstacle12]
all_now_obstacles = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, obstacle6, obstacle7, obstacle8, obstacle9, obstacle10, obstacle11, obstacle12]

# next obstacles #
obstacle1_n = Obstacle(300, 215, 380, 40, Planets.planets[Values.planet_num])
obstacle2_n = Obstacle(1100, 215, 380, 40, Planets.planets[Values.planet_num])
obstacle3_n = Obstacle(300, 585, 380, 40, Planets.planets[Values.planet_num])
obstacle4_n = Obstacle(1100, 585, 380, 40, Planets.planets[Values.planet_num])
obstacles_hori_n = [obstacle1_n, obstacle2_n, obstacle3_n, obstacle4_n]
actual_obstacles_hori_n = []

obstacle5_n = Obstacle(700, 100, 40, 180, Planets.planets[Values.planet_num])
obstacle6_n = Obstacle(700, 700, 40, 180, Planets.planets[Values.planet_num])
obstacles_vert_n = [obstacle5_n, obstacle6_n]
actual_obstacles_vert_n = []

obstacle7_n = Obstacle(200, 400, 30, 175, Planets.planets[Values.planet_num])
obstacle8_n = Obstacle(135, 327.5, 100, 30, Planets.planets[Values.planet_num])
obstacle9_n = Obstacle(135, 472.5, 100, 30, Planets.planets[Values.planet_num])
obstacle10_n = Obstacle(1200, 400, 30, 175, Planets.planets[Values.planet_num])
obstacle11_n = Obstacle(1265, 327.5, 100, 30, Planets.planets[Values.planet_num])
obstacle12_n = Obstacle(1265, 472.5, 100, 30, Planets.planets[Values.planet_num])
starter_obstacles_n = [obstacle7_n, obstacle8_n, obstacle9_n, obstacle10_n, obstacle11_n, obstacle12_n]
all_next_obstacles = [obstacle1_n, obstacle2_n, obstacle3_n, obstacle4_n, obstacle5_n, obstacle6_n, obstacle7_n, obstacle8_n, obstacle9_n, obstacle10_n, obstacle11_n, obstacle12_n]

# collections #
now_obstacles = []
next_obstacles = []

player_bullets = []
enemy_bullets = []


###########################################
#               Setup                     #
###########################################
def create_Player():
    global player
    player = Player(135, 400, characters.troopers[Values.trooper_num])

def update_enemies():
    for enemy in enemies:
        enemy.change_img(characters.troopers_e[Values.trooper_e_num].img_head)

def setup():
    player.reset()
    choose_enemy()
    choose_obstacle(actual_obstacles_vert, obstacles_vert)
    choose_obstacle(actual_obstacles_hori, obstacles_hori)
    combine_now_obstacles()
    choose_obstacle(actual_obstacles_vert_n, obstacles_vert_n)
    choose_obstacle(actual_obstacles_hori_n, obstacles_hori_n)
    combine_next_obstacles()

def reset():
    actual_enemies.clear()
    actual_obstacles_vert.clear()
    actual_obstacles_hori.clear()
    actual_obstacles_vert_n.clear()
    actual_obstacles_hori_n.clear()
    now_obstacles.clear()
    next_obstacles.clear()
    player_bullets.clear()
    enemy_bullets.clear()
    setup()

def choose_enemy():
    Values.no_enemy = False
    n = random.randint(2, 8)
    indexes = []

    for i in range(0, n):
        m = random.randint(0, 7)
        while m in indexes:
            m = random.randint(0, 7)
        list.append(indexes, m)
    for index in indexes:
        enemies[index].alive = True
        list.append(actual_enemies, enemies[index])

def choose_obstacle(main, sub):
    n = random.randint(1, 2)
    indexes = []

    for i in range(0, n):
        m = random.randint(0, 1)
        if not m in indexes:
            list.append(indexes, m)

    for index in indexes:
        list.append(main, sub[index])

def combine_now_obstacles():
    obstacles = actual_obstacles_hori + actual_obstacles_vert + starter_obstacles

    for obstacle in obstacles:
        list.append(now_obstacles, obstacle)

def combine_next_obstacles():
    obstacles = actual_obstacles_hori_n + actual_obstacles_vert_n + starter_obstacles_n

    for obstacle in obstacles:
        list.append(next_obstacles, obstacle)

def set_now_obstacle():
    actual_obstacles_vert.clear()
    actual_obstacles_hori.clear()
    now_obstacles.clear()
    choose_obstacle(actual_obstacles_vert, obstacles_vert)
    choose_obstacle(actual_obstacles_hori, obstacles_hori)
    combine_now_obstacles()

def set_next_obstacle():
    actual_obstacles_vert_n.clear()
    actual_obstacles_hori_n.clear()
    next_obstacles.clear()
    choose_obstacle(actual_obstacles_vert_n, obstacles_vert_n)
    choose_obstacle(actual_obstacles_hori_n, obstacles_hori_n)
    combine_next_obstacles()

def update_obstacles():
    for obstacle in all_now_obstacles:
        obstacle.new_planet(Planets.planets[Values.planet_num])
    for obstacle in all_next_obstacles:
        obstacle.new_planet(Planets.planets[Values.planet_num])


###########################################
#               Mains                     #
###########################################
def Player_main():
    if player.alive:
        key_move()
        player.mouse_get_weapon()
        player.bullet_collide(enemy_bullets)
        player.obstacle_collide(now_obstacles, Values.now_add)
        player.obstacle_collide(next_obstacles, Values.next_add)
        player.weapon_rotate()

        if player.troop.hero:
            player.mouse_get_collider()

        if Values.start_move:
            player.move_stage()
        else:
            player.move()

    player.paint_player()

def Bullet_player_main():
    for bullet in player_bullets:
        bullet.move()
        bullet.check_delete()
        bullet.paint_bullet()
        bullet.bullet_collide(now_obstacles, Values.now_add)
        bullet.bullet_collide(next_obstacles, Values.next_add)
        if bullet.delete:
            player_bullets.remove(bullet)

def Bullet_enemy_main():
    for bullet in enemy_bullets:
        bullet.move()
        bullet.check_delete()
        bullet.paint_bullet()
        bullet.bullet_collide(now_obstacles, Values.now_add)
        bullet.bullet_collide(next_obstacles, Values.next_add)
        if player.troop.hero:
            bullet.bullet_diflect(player.collider)
        if bullet.delete:
            enemy_bullets.remove(bullet)

def Enemy_main():
    if len(actual_enemies) == 0 and Values.can_no_enemy:
        Values.start_move = True
        Values.can_no_enemy = False
        Values.no_enemy = True

    for enemy in actual_enemies:
        enemy.paint_enemy()
        enemy.move()

        if player.troop.hero:
            enemy.enemy_bullet_collide(enemy_bullets)
            enemy.weapon_collide(player.collider)
        else:
            enemy.player_bullet_collide(player_bullets)

        if enemy.can_shoot and enemy.x < 1400:
            shoot_enemy(enemy.x, enemy.y)
            enemy.can_shoot = False
        if not enemy.alive:
            actual_enemies.remove(enemy)

def Obstacle_main():
    for obstacle in now_obstacles:
        obstacle.paint_obstacle(Values.now_add)
    for obstacle in next_obstacles:
        obstacle.paint_obstacle(Values.next_add)


###########################################
#               Actions                   #
###########################################
def move_stage():
    if Values.move_val >= 1400:
        Values.move_val = 0
        Values.move_stage = False
        Values.start_move = False

    if Values.move_stage:
        Values.move_val += player.xspeed
        for obstacle in all_now_obstacles:
            obstacle.x -= player.xspeed
        for obstacle in all_next_obstacles:
            obstacle.x -= player.xspeed
        Paint.display_x1 -= player.xspeed
        Paint.display_x2 -= player.xspeed

def shoot_player(mouse_x, mouse_y):
    new_player_bullet = player_bullet(player.x, player.y, mouse_x, mouse_y, player.bullet_path)
    list.append(player_bullets, new_player_bullet)

def shoot_enemy(enemy_x, enemy_y):
    new_enemy_bullet = enemy_bullet(enemy_x, enemy_y, player.x, player.y, enemies[0].bullet_path)
    list.append(enemy_bullets, new_enemy_bullet)

def change_col_planet():
    for planet in Planets.planets:
        planet.box_col = planet.def_col

def change_col_trooper():
    for trooper in characters.troopers:
        trooper.box_col = trooper.def_col

def change_col_trooper_e():
    for trooper_e in characters.troopers_e:
        trooper_e.box_col = trooper_e.def_col


###########################################
#               Input                     #
###########################################
def key_move():
    pressed = pygame.key.get_pressed()

    if not Values.start_move and not Values.move_stage and Values.no_enemy and pressed[pygame.K_RETURN]:
        choose_enemy()
        Values.obstacle = (Values.obstacle - 1) * -1
        Values.now_add = (Values.now_add - 1400) * -1
        Values.next_add = (Values.next_add - 1400) * -1

        for obstacle in all_next_obstacles:
            obstacle.x += 1400
        for obstacle in all_now_obstacles:
            obstacle.x += 1400

        Paint.display_x1 += 1400
        Paint.display_x2 += 1400

        if Values.obstacle == 1:
            set_now_obstacle()
        elif Values.obstacle == 0:
            set_next_obstacle()
        Values.can_no_enemy = True

    # if Values.can_restart and Values.no_enemy and pressed[pygame.K_RETURN]:
    #     Values.can_restart = False
    #     reset()

    if (not Values.press[0] and pressed[pygame.K_w]):
        Values.press[0] = True
    if (not Values.press[1] and pressed[pygame.K_s]):
        Values.press[1] = True
    if (not Values.press[2] and pressed[pygame.K_a]):
        Values.press[2] = True
    if (not Values.press[3] and pressed[pygame.K_d]):
        Values.press[3] = True

    if Values.press[0]:
        Player.yspeed = -1 * Player.speed
    elif Player.yspeed < 0:
        Player.yspeed = 0

    if Values.press[1]:
        Player.yspeed = 1 * Player.speed
    elif Player.yspeed > 0:
        Player.yspeed = 0

    if Values.press[2]:
        Player.xspeed = -1 * Player.speed
    elif Player.xspeed < 0:
        Player.xspeed = 0

    if Values.press[3]:
        Player.xspeed = 1 * Player.speed
    elif Player.xspeed > 0:
        Player.xspeed = 0

def mouse_check_start():
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if Values.start_button_rect[0] < pygame.mouse.get_pos()[0] < Values.start_button_rect[0] + \
                Values.start_button_rect[2] and Values.start_button_rect[1] < pygame.mouse.get_pos()[1] < Values.start_button_rect[1] + \
                Values.start_button_rect[3]:
            Values.starting = False
            update_obstacles()
            create_Player()
            update_enemies()
            Paint.back_img = pygame.image.load(imgpath.scarif_back_path).convert()

        planet_n = 0
        for planet in Planets.planets:
            if planet.rect[0] < pygame.mouse.get_pos()[0] < planet.rect[0] + planet.rect[2] and planet.rect[1] < pygame.mouse.get_pos()[1] < planet.rect[1] + planet.rect[3]:
                Values.planet_selected = True
                Values.planet_num = planet_n
                change_col_planet()
                planet.box_col = planet.pick_col
                return
            planet_n += 1

        trooper_n = 0
        for trooper in characters.troopers:
            if trooper.rect[0] < pygame.mouse.get_pos()[0] < trooper.rect[0] + trooper.rect[2] and trooper.rect[1] < \
                    pygame.mouse.get_pos()[1] < trooper.rect[1] + trooper.rect[3]:
                Values.trooper_selected = True
                Values.trooper_num = trooper_n
                change_col_trooper()
                trooper.box_col = trooper.pick_col
                return
            trooper_n += 1

    if pygame.mouse.get_pressed() == (0, 0, 1):
        trooper_e_n = 0
        for trooper_e in characters.troopers_e:
            if trooper_e.rect[0] < pygame.mouse.get_pos()[0] < trooper_e.rect[0] + trooper_e.rect[2] and trooper_e.rect[1] < \
                    pygame.mouse.get_pos()[1] < trooper_e.rect[1] + trooper_e.rect[3]:
                Values.trooper_e_selected = True
                Values.trooper_e_num = trooper_e_n
                change_col_trooper_e()
                trooper_e.box_col = trooper_e.pick_col
                return
            trooper_e_n += 1

def mouse_check():
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if Values.can_click and not Values.starting and not player.troop.hero:
            shoot_player(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            Values.can_click = False
