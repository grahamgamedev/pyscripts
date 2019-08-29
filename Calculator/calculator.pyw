from tkinter import *
import math
#background color
color = "lime"

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)                
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("calculator")
        self.configure(background=color)
        self.pack(fill=BOTH, expand=1)
        self.master.bind("<Return>", self.equ)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        edit = Menu(menu)
        edit.add_command(label="Undo", command=self.undo)
        edit.add_command(label="Clear", command=self.cle)
        menu.add_cascade(label="Edit", menu=edit)

        conv = Menu(menu)
        conv.add_command(label="Length", command=length.length)
        conv.add_command(label="Area", command=area.area)
        conv.add_command(label="Weight", command=weight.weight)
        conv.add_command(label="Temperature", command=temperature.temperature)
        menu.add_cascade(label="Conversion", menu=conv)

        Button(self, text="√",command=self.sqrt).place(x=10, y=10)
        Button(self, text="(",command=self.ob).place(x=30, y=10)
        Button(self, text=")",command=self.cb).place(x=50, y=10)
        Button(self, text="²",command=self.squ).place(x=70, y=10)

        Button(self, text="1",command=self.n1).place(x=10, y=40)
        Button(self, text="2",command=self.n2).place(x=30, y=40)
        Button(self, text="3",command=self.n3).place(x=50, y=40)
        Button(self, text="/",command=self.dev).place(x=70, y=40)

        Button(self, text="4",command=self.n4).place(x=10, y=70)
        Button(self, text="5",command=self.n5).place(x=30, y=70)
        Button(self, text="6",command=self.n6).place(x=50, y=70)
        Button(self, text="*",command=self.mul).place(x=70, y=70)

        Button(self, text="7",command=self.n7).place(x=10, y=100)
        Button(self, text="8",command=self.n8).place(x=30, y=100)
        Button(self, text="9",command=self.n9).place(x=50, y=100)
        Button(self, text="-",command=self.sub).place(x=70, y=100)

        Button(self, text=".",command=self.dec).place(x=10, y=130)   
        Button(self, text="0",command=self.n0).place(x=30, y=130)
        Button(self, text="=",command=self.equ).place(x=50, y=130)
        Button(self, text="+",command=self.add).place(x=70, y=130)

    def undo(a=0):
        s = e.get()[0:-1]
        e.delete(0, END)
        e.insert(0, s)
    def cle(a=0):
        e.delete(0, END)

    def sqrt(a=0):
        e.insert(END, "√")
    def ob(a=0):
       e.insert(END, "(")
    def cb(a=0):
        e.insert(END, ")")
    def squ(a=0):
        e.insert(END, "*" + e.get())

    def n1(a=0):
        e.insert(END, "1")
    def n2(a=0):
        e.insert(END, "2")
    def n3(a=0):
        e.insert(END, "3")
    def dev(a=0):
        e.insert(END, "/")

    def n4(a=0):
        e.insert(END, "4")
    def n5(a=0):
        e.insert(END, "5")
    def n6(a=0):
        e.insert(END, "6")
    def mul(a=0):
        e.insert(END, "*")

    def n7(a=0):
        e.insert(END, "7")
    def n8(a=0):
        e.insert(END, "8")
    def n9(a=0):
        e.insert(END, "9")
    def sub(a=0):
        e.insert(END, "-")

    def dec(a=0):
        e.insert(END, ".")
    def n0(a=0):
        e.insert(END, "0")
    def add(a=0):
        e.insert(END, "+")

    def equ(a=0, b=0):
        s = e.get()
        c = 0
        for char in s:
            c += 1
            if s[c:c + 1] == "=" and c < len(s) - 1:
                s = s[c + 1:]
                e.delete(0, END)
                e.insert(0, s)

#square root        
        if s[0:1] == "√":
            n = float(s[1:])
            output = math.sqrt(n)
#everything else
        else:
            output = eval(s)
            
        e.insert(END, "=")
        e.insert(END, output)

class length():
    def length():
        root = Tk()
        root.title("Conversion - Length")
        root.configure(background=color)
        
        il = Entry(root)
        il.place(x=0, y=10)
        il.insert(0, "Select a unit")
        ol = Entry(root)
        ol.place(x=100, y=10)
        ol.insert(0, "Select a unit")

        i = Entry(root)
        i.place(x=0, y=50)
        o = Entry(root)
        o.place(x=100, y=50)

        label = Label(root, text="Press enter to convert.", background=color)
        label.pack(fill=X, expand=1)
#units to convert
        def mmf():
            global fmul
            fmul = 0.001
            il.delete(0, END)
            il.insert(0, "From Millimetres")
        def mmt():
            global mul
            mul = 0.001 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Millimetres")
        def cmf():
            global fmul
            fmul = 0.01
            il.delete(0, END)
            il.insert(0, "From Centermeters")
        def cmt():
            global mul
            mul = 0.01 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Centermeters")
        def inchf():
            global fmul
            fmul = 254
            il.delete(0, END)
            il.insert(0, "From Inches")
        def incht():
            global mul
            mul = 39.3701 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Inches")
        def feetf():
            global fmul
            fmul = 3048
            il.delete(0, END)
            il.insert(0, "From Feet")
        def feett():
            global mul
            mul = 3.2808 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Feet")
        def mf():
            global fmul
            fmul = 1
            il.delete(0, END)
            il.insert(0, "From Meters")
        def mt():
            global mul
            mul = 1 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Meters")
        def kmf():
            global fmul
            fmul = 0.001
            il.delete(0, END)
            il.insert(0, "From Kilometers")
        def kmt():
            global mul
            mul = 1000 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Kilometers")
        def milesf():
            global fmul
            fmul = 1609.344
            il.delete(0, END)
            il.insert(0, "From Miles")
        def milest():
            global mul
            mul = 0.000621 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Miles")
#end of units
        def enter(a=None):
            global mul
            if i.get() != "":
                o.delete(0, END)
                o.insert(0, float(i.get()) * float(mul))
            elif o.get() != "":
                i.delete(0, END)
                i.insert(0, float(o.get()) / float(mul))
        def clear():
            i.delete(0, END)
            o.delete(0, END)

        root.bind("<Return>", enter)
        menu = Menu(root)
        root.config(menu=menu)

        fro = Menu(menu)
        fro.add_command(label="Millimetres", command=mmf)
        fro.add_command(label="Centermeters", command=cmf)
        fro.add_command(label="Inches", command=inchf)
        fro.add_command(label="Feet", command=feetf)
        fro.add_command(label="Meters", command=mf)
        fro.add_command(label="Kilometers", command=kmf)
        fro.add_command(label="Miles", command=milesf)
        menu.add_cascade(label="From", menu=fro)

        to = Menu(menu)
        to.add_command(label="Millimetres", command=mmt)
        to.add_command(label="Centermeters", command=cmt)
        to.add_command(label="Inches", command=incht)
        to.add_command(label="Feet", command=feett)
        to.add_command(label="Meters", command=mt)
        to.add_command(label="Kilometers", command=kmt)
        to.add_command(label="Miles", command=milest)
        menu.add_cascade(label="To", menu=to)

        Button(root, text="Clear",command=clear).pack(side=BOTTOM)
        root.geometry("200x200")
        root.mainloop()

class area():
    def area():
        root = Tk()
        root.title("Conversion - Area")
        root.configure(background=color)
        
        il = Entry(root)
        il.place(x=0, y=10)
        il.insert(0, "Select a unit")
        ol = Entry(root)
        ol.place(x=100, y=10)
        ol.insert(0, "Select a unit")

        i = Entry(root)
        i.place(x=0, y=50)
        o = Entry(root)
        o.place(x=100, y=50)

        label = Label(root, text="Press enter to convert.", background=color)
        label.pack(fill=X, expand=1)
#units to convert
        def mmf():
            global fmul
            fmul = 1000000
            il.delete(0, END)
            il.insert(0, "From Square Millimetres")
        def mmt():
            global mul
            mul = 0.000001 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Square Millimetres")
        def cmf():
            global fmul
            fmul = 0.0001
            il.delete(0, END)
            il.insert(0, "From Square Centermeters")
        def cmt():
            global mul
            mul = 10000 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Square Centermeters")
        def inchf():
            global fmul
            fmul = 0.000645
            il.delete(0, END)
            il.insert(0, "From Square Inches")
        def incht():
            global mul
            mul = 1550.003 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Square Inches")
        def feetf():
            global fmul
            fmul = 0.092903
            il.delete(0, END)
            il.insert(0, "From Square Feet")
        def feett():
            global mul
            mul = 10.76391 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Square Feet")
        def mf():
            global fmul
            fmul = 1
            il.delete(0, END)
            il.insert(0, "From Square Meters")
        def mt():
            global mul
            mul = 1 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Square Meters")
        def hectaref():
            global fmul
            fmul = 10000
            il.delete(0, END)
            il.insert(0, "From Hectares")
        def hectaret():
            global mul
            mul = 0.0001 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Hectares")
        def acref():
            global fmul
            fmul = 4036.856
            il.delete(0, END)
            il.insert(0, "From Acres")
        def acret():
            global mul
            mul = 0.000247 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Acres")
        def kmf():
            global fmul
            fmul = 1000000 
            il.delete(0, END)
            il.insert(0, "From Square Kilometers")
        def kmt():
            global mul
            mul = 0.000001 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Square Kilometers")
        def milesf():
            global fmul
            fmul = 2589988
            il.delete(0, END)
            il.insert(0, "From Square Miles")
        def milest():
            global mul
            mul = 0.00000038610216 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Square Miles")
#end of units
        def enter(a=None):
            global mul
            if i.get() != "":
                o.delete(0, END)
                o.insert(0, float(i.get()) * float(mul))
            elif o.get() != "":
                i.delete(0, END)
                i.insert(0, float(o.get()) / float(mul))
        def clear():
            i.delete(0, END)
            o.delete(0, END)

        root.bind("<Return>", enter)
        menu = Menu(root)
        root.config(menu=menu)

        fro = Menu(menu)
        fro.add_command(label="Square Millimetres", command=mmf)
        fro.add_command(label="Square Centermeters", command=cmf)
        fro.add_command(label="Square Inches", command=inchf)
        fro.add_command(label="Square Feet", command=feetf)
        fro.add_command(label="Square Meters", command=mf)
        fro.add_command(label="Hectares", command=hectaref)
        fro.add_command(label="Acres", command=acref)
        fro.add_command(label="Square Kilometers", command=kmf)
        fro.add_command(label="Square Miles", command=milesf)
        menu.add_cascade(label="From", menu=fro)

        to = Menu(menu)
        to.add_command(label="Square Millimetres", command=mmt)
        to.add_command(label="Square Centermeters", command=cmt)
        to.add_command(label="Square Inches", command=incht)
        to.add_command(label="Square Feet", command=feett)
        to.add_command(label="Square Meters", command=mt)
        to.add_command(label="Hectares", command=hectaret)
        to.add_command(label="Acres", command=acret)
        to.add_command(label="Square Kilometers", command=kmt)
        to.add_command(label="Square Miles", command=milest)
        menu.add_cascade(label="To", menu=to)

        Button(root, text="Clear",command=clear).pack(side=BOTTOM)
        root.geometry("200x200")
        root.mainloop()

class weight():
    def weight():
        root = Tk()
        root.title("Conversion - Weight")
        root.configure(background=color)
        
        il = Entry(root)
        il.place(x=0, y=10)
        il.insert(0, "Select a unit")
        ol = Entry(root)
        ol.place(x=100, y=10)
        ol.insert(0, "Select a unit")

        i = Entry(root)
        i.place(x=0, y=50)
        o = Entry(root)
        o.place(x=100, y=50)

        label = Label(root, text="Press enter to convert.", background=color)
        label.pack(fill=X, expand=1)
#units to convert
        def gf():
            global fmul
            fmul = 0.001
            il.delete(0, END)
            il.insert(0, "From Grams")
        def gt():
            global mul
            mul = 1000 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Grams")
        def ouncesf():
            global fmul
            fmul = 0.02835
            il.delete(0, END)
            il.insert(0, "From Ounces")
        def ouncest():
            global mul
            mul = 35.27396 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Ounces")
        def kgf():
            global fmul
            fmul = 1
            il.delete(0, END)
            il.insert(0, "From Kilograms")
        def kgt():
            global mul
            mul = 1 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Kilograms")
        def poundsf():
            global fmul
            fmul = 0.453592
            il.delete(0, END)
            il.insert(0, "From Pounds")
        def poundst():
            global mul
            mul = 2.204623 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Pounds")
        def stonef():
            global fmul
            fmul = 6.350293
            il.delete(0, END)
            il.insert(0, "From Stone")
        def stonet():
            global mul
            mul = 0.157473 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Stone")
        def mtonnesf():
            global fmul
            fmul = 1000
            il.delete(0, END)
            il.insert(0, "From Metric Tonnes")
        def mtonnest():
            global mul
            mul = 0.001 * fmul
            ol.delete(0, END)
            ol.insert(0, "To Metric Tonnes")
#end of units
        def enter(a=None):
            global mul
            if i.get() != "":
                o.delete(0, END)
                o.insert(0, float(i.get()) * float(mul))
            elif o.get() != "":
                i.delete(0, END)
                i.insert(0, float(o.get()) / float(mul))
        def clear():
            i.delete(0, END)
            o.delete(0, END)

        root.bind("<Return>", enter)
        menu = Menu(root)
        root.config(menu=menu)

        fro = Menu(menu)
        fro.add_command(label="Grams", command=gf)
        fro.add_command(label="Ounces", command=ouncesf)
        fro.add_command(label="Kilograms", command=kgf)
        fro.add_command(label="Pounds", command=poundsf)
        fro.add_command(label="Stone", command=stonef)
        fro.add_command(label="Metric Tonnes", command=mtonnesf)
        menu.add_cascade(label="From", menu=fro)

        to = Menu(menu)
        to.add_command(label="Grams", command=gt)
        to.add_command(label="Ounces", command=ouncest)
        to.add_command(label="Kilograms", command=kgt)
        to.add_command(label="Pounds", command=poundst)
        to.add_command(label="stone", command=stonet)
        to.add_command(label="Metric Tonnes", command=mtonnest)
        menu.add_cascade(label="To", menu=to)
        
        Button(root, text="Clear",command=clear).pack(side=BOTTOM)
        root.geometry("200x200")
        root.mainloop()

class temperature():
    def temperature():
        root = Tk()
        root.title("Conversion - Temperature")
        root.configure(background=color)

        label = Label(root, text="Celsius", background=color)
        label.place(x=0, y=10)
        label = Label(root, text="Fahrenheit", background=color)
        label.place(x=100, y=10)
        label = Label(root, text="Kelvin", background=color)
        label.place(x=200, y=10)

        c = Entry(root)
        c.place(x=0, y=50)
        f = Entry(root)
        f.place(x=100, y=50)
        k = Entry(root)
        k.place(x=200, y=50)

        label = Label(root, text="Press enter to convert.", background=color)
        label.pack(fill=X, expand=1)

        def enter(a=None):
            if c.get() != "":
                f.delete(0, END)
                f.insert(0, (float(c.get()) * 9/5) + 32)
                k.delete(0, END)
                k.insert(0, float(c.get()) + 273.15)
            elif f.get() != "":
                c.delete(0, END)
                c.insert(0, (float(f.get()) - 32) * 5/9)
                k.delete(0, END)
                k.insert(0, float(c.get()) + 273.15)
            elif k.get() != "":
                c.delete(0, END)
                c.insert(0, float(k.get()) - 273.15)
                f.delete(0, END)
                f.insert(0, (float(c.get()) * 9/5) + 32)
        def clear():
            c.delete(0, END)
            f.delete(0, END)
            k.delete(0, END)

        root.bind("<Return>", enter)
        Button(root, text="Clear",command=clear).pack(side=BOTTOM)
        root.geometry("300x200")
        root.mainloop()

#part of main window
root = Tk()

e = Entry(root)
e.pack()
e.insert(END, "")

root.geometry("100x200")
app = Window(root)
root.mainloop()

