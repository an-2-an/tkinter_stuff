import tkinter as tk

root = tk.Tk()
root.title("RGB")
root.geometry("500x200")
FONT = ('Arial', 20)

color_number = tk.IntVar()
color_number.set(3)

red = tk.Radiobutton(root, text='red', font=FONT, variable=color_number, value=1, indicatoron=0)
red.grid(row=0, column=0, sticky='w')
green = tk.Radiobutton(root, text='green', font=FONT, variable=color_number, value=2, indicatoron=0)
green.grid(row=1, column=0, sticky='w')
blue = tk.Radiobutton(root, text='blue', font=FONT, variable=color_number, value=3, indicatoron=0)
blue.grid(row=2, column=0, sticky='w')


has_circle = tk.BooleanVar()
has_circle.set(False)
circle = tk.Checkbutton(root, text='circle', font=FONT, variable=has_circle, onvalue=True, offvalue=False)
circle.grid(row=0, column=2)

canvas = tk.Canvas(root, width=300, height=200, bg='white')
canvas.grid(row=0, column=1, rowspan=4)

def click():
    color = {1: 'red', 2: 'green', 3: 'blue'}.get(color_number.get())
    # print(color)
    canvas.delete('all')
    canvas.config(bg=color)
    if has_circle.get():
        canvas.create_oval(0, 0, 100, 100, fill='white')

btn = tk.Button(root, text='Color Me', command=click)
btn.grid(row=3, column=0)

root.mainloop()

