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
        if not mx - self.left < self.cell_size * self.width or\
                not my - self.top < self.cell_size * self.height:
            return None
        return (mx - self.left) // self.cell_size + 1, (my - self.top) // self.cell_size + 1


if __name__ == '__main__':
    pygame.init()
    size = w, h = 800, 600
    screen = pygame.display.set_mode(size)
    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ans = board.square_pushed(event.pos)
                print(f'({ans[0] - 1}, {ans[1] - 1})')
        screen.fill((0, 0, 0))
        board.render()
        pygame.display.flip()
