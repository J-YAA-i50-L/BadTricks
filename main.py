from Door import *
from User import *
from ExitCross import *
from GeneralFunctions import *
from Top import *
from LevelDoor import *
from Star import *


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
    PrintArea(authorization_sprites)
    PrintArea(authorization_sprites, 'pas')
    ExitСross(authorization_sprites, 'back')
    music('menu')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                authorization_sprites.update(event)
                if signal_output() == 'exit':
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_input(None)
                    return start_screen()  # Завершаем работу на авторизации и открываем стартовое окно
        authorization_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def level_choice(): # выбор уровня
    ExitСross(level_choice_sprites, 'back') # выход
    # каждая дверь отдельно
    LevelDoor(level_choice_sprites, 250, 40, 'fiz')
    LevelDoor(level_choice_sprites, 680, 40, 'xim')
    LevelDoor(level_choice_sprites, 60, 415, 'tex')
    LevelDoor(level_choice_sprites, 475, 415, 'bio')
    LevelDoor(level_choice_sprites, 880, 415, 'lit')
    # каждая звезда отдельно
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
                if signal_output() == 'exit':
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_input(None)
                    return start_screen()  # Завершаем работу выбора уровня и открываем стартовое окно
        level_choice_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
