import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
width, height = 600, 300
image_size = 600, 300
size = width, height
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 255))
x = 10
v = 200  # пикселей в секунду
fps = 60
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("gameover.png")
sprite.image = pygame.transform.scale(sprite.image, image_size)

sprite.rect = sprite.image.get_rect()
sprite.rect.x = -image_size[0]
all_sprites.add(sprite)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if sprite.rect.x + image_size[0] < width:
        sprite.rect.x += v * fps / 1000
    all_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
