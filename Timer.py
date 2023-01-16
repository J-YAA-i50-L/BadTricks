from GeneralFunctions import *


class Timer(pygame.sprite.Sprite):
    image = load_image("clock.png", cat='data')

    def __init__(self, group):
        super().__init__(group)
        self.group = group
        self.image = pygame.transform.scale(Timer.image, (Timer.image.get_width() * 0.2 * (WIDTH / 1700),
                                            Timer.image.get_height() * 0.2 * (HEIGHT / 850)))
        self.rect = self.image.get_rect()
        self.rect.x = 1400 * (WIDTH / 1700)
        self.rect.y = 5 * (HEIGHT / 850)
        self.time_counter = 0
        self.game_time = 0
        self.number = Number(self.group, '0', 0)

    def update_time(self):
        self.time_counter += 1
        if self.time_counter % 50 == 0:
            self.game_time += 1
            if self.game_time <= 9999:
                for i in range(len(list(str(self.game_time)))):
                    if self.number.get_num() != int(list(str(self.game_time))[self.number.get_nom()]):
                        self.number.kill()
                        print(1)
                    self.number = Number(self.group, list(str(self.game_time))[i], i)

    def get_time(self):
        return self.game_time


num_dict = {'0': '0.png',
            '1': '1.png',
            '2': '2.png',
            '3': '3.png',
            '4': '4.png',
            '5': '5.png',
            '6': '6.png',
            '7': '7.png',
            '8': '8.png',
            '9': '9.png'}


class Number(pygame.sprite.Sprite):
    def __init__(self, group, num, nomer):
        super().__init__(group)
        self.image = load_image(num_dict[num], cat='data')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.2 * (WIDTH / 1700) + 1,
                                                         self.image.get_height() * 0.2 * (HEIGHT / 850) + 1))
        self.rect = self.image.get_rect()
        self.rect.y = -20
        self.rect.x = (WIDTH / 1700) * 1360 + nomer * 40 * (WIDTH / 1700)
        self.num = num
        self.nom = nomer

    def get_num(self):
        return int(self.num)

    def get_nom(self):
        return int(self.nom)


