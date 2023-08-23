from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
root=tk.Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")
def BMI():
    he=float(height.get())
    we=float(weight.get())
    m=he/100
    bmi=round(float(we/m**2),1)
    l1.config(text=bmi)
    if bmi<=18.5:
        l2.config(text="Underweight")
        l3.config(text="You have lower weigt than normal")
    elif bmi>18.5 and bmi<=25:
        l2.config(text="Normal")
        l3.config(text="You are healthy")
    elif bmi>25 and bmi<=30:
        l2.config(text="Overweight")
        l3.config(text="You have more weigt than normal")
    else:
        l2.config(text="Obes")
        l3.config(text="You may have health risk if you do not lose weight ")
        
#icon image
iconimg=tk.PhotoImage(file="images/icon.png")
root.iconphoto(False,iconimg)
#top part
top=tk.PhotoImage(file="images/top.png")
topimg=tk.Label(root,image=top,bg="#f0f1f5")
topimg.place(x=-10,y=-10)
#bottom part
tk.Label(root,width=72,height=18,bg="#ADD8E6").pack(side=tk.BOTTOM)
#boxes
box=tk.PhotoImage(file="images/box.png")
tk.Label(root,image=box).place(x=20,y=100)
tk.Label(root,image=box).place(x=240,y=100)
#scale of measurement
scale=tk.PhotoImage(file="images/scale.png")
tk.Label(root,image=scale,bg="#add8e6").place(x=20,y=310)

#sliders
#for height
cvalue=tk.DoubleVar()
def getcvalue():
    return '{: .2f}'.format(cvalue.get())
def slider_changed():
    height.set(getcvalue())
    size=int(float(getcvalue()))
    img=(Image.open("images/man.jpg"))
    reimg=img.resize(50,10+size)
    p2=ImageTk.PhotoImage(reimg)
    man.config(image=p2)
    man.place(x=70,y=550-size)
    man.image=p2 
    
style=ttk.Style("Tscale",background="white")
slider=ttk.Scale(root,from_=0,to=220,orient='horizontal',style="Tscale",command=slider_changed,variable=cvalue)
slider.place(x=80,y=250)
#for weight
cval=tk.DoubleVar()
def getcval():
    return '{: .2f}'.format(cvalue.get())
def sliderchanged():
    weight.set(getcval())
    
style2=ttk.Style("Tscale",bg="white")
slider2=ttk.Scale(root,from_=0,to=220,orient='horizontal',style2="Tscale",command=sliderchanged,variable=cval)
slider2.place(x=80,y=250)
#entery box for data
height=tk.StringVar()
weight=tk.StringVar()
h=tk.Entry(root,textvariable=height,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)
h.place(x=35,y=160)
height.set(getcvalue())
w=tk.Entry(root,textvariable=weight,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)
w.place(x=225,y=160)
weight.set(getcval())

#manfigure settingup
man=tk.Label(root,bg="#add8e6")
man.place(x=70,y=530)
tk.Button(root,text="View Result",width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white").place(x=280,y=340)
l1=tk.Label(root,font="arial 60 bold",bg="#add8e6",fg="fff")
l1.place(x=125,y=305)
l2=tk.Label(root,font="arial 20 bold",bg="#add8e6",fg="3b3a3a")
l2.place(x=280,y=430)
l3=tk.Label(root,font="arial 10",bg="#add8e6",)
l3.place(x=200,y=500)



root.mainloop()