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
        self.stop_counter = 0
        self.move_counter = 0
        self.rmove = False
        self.lmove = False

    def update(self, *args):
        if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_RIGHT:
            self.rmove = True
            self.lmove = False
            self.rect = self.rect.move(5, 0)
        elif args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_LEFT:
            self.rmove = False
            self.lmove = True
            self.rect = self.rect.move(-5, 0)
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
        else:
            self.stop_counter += 1
            if self.stop_counter // 25 % 2 == 1:
                self.image = self.frames[1]
            else:
                self.image = self.frames[0]