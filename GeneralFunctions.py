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
text_log = ''
text_pas = ''
signal_auth = None
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
meny_sprites = pygame.sprite.Group()
authorization_sprites = pygame.sprite.Group()
top_sprites = pygame.sprite.Group()
level_choice_sprites = pygame.sprite.Group()
top_sprites = pygame.sprite.Group()
level1_sprites = pygame.sprite.Group()
button_sound = pygame.mixer.Sound('Music/button.wav')
menu_music = False
lvl1_music = False


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


def music(type_music): # добавляем музыку в зависимомти от текущего экрана
    global menu_music
    global lvl1_music
    if type_music == 'menu':
        if not menu_music:
            pygame.mixer.music.load('Music/01Menu.wav')
            pygame.mixer.music.play(-1)
            menu_music = True
            lvl1_music = False
    elif type_music == 'lvl1':
        if not lvl1_music:
            pygame.mixer.music.load('Music/04Chapter 1 Theme.wav')
            pygame.mixer.music.play(-1)
            menu_music = False
            lvl1_music = True


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line for line in mapFile]

    return level_map


def generate_level(level, tile): # генерациы уровня
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '_':
                tile('floor', x, y)
            elif level[y][x] == '|':
                tile('wall', x, y)
            elif level[y][x] == '.':
                tile('fon', x, y)
            elif level[y][x] == '0':
                tile('window', x, y)
            elif level[y][x] == ' ':
                tile('sky', x, y)
            elif level[y][x] == '#':
                tile('roof', x, y)
            elif level[y][x] == 'B':
                tile('box', x, y)