import pygame


def draw(n):
    pi = 3.14
    screen.fill(color=pygame.Color('black'))
    dx = 150 / n
    for i in range(n):
        pygame.draw.ellipse(screen, pygame.Color('white'), (dx * i, 0, 300 - dx * i * 2, 300),
                            width=1)
    for j in range(n):
        pygame.draw.ellipse(screen, pygame.Color('white'), (0, dx * j, 300, 300 - dx * j * 2),
                            width=1)


if __name__ == '__main__':
    pygame.init()
    try:
        n = int(input())
        size = (300, 300)
        screen = pygame.display.set_mode(size)
        draw(n)
    except:
        print('Введены данные в неверном формате')
        exit(0)
    pygame.display.set_caption('Сфера')
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
