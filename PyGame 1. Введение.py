import pygame


def draw(n):
    screen.fill(color=pygame.Color('yellow'))
    for i in range(300 // n):
        for j in range(300 // n):
            pygame.draw.polygon(screen, color=pygame.Color('orange'),
                                points=((j * n, i * n + n / 2),
                                        (j * n + n / 2, i * n + n),
                                        (j * n + n, i * n + n / 2),
                                        (j * n + n / 2, i * n),
                                        (j * n, i * n + n / 2)))


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
    pygame.display.set_caption('Ромбики')
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
