import math

import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Background Demo')

# load button image
bg_img = pygame.image.load('bg.png').convert_alpha()
bg_img_width = bg_img.get_width()
bg_img_rect = bg_img.get_rect()

# define game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_img_width) + 1


# game loop
run = True
while run:
    clock.tick(FPS)

    #draw scrolling background
    for i in range(tiles):
        screen.blit(bg_img, (i * bg_img_width + scroll, 0))
        bg_img_rect.x = i * bg_img_width + scroll
        pygame.draw.rect(screen, (255, 0, 0), bg_img_rect, 1)

    # scroll background
    scroll -= 5

    if abs(scroll) > bg_img_width:
        scroll = 0

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
