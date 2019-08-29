from tkinter import *
import time, random, threading, os
def new():
    f = open("put text hear.txt","w")
    f.write("Test")
    f.close

def edit():
    os.startfile("put text hear.txt")
    
def start():
    f = open("put text hear.txt","r")
    text = f.read()
    f.close
    
    for char in text:
        t.insert("end",char)
        time.sleep(random.randint(0,150)/1000.0)

def starting():
    tsss = threading.Thread(target=start)
    tsss.start()

root = Tk()
root.winfo_toplevel().title("Scroll Text")
t = Text(root)
t.pack()
Button(root,text="Start",command=starting).pack()
Button(root,text="New",command=new).pack(side=LEFT)
Button(root,text="Open",command=edit).pack(side=RIGHT)
root.mainloop()
