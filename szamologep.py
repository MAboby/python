# -*- coding: ISO-8859-2 -*-
from Tkinter import *
def osszead():
    x = eval(mezo1.get())
    y = eval(mezo2.get())
    z = x + y
    mezo3.delete(0,END)
    mezo3.insert(0,'Eredm�ny: '+str(z))

def kivon():
    x = eval(mezo1.get())
    y = eval(mezo2.get())
    z = x - y
    mezo3.delete(0,END)
    mezo3.insert(0,'Eredm�ny: '+str(z))

def szoroz():
    x = eval(mezo1.get())
    y = eval(mezo2.get())
    z = x * y
    mezo3.delete(0,END)
    mezo3.insert(0,'Eredm�ny: '+str(z))

def oszt():
    x = eval(mezo1.get())
    y = eval(mezo2.get())
    z = x / y
    mezo3.delete(0,END)
    mezo3.insert(0,'Eredm�ny: '+str(z))

ablak1 = Tk()
mezo1 = Entry(ablak1)
mezo1.pack()
mezo2 = Entry(ablak1)
mezo2.pack()
gomb1 = Button(ablak1, text='�sszead�s', command=osszead)
gomb1.pack()
gomb2 = Button(ablak1, text='Kivon�s', command=kivon)
gomb2.pack()
gomb3 = Button(ablak1, text='Szorz�s', command=szoroz)
gomb3.pack()
gomb4 = Button(ablak1, text='Oszt�s', command=oszt)
gomb4.pack()
mezo3 = Entry(ablak1)
mezo3.pack()
gomb5 = Button(ablak1, text='Kil�p�s', command = ablak1.destroy)
gomb5.pack()
ablak1.mainloop()