import pygame


def draw(w, hue):
    screen.fill(color=pygame.Color('black'))

    color = pygame.Color(0, 0, 0)
    hsv = color.hsva
    color.hsva = (hue, 100, 75, hsv[3])
    x = 150 - (w + w // 2) // 2
    y = (300 - w - w // 2) // 2 + w // 2
    pygame.draw.rect(screen, color, rect=(x, y, w, w))

    color = pygame.Color(0, 0, 0)
    hsv = color.hsva
    color.hsva = (hue, 100, 100, hsv[3])
    x1 = (150 - (w + w // 2) // 2) + w // 2
    y1 = (300 - w - w // 2) // 2
    x2 = (150 - (w + w // 2) // 2) + w // 2 + w
    y2 = (300 - w - w // 2) // 2
    x3 = (150 - (w + w // 2) // 2) + w
    y3 = (300 - w - w // 2) // 2 + w // 2
    x4 = 150 - (w + w // 2) // 2
    y4 = (300 - w - w // 2) // 2 + w // 2
    pygame.draw.polygon(screen, color, ((x1, y1),
                                        (x2, y2),
                                        (x3, y3),
                                        (x4, y4)))

    color = pygame.Color(0, 0, 0)
    hsv = color.hsva
    color.hsva = (hue, 100, 50, hsv[3])
    x1 = (150 - (w + w // 2) // 2) + w
    y1 = (300 - w - w // 2) // 2 + w // 2 + w
    x4 = (150 - (w + w // 2) // 2) + w + w // 2
    y4 = (300 - w - w // 2) // 2 + w
    pygame.draw.polygon(screen, color, ((x2, y2),
                                        (x3, y3),
                                        (x1, y1),
                                        (x4, y4)))


if __name__ == '__main__':
    pygame.init()
    try:
        w, hue = map(int, input().split())
        size = (300, 300)
        if w > 150 or w % 4 != 0 or not 0 <= hue <= 100:
            raise IndexError
        screen = pygame.display.set_mode(size)
        draw(w, hue)
    except:
        print('Введены данные в неверном формате')
        exit(0)
    pygame.display.set_caption('Куб')
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
