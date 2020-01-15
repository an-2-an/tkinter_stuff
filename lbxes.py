import tkinter as tk

root = tk.Tk()
root.title("listbox")
root.geometry("500x400")
FONT = ('Arial', 20)
W = 200
n = 10

def click(e):
    # v1 = box.get('active') #так не работает правильно
    w = e.widget
    print(w.curselection())
    index = int(w.curselection()[0])
    v1 = w.get(index)
    canvas.delete('all')
    d = W * (v1 / 100) / 2
    canvas.create_rectangle(W//2-d, W//2-d, W//2+d, W//2+d, width=3, fill='yellow')
    canvas.create_text(W//2, W//2, text=str(v1))


box = tk.Listbox(root, width=10, height=n, font=FONT, selectmode=tk.SINGLE)
for i in range(1, n+1):
    box.insert('end', i * 10)
box.pack(side='left')
box.bind('<<ListboxSelect>>', click)

canvas = tk.Canvas(width=W, height=W, bg='white')
canvas.pack(side='left')

root.mainloop()