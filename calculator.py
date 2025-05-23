from tkinter import *
window = Tk()
window.geometry('500x500')

#Functions
#to enter numbers
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result)+str(num))

#operator functions
def add():
    n1 = e.get()
    global operation
    operation = 'addition'
    global i
    i = int(n1)
    e.delete(0, END)

def sub():
    n1 = e.get()
    global operation
    operation = 'subtraction'
    global i
    i = int(n1)
    e.delete(0, END)

def mult():
    n1 = e.get()
    global operation
    operation = 'multiplication'
    global i
    i = int(n1)
    e.delete(0, END)

def div():
    n1 = e.get()
    global operation
    operation = 'division'
    global i
    i = int(n1)
    e.delete(0, END)

#equals function
def equal():
    n2 = e.get()
    e.delete(0,END)
    if operation == 'addition':
        e.insert(0, i+int(n2))
    elif operation == 'subtraction':
        e.insert(0, i-int(n2))
    elif operation == 'multiplication':
        e.insert(0, i*int(n2))
    elif operation == 'division':
        e.insert(0, i/int(n2))

#clearing the entry box
def clear():
    e.delete(0, END)

#Entry Box
e = Entry(window, width=56, borderwidth=5)
e.place(x=0,y=0)

#Buttons
b = Button(window, width=12, text='1', command=lambda:click(1))
b.place(x=10,y=60)

b = Button(window, width=12, text='2', command=lambda:click(2))
b.place(x=80,y=60)

b = Button(window, width=12, text='3', command=lambda:click(3))
b.place(x=170,y=60)

b = Button(window, width=12, text='4', command=lambda:click(4))
b.place(x=10,y=120)

b = Button(window, width=12, text='5', command=lambda:click(5))
b.place(x=80,y=120)

b = Button(window, width=12, text='6', command=lambda:click(6))
b.place(x=170,y=120)

b = Button(window, width=12, text='7', command=lambda:click(7))
b.place(x=10,y=180)

b = Button(window, width=12, text='8', command=lambda:click(8))
b.place(x=80,y=180)

b = Button(window, width=12, text='9', command=lambda:click(9))
b.place(x=170,y=180)

b = Button(window, width=12, text='0', command=lambda:click(0))
b.place(x=10,y=240)

b = Button(window, width=12, text='+', command=add)
b.place(x=80,y=240)

b = Button(window, width=12, text='-', command=sub)
b.place(x=170,y=240)

b = Button(window, width=12, text='*', command=mult)
b.place(x=10,y=300)

b = Button(window, width=12, text='/', command=div)
b.place(x=80,y=300)

b = Button(window, width=12, text='=', command=equal)
b.place(x=170,y=300)

b = Button(window, width=12, text='Clear', command=clear)
b.place(x=10,y=360)

mainloop()