import pygame


def draw(w, n):
    screen.fill((0, 0, 0))
    sp = ['red', 'green', 'blue']
    x, y = w * n, w * n
    for i in range(n):
        color = sp[i % 3]
        pygame.draw.circle(surface=screen, center=(x, y), radius=w + i * w,
                           color=pygame.Color(color), width=w)


if __name__ == '__main__':
    pygame.init()
    try:
        width, colvo = map(int, input().split())
        size = (width * colvo * 2, width * colvo * 2)
        screen = pygame.display.set_mode(size)
        draw(width, colvo)
    except:
        print('Введены данные в неверном формате')
        exit(0)
    pygame.display.set_caption('Мишень')
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
