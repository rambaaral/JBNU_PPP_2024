import pygame
import math

# Pygame 초기화
pygame.init()

# 화면 설정
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Central Gravity Simulation with Damping")

# 색상 설정
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 중심과 반지름 설정
center_x, center_y = width // 2, height // 2
radius = 100

# 물리적 설정
ball_radius = 9
ball_x, ball_y = center_x + radius - ball_radius, center_y  # 초기 위치
velocity_x, velocity_y = 0 , 10  # 초기 속도 (수직 속도)

# 중력 설정
gravity_strength = 0.1
damping_factor = 0.9999999999999999999  # 감쇠 계수

# 시계 설정
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 여러 번의 작은 업데이트로 공의 위치를 세밀하게 조정
    for _ in range(10):
        # 중심까지의 거리 계산
        distance_to_center = math.sqrt((ball_x - center_x) ** 2 + (ball_y - center_y) ** 2)

        # 중력 가속도 계산 (중심을 향하는 방향)
        gravity_x = -gravity_strength * (ball_x - center_x) / distance_to_center
        gravity_y = -gravity_strength * (ball_y - center_y) / distance_to_center

        # 속도 업데이트
        velocity_x += gravity_x / 10
        velocity_y += gravity_y / 10

        # 감쇠 계수 적용
        velocity_x *= damping_factor
        velocity_y *= damping_factor

        # 위치 업데이트
        ball_x += velocity_x / 10
        ball_y += velocity_y / 10

        # 벽과의 충돌 감지 및 반사
        distance_to_center = math.sqrt((ball_x - center_x) ** 2 + (ball_y - center_y) ** 2)
        if distance_to_center + ball_radius > radius:
            # 반사 속도 계산
            normal_x = (ball_x - center_x) / distance_to_center
            normal_y = (ball_y - center_y) / distance_to_center
            dot_product = velocity_x * normal_x + velocity_y * normal_y
            velocity_x -= 2 * dot_product * normal_x
            velocity_y -= 2 * dot_product * normal_y
            # 벽을 넘지 않도록 위치 조정
            ball_x = center_x + (radius - ball_radius) * normal_x
            ball_y = center_y + (radius - ball_radius) * normal_y

    # 화면 업데이트
    screen.fill(black)
    pygame.draw.circle(screen, white, (center_x, center_y), radius, 2)
    pygame.draw.circle(screen, red, (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
