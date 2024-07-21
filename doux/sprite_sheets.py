import pygame

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()

BG = (50, 50, 50)
BLACK = (0, 0, 0)

def get_image(sheet, frame, width, height, scale, colour):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colour)
    return image

# anmation list
animation_list = []
animation_steps = [4, 6, 3, 4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 75
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(get_image(sprite_sheet_image, step_counter, 24, 24, 3, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)
    # animation_list.append(get_image(sprite_sheet_image, x, 24, 24, 3, BLACK))
# frame_0 = get_image(sprite_sheet_image, 0, 24, 24, 3, BLACK)
# frame_1 = get_image(sprite_sheet_image, 1, 24, 24, 3, BLACK)
# frame_2 = get_image(sprite_sheet_image, 2, 24, 24, 3, BLACK)

run = True
while run:
    # update background
    screen.fill(BG)
    # display image
    # screen.blit(sprite_sheet_image, (0, 0))

    # for x in range(animation_steps):
    #     screen.blit(animation_list[x], (x * 48, 0))

    # screen.blit(frame_0, (0, 0))
    # screen.blit(frame_1, (48, 0))
    # screen.blit(frame_2, (96, 0))

    # update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    # show frame image
    screen.blit(animation_list[action][frame], (0, 0))

    key = pygame.key.get_pressed()
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                action += 1
                frame = 0

    pygame.display.update()

pygame.quit()

