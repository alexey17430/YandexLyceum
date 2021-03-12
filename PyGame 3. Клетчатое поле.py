import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    color = pygame.Color('black')
                    pygame.draw.rect(screen, color,
                                     (self.left + j * self.cell_size,
                                      self.top + i * self.cell_size,
                                      self.cell_size,
                                      self.cell_size))

                else:
                    color = pygame.Color('white')
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

    def square_pushed(self, mouse_pos):
        mx, my = mouse_pos
        if not self.left < mx < self.cell_size * self.width + self.left or \
                not self.top < my < self.cell_size * self.height + self.top:
            return None
        square_coords = ((mx - self.left) // self.cell_size + 1,
                         (my - self.top) // self.cell_size + 1)
        self.recolor(square_coords)

    def recolor(self, coords):
        x, y = coords
        x -= 1
        y -= 1

        if self.board[y][x] == 1:
            self.board[y][x] = 0
        else:
            self.board[y][x] = 1

        for i in range(self.height):
            if self.board[i][x] == 1:
                self.board[i][x] = 0
            else:
                self.board[i][x] = 1

        for j in range(self.width):
            if self.board[y][j] == 1:
                self.board[y][j] = 0
            else:
                self.board[y][j] = 1


if __name__ == '__main__':
    pygame.init()
    size = w, h = 800, 600
    screen = pygame.display.set_mode(size)
    board = Board(5, 7)
    board.set_view(30, 30, 75)
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
