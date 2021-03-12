import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0
    v = 10
    fps = 30
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('blue'))
    r = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill(pygame.Color('blue'))
                r = 5
                x, y = event.pos
                pygame.draw.circle(screen, pygame.Color('yellow'), (x, y), r)
        if r > 0:
            r += v / fps
            pygame.draw.circle(screen, pygame.Color('yellow'), (x, y), r)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
