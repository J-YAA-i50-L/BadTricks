from GeneralFunctions import *
import pygame
from screeninfo import get_monitors

file_camer = {0: 'Cam_0.png', 1: 'Cam_1.png', 2: 'Cam_2.png'}


class Camera(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.tick = 0
        self.frames = []
        for i in range(3):
            cam = load_image(f"Cam_{i}.png", cat='Camera')
            cam_image = pygame.transform.scale(cam, (cam.get_width() * 0.1,
                                                     cam.get_height() * 0.1))
            self.frames.append(cam_image)
        self.image = self.frames[1]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = int(int(x) * (WIDTH / 1700) * 34)
        self.rect.y = int(int(y) * (HEIGHT / 850) * 34)
        self.k = 0
        self.count = 0
        self.rmove = False
        self.lmove = False
        self.move = True
        self.nothing = None

    def update(self, *args):
        self.tick += 1
        self.animation()

    def animation(self):
        if self.tick % 300 == 0 and self.k != 20 or self.move:
            self.image = self.frames[1]
            if self.k == 20:
                self.count += 1
                if self.count % 2 == 0:
                    self.rmove = True
                    self.lmove = False
                    Nothing(int(int(self.x) * (WIDTH / 1700) * 34) + 140 * (WIDTH / 1700),
                            int(int(self.y) * (HEIGHT / 850) * 34),
                            9 * (WIDTH / 1700) * 34, 34 * 6 * (HEIGHT / 850))
                else:
                    self.rmove = False
                    self.lmove = True
                    Nothing(int(int(self.x) * (WIDTH / 1700) * 34) - 8 * (WIDTH / 1700) * 34,
                            int(int(self.y) * (HEIGHT / 850) * 34),
                            8 * (WIDTH / 1700) * 34, 34 * 6 * (HEIGHT / 850))
                self.move = False
            else:
                self.move = True
            self.k += 1

        elif self.rmove:
            self.k = 0
            self.image = self.frames[2]

        elif self.lmove:
            self.k = 0
            self.image = self.frames[0]


class Nothing(pygame.sprite.Sprite):
    image = load_image("nothing.png", cat='data')

    def __init__(self, x, y, wigth, height):
        super().__init__(npc_sprites)
        self.image = pygame.transform.scale(Nothing.image, (Nothing.image.get_width() / 1700 * wigth,
                                                     Nothing.image.get_height() / 850 * height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tick = 1

    def update(self, *args):
        self.tick += 1
        if self.tick % 300 == 0:
            self.kill()
