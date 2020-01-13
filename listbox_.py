import tkinter as tk

root = tk.Tk()
root.title("listbox")
root.geometry("300x400")
FONT = ('Arial', 20)

n = 10

box = tk.Listbox(root, width=10, height=n, font=FONT, selectmode=tk.EXTENDED)
for i in range(1, n+1):
    box.insert('end', i * 10)
box.pack(side='left')

def click():
    # v1 = box.get('active')
    # print('value =', v1, type(v1))
    items = box.curselection()
    print(items)
    values = [box.get(i) for i in items]
    print(sum(values))

btn = tk.Button(root, text='Click', font=FONT, command=click)
btn.pack(side='left')

root.mainloop()

