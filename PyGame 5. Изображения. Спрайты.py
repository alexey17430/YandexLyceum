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
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Машинка')
    clock = pygame.time.Clock()
    fps = 60

    car_image = load_image('car.png')
    all_sprites = pygame.sprite.Group()
    im_x, im_y = 0, 0
    car = pygame.sprite.Sprite(all_sprites)
    car.image = car_image
    car.rect = car.image.get_rect()
    car.rect.x = im_x
    car.rect.y = im_y
    car.update()
    all_sprites.draw(screen)
    speed = 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if im_x + car.rect.width == 600:
            speed = -1
        if im_x == 0:
            speed = 1
        all_sprites = pygame.sprite.Group()
        car = pygame.sprite.Sprite(all_sprites)
        if speed == 1:
            car.image = car_image
            car.rect = car.image.get_rect()
        else:
            car.image = pygame.transform.flip(car_image, True, False)
            car.rect = car.image.get_rect()

        im_x += speed
        car.rect.x = im_x
        car.rect.y = im_y
        car.update()

        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
