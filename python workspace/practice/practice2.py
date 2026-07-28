import random
import os
import pygame

pygame.init()

# 스크린창 크기
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("RPG")

clock = pygame.time.Clock()

# 사용자 지정
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경화면 이미지 로드
background = pygame.image.load(os.path.join(image_path, "background.png"))

# stage 설정
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 설정
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height
character_speed = 0.3
character_to_x = 0

#weapon 설정
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 0.5

# ball 기본 설정
balls = {
    
}

# 이벤트 루프
running = True
while(running):
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed

            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed

            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos]) 

            elif event.key == pygame.K_ESCAPE:
                running = False
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
                

    character_x_pos += character_to_x * dt

    weapons = [[w[0], w[1] - weapon_speed * dt] for w in weapons]

    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    pygame.display.update()

pygame.time.delay(1000)
pygame.quit()