import os
import sys
import pygame
from screeninfo import get_monitors
from GeneralFunctions import terminate, load_image
pygame.init()
pygame.key.set_repeat(200, 70)
# Разрешение экрана
screen_info = str(get_monitors()[0])[8:-1].split(', ')
WIDTH = int(screen_info[2][6:])
HEIGHT = int(screen_info[3][7:])
FPS = 50
STEP = 10
signal_start = None
signal_auth = None
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
meny_sprites = pygame.sprite.Group()
authorization_sprites = pygame.sprite.Group()


class Boor(pygame.sprite.Sprite):  # Класс Boor для начала новой игры
    # Открываем изображение и маштабируем его
    door = load_image("meny_door.jpg", cat='Sprite_meny_play')
    image = pygame.transform.scale(door, (door.get_width() * (WIDTH / 1000),
                                          door.get_height() * (HEIGHT / 1000)))

    def __init__(self, group):
        super().__init__(group)
        self.image = Boor.image
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = 412 * (WIDTH / 1069) + 1
        self.rect.y = 858 * (HEIGHT / 1020) + 1

    def update(self, *args):
        if args and self.rect.collidepoint(args[0].pos):
            pygame.draw.rect(self.image, pygame.Color('#cc5500'),
                             (0, 0, self.image.get_width(), self.image.get_height()), 5)
        else:
            pygame.draw.rect(self.image, pygame.Color('#6f6677'),
                             (0, 0, self.image.get_width(), self.image.get_height()), 5)


class User(pygame.sprite.Sprite):  # Класс User для авторизации и сохранения прогресса
    # Открываем изображение и маштабируем
    user = load_image("sprite_user.png", cat='Sprite_meny_play')
    image = pygame.transform.scale(user, ((user.get_width() / 2) * (WIDTH / 1000),
                                          (user.get_height() / 1.85) * (HEIGHT / 1000)))

    def __init__(self, group):
        super().__init__(group)
        self.image = User.image
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = 995 * (WIDTH / 1069) + 1
        self.rect.y = 15 * (HEIGHT / 1020) + 1

    def update(self, *args):
        global signal_start
        if args and self.rect.collidepoint(args[0].pos):
            pygame.draw.rect(self.image, pygame.Color('#3b83bd'),
                             (0, 0, self.image.get_width(), self.image.get_height() + 1), 3)
        else:
            pygame.draw.rect(self.image, pygame.Color('#7da4c5'),
                             (0, 0, self.image.get_width(), self.image.get_height() + 1), 3)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            signal_start = 'auth'


class Top(pygame.sprite.Sprite):  # Класс Top таблица лучших играков
    # Открываем изображение и маштабируем
    top = load_image("sprite_top.png", cat='Sprite_meny_play')
    image = pygame.transform.scale(top, ((top.get_width() / 2) * (WIDTH / 1000),
                                         (top.get_height() / 1.87) * (HEIGHT / 1000)))

    def __init__(self, group):
        super().__init__(group)
        self.image = Top.image
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = 905 * (WIDTH / 1069) + 1
        self.rect.y = 15 * (HEIGHT / 1020) + 1

    def update(self, *args):
        global signal_start
        if args and self.rect.collidepoint(args[0].pos):
            pygame.draw.rect(self.image, pygame.Color('#3b83bd'),
                             (0, 0, self.image.get_width(), self.image.get_height() + 1), 3)
        else:
            pygame.draw.rect(self.image, pygame.Color('#7da4c5'),
                             (0, 0, self.image.get_width(), self.image.get_height() + 1), 3)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            signal_start = 'top'


class ExitСross(pygame.sprite.Sprite):  # Класс ExitСross для выхода из игры или возвращение назад
    # Открываем изображение и маштабируем
    top = load_image("exit_cross.png", cat='Sprite_meny_play')
    image = pygame.transform.scale(top, ((top.get_width()) * (WIDTH / 1069),
                                         (top.get_height()) * (HEIGHT / 1020)))

    def __init__(self, group, status='ter'):
        super().__init__(group)
        self.image = ExitСross.image
        self.rect = self.image.get_rect()
        self.status = status
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = 5 * (WIDTH / 1069) + 1
        self.rect.y = 5 * (HEIGHT / 1020) + 1

    def update(self, *args):
        global signal_auth
        if (args and args[0].type == pygame.MOUSEBUTTONDOWN and
                self.rect.collidepoint(args[0].pos) and self.status == 'ter'):
            terminate()
        elif(args and args[0].type == pygame.MOUSEBUTTONDOWN and
                self.rect.collidepoint(args[0].pos) and self.status == 'back'):
            signal_auth = 'back'


class PrintArea(pygame.sprite.Sprite):  # Класс PrintArea для ввода информации в авторизации
    # Открываем изображение и маштабируем
    load_im = load_image("print_area.png", cat='Sprite_meny_play')
    image = pygame.transform.scale(load_im, (load_im.get_width() * (WIDTH / 2779),
                                             load_im.get_height() * (HEIGHT / 1381)))

    def __init__(self, group, status='log'):
        super().__init__(group)
        self.image = PrintArea.image
        self.rect = self.image.get_rect()
        self.status = status
        # Координаты левого верхнего угла с учетом размера экранна
        if self.status == "log":  # Для логина
            self.rect.x = 955 * (WIDTH / 2779) + 1
            self.rect.y = 502 * (HEIGHT / 1381) + 1
        if self.status == "pas":  # Для пароля
            self.rect.x = 954 * (WIDTH / 2779) + 1
            self.rect.y = 733 * (HEIGHT / 1381) + 1

    # def update(self, *args):
    #     if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
    #         terminate()


def start_screen():
    global signal_start
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
                meny_sprites.update(event)
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
authorization()
running = True

while running:
    screen.fill(pygame.Color(0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    pygame.display.flip()
    clock.tick(FPS)

terminate()