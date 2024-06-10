import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 설정
g = 9.8  # 중력 가속도 (m/s^2)
dt = 0.1  # 시간 간격 (s)
bounce_coefficient = 0.9  # 튕기는 계수

# 초기 위치와 속도
x_init = 5
y_init = 10
v_x_init = 0
v_y_init = 0

# 장애물 설정 (x, y, 반지름)
obstacles = [(3, 5, 1), (7, 7, 1), (5, 3, 1)]

# 설정
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)

ball, = ax.plot([], [], 'o', markersize=15)
obstacle_patches = [plt.Circle((obs[0], obs[1]), obs[2], color='gray') for obs in obstacles]
for patch in obstacle_patches:
    ax.add_patch(patch)

# 초기화 함수
def init():
    ball.set_data(x_init, y_init)
    return ball,

# 애니메이션 업데이트 함수
def update(frame):
    global x_init, y_init, v_x_init, v_y_init
    # 속도와 위치 업데이트
    v_y_init += -g * dt
    x_init += v_x_init * dt
    y_init += v_y_init * dt

    # 바닥에 닿았을 때 튕김 처리
    if y_init < 0:
        y_init = 0
        v_y_init = -v_y_init * bounce_coefficient
    
    # 벽에 닿았을 때 튕김 처리
    if x_init < 0 or x_init > 10:
        v_x_init = -v_x_init * bounce_coefficient

    # 장애물과 충돌 처리
    for obs in obstacles:
        obs_x, obs_y, obs_r = obs
        if (x_init - obs_x)**2 + (y_init - obs_y)**2 < obs_r**2:
            # 단순 반사 처리
            v_x_init = -v_x_init * bounce_coefficient
            v_y_init = -v_y_init * bounce_coefficient

    ball.set_data(x_init, y_init)
    return ball,

# 애니메이션 설정
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), init_func=init, blit=True)

# 애니메이션 재생
plt.show()
