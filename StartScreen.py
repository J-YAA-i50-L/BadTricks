import pygame
from GeneralFunctions import terminate, load_image


class Boor(pygame.sprite.Sprite):
    # Открываем изображение и маштабируем
    door = load_image("meny_door.jpg", cat='Sprite_meny_play')
    image = pygame.transform.scale(door, (door.get_width() * (WIDTH / 1000), door.get_height() * (HEIGHT / 1000)))

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


class User(pygame.sprite.Sprite):
    # Открываем изображение и маштабируем
    user = load_image("sprite_user.png", cat='Sprite_meny_play')
    image = pygame.transform.scale(user, ((user.get_width() / 2) * (WIDTH / 1000), (user.get_height() / 1.9) * (HEIGHT / 1000)))

    def __init__(self, group):
        super().__init__(group)
        self.image = User.image
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = 995 * (WIDTH / 1069) + 1
        self.rect.y = 15 * (HEIGHT / 1020) + 1

    def update(self, *args):
        if args and self.rect.collidepoint(args[0].pos):
            pygame.draw.rect(self.image, pygame.Color('#3b83bd'),
                             (0, 0, self.image.get_width(), self.image.get_height() + 1), 3)
        else:
            pygame.draw.rect(self.image, pygame.Color('#7da4c5'),
                             (0, 0, self.image.get_width(), self.image.get_height() + 1), 3)


class Top(pygame.sprite.Sprite):
    # Открываем изображение и маштабируем
    top = load_image("sprite_top.png", cat='Sprite_meny_play')
    image = pygame.transform.scale(top, ((top.get_width() / 2) * (WIDTH / 1000), (top.get_height() / 2) * (HEIGHT / 1000)))

    def __init__(self, group):
        super().__init__(group)
        self.image = Top.image
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = 905 * (WIDTH / 1069) + 1
        self.rect.y = 15 * (HEIGHT / 1020) + 1

    def update(self, *args):
        if args and self.rect.collidepoint(args[0].pos):
            pygame.draw.rect(self.image, pygame.Color('#3b83bd'),
                             (0, 0, self.image.get_width(), self.image.get_height() + 1), 3)
        else:
            pygame.draw.rect(self.image, pygame.Color('#7da4c5'),
                             (0, 0, self.image.get_width(), self.image.get_height() + 1), 3)


class Exit_cross(pygame.sprite.Sprite):
    # Открываем изображение и маштабируем
    top = load_image("exit_cross.png", cat='Sprite_meny_play')
    image = pygame.transform.scale(top, ((top.get_width() / 1.1) * (WIDTH / 1069), (top.get_height() / 1.1) * (HEIGHT / 1020)))

    def __init__(self, group):
        super().__init__(group)
        self.image = Exit_cross.image
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = 10 * (WIDTH / 1069) + 1
        self.rect.y = 10 * (HEIGHT / 1020) + 1

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            terminate()


def start_screen():
    fon = pygame.transform.scale(load_image('meny.jpg', cat='Sprite_meny_play'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    Boor(meny_sprites)
    User(meny_sprites)
    Top(meny_sprites)
    Exit_cross(meny_sprites)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                meny_sprites.update(event)
        meny_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)