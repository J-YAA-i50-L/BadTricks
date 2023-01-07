from GeneralFunctions import *

tile_images = {'floor': load_image('Floor0.png', cat='Tex'), 'wall':load_image('Wall0.png', cat='Tex')}
all_sprites = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(all_sprites)
        floor = tile_images[tile_type]
        self.image = pygame.transform.scale(floor, (floor.get_width() * (WIDTH / 1600),
                                        floor.get_height() * (HEIGHT / 800)))
        self.rect = self.image.get_rect().move(32 * WIDTH / 1600 * pos_x, 32 * HEIGHT / 800 * pos_y)


def generate_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '_':
                Tile('floor', x, y)
            elif level[y][x] == '|':
                Tile('wall', x, y)


while True:
    screen.fill((0, 0, 0))
    generate_level(load_level('test_lvl.txt'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
