# красный ходит первым
# если игрок нажал не на свой цвет, то он должен ещё раз нажать на круг, но уже своего цвета
import pygame
from random import randint


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = randint(0, 100) % 2
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.red_user = True

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                color = pygame.Color('black')

                pygame.draw.rect(screen, color,
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size,
                                  self.cell_size))

                pygame.draw.rect(screen, pygame.Color('white'),
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size,
                                  self.cell_size), 1)

                if self.board[i][j] == 1:
                    # красный
                    color = pygame.Color('red')
                    pygame.draw.circle(screen, color,
                                       (self.left + j * self.cell_size + (self.cell_size // 2),
                                        self.top + i * self.cell_size + (self.cell_size // 2)),
                                       (self.cell_size // 2 - 2))
                elif self.board[i][j] == 0:
                    # синий
                    color = pygame.Color('blue')
                    pygame.draw.circle(screen, color,
                                       (self.left + j * self.cell_size + (self.cell_size // 2),
                                        self.top + i * self.cell_size + (self.cell_size // 2)),
                                       (self.cell_size // 2 - 2))

    def square_pushed(self, mouse_pos):
        mx, my = mouse_pos
        if not self.left < mx < self.cell_size * self.width + self.left or \
                not self.top < my < self.cell_size * self.height + self.top:
            return None
        square_coords = ((mx - self.left) // self.cell_size + 1,
                         (my - self.top) // self.cell_size + 1)
        self.recolor(square_coords)

    # 1 - красный, 0 - синий
    def recolor(self, coords):
        x, y = coords
        x -= 1
        y -= 1
        # красный нажал на кнопку синего и наоборот
        if (self.board[y][x] == 0 and self.red_user) or \
                (self.board[y][x] == 1 and not self.red_user):
            return None
        num = 1 if self.red_user else 0
        self.red_user = False if self.red_user else True

        for i in range(self.height):
            self.board[i][x] = num

        for j in range(self.width):
            self.board[y][j] = num


if __name__ == '__main__':
    number_of_squers = int(input())
    pygame.init()
    size = w, h = 600, 600
    screen = pygame.display.set_mode(size)
    board = Board(number_of_squers, number_of_squers)
    board.set_view(50, 50, 500 // number_of_squers)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.square_pushed(event.pos)
        screen.fill((0, 0, 0))
        board.render()
        pygame.display.flip()
