from StartScreen import *
from User import *
from ExitCross import *
from GeneralFunctions import *


def start_screen():
    fon = pygame.transform.scale(load_image('meny.jpg', cat='Sprite_meny_play'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    Boor(meny_sprites)
    User(meny_sprites)
    # Top(meny_sprites)
    ExitСross(meny_sprites)
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
            if event.type == pygame.KEYDOWN:
                authorization_sprites.update(event)

        authorization_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
