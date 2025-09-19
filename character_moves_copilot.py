from pico2d import *
import math

open_canvas()
ch = load_image('character.png')
gr = load_image('grass.png')

# 운동 상태: 0=사각, 1=삼각, 2=원
move_state = 0

# 사각운동 좌표
rect_points = [(10, 70), (780, 70), (780, 550), (10, 550)]
rect_idx = 0
cx, cy = rect_points[0]

# 삼각운동 좌표
tri_points = [(400, 550), (780, 70), (10, 70)]
tri_idx = 0

# 원운동 변수
circle_center = (400, 300)
circle_radius = 250
circle_angle = 0.0
PI = math.pi

while True:
    clear_canvas()
    gr.draw_now(400, 10)
    ch.draw_now(cx, cy)

    if move_state == 0:  # 사각운동
        next_idx = (rect_idx + 1) % 4
        tx, ty = rect_points[next_idx]
        dx, dy = tx - cx, ty - cy
        dist = math.hypot(dx, dy)
        if dist < 5:
            rect_idx = next_idx
            cx, cy = rect_points[rect_idx]
            if rect_idx == 0:
                move_state = 1
                tri_idx = 0
                cx, cy = tri_points[0]
        else:
            cx += 5 * dx / dist
            cy += 5 * dy / dist

    elif move_state == 1:  # 삼각운동 (방향 반대로)
        next_idx = (tri_idx - 1) % 3
        tx, ty = tri_points[next_idx]
        dx, dy = tx - cx, ty - cy
        dist = math.hypot(dx, dy)
        if dist < 5:
            tri_idx = next_idx
            cx, cy = tri_points[tri_idx]
            if tri_idx == 0:
                move_state = 2
                circle_angle = 2 * PI  # 원운동 시작 각도를 2*PI로 설정
        else:
            cx += 5 * dx / dist
            cy += 5 * dy / dist

    elif move_state == 2:  # 원운동 (방향 반대)
        cx = circle_center[0] + circle_radius * math.cos(circle_angle)
        cy = circle_center[1] + circle_radius * math.sin(circle_angle)
        circle_angle -= 0.02 * PI
        if circle_angle <= 0:
            move_state = 0
            rect_idx = 0
            cx, cy = rect_points[0]
            circle_angle = 0.0

    delay(0.016)

close_canvas()
