from GeneralFunctions import *


class Pit(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.frames = []
        for i in range(12):
            pit = load_image(f"Pit_{i}.png", cat='Sprite_Piter')
            pit_image = pygame.transform.scale(pit, (pit.get_width() * 0.1 * (WIDTH / 1700),
                                                     pit.get_height() * 0.1 * (HEIGHT / 850)))
            self.frames.append(pit_image)
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = x * (WIDTH / 1700) * 34
        self.rect.y = y * (HEIGHT / 850) * 34
        self.group = group
        self.stop_counter = 0
        self.move_counter = 0
        self.rmove = False
        self.lmove = False
        self.dmove = False
        self.umove = False
        self.start_pos = 0

    def update(self, *args):
        # print([self.rect.x, self.rect.y])
        if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_DOWN:
            for coord in info_subject()[1]:
                if (self.rect.left + 30 * (WIDTH / 1700) >= coord[0] * 34 * (WIDTH / 1700)
                    and self.rect.right - 30 * (WIDTH / 1700) <= (coord[0] + 2) * 34 * (WIDTH / 1700)
                    and (coord[1] - 3) * (HEIGHT / 850 * 34) <= self.rect.bottom <= (coord[1] + 3) * (
                        HEIGHT / 850 * 34) and not self.dmove and not self.umove):
                    self.start_pos = self.rect.bottom
                    self.dmove = True
                    self.rmove = False
                    self.lmove = False
                    self.umove = False
        elif args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_UP:
            for coord in info_subject()[1]:
                if (self.rect.left + 30 * (WIDTH / 1700) >= coord[0] * 34 * WIDTH / 1700
                    and self.rect.right - 30 * (WIDTH / 1700) <= (coord[0] + 2) * 34 * WIDTH / 1700
                    and (coord[1] + 4) * (HEIGHT / 850 * 34) <= self.rect.bottom <= (coord[1] + 10) * (
                        HEIGHT / 850 * 34) and not self.umove and not self.dmove):
                    self.start_pos = self.rect.bottom
                    self.umove = True
                    self.rmove = False
                    self.lmove = False
                    self.dmove = False
        elif args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_RIGHT and not self.dmove and not self.umove:
            print(info_subject()[2])
            if [(self.rect.x // 10 * 10 + 5) + (40 * (WIDTH / 1750) // 10 * 10),
               (self.rect.y - 5 * (HEIGHT / 850)) // 10 * 10] not in info_subject()[2]:
                self.rmove = True
                self.lmove = False
                self.rect = self.rect.move(10, 0)
            else:
                self.rmove = False
                self.lmove = False
        elif args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_LEFT and not self.dmove and not self.umove:
            if [self.rect.x // 10 * 10 + 5 - (30 * (WIDTH / 1750) // 10 * 10),
               (self.rect.y - (5 * (HEIGHT / 850)) // 10 * 10)] not in info_subject()[2]:
                self.rmove = False
                self.lmove = True
                self.rect = self.rect.move(-10, 0)
            else:
                self.rmove = False
                self.lmove = False
        else:
            self.rmove = False
            self.lmove = False

    def animation(self):
        if self.rmove:
            self.move_counter += 1
            if self.move_counter // 20 % 2 == 1:
                self.image = self.frames[4]
            else:
                self.image = self.frames[5]
        elif self.lmove:
            self.move_counter += 1
            if self.move_counter // 20 % 2 == 1:
                self.image = self.frames[6]
            else:
                self.image = self.frames[7]
        elif self.dmove:
            self.rmove = False
            self.lmove = False
            self.umove = False
            if self.rect.bottom - self.start_pos <= 238 * (WIDTH / 1750):
                self.move_counter += 1
                if self.move_counter // 20 % 2 == 1:
                    self.image = self.frames[9]
                    self.rect = self.rect.move(0, 2)
                else:
                    self.image = self.frames[10]
                    self.rect = self.rect.move(0, 2)
            else:
                self.dmove = False
        elif self.umove:
            self.rmove = False
            self.lmove = False
            self.dmove = False
            if self.start_pos - self.rect.bottom <= 238 * (WIDTH / 1750):
                self.move_counter += 1
                if self.move_counter // 20 % 2 == 1:
                    self.image = self.frames[9]
                    self.rect = self.rect.move(0, -2)
                else:
                    self.image = self.frames[10]
                    self.rect = self.rect.move(0, -2)
            else:
                self.umove = False
        else:
            self.stop_counter += 1
            if self.stop_counter // 25 % 2 == 1:
                self.image = self.frames[1]
            else:
                self.image = self.frames[0]

    def end(self):
        self.image = self.frames[11]
        ruchka_sound.play()



