from GeneralFunctions import *


class Journal(pygame.sprite.Sprite):
    image = load_image('journal.png', cat='Tex')

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = pygame.transform.scale(Journal.image, (Journal.image.get_width() * (WIDTH / 1700),
                                                            Journal.image.get_height() * (HEIGHT / 850)))
        self.rect = self.image.get_rect()
        self.rect.x = x * (WIDTH / 1700) * 34
        self.rect.y = y * (HEIGHT / 850) * 34 + (15 * (HEIGHT / 850))
