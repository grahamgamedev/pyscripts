from tkinter import *

root = Tk()
s = ""
e = Entry(root)
e.pack()

def cle():
    global s
    e.place(x=0, y=0)
    e.insert(0, "")
    s = ""

def callback():
    print(e.get())

b = Button(root, text="get", width=10, command=callback)
b.pack()
b = Button(root, text="cle", width=10, command=cle)
b.pack()

mainloop()

