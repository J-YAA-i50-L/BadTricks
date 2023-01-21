from GeneralFunctions import *


# изображение к элементу
tile_images = {'floor': load_image('Floor0.png', cat='Tex'),
               'wall': load_image('Wall0.png', cat='Tex'),
               'fon': load_image('Fon0.png', cat='Tex'),
               'window': load_image('Window0.png', cat='Tex'),
               'sky': load_image('Sky0.png', cat='Tex'),
               'roof': load_image('roof0.png', cat='Tex'),
               'box': load_image('box0.png', cat='Tex'),
               'WallDoor': load_image('Wall_Door0.png', cat='Tex'),
               'table': load_image('Table.png', cat='Tex'),
               'pedestal': load_image('Pedestal.png', cat='Tex'),
               'box_book': load_image('box_book.png', cat='Tex')}


class Tile1(pygame.sprite.Sprite):  # отрисовка уровня
    def __init__(self, tile_type, pos_x, pos_y):
        print(1)
        super().__init__(level1_sprites)
        floor = tile_images[tile_type]
        self.image = pygame.transform.scale(floor, (floor.get_width() * (WIDTH / 1700) + 1,
                                            floor.get_height() * (HEIGHT / 850) + 1))
        self.rect = self.image.get_rect().move(34 * WIDTH / 1700 * pos_x, 34 * HEIGHT / 850 * pos_y)