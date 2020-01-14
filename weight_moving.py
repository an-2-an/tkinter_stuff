import tkinter as tk
import time
from math import sin, cos, radians

W, H = 700, 500
R, X0, Y0, DT, V, ALPHA, G = 5, 0, 0, 0.1, 70, 70, 9.8
x, y, t = X0, Y0, 0.0
y_max = Y0
vx = V * cos(radians(ALPHA))
vy = V * sin(radians(ALPHA))

root = tk.Tk()
canvas = tk.Canvas(root, width=W, height=H, bg='white')
canvas.pack()

ball = canvas.create_oval(0, 0, 0, 0, fill='green')
info = canvas.create_text(10, 10, text='', anchor='nw')

def draw_ball():
    canvas.coords(ball, x-R, (H-y)-R, x+R, (H-y)+R)
    canvas.itemconfig(info, text=f'x={int(x)} y={int(y)}')

draw_ball()

def count_xy():
    global x, y, y_max
    x = X0 + vx * t
    y = Y0 + vy * t - G * t**2 / 2.0
    y_max = max(y, y_max)

def move(e):
    global t
    time.sleep(DT)
    t += DT
    count_xy()
    # print(t, x, y)
    draw_ball()
    root.update()
    if y > 0:
        move(e)
    else:
        finish()

def finish():
    canvas.create_line(0, (H-y_max), W, (H-y_max), dash=(5, 5))
    canvas.create_line(x, 0, x, H, dash=(5, 5))

canvas.bind('<Button-1>', move)
root.mainloop()

