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
        self.rect.x = int(int(x) * (WIDTH / 1700) * 34)
        self.rect.y = int(int(y) * (HEIGHT / 850) * 34)
        self.k = 0
        self.count = 0
        self.rmove = False
        self.lmove = False
        self.move = True

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
                else:
                    self.rmove = False
                    self.lmove = True
                print(self.count)
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
