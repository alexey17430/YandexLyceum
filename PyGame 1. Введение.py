import pygame


def draw(w, h):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, pygame.Color(255, 0, 0), (2, 2, w - 3, h - 3), 0)


if __name__ == '__main__':
    try:
        width, height = map(int, input().split())
        pygame.init()
        size = (width, height)
        screen = pygame.display.set_mode(size)
        draw(width, height)
        pygame.display.set_caption('Прямоугольник')
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except:
        print('Неверный формат введённых данных')
        exit(0)
