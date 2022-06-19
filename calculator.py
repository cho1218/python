from tkinter import *
window= Tk()

def a():
    entry1.insert(END, "7")
def b():
    entry1.insert(END, "8")
def c():
    entry1.insert(END, "9")
def d():
    entry1.insert(END, "4")
def e():
    entry1.insert(END, "5")
def f():
    entry1.insert(END, "6")
def g():
    entry1.insert(END, "1")
def h():
    entry1.insert(END, "2")
def i():
    entry1.insert(END, "3")
def j():
    entry1.insert(END, "0")
def u():
    entry1.insert(END, ".")
def v():
    entry1.insert(END, "*")
def w():
    entry1.insert(END, "+")
def x():
    entry1.insert(END, "/")
def y():
    entry1.insert(END, "-")
def z():
    str=entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, eval(str))
def dele():
    entry1.delete(0, END)
    
entry1=Entry(window,bg="yellow",width=37)
entry1.grid(row=0,column=0,columnspan=5)

bn7=Button(window,text="7",width=6,height=1,command=a)
bn8=Button(window,text="8",width=6,height=1,command=b)
bn9=Button(window,text="9",width=6,height=1,command=c)
bncal1=Button(window,text="/",width=6,height=1,command=x)
bncal2=Button(window,text="C",width=6,height=1,command=dele)
bn4=Button(window,text="4",width=6,height=1,command=d)
bn5=Button(window,text="5",width=6,height=1,command=e)
bn6=Button(window,text="6",width=6,height=1,command=f)
bncal3=Button(window,text="*",width=6,height=1,command=v)
bn_1=Button(window,width=6,height=1)
bn1=Button(window,text="1",width=6,height=1,command=g)
bn2=Button(window,text="2",width=6,height=1,command=h)
bn3=Button(window,text="3",width=6,height=1,command=i)
bncal4=Button(window,text="-",width=6,height=1,command=y)
bn_2=Button(window,width=6,height=1)
bn0=Button(window,text="0",width=6,height=1,command=j)
bncal5=Button(window,text=".",width=6,height=1,command=u)
bncal6=Button(window,text="=",width=6,height=1,command=z)
bncal7=Button(window,text="+",width=6,height=1,command=w)
bn_3=Button(window,width=6,height=1)

entry1.grid(row=0,column=0,columnspan=5)

bn7.grid(row=1,column=0)
bn8.grid(row=1,column=1)
bn9.grid(row=1,column=2)
bncal1.grid(row=1,column=3)
bncal2.grid(row=1,column=4)
bn4.grid(row=2,column=0)
bn5.grid(row=2,column=1)
bn6.grid(row=2,column=2)
bncal3.grid(row=2,column=3)
bn_1.grid(row=2,column=4)
bn1.grid(row=3,column=0)
bn2.grid(row=3,column=1)
bn3.grid(row=3,column=2)
bncal4.grid(row=3,column=3)
bn_2.grid(row=3,column=4)
bn0.grid(row=4,column=0)
bncal5.grid(row=4,column=1)
bncal6.grid(row=4,column=2)
bncal7.grid(row=4,column=3)
bn_3.grid(row=4,column=4)


window.mainloop()
