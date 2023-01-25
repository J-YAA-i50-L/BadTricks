import time

import pygame.sprite

from Door import *
from User import *
from ExitCross import *
from GeneralFunctions import *
from TopScreen import *
from LevelDoor import *
from Door import *
from Star import *
from Lvl1 import *
from Pit import *
from Timer import *
from Stear import *
from Camera import *
from Journal import *
from Robot import *
name_level = ''


def start_screen():
    fon = pygame.transform.scale(load_image('meny.jpg', cat='Sprite_meny_play'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    Boor(meny_sprites)
    User(meny_sprites)
    Top(meny_sprites)
    ExitСross(meny_sprites)
    music('menu')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                meny_sprites.update(event)
                if signal_output() == 'auth':
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_input(None)
                    return authorization()  # Завершаем работу стартового окна и открываем окно авторизации
                if signal_output() == 'top':
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_input(None)
                    return top_users()  # Завершаем работу стартового окна и открываем окно авторизации
                elif signal_output() == 'lvl_choice':
                    signal_input(None)
                    return level_choice()
        meny_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def authorization():  # Авторизация
    pygame.display.flip()
    fon = pygame.transform.scale(load_image('authorization.png', cat='Sprite_meny_play'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    PrintArea(authorization_sprites, 'log')
    PrintArea(authorization_sprites, 'pas')
    ExitСross(authorization_sprites, 'back')
    ButtonRun(authorization_sprites)
    Registration(authorization_sprites)
    music('menu')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                else:
                    authorization_sprites.update(event)
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                authorization_sprites.update(event)
                if signal_output() == 'exit':
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_input(None)
                    return start_screen()  # Завершаем работу на авторизации и открываем стартовое окно
                if signal_output() == 'registration':
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_input(None)
                    return registration()  # Завершаем работу на авторизации и открываем стартовое окно
                if signal_output() == 'run':
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_input(None)
                    return level_choice()
                if signal_output() == 'not_run':
                    VerdictUsers(authorization_sprites)
        authorization_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def registration():  # Регистрация
    pygame.display.flip()
    fon = pygame.transform.scale(load_image('registration_user.png', cat='Sprite_meny_play'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    PrintArea(reg_sprites, 'log', 'reg')
    PrintArea(reg_sprites, 'pas', 'reg')
    ExitСross(reg_sprites, 'back')
    ButtonRun(reg_sprites, 'reg')
    music('menu')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                else:
                    reg_sprites.update(event)
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                reg_sprites.update(event)
                if signal_output() == 'exit':
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_input(None)
                    return start_screen()  # Завершаем работу на авторизации и открываем стартовое окно
        reg_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def top_users():  # Топ играков
    pygame.display.flip()
    fon = pygame.transform.scale(load_image('top_user.png', cat='Sprite_meny_play'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    ExitСross(top_sprites, 'back')
    font = pygame.font.SysFont('arial', int(110 * (HEIGHT / 1381)))
    coord_x = 1000 * (WIDTH / 2648)
    coord_y = 360 * (HEIGHT / 1381)
    music('menu')
    for line in top_str():
        string_rendered = font.render(line, 100, pygame.Color('black'))
        screen.blit(string_rendered, (coord_x, coord_y))
        coord_y += 165 * (HEIGHT / 1381)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                top_sprites.update(event)
                if signal_output() == 'exit':
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_input(None)
                    return start_screen()  # Завершаем работу на авторизации и открываем стартовое окно
        top_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def level_choice():  # Выбор уровня
    global name_level
    ExitСross(level_choice_sprites, 'back')  # Выход
    # Каждая дверь отдельно
    LevelDoor(level_choice_sprites, 250, 40, 'fiz')
    LevelDoor(level_choice_sprites, 680, 40, 'xim')
    LevelDoor(level_choice_sprites, 60, 415, 'tex')
    LevelDoor(level_choice_sprites, 475, 415, 'bio')
    LevelDoor(level_choice_sprites, 880, 415, 'lit')
    # Каждая звезда отдельно
    Star(level_choice_sprites, 475, 60, 'fiz', 1)
    Star(level_choice_sprites, 525, 80, 'fiz', 2)
    Star(level_choice_sprites, 575, 60, 'fiz', 3)
    Star(level_choice_sprites, 905, 60, 'xim', 1)
    Star(level_choice_sprites, 955, 80, 'xim', 2)
    Star(level_choice_sprites, 1005, 60, 'xim', 3)
    Star(level_choice_sprites, 285, 415, 'tex', 1)
    Star(level_choice_sprites, 335, 435, 'tex', 2)
    Star(level_choice_sprites, 385, 415, 'tex', 3)
    Star(level_choice_sprites, 700, 415, 'bio', 1)
    Star(level_choice_sprites, 750, 435, 'bio', 2)
    Star(level_choice_sprites, 800, 415, 'bio', 3)
    Star(level_choice_sprites, 1105, 415, 'lit', 1)
    Star(level_choice_sprites, 1155, 435, 'lit', 2)
    Star(level_choice_sprites, 1205, 415, 'lit', 3)
    bg = pygame.transform.scale(load_image('level_choise_bg.png', cat='Level_choise'), (WIDTH, HEIGHT))
    music('menu')
    while True:
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                level_choice_sprites.update(event)
                name_level = signal_output()
                if signal_output() == 'exit':
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_input(None)
                    return start_screen()  # Завершаем работу выбора уровня и открываем стартовое окно
                elif name_level != None and 'lvl' == name_level[:3]:
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_input(None)
                    return lvl()  # Завершаем работу выбора уровня и открываем первый уровень
        level_choice_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def lvl():
    print(name_level)
    generate_level(load_level(f'{name_level}.txt'), Tile1)
    Timer(level_sprites)
    ExitСross(level_sprites, 'back')
    info = info_subject()
    journal = Journal(level_sprites, info[-2][0][0], info[-2][0][1])
    timer = Timer(level_sprites)
    music('lvl1')
    info = info_subject()
    for j in info[0]:
        Camera(npc_sprites, j[0], j[1])
    for j in info[1]:
        Stear(level_sprites, j[0], j[1])
    Number(level_sprites, '0', 0)
    pit = Pit(level_sprites, info[-1][0][0], info[-1][0][1])
    while True:
        screen.fill((0, 0, 0))
        timer.update_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            level_sprites.update(event)
            if signal_output() == 'exit':
                screen.fill(pygame.Color(0, 0, 0))
                signal_input(None)
                return level_choice()
        if pygame.sprite.collide_rect(pit, journal):
            pit.end()
            level1_sprites.draw(screen)
            npc_sprites.draw(screen)
            pygame.display.flip()
            time.sleep(3)
            win_sound.play()
            all_time = timer.get_time()
            # тут нужно сделать запись сохранения в файл в зависимости от all_time
            screen.fill(pygame.Color(0, 0, 0))
            return level_choice()
        else:
            pit.animation()
        npc_sprites.update()
        level1_sprites.draw(screen)
        npc_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
