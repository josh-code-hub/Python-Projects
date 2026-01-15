import tkinter as tk

def add():
    result.set(int(entry1.get()) + int(entry2.get()))

root = tk.Tk()
root.title("Simple Calculator")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Add", command=add).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
