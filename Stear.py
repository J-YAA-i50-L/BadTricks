from GeneralFunctions import *


class Stear(pygame.sprite.Sprite):
    image = load_image('stear.png', cat='Tex')

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Stear.image
        self.rect = self.image.get_rect()
        self.rect.x = x * (WIDTH / 1700)
        self.rect.y = y * (HEIGHT / 850)