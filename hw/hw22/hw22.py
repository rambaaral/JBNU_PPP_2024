import pymunk
import pymunk.pygame_util
import pygame
import math
import json

# 위치 파일 불러오기
positions_file = 'positions.json'

def load_positions(file_path):
    with open(file_path, 'r') as f:
        positions = json.load(f)
    return positions

# 위치 불러오기
circle_positions = load_positions(positions_file)

# 원래 이미지 크기 설정 (예: 800x600)
original_width = 611
original_height = 600

# 화면 확대 비율 설정
scale_factor = 2
scaled_width = int(original_width * scale_factor)
scaled_height = int(original_height * scale_factor)

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
    shape.elasticity = 0.5
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
circle_radius = 3  # 원형 장애물 반지름 설정
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
