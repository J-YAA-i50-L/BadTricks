from GeneralFunctions import *


class LevelDoor(pygame.sprite.Sprite): # дверь для выбора уровня
    # Открываем изображение и маштабируем
    door = load_image("Door0.png", cat='Door')
    door_image = pygame.transform.scale(door, (door.get_width() * 0.25 * (WIDTH / 1280),
                                        door.get_height() * 0.25 * (HEIGHT / 720)))
    open_door = load_image("Door1.png", cat='Door')
    open_door_image = pygame.transform.scale(open_door, (open_door.get_width() * 0.25 * (WIDTH / 1280),
                                             open_door.get_height() * 0.25 * (HEIGHT / 720)))

    def __init__(self, group, x, y, predmet):
        super().__init__(group)
        self.predmet = predmet
        self.image = LevelDoor.door_image
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = x * (WIDTH / 1280)
        self.rect.y = y * (HEIGHT / 720)
        self.button_play = True

    def update(self, *args):
        if args:
            if self.rect.collidepoint(args[0].pos):
                self.image = LevelDoor.open_door_image
                if self.button_play:
                    button_sound.play()
                    self.button_play = False
            else:
                self.image = LevelDoor.door_image
                self.button_play = True
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if self.predmet == 'tex':
                signal_input('lvl1')
