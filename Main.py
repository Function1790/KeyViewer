from tkinter import *
from tkinter.font import *
from threading import *
from keyboard import *

base=[40, 40]
add=[80, 70]

root=Tk()
root.geometry("600x300")
root.configure(bg="black")
root.title("KeyViewer")

fontA=Font(size=40)

class setLabel:
    def __init__(self, key, txt, pos_x, pos_y, wid):
        if wid==0:
            widthA=2
        else:
            widthA=wid
        self.key=key
        self.txt=txt
        self.lb=Label(text=txt,font=fontA, width=widthA)
        self.lb.place(x=pos_x, y=pos_y)

w=setLabel("up","▲",(base[0]+(add[0]*1)), (base[1]+(add[1]*1)),0)
a=setLabel("left","◀",(base[0]+(add[0]*0)), (base[1]+(add[1]*2)),0)
s=setLabel("down","▼",(base[0]+(add[0]*1)), (base[1]+(add[1]*2)),0)
d=setLabel("right","▶",(base[0]+(add[0]*2)), (base[1]+(add[1]*2)),0)
shift=setLabel("shift","shift",(base[0]+(add[0]*4)), (base[1]+(add[1]*1)),5)
ctrl=setLabel("ctrl","ctrl",(base[0]+(add[0]*4)), (base[1]+(add[1]*2)),3)

def changeKey(this):
    if is_pressed(this.key):
        this.lb.config(bg="red")
    else:
        this.lb.config(bg="white")

def changeThread():
    while True:
        changeKey(w)
        changeKey(a)
        changeKey(s)
        changeKey(d)
        changeKey(shift)
        changeKey(ctrl)

th=Thread(target=changeThread)
th.start()

root.mainloop()
