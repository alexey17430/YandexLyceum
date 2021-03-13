import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
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


if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)

    person_image = load_image('creature.png')
    all_sprites = pygame.sprite.Group()
    im_x, im_y = 0, 0
    person = pygame.sprite.Sprite(all_sprites)
    person.image = person_image
    person.rect = person.image.get_rect()
    person.rect.x = im_x
    person.rect.y = im_y
    person.update()
    all_sprites.draw(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                all_sprites = pygame.sprite.Group()
                person = pygame.sprite.Sprite(all_sprites)
                person.image = person_image
                person.rect = person.image.get_rect()
                if event.scancode == 82:
                    im_y -= 10
                elif event.scancode == 79:
                    im_x += 10
                elif event.scancode == 81:
                    im_y += 10
                elif event.scancode == 80:
                    im_x -= 10
                person.rect.x = im_x
                person.rect.y = im_y
                person.update()

        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
