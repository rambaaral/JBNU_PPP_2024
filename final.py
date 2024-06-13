import pymunk
import pymunk.pygame_util
import pygame
import math

# Pygame 설정
pygame.init()
screen = pygame.display.set_mode((400, 800))  # 화면 너비를 줄임
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Pymunk 공간 설정
space = pymunk.Space()
space.gravity = (0, 900)  # 중력 설정 (단위: 픽셀/제곱초)

# 공 생성 함수
def create_ball(space, position):
    body = pymunk.Body(1, math.inf)
    body.position = position
    shape = pymunk.Circle(body, 15)  # 공의 반지름을 원래대로 15로 설정
    shape.elasticity = 0.9
    space.add(body, shape)
    return shape

# 마름모 생성 함수
def create_diamond(space, position, size):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = position
    points = [(0, size), (size, 0), (0, -size), (-size, 0)]
    shape = pymunk.Poly(body, points)
    shape.elasticity = 0.9
    space.add(body, shape)
    return shape

# 경계 생성 함수
def create_boundaries(space, width, height):
    static_body = space.static_body
    boundaries = [
        pymunk.Segment(static_body, (0, 0), (0, height), 1),  # 왼쪽 경계
        pymunk.Segment(static_body, (0, height), (width, height), 1),  # 상단 경계
        pymunk.Segment(static_body, (width, height), (width, 0), 1),  # 오른쪽 경계
        pymunk.Segment(static_body, (width, 0), (0, 0), 1)  # 하단 경계
    ]
    for boundary in boundaries:
        boundary.elasticity = 0.9
        space.add(boundary)

# 마름모 생성
diamond_size = 10  # 마름모 크기 설정
diamond_positions = [
    (50, 600), (100, 600), (150, 600), (200, 600), (250, 600), (300, 600), (350, 600),
    (75, 500), (125, 500), (175, 500), (225, 500), (275, 500), (325, 500),
    (50, 400), (100, 400), (150, 400), (200, 400), (250, 400), (300, 400), (350, 400),
    (75, 300), (125, 300), (175, 300), (225, 300), (275, 300), (325, 300),
    (50, 200), (100, 200), (150, 200), (200, 200), (250, 200), (300, 200), (350, 200)
]
diamonds = [create_diamond(space, pos, diamond_size) for pos in diamond_positions]

# 경계 생성
create_boundaries(space, 400, 800)  # 화면 크기에 맞게 경계 생성

# 공 리스트
balls = []

# 발사 각도
launch_angle = math.pi / 2  # 위쪽 방향

# 애니메이션 업데이트 함수
def update():
    global balls, launch_angle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 공 생성 및 발사
                ball = create_ball(space, (200, 50))  # 발사 위치를 상단 중앙으로 이동
                balls.append(ball)
                impulse = 500  # 발사 힘 (10배 줄임)
                ball.body.apply_impulse_at_local_point((impulse * math.cos(launch_angle), -impulse * math.sin(launch_angle)), (0, 0))
            if event.key == pygame.K_LEFT:
                launch_angle += 0.1
            if event.key == pygame.K_RIGHT:
                launch_angle -= 0.1

    screen.fill((255, 255, 255))
    step_dt = 1 / 120.0  # 더 작은 시간 스텝
    for _ in range(2):  # 시뮬레이션 정확성을 위해 두 번 스텝 실행
        space.step(step_dt)
    space.debug_draw(draw_options)

    # 발사 경로 표시
    start_pos = (200, 50)
    end_pos = (200 + 60 * math.cos(launch_angle), 50 - 60 * math.sin(launch_angle))
    pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 5)

    pygame.display.flip()
    clock.tick(60)
    return True

# 애니메이션 실행
running = True
while running:
    running = update()

pygame.quit()
