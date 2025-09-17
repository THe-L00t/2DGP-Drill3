from pico2d import *
import math

open_canvas()
ch = load_image('character.png')
gr = load_image('grass.png')

rTogle = True
line = 1
cx,cy = 10, 70
time = 0.0

while (True):
    clear_canvas()

    if rTogle:
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
                rTogle = False
    else:
        cx = 400 + 250 * math.cos(time)
        cy = 300 + 250 * math.sin(time)
        time += 0.09

    delay(0.016)
    gr.draw_now(400, 10)
    ch.draw_now(cx,cy)

close_canvas()
