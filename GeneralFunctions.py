import os
import sys
import pygame
from screeninfo import get_monitors
import time
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
name_info = 'info.txt'
signal_auth = None
camera_coords = []
rove_coords = []
wall_coords = []
user_coords = []
journal_coords = []
door_coords = []
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
meny_sprites = pygame.sprite.Group()
authorization_sprites = pygame.sprite.Group()
top_sprites = pygame.sprite.Group()
reg_sprites = pygame.sprite.Group()
level_choice_sprites = pygame.sprite.Group()
level_sprites = pygame.sprite.Group()
timer_sprites = pygame.sprite.Group()
npc_sprites = pygame.sprite.Group()
button_sound = pygame.mixer.Sound('Music/button.wav')
ruchka_sound = pygame.mixer.Sound('Music/ruchka.wav')
win_sound = pygame.mixer.Sound('Music/win.wav')
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


def terminate():  # Программа завершает работу
    pygame.quit()
    sys.exit()


def music(type_music):  # Добавляем музыку в зависимомти от текущего экрана
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
    # Читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line for line in mapFile]
    return level_map


def generate_level(level, tile):  # Генерациы уровня
    s = {'.': 'fon', ' ': 'sky', '_': 'floor', '|': 'wall',
         '0': 'window', '#': 'roof', 'B': 'box', 'y': 'fon_dock',
         'P': 'pk', 'b': 'box_book', 't': 'table', 'p': 'pedestal',
         ',': 'fon_bio'}
    global camera_coords, rove_coords, user_coords, journal_coords, wall_coords, door_coords
    camera_coords = []
    rove_coords = []
    user_coords = []
    journal_coords = []
    wall_coords = []
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':  # Спавн игрока
                tile(s[level[y][x + 1]], x, y)
                user_coords.append([x, y])
            elif level[y][x] == '#':
                tile('roof', x, y)
            elif level[y][x] == 'B':
                tile('box', x, y)
            elif level[y][x] == 'C':  # Камера
                tile(s[level[y][x + 1]], x, y)
                camera_coords.append([x, y])
            elif level[y][x] == 'R':  # Лестница Металическая(300р.)
                tile('floor', x, y)
                rove_coords.append([x, y])
            elif level[y][x] == 'D':  # Дверь в стене
                tile('WallDoor', x, y)
            elif level[y][x] == 'G':
                tile(s[level[y][x + 1]], x, y)
                journal_coords.append([x, y])
            elif level[y][x] == '|':
                tile('wall', x, y)
                wall_coords.append([x, y])
            else:
                if level[y][x] != '\n':
                    tile(s[level[y][x]], x, y)
    print(list(map(lambda x: [int(x[0] * (WIDTH / 1750) * 34),
                                      int(x[1] * (HEIGHT / 850) * 34)], wall_coords)))
    wall_coords = list(map(lambda x: [int(x[0] * (WIDTH / 1750) * 34 // 10 * 10 + 5),
                                      int((x[1] * (HEIGHT / 850)) * 34 // 10 * 10)], wall_coords))


def info_subject():
    # print('\t', wall_coords)
    return camera_coords, rove_coords, wall_coords, journal_coords, user_coords


def door_info():
    return door_coords


def read_progress():  # Чтение файла c прогресом
    s = {4: 'fiz', 5: 'xim', 1: 'tex', 2: 'bio', 3: 'lit'}
    znach = {'*': True, ' ': False}
    with open(f"data/progress/{name_info}", encoding="utf-8") as f:
        read_data = f.read().split('\n')
        if len(read_data) < 5:
            for _ in range(5 - len(read_data)):
                read_data.append('')
        result = []
        for i in read_data:
            if len(i) < 3:
                for _ in range(3 - len(i)):
                    i += ' '
            result.append([znach[j] for j in i])
        read_data = result
        slov = {}
        for n, i in enumerate(read_data):
            slov[s[n + 1]] = i
        read_data = slov
    return read_data


def recording_progress(data):  # Запись прогреса в файл прогерсса
    with open(f"data/progress/{name_info}", 'r+') as f:
        read_data = f.read().split('\n')
        f.truncate(0)
    with open(f"data/progress/{name_info}", "w") as f:
        for i in read_data[:-1]:
            print(i, file=f)
        print(data, file=f)


def file_progress(name):
    global name_info
    name_info = name


class Mig(pygame.sprite.Sprite):
    image = load_image("yimg.png", cat='data')

    def __init__(self):
        super().__init__(npc_sprites)
        self.image = pygame.transform.scale(Mig.image, (Mig.image.get_width() / 1700 * 100,
                                                            Mig.image.get_height() / 850 * 100))
        self.rect = self.image.get_rect()