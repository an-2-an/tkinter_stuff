import tkinter as t
import time
import random

class Bullet:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c
        self.radius = 5
        self.bullet = self.c.create_oval(self.x - self.radius, self.y - self.radius,
                                    self.x + self.radius, self.y + self.radius)
    def move(self):
        self.y -= 10
        self.c.coords(self.bullet, self.x - self.radius, self.y - self.radius,
                                    self.x + self.radius, self.y + self.radius)
        

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
label_score = t.Label(root, text='0', font='courier 20 bold')
label_score.pack()
canvas = t.Canvas(root, width=600, height=600)
canvas.pack()

keys = {'left': 37, 'right': 39, 'up': [38, 32]}
bullets = []
x_boot = 300
boot = canvas.create_rectangle(x_boot-20, 600, x_boot+20, 580)
target = Target(random.randint(30, 570), random.randint(10, 70), canvas)
score = 0

def keypress(e):
    global x_boot, bullets
    if e.keycode in keys['up']:
        bullets.append(Bullet(x_boot, 575, canvas))
    if e.keycode == keys['left']:
        x_boot -= 10
        if x_boot < 20: x_boot = 20
    if e.keycode == keys['right']:
        x_boot += 10
        if x_boot > 580: x_boot = 580
    canvas.coords(boot, x_boot-20, 600, x_boot+20, 580)
    
def start():
    while True:
        global bullets, targets, score
        for b in bullets:
            b.move()
            if (target.x - 30 < b.x < target.x + 30) and (target.y - 10 < b.y < target.y + 10):
                target.move()
                score += 1
                label_score['text'] = str(score)
        root.update()
        if len(bullets) > 0 and bullets[0].y < -10:
            del bullets[0]
        time.sleep(0.05)
        
    

root.bind('<Key>', keypress)   
start()

root.mainloop()
