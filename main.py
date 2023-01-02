from StartScreen import *
from User import *
from ExitCross import *
from GeneralFunctions import *


def start_screen():
    fon = pygame.transform.scale(load_image('meny.jpg', cat='Sprite_meny_play'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    Boor(meny_sprites)
    User(meny_sprites)
    Top(meny_sprites)
    ExitСross(meny_sprites)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                signal_start = meny_sprites.update(event)
                print(signal_start)
                if signal_start == 'auth':
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_start = None
                    return authorization()  # Завершаем работу стартового окна и открываем окно авторизации
        meny_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def authorization():  # Авторизация
    global signal_auth
    pygame.display.flip()
    fon = pygame.transform.scale(load_image('authorization.png', cat='Sprite_meny_play'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    PrintArea(authorization_sprites)
    PrintArea(authorization_sprites, 'pas')
    ExitСross(authorization_sprites, 'back')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                authorization_sprites.update(event)
                if signal_auth == 'back':
                    screen.fill(pygame.Color(0, 0, 0))
                    signal_auth = None
                    return start_screen()  # Завершаем работу на авторизации и открываем стартовое окно
        authorization_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
