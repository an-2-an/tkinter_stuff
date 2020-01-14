import tkinter as t
import time
import random
from math import pi, sin, cos


class Vector:
    def __init__(self, length, alpha, c):
        self.c = c
        x1, y1 = 0, 600
        dx = length * cos(alpha / 180.0 * pi)
        dy = length * sin(alpha / 180.0 * pi)
        x2, y2 = x1 + dx, y1 - dy
        self.vector = self.c.create_line(x1, y1, x2, y2)

    def draw(self, length, alpha):
        x1, y1 = 0, 600
        dx = length * cos(alpha / 180.0 * pi)
        dy = length * sin(alpha / 180.0 * pi)
        x2, y2 = x1 + dx, y1 - dy
        self.c.coords(self.vector, x1, y1, x2, y2)
        
        
    
class Bullet:
    def __init__(self, x, y, c, root):
        self.x = x
        self.y = y
        self.c = c
        self.root = root
        self.radius = 5
        self.bullet = self.c.create_oval(self.x - self.radius, self.y - self.radius,
                                    self.x + self.radius, self.y + self.radius)
    def move(self):
        self.c.coords(self.bullet, self.x - self.radius, self.y - self.radius,
                                    self.x + self.radius, self.y + self.radius)
        self.root.update()
        
    def bang(self, length, alpha):
        vx = length * cos(alpha / 180.0 * pi)
        vy = length * sin(alpha / 180.0 * pi)
        dt = 0.1
        g = 10
        t = 0
        while True:
            t += 2 * dt
            self.x = vx * t
            self.y = 600 - (vy * t - (g * t**2 / 2.0))
            if self.y > 600:
                self.c.create_oval(self.x-2, 598, self.x+2, 602, fill='red')
                self.x, self.y = 0, 600
                self.move()
                break
            self.move()
            #print(self.x, self.y)
            time.sleep(dt / 2)

    
        

class Target:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c
        self.target = self.c.create_rectangle(self.x - 30, self.y - 10,
                                    self.x + 30, self.y + 10)
        self.c.itemconfig(self.target, fill='red')
        
    def move(self):
        self.x = random.randint(30, 570)
        self.y = random.randint(10, 70)
        self.c.coords(self.target, self.x - 30, self.y - 10,
                                    self.x + 30, self.y + 10)
        self.c.itemconfig(self.target, fill='#' + ''.join('%02x' % random.randint(0, 255) for i in range(3)))

    def bang(self):
        pass
    

root = t.Tk()

canvas = t.Canvas(root, width=1200, height=600, borderwidth=1, relief='solid')
canvas.pack()

label = t.Label(root, text='0', font='courier 20 bold')
label.pack()

keys = {'left': 37, 'right': 39, 'up': 38, 'down': 40, 'space': 32}

alpha = 45
length = 20
label['text'] = 'speed: {},  alpha: {}'.format(length, alpha)

vector = Vector(length, alpha, canvas)
bullet = Bullet(0, 600, canvas, root)

def keypress(e):
    global alpha, length
    if e.keycode == keys['up']:
        length += 2
    if e.keycode == keys['down']:
        length -= 2
    if e.keycode == keys['left']:
        alpha += 1
    if e.keycode == keys['right']:
        alpha -= 1
    if e.keycode == keys['space'] and bullet.x == 0:
        bullet.bang(length, alpha)
    vector.draw(length, alpha)
    label['text'] = 'speed: {},  alpha: {}'.format(length, alpha)
        
    
        
    

root.bind('<Key>', keypress)   

root.mainloop()
