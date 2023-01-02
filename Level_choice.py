from GeneralFunctions import *


def level_choice():
    bg = pygame.transform.scale(load_image('level_choise_bg.png', cat='Level_choise'), (WIDTH, HEIGHT))
    while True:
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)


level_choice()
