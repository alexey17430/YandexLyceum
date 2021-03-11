import pygame


def draw(w, h):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, pygame.Color(255, 255, 255), (0, 0), (w, h), 5)
    pygame.draw.line(screen, pygame.Color(255, 255, 255), (w, 0), (0, h), 5)


if __name__ == '__main__':
    try:
        w, h = map(int, input().split())
        pygame.init()
        size = (w, h)
        screen = pygame.display.set_mode(size)
        draw(w, h)
    except:
        print('Неверный формат введённых данных')
        exit(0)
    pygame.display.set_caption('Крест')
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
