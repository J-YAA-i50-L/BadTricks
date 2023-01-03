from GeneralFunctions import *


class Star(pygame.sprite.Sprite):
    star = load_image('Star_0.png', cat='Star')
    star_image = pygame.transform.scale(star, (star.get_width() * 0.08 * (WIDTH / 1280),
                                        star.get_height() * 0.08 * (HEIGHT / 720)))

    def __init__(self, group, x, y, predmet, nom):
        super().__init__(group)
        self.predmet = predmet
        self.nom = nom
        self.image = Star.star_image
        self.rect = self.image.get_rect()
        self.rect.x = x * (WIDTH / 1280)
        self.rect.y = y * (HEIGHT / 720)