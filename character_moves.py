from pico2d import *
import math

open_canvas()
ch = load_image('character.png')
gr = load_image('grass.png')

rTogle = 1
line = 1
cx,cy = 10, 70
time = 0.0
PI = 3.141592

while (True):
    clear_canvas()

    if rTogle == 1:
        if line == 1:
            cx += 5
            if cx > 780:
                line =2
        elif line == 2:
            cy += 5
            if cy > 550:
                line = 3
        elif line == 3:
            cx -= 5
            if cx < 20:
                line = 4
        elif line == 4:
            cy -= 5
            if cy < 70:
                line = 1
                rTogle = 2
                cx, cy = 10, 70

    elif rTogle == 2:
        if line == 1:
            cx += 5
            if cx > 780:
                line =2
        elif line == 2:
            cy += 5
            cx -= 4
            if cy > 550:
                line = 3
        elif line == 3:
            cy -= 5
            cx -= 4
            if cx < 20:
                line = 1
                rTogle = 3

    elif rTogle == 3:
        cx = 400 + 250 * math.cos(-time*PI)
        cy = 300 + 250 * math.sin(-time*PI)
        time += 0.02
        if(time >2):
            time = 0
            rTogle = 1
            cx,cy = 10,70


    delay(0.016)
    gr.draw_now(400, 10)
    ch.draw_now(cx,cy)

close_canvas()
