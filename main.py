import os
import sys
import pygame
from tkinter import *

root = Tk()
pygame.init()
pygame.key.set_repeat(200, 70)
# Разрешение экрана
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
FPS = 50
STEP = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
meny_sprites = pygame.sprite.Group()


def load_image(name, color_key=None, cat='data'):
    fullname = os.path.join(cat, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


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
        im = self.image.copy()
        if args and self.rect.collidepoint(args[0].pos):
            pygame.draw.rect(self.image, pygame.Color('#f7943c'),
                             (0, 0, self.image.get_width() - 1, self.image.get_height() - 1), 3)
        else:
            pygame.draw.rect(self.image, pygame.Color('#6f6677'),
                             (0, 0, self.image.get_width() - 1, self.image.get_height() - 1), 3)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('meny.jpg', cat='Sprite_meny_play'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    Boor(meny_sprites)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEMOTION:
                meny_sprites.update(event)
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     return  # начинаем игру
        meny_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
running = True

while running:
    screen.fill(pygame.Color(0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    pygame.display.flip()
    clock.tick(FPS)

terminate()