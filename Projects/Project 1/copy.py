def enternumber0(event):
    e1.insert(END,0)
def enternumber1(event):
    e1.insert(END,1)
def enternumber2(event):
    e1.insert(END,2)
def enternumber3(event):
    e1.insert(END,3)
def enternumber4(event):
    e1.insert(END,4)
def enternumber5(event):
    e1.insert(END,5)
def enternumber6(event):
    e1.insert(END,6)
def enternumber7(event):
    e1.insert(END,7)
def enternumber8(event):
    e1.insert(END,8)
def enternumber9(event):
    e1.insert(END,9)
from tkinter import *
def reta():
    a=float(e1.get())
    e1.delete(0,END)
    return a
def ent():
    e1=Entry(windows)
def add(event):
    x=reta()
    ent()
    y=reta()
    v=x+y
    print(v)
def equal(event):
    v=add(event)
    e1.insert(END,v)
def dele():
    e1.delete(0,END)
def dele1():
    e1.delete(1,0)
windows=Tk()
e1=Entry(windows,width=20)
e1.grid(row=0,columnspan=9)
b1=Button(windows,text=' 7 ')
b1.grid(row=1,column=1)
b1.bind("<Button-1>",enternumber7)
b2=Button(windows,text=' 8 ')
b2.grid(row=1,column=2)
b2.bind("<Button-1>",enternumber8)
b3=Button(windows,text=' 9 ')
b3.grid(row=1,column=3)
b3.bind("<Button-1>",enternumber9)
b4=Button(windows,text=' /  ')
b4.grid(row=1,column=4)
b5=Button(windows,text=' AC',command=dele)
b5.grid(row=1,column=5)
b6=Button(windows,text='  C  ',command=dele1)
b6.grid(row=1,column=6)
b7=Button(windows,text=' 4 ')
b7.grid(row=2,column=1)
b7.bind("<Button-1>",enternumber4)
b8=Button(windows,text=' 5 ')
b8.grid(row=2,column=2)
b8.bind("<Button-1>",enternumber5)
b9=Button(windows,text=' 6 ')
b9.grid(row=2,column=3)
b9.bind("<Button-1>",enternumber6)
b10=Button(windows,text='  * ')
b10.grid(row=2,column=4)
b11=Button(windows,text='  (   ')
b11.grid(row=2,column=5)
b12=Button(windows,text='   )  ')
b12.grid(row=2,column=6)
b13=Button(windows,text=' 1 ')
b13.grid(row=3,column=1)
b13.bind("<Button-1>",enternumber1)
b14=Button(windows,text=' 2 ')
b14.grid(row=3,column=2)
b14.bind("<Button-1>",enternumber2)
b15=Button(windows,text=' 3 ')
b15.grid(row=3,column=3)
b15.bind("<Button-1>",enternumber3)
b16=Button(windows,text='  - ')
b16.grid(row=3,column=4)
b17=Button(windows,text='  R  ')
b17.grid(row=3,column=5)
b18=Button(windows,text='  xx ')
b18.grid(row=3,column=6)
b19=Button(windows,text=' 0 ')
b19.grid(row=4,column=1)
b19.bind("<Button-1>",enternumber0)
b20=Button(windows,text=' .  ')
b20.grid(row=4,column=2)
b21=Button(windows,text=' %')
b21.grid(row=4,column=3)
b22=Button(windows,text=' + ')
b22.grid(row=4,column=4)
b22.bind("<Button-1>",add)
b23=Button(windows,text='  =  ')
b23.grid(row=4,column=5)
b23.bind("<Button-1>",equal)
windows.mainloop()