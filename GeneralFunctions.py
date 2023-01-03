import os
import sys
import pygame
from screeninfo import get_monitors
pygame.init()
pygame.key.set_repeat(200, 70)
# Разрешение экрана
screen_info = str(get_monitors()[0])[8:-1].split(', ')
WIDTH = int(screen_info[2][6:])
HEIGHT = int(screen_info[3][7:])
FPS = 50
STEP = 10
signal_start = ''
signal_auth = None
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
meny_sprites = pygame.sprite.Group()
authorization_sprites = pygame.sprite.Group()
top_sprites = pygame.sprite.Group()


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


def signal_output():
    global signal_start
    return signal_start


def signal_input(signal):
    global signal_start
    signal_start = signal


def terminate():
    pygame.quit()
    sys.exit()
