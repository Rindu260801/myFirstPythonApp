import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

#command
def button():
    print(textme.get())
    textme.set('button pressed')
#main window
root = ttk.Window(themename='darkly',title='my first Variable Text')

#variable
textme = tk.StringVar(value='start value')

#widget header
header = ttk.Label(master = root, textvariable =  textme , font = 'arial 12')


#widget form
form = ttk.Entry(master = root, textvariable = textme , font='courier 12')
form2 = ttk.Text(master = root,font='courier 12')
ttk.Text()
header.pack()
form2.pack()
form.pack()

#widget button
button1 = ttk.Button(master= root, text='save to console',command=button)
button1.pack()

root.mainloop()