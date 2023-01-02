from GeneralFunctions import *

signal_start = None


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
