import cv2
import numpy as np
import pymunk
import pymunk.pygame_util
import pygame
import math
import json

# 이미지에서 초록색 점의 위치 추출 함수
def extract_green_dots(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("이미지를 로드할 수 없습니다.")
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 초록색 범위 설정 (HSV)
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    
    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(image, image, mask=mask)
    
    # 컨투어 찾기
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    positions = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cx = x + w // 2
        cy = y + h // 2
        positions.append((cx, cy))
    
    return positions, image.shape[1], image.shape[0]

# 이미지에서 초록색 점 위치 추출 및 저장
image_path = 'abcde.jpg'  # 코드 파일과 같은 폴더에 있는 이미지 파일 경로
circle_positions, img_width, img_height = extract_green_dots(image_path)

# 위치 저장
with open('positions.json', 'w') as f:
    json.dump(circle_positions, f)

# 화면 확대 비율 설정
scale_factor = 2
scaled_width = int(img_width * scale_factor)
scaled_height = int(img_height * scale_factor)

# Pygame 초기화
pygame.init()
screen = pygame.display.set_mode((scaled_width, scaled_height))  # 확대된 화면 크기 설정
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Pymunk 공간 설정
space = pymunk.Space()
space.gravity = (0, 980)  # 중력 값을 더 현실적으로 조정 (약 9.8m/s²)

# 공 생성 함수
def create_ball(space, position):
    body = pymunk.Body(1, math.inf)  # 무한 관성 모멘트를 가진 동적 바디
    body.position = position
    shape = pymunk.Circle(body, 15)  # 반지름 15
    shape.elasticity = 0.9
    space.add(body, shape)
    return shape

# 원형 장애물 생성 함수
def create_circle(space, position, radius):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)  # 정적 바디
    body.position = position
    shape = pymunk.Circle(body, radius)  # 반지름 radius의 원형 모양
    shape.elasticity = 0.9
    space.add(body, shape)
    return shape

# 경계 생성 함수 (왼쪽과 오른쪽 경계만 생성)
def create_boundaries(space, width, height):
    static_body = space.static_body
    boundaries = [
        pymunk.Segment(static_body, (0, 0), (0, height), 1),  # 왼쪽 경계
        pymunk.Segment(static_body, (width, 0), (width, height), 1)  # 오른쪽 경계
    ]
    for boundary in boundaries:
        boundary.elasticity = 0.9
        space.add(boundary)

# 원형 장애물 생성
circle_radius = 10  # 원형 장애물 반지름 설정
scaled_circle_positions = [(int(pos[0] * scale_factor), int(pos[1] * scale_factor)) for pos in circle_positions]
circles = [create_circle(space, pos, circle_radius) for pos in scaled_circle_positions]

# 경계 생성
create_boundaries(space, scaled_width, scaled_height)  # 확대된 크기에 맞게 경계 생성

# 공 리스트
balls = []

# 애니메이션 업데이트 함수
def update():
    global balls

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 공 생성 및 떨어뜨리기
                ball = create_ball(space, (scaled_width // 2, -30))  # 발사 위치를 화면 바로 위로 이동
                balls.append(ball)

    # 공의 위치를 확인하여 화면 아래로 벗어난 공 제거
    balls = [ball for ball in balls if ball.body.position.y <= scaled_height]

    screen.fill((255, 255, 255))
    step_dt = 1 / 120.0  # 더 작은 시간 스텝
    for _ in range(2):  # 시뮬레이션 정확성을 위해 두 번 스텝 실행
        space.step(step_dt)
    space.debug_draw(draw_options)

    pygame.display.flip()
    clock.tick(60)
    return True

# 애니메이션 실행
running = True
while running:
    running = update()

pygame.quit()
