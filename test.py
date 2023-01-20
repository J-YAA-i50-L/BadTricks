import pygame


def draw(count):
    global size
    k = 300 // (count * 2)
    x1 = 0
    y1 = 0
    h = 300
    w = 300
    for i in range(count):
        pygame.draw.ellipse(screen, (255, 255, 255), (x1, y1, h, w), -2)
        pygame.draw.ellipse(screen, (255, 255, 255), (y1, x1, w, h), 1)
        y1 += k
        w -= 2 * k


n = input()
f = True
if n in '.':
    print("Неправильный формат ввода")
    f = False

if __name__ == '__main__' and f:
    pygame.init()
    pygame.display.set_caption('Сфера')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    draw(int(n))
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()
