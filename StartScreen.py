from GeneralFunctions import *


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
