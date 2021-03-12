import pygame
from random import randint

WHITE = (255, 255, 255)


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 10 or self.x > width - 10:
            self.vx *= -1
        if self.y < 10 or self.y > height - 10:
            self.vy *= -1

    def coords(self):
        return self.x, self.y


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    balls = []
    running = True
    v = 100
    fps = 60
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    ball = Ball(*event.pos)
                    balls.append(ball)

        screen.fill((0, 0, 0))
        for ball in balls:

            pygame.draw.circle(screen, WHITE, ball.coords(), 10)
            ball.move()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
