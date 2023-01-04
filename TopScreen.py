from GeneralFunctions import *
from sqlite3 import connect


class Top(pygame.sprite.Sprite):  # Класс Top таблица лучших играков
    # Открываем изображение и маштабируем
    top = load_image("sprite_top.png", cat='Sprite_meny_play')
    image = pygame.transform.scale(top, ((top.get_width() / 2) * (WIDTH / 1000),
                                         (top.get_height() / 1.87) * (HEIGHT / 1000)))

    def __init__(self, group):
        super().__init__(group)
        self.image = Top.image
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = 905 * (WIDTH / 1069) + 1
        self.rect.y = 15 * (HEIGHT / 1020) + 1
        self.button_play = True

    def update(self, *args):
        global signal_start
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
            signal_input('top')


def top_str():
    con = connect("BadTriks_bd.sqlite")
    cur = con.cursor()
    result = cur.execute(f"""SELECT DISTINCT login, rating FROM user ORDER BY rating DESC""").fetchall()
    con.close()
    if len(result) >= 5:
        result = result[:5]
    return [f'{n + 1}.  {i[0]}   {i[-1]}' for n, i in enumerate(result)]
