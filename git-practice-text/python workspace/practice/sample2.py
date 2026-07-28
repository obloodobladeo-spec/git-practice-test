import pygame
import os

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons= []

running = True
while(running):
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                weapon_x_pos = 0
                weapon_y_pos = 480
                weapons.append([weapon_x_pos, weapon_y_pos])

    weapons = [[w[0], w[1] - 10] for w in weapons]
    
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]
    print(weapons)

pygame.quit()