import os
import pygame
#########################################################
# 기본 초기화 부분(반드시 해야 하는 것들)
pygame.init() # 초기화 반드시 필요

# 게임을 띄울 프레임 크기
screen_width = 640 # 가로 크가
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 = 프로그램 이름(스크린에 띄울 프로그램 이름)
pygame.display.set_caption("Pang Game")# 게임이름

# FPS
clock = pygame.time.Clock()
########################################################

# 1. 사용자 게임 초기화 (배경 이미지, 게임 이미지, 좌표, 폰트, 속도 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치를 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# stage 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지 높이 위에 캐릭터를 두기 위해

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height ze[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

running = True
while running:
    dt = clock.tick(30)
    
    # 2. 이벤트 처리 (키보트, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히면 이벤트가 발생하는가?
            running = False # 게임이 진행중이 아님.

    # 3. 게임 케릭터 위치 정의    

    # 4. 충돌 처= character_si리

    # 5. 화면 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    # 게임화면 다시 그리기
    pygame.display.update()

# pygame 종료 처리
pygame.quit()
