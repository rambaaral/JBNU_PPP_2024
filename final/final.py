import pymunk
import pymunk.pygame_util
import pygame
import math
import json
import random
import tkinter as tk
from tkinter import simpledialog


# 위치 불러오기
circle_positions = [[461, 486], [149, 486], [441, 486], [169, 486], [169, 486], [441, 486], [148, 486], [462, 486], [419, 486], [191, 486], [190, 486], [420, 486], [471, 465], [139, 465], [450, 465], [160, 465], [429, 465], [181, 465], [408, 465], [202, 465], [201, 465], [409, 465], [180, 465], [430, 465], [159, 465], [451, 465], [138, 465], [472, 465], [461, 445], [149, 445], [419, 444], [191, 444], [149, 445], [461, 445], [440, 444], [170, 444], [190, 443], [420, 443], [169, 444], [441, 444], [484, 436], [126, 436], [126, 436], [484, 436], [475, 423], [135, 423], [133, 423], [477, 423], [392, 421], [218, 421], [216, 421], [394, 421], [369, 418], [241, 418], [241, 419], [369, 419], [481, 417], [129, 417], [127, 418], [483, 418], [488, 412], [122, 412], [121, 413], [489, 413], [494, 406], [116, 406], [115, 406], [495, 406], [176, 375], [434, 375], [433, 371], [177, 371], [176, 366], [434, 366], [435, 359], [175, 359], [174, 359], [436, 359], [437, 351], [173, 351], [172, 351], [438, 351], [440, 344], [170, 344], [170, 344], [440, 344], [442, 337], [168, 337], [167, 337], [443, 337], [323, 302], [287, 302], [285, 302], [325, 302], [317, 293], [293, 293], [293, 293], [317, 293], [430, 287], [180, 287], [180, 287], [430, 287], [421, 285], [189, 285], [188, 284], [422, 284], [413, 282], [197, 282], [196, 282], [414, 282], [317, 280], [293, 280], [292, 280], [318, 280], [401, 278], [209, 278], [208, 278], [402, 278], [468, 275], [142, 275], [446, 275], [164, 275], [391, 275], [219, 275], [162, 275], [448, 275], [141, 275], [469, 275], [222, 274], [388, 274], [380, 272], [230, 272], [234, 271], [376, 271], [361, 268], [249, 268], [285, 265], [325, 265], [325, 263], [285, 263], [259, 267], [351, 267], [340, 264], [270, 264], [317, 263], [293, 263], [292, 263], [318, 263], [456, 257], [154, 257], [154, 258], [456, 258], [476, 256], [134, 256], [174, 257], [436, 257], [133, 256], [477, 256], [435, 257], [175, 257], [413, 253], [197, 253], [196, 253], [414, 253], [290, 249], [320, 249], [320, 248], [290, 248], [466, 236], [144, 236], [446, 237], [164, 237], [163, 237], [447, 237], [142, 236], [468, 236], [316, 234], [294, 234], [293, 234], [317, 234], [369, 232], [241, 232], [240, 233], [370, 233], [354, 225], [256, 225], [255, 225], [355, 225], [336, 219], [274, 219], [274, 220], [336, 220], [305, 203], [305, 203], [324, 199], [286, 199], [286, 199], [324, 199], [426, 183], [184, 183], [366, 177], [244, 177], [313, 177], [297, 177], [245, 177], [365, 177], [296, 177], [314, 177], [335, 177], [275, 177], [274, 177], [336, 177], [427, 175], [183, 175], [183, 179], [427, 179], [429, 168], [181, 168], [180, 168], [430, 168], [398, 173], [212, 173], [211, 173], [399, 173], [178, 161], [432, 161], [432, 160], [178, 160], [392, 158], [218, 158], [346, 157], [264, 157], [325, 158], [285, 158], [264, 157], [346, 157], [217, 158], [393, 158], [305, 157], [305, 157], [284, 157], [326, 157], [437, 154], [173, 154], [389, 151], [221, 151], [221, 151], [389, 151], [443, 149], [167, 149], [169, 151], [441, 151], [226, 145], [384, 145], [384, 145], [226, 145], [334, 138], [276, 138], [315, 138], [295, 138], [275, 138], [335, 138], [295, 137], [315, 137], [442, 135], [168, 135], [168, 135], [442, 135], [364, 135], [246, 135], [245, 135], [365, 135], [169, 129], [441, 129], [440, 128], [170, 128], [173, 121], [437, 121], [305, 116], [305, 116], [435, 118], [175, 118], [381, 114], [229, 114], [354, 115], [256, 115], [325, 115], [285, 115], [285, 115], [325, 115], [258, 115], [352, 115], [229, 114], [381, 114], [177, 115], [433, 115], [428, 109], [182, 109], [182, 108], [428, 108], [421, 103], [189, 103], [188, 103], [422, 103], [414, 100], [196, 100], [195, 99], [415, 99], [407, 97], [203, 97], [400, 94], [210, 94], [393, 94], [217, 94], [210, 95], [400, 95], [386, 89], [224, 89], [224, 89], [386, 89], [346, 85], [264, 85], [296, 84], [314, 84], [264, 85], [346, 85], [313, 84], [297, 84], [386, 81], [224, 81], [223, 81], [387, 81], [227, 74], [383, 74], [382, 73], [228, 73], [376, 68], [234, 68], [233, 67], [377, 67], [369, 64], [241, 64], [239, 64], [371, 64], [361, 62], [249, 62], [248, 62], [362, 62], [273, 53], [337, 53], [338, 52], [272, 52], [317, 52], [293, 52], [293, 52], [317, 52]]

# 원래 이미지 크기 설정 (예: 410x600)
original_width = 410
original_height = 600

# 화면 확대 비율 설정
scale_factor = 2
scaled_width = int(original_width * scale_factor)
scaled_height = int(original_height * scale_factor)

# Pygame 초기화
pygame.init()
screen = pygame.display.set_mode((scaled_width, scaled_height))
clock = pygame.time.Clock()

# 기본 폰트 설정
font = pygame.font.SysFont("Malgun Gothic", 50)

# Pymunk 공간 설정
space = pymunk.Space()
space.gravity = (0, 980)

# Pygame 용 DrawOptions 설정
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Tkinter 설정
root = tk.Tk()
root.title("공 게임 관리")
root.geometry("300x200")

# Tkinter 위젯 설정
ball_count = tk.IntVar()
refund_amount = tk.IntVar()

def add_balls():
    global ball_count
    amount = simpledialog.askinteger("투입 금액", "1000원 단위의 금액을 입력하세요:")
    if amount and amount % 1000 == 0:
        ball_count.set(ball_count.get() + amount // 10)

def refund_balls():
    global ball_count, refund_amount
    refund_amount.set(refund_amount.get() + ball_count.get() * 5)
    ball_count.set(0)

add_button = tk.Button(root, text="투입", command=add_balls)
add_button.pack()

refund_button = tk.Button(root, text="환급", command=refund_balls)
refund_button.pack()

ball_count_label = tk.Label(root, textvariable=ball_count)
ball_count_label.pack()

refund_amount_label = tk.Label(root, textvariable=refund_amount)
refund_amount_label.pack()

# 공 생성 함수
def create_ball(space, position):
    body = pymunk.Body(1, math.inf)
    body.position = position
    shape = pymunk.Circle(body, 9)
    shape.elasticity = 0.7
    space.add(body, shape)
    return shape

# 원형 장애물 생성 함수
def create_circle(space, position, radius, elasticity=0.7):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.elasticity = elasticity
    space.add(body, shape)
    return shape

# 윗면이 뚫린 4각형 장애물 생성 함수
def create_open_top_rectangle(space, positions):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    space.add(body)
    left_segment = pymunk.Segment(body, positions[0], positions[1], 1)
    right_segment = pymunk.Segment(body, positions[2], positions[3], 1)
    bottom_segment = pymunk.Segment(body, positions[1], positions[3], 1)
    for segment in [left_segment, right_segment, bottom_segment]:
        segment.elasticity = 0.7
    space.add(left_segment, right_segment, bottom_segment)
    return positions[0][0], positions[3][0], positions[1][1], positions[0][1]

# 경계 생성 함수
def create_boundaries(space, width, height):
    static_body = space.static_body
    boundaries = [
        pymunk.Segment(static_body, (0, 0), (0, height), 1),
        pymunk.Segment(static_body, (width, 0), (width, height), 1)
    ]
    for boundary in boundaries:
        boundary.elasticity = 0.7
        space.add(boundary)

# 원형 장애물 생성
circle_radius = 3
scaled_circle_positions = [(int(pos[0] * scale_factor) - 200, int(pos[1] * scale_factor)) for pos in circle_positions if not math.isnan(pos[0]) and not math.isnan(pos[1])]
circles = [create_circle(space, pos, circle_radius) for pos in scaled_circle_positions]

# 추가 원형 장애물 생성 (탄성 계수를 다르게 설정)
additional_circle_positions = [
    (176, 412),
    (433, 412),
    (413, 220),
    (196, 220)
]
elasticities = [2, 2, 2, 2]  # 각 원형 장애물의 탄성 계수
scaled_additional_circle_positions = [(int(pos[0] * scale_factor) - 200, int(pos[1] * scale_factor)) for pos in additional_circle_positions]
additional_circles = [create_circle(space, pos, 30, elasticity=elasticity) for pos, elasticity in zip(scaled_additional_circle_positions, elasticities)]

# 윗면이 뚫린 4각형 장애물 생성
rectangle_positions = [
    (285, 320),
    (285, 340),
    (325, 320),
    (325, 340)
]
scaled_rectangle_positions = [(int(pos[0] * scale_factor) - 200, int(pos[1] * scale_factor)) for pos in rectangle_positions]
left, right, bottom, top = create_open_top_rectangle(space, scaled_rectangle_positions)

# 경계 생성
create_boundaries(space, scaled_width, scaled_height)

# 공 리스트
balls = []

# 확률에 따라 결과를 선택하는 함수
def get_result():
    rand = random.random()
    if rand < 0.7:
        return "꽝"
    elif rand < 0.995:
        return "당첨"
    else:
        return "잭팟"

# 결과를 화면에 표시하는 함수
def display_result(text):
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(scaled_width // 2, int(scaled_height * 0.7)))
    screen.blit(text_surface, text_rect)

# 애니메이션 업데이트 함수
def update():
    global balls, last_result, ball_count, refund_amount
    new_result = None

    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            root.quit()
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ball_count.get() > 0:
                x_position = scaled_width // 2 + random.randint(-5, 5)
                ball = create_ball(space, (x_position, -30))
                balls.append(ball)
                ball_count.set(ball_count.get() - 1)

    # 공의 위치를 확인하여 화면 아래로 벗어난 공 제거
    balls[:] = [ball for ball in balls if ball.body.position.y <= scaled_height]

    # 공이 상자 밑변에 닿았는지 확인하고 제거
    balls_to_remove = [ball for ball in balls if bottom - 10 <= ball.body.position.y <= bottom + 10 and left < ball.body.position.x < right]

    for ball in balls_to_remove:
        new_result = get_result()
        print(f"Removing ball at position: {ball.body.position} with result: {new_result}")
        space.remove(ball.body, ball)
        balls.remove(ball)
        if new_result == "당첨":
            ball_count.set(ball_count.get() + 20)
        elif new_result == "잭팟":
            ball_count.set(ball_count.get() + 500)

    screen.fill((255, 255, 255))
    step_dt = 1 / 120.0
    for _ in range(2):
        space.step(step_dt)
    space.debug_draw(draw_options)

    if new_result:
        last_result = new_result

    if last_result:
        display_result(last_result)

    pygame.display.flip()
    return True

# 애니메이션 실행
last_result = None
running = True
while running:
    running = update()
    try:
        root.update()
    except tk.TclError:
        running = False

pygame.quit()
