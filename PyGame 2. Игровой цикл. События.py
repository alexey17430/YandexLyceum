import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('К щелчку')
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    running = True

    fps = 80
    clock = pygame.time.Clock()

    pygame.draw.circle(screen, pygame.Color('red'), (250, 250), 20)
    moving_now = False
    cx, cy = 250, 250

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                moving_now = True
                mx, my = event.pos
                if cx < mx:
                    dx = 1
                elif cx > mx:
                    dx = -1
                else:
                    dx = 0

                if cy < my:
                    dy = 1
                elif cy > my:
                    dy = -1
                else:
                    dy = 0
        if moving_now and cx != mx and cy != my:
            cx += dx
            cy += dy
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, pygame.Color('red'), (cx, cy), 20)
        elif moving_now and cx == mx and cy == my:
            moving_now = False
            dx = 0
            dy = 0
        elif moving_now and cx == mx and cy != my:
            dx = 0
            cx += dx
            cy += dy
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, pygame.Color('red'), (cx, cy), 20)
        elif moving_now and cx != mx and cy == my:
            dy = 0
            cx += dx
            cy += dy
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, pygame.Color('red'), (cx, cy), 20)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
