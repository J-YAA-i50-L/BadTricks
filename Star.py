from GeneralFunctions import *


class Star(pygame.sprite.Sprite):
    star = load_image('Star_0.png', cat='Star')
    star_image = pygame.transform.scale(star, (star.get_width() * 0.08 * (WIDTH / 1280),
                                        star.get_height() * 0.08 * (HEIGHT / 720)))
    star = load_image('Star_1.png', cat='Star')
    star_image_1 = pygame.transform.scale(star, (star.get_width() * 0.08 * (WIDTH / 1280),
                                          star.get_height() * 0.08 * (HEIGHT / 720)))

    def __init__(self, group, x, y, predmet, meaning):
        super().__init__(group)
        self.predmet = predmet
        self.meaning = meaning
        spicok = read_progress()
        if spicok[self.predmet][self.meaning - 1]:
            self.image = Star.star_image
        else:
            self.image = Star.star_image_1
        self.rect = self.image.get_rect()
        self.rect.x = x * (WIDTH / 1280)
        self.rect.y = y * (HEIGHT / 720)
