import tkinter as tki

root = tki.Tk()
d = 20
m = 30
n = 50
dt = 200

canvas = tki.Canvas(root, width=d*n, height=d*m, bg='lightgrey')
canvas.pack(padx=5, pady=5)

cells = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(0), 
    cells.append(row)


cells[12][12] = 1
cells[12][14] = 1

def draw_grid():
    for i in range(0, d*m+1, d):
        canvas.create_line(0, i, n*d, i)
    for i in range(0, d*n+1, d):
        canvas.create_line(i, 0, i, m*d)

def fill():
    global cells, canvas
    canvas.delete('all')
    draw_grid()
    for i in range(m):
        for j in range(n):
            if cells[i][j] == 1:
                canvas.create_rectangle(j*d, i*d, j*d+d, i*d+d, fill='green')
    next_gen()
    root.after(dt, fill)

def next_gen():
    global cells
    sums = [[get_cell_sum(i, j) for j in range(n)] for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            s = sums[i][j]
            canvas.create_text(j*d+d/2, i*d+d/2, text=str(s))
            if cells[i][j] == 0 and s in [2,3]:
                cells[i][j] = 1
            else:
                cells[i][j] = 0
    

def get_cell_sum(i, j):
    global cells, m, n
    s = 0
    if i > 0: s += cells[i-1][j] #up
    if i < m-1: s += cells[i+1][j] #down
    if j > 0: s += cells[i][j-1] #left
    if j < n-1: s += cells[i][j+1] #right
    if i > 0 and j > 0: s += cells[i-1][j-1] #left-up
    if i < m-1 and j > 0: s += cells[i+1][j-1] #left-down
    if i > 0 and j < n-1: s += cells[i-1][j+1] #right-up
    if i < m-1 and j < n-1: s += cells[i+1][j+1] #right-down
    
    return s
                
        
    

fill()
root.mainloop()
