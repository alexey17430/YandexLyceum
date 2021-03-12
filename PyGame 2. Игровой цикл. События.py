import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Я слежу за тобой')
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    running = True
    colvo = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.TEXTEDITING:
                screen.fill((0, 0, 0))
                colvo += 1
                font = pygame.font.Font(None, 100)
                text = font.render(f"{colvo}", True, (255, 0, 0))
                text_y = height // 2 - text.get_height() // 2
                text_x = width // 2 - text.get_width() // 2
                text_w = text.get_width()
                text_h = text.get_height()
                screen.blit(text, (text_x, text_y))
        pygame.display.flip()
    pygame.quit()
