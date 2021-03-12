import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Перетаскивание')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    running = True
    v = 100
    fps = 60
    clock = pygame.time.Clock()
    clicked = False
    rx, ry = 0, 0
    w, h = 100, 100
    pygame.draw.rect(screen, pygame.Color('green'), (rx, ry, w, h))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = event.pos
                    if rx <= mx <= rx + w and ry <= my <= ry + h and not clicked:
                        clicked = True
                        dx = mx - rx
                        dy = my - ry

            if event.type == pygame.MOUSEMOTION and clicked:
                screen.fill((0, 0, 0))
                mx, my = event.pos
                rx, ry = mx - dx, my - dy
                pygame.draw.rect(screen, pygame.Color('green'), (rx, ry, w, h))
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
