from GeneralFunctions import *
from sqlite3 import connect


class User(pygame.sprite.Sprite):  # Класс User для авторизации и сохранения прогресса
    # Открываем изображение и маштабируем
    user = load_image("sprite_user.png", cat='Sprite_meny_play')
    image = pygame.transform.scale(user, ((user.get_width() / 2) * (WIDTH / 1000),
                                          (user.get_height() / 1.85) * (HEIGHT / 1000)))

    def __init__(self, group):
        super().__init__(group)
        self.image = User.image
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = 995 * (WIDTH / 1069) + 1
        self.rect.y = 15 * (HEIGHT / 1020) + 1
        self.button_play = True

    def update(self, *args):
        if args and self.rect.collidepoint(args[0].pos):
            pygame.draw.rect(self.image, pygame.Color('#3b83bd'),
                             (0, 0, self.image.get_width(), self.image.get_height() + 1), 3)
            if self.button_play:
                button_sound.play()
                self.button_play = False
        else:
            pygame.draw.rect(self.image, pygame.Color('#7da4c5'),
                             (0, 0, self.image.get_width(), self.image.get_height() + 1), 3)
            self.button_play = True
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            signal_input('auth')


class PrintArea(pygame.sprite.Sprite):  # Класс PrintArea для ввода информации в авторизации

    def __init__(self, group, status):
        super().__init__(group)
        self.status = status
        self.open()
        if self.status == "pas":  # Для пароля
            self.image = self.imagee_copy
            self.rect = self.image.get_rect()
        else:
            self.image = self.image_copy
            self.rect = self.image.get_rect()
        self.text_input = ''
        self.flag = False
        # Координаты левого верхнего угла с учетом размера экранна
        if self.status == "log":  # Для логина
            self.rect.x = 955 * (WIDTH / 2779) + 1
            self.rect.y = 502 * (HEIGHT / 1381) + 1
        if self.status == "pas":  # Для пароля
            self.rect.x = 954 * (WIDTH / 2779) + 1
            self.rect.y = 733 * (HEIGHT / 1381) + 1

    def update(self, *args):
        global text_log
        global text_pas
        self.open()
        if args[0].type == pygame.MOUSEBUTTONDOWN:
            if args and self.rect.collidepoint(args[0].pos) and args[0].type == pygame.MOUSEBUTTONDOWN and not self.flag:
                self.flag = True
            else:
                self.flag = False
                signal_input(self.text_input)
        if args[0].type == pygame.KEYDOWN and self.flag:
            if len(self.text_input) <= 22:
                if args[0].key == pygame.K_BACKSPACE:
                    self.text_input = self.text_input[:-1]
                    if self.status == "pas":
                        self.image = self.imagee_copy
                    else:
                        self.image = self.image_copy
                else:
                    self.text_input += args[0].unicode
            text = (self.text_input, (25, 5))
            font = pygame.font.SysFont('arial', int(80 * (HEIGHT / 1381)))
            string_rendered = font.render(text[0], 20, pygame.Color('black'))
            self.image.blit(string_rendered, text[-1])
            if self.status == "pas":  # Для пароля
                text_pas = self.text_input
            else:
                text_log = self.text_input

    def open(self):
        # Открываем изображение и маштабируем
        load_im = load_image("print_area.png", cat='Sprite_meny_play')
        self.image_copy = pygame.transform.scale(load_im, (load_im.get_width() * (WIDTH / 2779),
                                                 load_im.get_height() * (HEIGHT / 1381)))
        self.imagee_copy = pygame.transform.scale(load_im, (load_im.get_width() * (WIDTH / 2779),
                                                  load_im.get_height() * (HEIGHT / 1381)))


class ButtonRun(pygame.sprite.Sprite):  # Кнопка "продолжить"
    # Открываем изображение и маштабируем
    load_im = load_image("button_run.png", cat='Sprite_meny_play')
    image = pygame.transform.scale(load_im, (load_im.get_width() * (WIDTH / 2779),
                                             load_im.get_height() * (HEIGHT / 1381)))
    load_im_clik = load_image("button_run_clik.png", cat='Sprite_meny_play')
    image_clik = pygame.transform.scale(load_im_clik, (load_im.get_width() * (WIDTH / 2779),
                                             load_im.get_height() * (HEIGHT / 1381)))

    def __init__(self, group):  # При созданиии класса
        super().__init__(group)
        self.image = ButtonRun.image
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = 1055 * (WIDTH / 2779) + 1
        self.rect.y = 900 * (HEIGHT / 1381) + 1

    def update(self, *args):  # Результаты события
        if args[0].type == pygame.MOUSEMOTION or args[0].type == pygame.MOUSEBUTTONDOWN:  # Если событие мыши
            if args and self.rect.collidepoint(args[0].pos):  # Если мышь наведена на кнопу
                self.image = ButtonRun.image_clik  # Меняем изображение
            else:
                self.image = ButtonRun.image  # Меняем на исходное
            if args and self.rect.collidepoint(args[0].pos) and args[0].type == pygame.MOUSEBUTTONDOWN:
                # Если была нажата кнопка мыши проверяем логин и пароль
                # Если они совпадают с данными бд мы сохраняем файл с прогресом и запускаем окно выбора уровня
                if proverca_user(text_log, text_pas):
                    signal_input('run')
                else:
                    print('Не верное имя или пароль')


class Registration(pygame.sprite.Sprite): # Конпка регистрация
    load_im = load_image("registration.png", cat='Sprite_meny_play')
    image = pygame.transform.scale(load_im, (load_im.get_width() * 1.5 * (WIDTH / 2779),
                                             load_im.get_height() * 1.5 * (HEIGHT / 1381)))

    def __init__(self, group):
        super().__init__(group)
        self.image = Registration.image
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = 2095 * (WIDTH / 2779) + 1
        self.rect.y = 15 * (HEIGHT / 1381) + 1

    def update(self, *args):
        if args[0].type == pygame.MOUSEMOTION or args[0].type == pygame.MOUSEBUTTONDOWN:  # Если событие мыши
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                signal_input('registration')


def proverca_user(log, pas):  # Проверка логина и пароля
    global name_info
    print(log, pas)
    con = connect("BadTriks_bd.sqlite")
    cur = con.cursor()
    result = cur.execute(f"""SELECT DISTINCT login, password, progress FROM user ORDER BY rating DESC""").fetchall()
    con.close()
    for i in result:
        if log == i[0] and pas == str(i[1]):
            name_info = i[2]
            return True
        else:
            return False
