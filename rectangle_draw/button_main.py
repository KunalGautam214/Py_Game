import pygame

from rectangle_draw.button import Button

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

# load button image
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

# create button instances
start_button = Button(100, 200, start_img, 0.8)
exit_button = Button(400, 200, exit_img, 0.8)

# game loop
run = True
while run:
    screen.fill((202, 228, 241))

    if start_button.draw(screen):
        print('Start')

    if exit_button.draw(screen):
        print('Exit')
        run = False

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
