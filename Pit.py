from GeneralFunctions import *


class Pit(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.frames = []
        for i in range(12):
            pit = load_image(f"Pit_{i}.png", cat='Sprite_Piter')
            pit_image = pygame.transform.scale(pit, (pit.get_width() * 0.1 * (WIDTH / 1700),
                                                     pit.get_height() * 0.1 * (HEIGHT / 850)))
            self.frames.append(pit_image)
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = x * (WIDTH / 1700)
        self.rect.y = y * (HEIGHT / 850)
        self.frame_counter = 0
        self.stop = True
