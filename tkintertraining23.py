import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import sympy as smp

def button_func():
    print('button yes pressed')

#window 1
root = ttk.Window(themename='darkly')
root.title('new one')
root.geometry('200x500')

#create
textBox = ttk.Frame(master=root)
titlebox = ttk.Label(master=textBox, text='Write your Dream Here!', font='montserrat 13 bold',)
box1 = ttk.Entry(master=textBox)
titlebox.pack()
box1.pack()
textBox.pack(pady=5)

#create again
text1 = ttk.Text(master = root)
text1.pack()

def button_hello():
    print('Hello World')


#button
buttonsend = ttk.Button(master = root, text = 'yes', command = button_func)
buttonsend.pack(pady = 10)

#exercise
hello_world = ttk.Label(master=root, text='Press Me to get Hello World!',font = 'montserrat 12 bold')
hello_world.pack(pady=5)

buttonhello = ttk.Button(master = root, text = 'hello', command = button_hello)
buttonhello.pack()


#run mainwindow
root.mainloop()
