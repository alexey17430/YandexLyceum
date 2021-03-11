import pygame


def draw(width, colvo):
    screen.fill((0, 0, 0))
    sqr_width = width / colvo
    color_start = 'black'
    for i in range(colvo):
        color = color_start
        for j in range(colvo):
            if color == 'white':
                pygame.draw.rect(screen, pygame.Color('white'), (
                width - sqr_width * (colvo - j), width - sqr_width * (i + 1),
                sqr_width, sqr_width), 0)
                color = 'black'
            else:
                color = 'white'
        if color_start == 'black':
            color_start = 'white'
        else:
            color_start = 'black'


if __name__ == '__main__':
    pygame.init()
    try:
        a, n = map(int, input().split())
        size = (a, a)
        screen = pygame.display.set_mode(size)
        draw(a, n)
    except:
        print('Введены данные в неверном формате')
        exit(0)
    pygame.display.set_caption('Шахматная клетка')
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
