import pygame


def draw():
    screen.fill(color=pygame.Color('black'))
    x, y = 0, 0
    for i in range(12):
        for j in range(10):
            if i % 2 != 0 and j == 0:
                pygame.draw.rect(screen, pygame.Color('red'), (x, y, 15, 15))
                pygame.draw.rect(screen, pygame.Color('white'), (x + 15, y, 2, 15))
                x += 17
            else:
                pygame.draw.rect(screen, pygame.Color('red'), (x, y, 30, 15))
                pygame.draw.rect(screen, pygame.Color('white'), (x + 30, y, 2, 15))
                x += 32

        pygame.draw.rect(screen, pygame.Color('white'), (0, y + 15, 300, 2))
        y += 17
        x = 0


if __name__ == '__main__':
    pygame.init()
    try:
        size = (300, 200)
        screen = pygame.display.set_mode(size)
        draw()
    except:
        print('Введены данные в неверном формате')
        exit(0)
    pygame.display.set_caption('Кирпичи')
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
