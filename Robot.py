from GeneralFunctions import *


class Robot(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.frames = []
        for i in range(12):
            robot = load_image(f"sprite_robot{i}.png", cat='Sprite_robot')
            pit_image = pygame.transform.scale(robot, (robot.get_width() * 0.1 * (WIDTH / 1700),
                                                     robot.get_height() * 0.1 * (HEIGHT / 850)))
            self.frames.append(pit_image)
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = x * (WIDTH / 1700) * 34
        self.rect.y = y * (HEIGHT / 850) * 34 + 5
        self.lmove = True
        self.rmove = False
        self.y = y

    def update(self):
        for coord in door_info():
            if self.y == coord[-1]:
                if self.rmove:
                    if self.rect.right >= coord[0] - 5:
                        self.rmove = False
                        self.lmove = True
                elif self.lmove:
                    if self.rect.left <= coord[0] + 5:
                        self.rmove = True
                        self.lmove = False
        if self.rmove:
            self.rect = self.rect.move(1, 0)
        elif self.lmove:
            self.rect = self.rect.move(-1, 0)
            self.rect = self.rect.move(-1, 0)
