from GeneralFunctions import *


class ExitСross(pygame.sprite.Sprite):  # Класс ExitСross для выхода из игры или возвращение назад
    # Открываем изображение и маштабируем
    top = load_image("exit_cross.png", cat='Sprite_meny_play')
    image = pygame.transform.scale(top, ((top.get_width()) * (WIDTH / 1069),
                                         (top.get_height()) * (HEIGHT / 1020)))

    def __init__(self, group, status='ter'):
        super().__init__(group)
        self.image = ExitСross.image
        self.rect = self.image.get_rect()
        self.status = status
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = 5 * (WIDTH / 1069) + 1
        self.rect.y = 5 * (HEIGHT / 1020) + 1

    def update(self, *args):
        if (args and args[0].type == pygame.MOUSEBUTTONDOWN and
                self.rect.collidepoint(args[0].pos) and self.status == 'ter'):
            terminate()
        elif(args and args[0].type == pygame.MOUSEBUTTONDOWN and
                self.rect.collidepoint(args[0].pos) and self.status == 'back'):
            signal_input('exit')
