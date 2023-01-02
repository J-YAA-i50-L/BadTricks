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
        if args and self.rect.collidepoint(args[0].pos) and args[0].type == pygame.MOUSEBUTTONDOWN:
            signal_input('lvl_choice')
