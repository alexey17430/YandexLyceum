import os
import sys
import pygame
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
arrow_image = load_image('arrow.png')
all_sprites = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            all_sprites = pygame.sprite.Group()
            bomb = pygame.sprite.Sprite(all_sprites)
            bomb.image = arrow_image
            bomb.rect = bomb.image.get_rect()
            bomb.rect.x = event.pos[0]
            bomb.rect.y = event.pos[1]
            bomb.update()
    screen.fill(pygame.Color('black'))
    if all_sprites is not None and pygame.mouse.get_focused():
        pygame.mouse.set_visible(False)
        all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
